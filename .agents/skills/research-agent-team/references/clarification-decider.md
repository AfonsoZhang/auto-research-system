# 澄清卡自动代选

只供 research 根层已启动自动模式任务的主 Agent 使用。用户已授权自动代选时，
把调查充分的现有卡片交给 `research_clarification.choose_card`；普通修改、
单技能调用或子项目日常工作不因此进入代选。该工具只返回建议，不执行选项动作。

自动模式的卡片由主 Agent 标记 `execution_mode: "unattended_research"`。
这是保留兼容的内部字段值；对用户及工作流统一称“自动模式”，不表示另一种模式。
配置开启 `automatic_selection` 且卡片标记匹配时，才自动采纳有效的模型选择；
其他模式或缺少标记时只给建议。该标记须来自本次用户委托，不能从用户暂未回复推断。
“在自动模式启用决策模型”属于配置请求，本身不启动科研任务。

The [post-selection human checkpoint](../../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
is excluded from automatic selection, including in automatic mode. Topic approval
cards use `decision_kind: "topic_approval"`, `delegated: false` and no default ID.
Without an actual user choice, the tool returns `user_required` with reason
`topic_approval_requires_user` before inference or any single-option shortcut,
even if a caller incorrectly marks the card delegated. The main agent must wait;
there is no fallback/default decision for this checkpoint. Populate `user_choice`
only from the user's reply to the reported topic/version, recorded in the tracker.

## 输入与结果

每卡一个问题，2–3 个选项，稳定选项 ID。包含背景、用户偏好和约束，并标明已授权
的候选 ID、默认项、是否已有用户回答。权限判断由主 Agent 根据真实指示完成；
不能让模型创造授权。等待新增授权的卡片不调用模型来代替用户批准。

For topic cards, first apply the
[context policy](../../shared-references/topic-context-policy.md#accept-the-choice-and-preserve-its-origin).
Check the options and consequential constraints against the scoped brief and
source evidence. The card model cannot recover omitted alternatives. Distinguish
user requirements from facts, preferences and agent choices in the existing
background/tracker; an ordinary model-selected option remains a delegated decision
after summarization. Such a decision never supplies the required topic approval.

发送给 OpenDecider 的问题、背景、选项、约束和偏好统一使用英文。
用户原始要求若是中文，由主 Agent 忠实转述为英文，原文作为来源保留供核对；
不得因翻译删改约束或增加授权。自动模式流程的工作语言与材料格式遵循
`SKILL.md` 的 Working language and artifact formats；仅最终用户汇报使用中文。

不要把“推荐”“默认 A”作为候选描述的内容喂给模型。给各选项同等充分的后果、
收益和代价，避免只是复读主 Agent 的推荐。模型的输入保留卡片原意；如需翻译，
同时保留原始卡片并说明翻译，不凭翻译丢失约束。

输出区分 `selected`、`main_agent_required` 和 `user_required`。只在前者采用已授权
选项；其他情况回到主 Agent 的既有规则。模型失败或不确定时不伪造概率或解释。
主 Agent 的解释基于证据，并与模型实际只输出的选择/概率分开记录。

记录复用卡片/项目跟踪器：卡片 ID 与版本或输入摘要哈希、选项、返回值、模型与版本、
实际决策来源（user / model / main_agent）、采用的行动及结果。开始依赖工作前再查
用户新回复；新回复优先调整尚未执行的工作。

## 本地接入

MCP 配置只放 research 根层；Claude/Codex 使用同一 `scripts/clarification_decider.py`。
脚本、文档与团队技能一起保留根层，不向旧版子项目复制。依赖环境位于
`$RESEARCH_ROOT/.venvs/clarification-decider/`，运行配置/模型位于
`$RESEARCH_ROOT/.tools/clarification-decider/`，避免虚拟环境及权重进入技能同步。

模型与后端由配置决定，不绑定某个模型或服务商（`config.example.json`；路径可用
`DECIDER_CONFIG` 覆盖）：
- `backend: "local_gguf"`：按需启动本地 llama.cpp 服务，加载 `model_path` 指定的权重；
- `backend: "openai_compatible"`：任何返回 `top_logprobs` 的 OpenAI 兼容端点（vLLM、
  LM Studio、Ollama、llama.cpp、托管网关），`base_url` + `served_model`，密钥从
  `api_key_env` 指定的环境变量读取；
- 未配置：始终返回 `main_agent_required`。
只暴露 `choose_card`，不接入上游的任务路由、guard 或研究评价工具。换用其他模型后，
须先在本地英文卡片上重新验证，再开启 `automatic_selection`。
模型/接口未就绪时明确返回 `main_agent_required`，禁止把兜底视为模型成功。

用户授权后才可在自动模式使用决策模型；下载或推理不可用时由主 Agent 代选。
权重与实际测试状态以 `.tools/clarification-decider/config.json` 及其引用的验证记录为准，
不能仅凭安装包或 MCP 握手通过声称模型已运行。需要重新下载权重时可执行
`python3 $RESEARCH_ROOT/.agents/skills/research-agent-team/scripts/download_decider_weights.py`；
该脚本固定当次官方 revision 并验证权重 SHA-256，不自动开启模型代选。

两端的实际入口是工具 `choose_card(card={...})`。卡片 JSON 字段：
`card_id`、`question`、`background`、`options`（ID: 描述）、`authorized_option_ids`、
`delegated`；可选 `constraints`、`preferences`、`user_choice`、`default_id`、`execution_mode`、
`decision_kind`（选题人工门禁必须标记为 `topic_approval`）。
`default_id` 不发送给模型。命令行复查可用：
`$RESEARCH_ROOT/.venvs/clarification-decider/bin/python $RESEARCH_ROOT/.agents/skills/research-agent-team/scripts/clarification_decider.py --card <卡片.json>`。

先验证英文卡片上的约束遵守、偏好响应、换序稳定性，再据实际结果决定自动采用范围。
输出概率不等于在本工作区测得的正确率，不能直接拿固定置信度当科研判断的成功率。
没有通过本地回放前只作建议，由主 Agent 作最终选择；调参样本与最终评价样本分开。
少量合成卡片验证接入和基本行为，不代表真实研究决策的正确率。
