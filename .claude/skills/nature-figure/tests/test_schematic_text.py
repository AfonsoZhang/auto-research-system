import importlib.util
from pathlib import Path
import tempfile
import unittest
import cairosvg

spec = importlib.util.spec_from_file_location('schematic_text', Path(__file__).parents[1]/'scripts/audit_schematic_text.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class RenderedTextTest(unittest.TestCase):
    def render(self, body):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        p = Path(tmp.name)/'test.pdf'
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100">{body}</svg>'
        cairosvg.svg2pdf(bytestring=svg.encode(),write_to=str(p))
        return module.audit(str(p))

    def test_cairo_transformed_text_uses_effective_size(self):
        r=self.render('<text x="10" y="40" font-size="16">Readable</text>')
        self.assertEqual(r['verdict'],'PASS')
        self.assertAlmostEqual(r['min_found_pt'],12,places=2)

    def test_small_text_still_fails(self):
        r=self.render('<text x="10" y="40" font-size="4">Too small</text>')
        self.assertEqual(r['verdict'],'FAIL')

    def test_no_extractable_text_is_not_a_pass(self):
        self.assertEqual(self.render('<rect width="100" height="50"/>')['verdict'],'NOT AUDITABLE')


if __name__=='__main__':
    unittest.main()
