"""Offline contract tests; these do not evaluate OpenDecider model quality."""
import copy
import unittest
from unittest.mock import Mock
from clarification_decider import choose


BASE = {'card_id': 'D-test', 'question': 'Which plan meets the goal?', 'background': 'A small pilot is requested.',
        'constraints': ['No paid API calls.'], 'preferences': ['Prefer a reusable implementation.'],
        'options': {'A': 'Run a free local pilot.', 'B': 'Use an already authorized local simulator.'},
        'authorized_option_ids': ['A', 'B'], 'delegated': True, 'default_id': 'A',
        'execution_mode': 'unattended_research'}


def response(state, question, options):
    return {'answers': {'card': {'choice': 'B', 'probabilities': {'A': 0.1, 'B': 0.9}}}}


class Cards(unittest.TestCase):
    def test_user_reply_wins_without_model(self):
        card = dict(BASE, user_choice='A')
        result = choose(card, lambda *_: self.fail('model called'))
        self.assertEqual((result['source'], result['choice']), ('user', 'A'))

    def test_no_delegation_never_calls_model(self):
        result = choose(dict(BASE, delegated=False), lambda *_: self.fail('model called'))
        self.assertEqual(result['status'], 'user_required')

    def test_topic_approval_cannot_be_delegated_or_defaulted(self):
        for automatic in (False, True):
            for delegated in (False, True):
                for allowed in (['A', 'B'], ['A']):
                    with self.subTest(automatic=automatic, delegated=delegated, allowed=allowed):
                        infer = Mock(side_effect=response)
                        card = dict(BASE, decision_kind='topic_approval',
                                    delegated=delegated, authorized_option_ids=allowed)
                        result = choose(card, infer, automatic=automatic)
                        self.assertEqual(result['status'], 'user_required')
                        self.assertEqual(result['reason'], 'topic_approval_requires_user')
                        self.assertIsNone(result['choice'])
                        self.assertEqual(result['source'], 'none')
                        self.assertFalse(result['action_executed'])
                        infer.assert_not_called()

    def test_topic_approval_records_explicit_user_decision(self):
        for choice in BASE['options']:
            with self.subTest(choice=choice):
                infer = Mock(side_effect=response)
                card = dict(BASE, decision_kind='topic_approval', delegated=False,
                            user_choice=choice)
                result = choose(card, infer, automatic=True)
                self.assertEqual((result['status'], result['source'], result['choice']),
                                 ('selected', 'user', choice))
                self.assertFalse(result['action_executed'])
                infer.assert_not_called()

    def test_topic_approval_does_not_grant_missing_resource_authority(self):
        infer = Mock(side_effect=response)
        card = dict(BASE, decision_kind='topic_approval', delegated=False,
                    user_choice='B', authorized_option_ids=['A'])
        result = choose(card, infer, automatic=True)
        self.assertEqual(result['status'], 'user_required')
        self.assertEqual(result['reason'], 'authorization_or_resource_needed')
        infer.assert_not_called()

    def test_unauthorized_options_never_reach_model(self):
        card = copy.deepcopy(BASE)
        card['options']['C'] = 'Buy an unauthorized API subscription.'
        def capture(state, question, options):
            self.assertNotIn('C', options)
            self.assertNotIn('default_id', state)
            return response(state, question, options)
        result = choose(card, capture, automatic=True)
        self.assertEqual(result['choice'], 'B')

    def test_unvalidated_model_is_advisory(self):
        result = choose(BASE, response)
        self.assertEqual(result['status'], 'main_agent_required')
        self.assertIsNone(result['choice'])
        self.assertEqual(result['suggested_choice'], 'B')

    def test_automatic_model_selection_requires_unattended_mode(self):
        for mode in (None, 'interactive_research', 'single_task'):
            result = choose(dict(BASE, execution_mode=mode), response, automatic=True)
            self.assertEqual(result['status'], 'main_agent_required')
            self.assertIsNone(result['choice'])
            self.assertEqual(result['suggested_choice'], 'B')
            self.assertEqual(result['reason'], 'automatic_selection_outside_unattended_mode')

    def test_validated_unattended_model_selects_without_executing(self):
        result = choose(BASE, response, automatic=True)
        self.assertEqual((result['status'], result['source'], result['choice']), ('selected', 'model', 'B'))
        self.assertFalse(result['action_executed'])

    def test_backend_failure_is_not_a_decision(self):
        def fail(*_):
            raise ConnectionError('offline')
        result = choose(BASE, fail, automatic=True)
        self.assertEqual(result['status'], 'main_agent_required')
        self.assertNotIn('probabilities', result)
        self.assertFalse(result['action_executed'])

    def test_malformed_distribution_cannot_select(self):
        for p in (float('nan'), -1, 2):
            def malformed(*_):
                return {'answers': {'card': {'choice': 'B', 'probabilities': {'A': p, 'B': 0.9}}}}
            self.assertEqual(choose(BASE, malformed, automatic=True)['status'], 'main_agent_required')

    def test_outside_choice_cannot_select(self):
        def malformed(*_):
            return {'answers': {'card': {'choice': 'C', 'probabilities': {'A': 0.1, 'B': 0.9}}}}
        self.assertEqual(choose(BASE, malformed, automatic=True)['status'], 'main_agent_required')

    def test_tie_returns_to_main_agent(self):
        def tied(*_):
            return {'answers': {'card': {'choice': 'A', 'probabilities': {'A': 0.5, 'B': 0.5}}}}
        self.assertEqual(choose(BASE, tied, automatic=True)['reason'], 'tied_options')

    def test_three_choices_and_unknown_authority(self):
        with self.assertRaises(ValueError):
            choose(dict(BASE, authorized_option_ids=['Z']), response)


if __name__ == '__main__':
    unittest.main()
