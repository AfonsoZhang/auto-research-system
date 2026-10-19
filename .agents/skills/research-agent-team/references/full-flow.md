# Research stages, shared state and delivery

This is the stage map and completion reference for the unified research controller.
In on-demand mode, use only the stages relevant to the requested scope; a suggested
next stage remains a recommendation. The full-paper default and continuous
execution rules apply only when automatic mode is explicitly activated for
this task. Automatic mode uses the same goal and evidence checks. Reading,
installing or editing these instructions does not launch research work.

Resolve a named specialist below to `../../<skill-name>/SKILL.md` relative to this
reference and read its instructions for the current task. Select the needed
skills within a row; the list does not require calling every skill.

## 起点、终点与推进

以用户当前目标及项目已有成果确定起点，验收仍有效的已有产物，补齐缺口后继续。
自动模式下，论文研究任务未指定更窄终点时，默认完成下面全部适用阶段，交付完整论文稿及复现包。
用户明确要求的单项修改仍是单项任务，不因使用某技能自动扩成整篇论文。
自动模式任务中，选题、计划或 pilot 通过只是中间节点；选题后必须先通过人工门禁，
用户明确同意后，主 Agent 继续其余已授权阶段，无需用户逐阶段回复。

| 阶段 | 按需使用现有技能 | 完成条件与交接物 |
|---|---|---|
| 问题发现与选题 | brainstorming-research-ideas、research-companion、idea-evaluator、novelty-check | 候选比较、核心问题、贡献类型、选定范围及可验证的区别；文献核验可返回修正候选判断 |
| Topic approval | Main agent reports to the user | Apply the mandatory human checkpoint below; record explicit approval before dependent work |
| 文献综述与证据核验 | research-lit、deep-research（请求完整综述时）、nature-reader、nature-ref-verifier | 可追溯的文献记录、发表状态、最接近工作和证据缺口；遵循已有 publication-policy |
| Venue, benchmark selection and research design | select-venue, benchmark-research-skill, experiment-plan | Official requirements; reuse decision with source evidence and measurement fit; documented gap for any new benchmark; claim-linked design, suitable resources, decisive pilot and budget/stop conditions |
| 实现与最小实验 | experiment-bridge、run-experiment、analyze-results | 可运行实现、测量检查、真实原始结果及继续/补测/止损依据 |
| 正式研究与分析 | run-experiment、analyze-results | 完成已授权的必要比较/控制，记录失败和缺失，结论能追溯到结果 |
| 论证与写作 | good-story、ts-paper-plan、paper-writer、nature-figure、ts-paper-cite | 基于证据的完整稿、图表和真实引用；不写成实验时间线，不因迭代无依据地收窄主张 |
| 限制与声明草稿 | limitation-and-risk-writer、ai-use-drafter | 作者视角的实际限制；AI-use 仅独立草稿，留给用户修改，禁止自动写入正文或投稿表单 |
| 修订与验证 | paper-polish、pre-submission-reviewer、nature-ref-verifier；需要时 paper-claim-audit | 修复实际问题并核验引用、主张/图表/数值一致性与适用格式；未解决项如实列出 |
| 最终交付 | 主 Agent；自动模式下按需使用 research-editor/qa | 达到本次终点的可检查产物；完整论文任务交付可打开的稿件、适用的编译输出和复现材料、结果来源、验证结论与剩余问题 |

For topic work, use the [context policy](../../shared-references/topic-context-policy.md)
before loading historical evaluations. The selection handoff preserves the brief's
sources, fresh/continuation/reselection mode, initial candidates, later evidence
and actual input-boundary checks. A decision records its source and authority;
reuse of an artifact alone does not establish a constraint for a new topic.

Apply the [post-selection human checkpoint](../../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
after preparing a reviewable topic proposal. Preliminary literature/novelty checks
may inform selection; the full downstream stages wait for the user's explicit
decision. Keep the approval bound to the reported topic/version and scope when
recovering a session. An absent reply cannot supply approval in automatic mode.

上表是覆盖清单，不要求重复已经完成且输入未变的阶段。按贡献类型调整实际方法：
综述、理论、立场或复现论文沿用 paper-type-routing，不能强塞不适用的实验或新方法。
记录某阶段不适用的具体理由。写作中的补证据可回到相关阶段；已有有效检查无需全部重做。
一般论文任务的终点是材料交付；真实投稿、发信、公开发布等外部动作按已有明确授权处理。

Before accepting a research result for a dependent stage, apply the shared
[scientific acceptance checks](../../shared-references/research-autonomy.md#scientific-acceptance-is-separate-from-execution-completion).
Record execution completion and evidential status separately in the existing
record, with the protocol version, actual result sources and supported claim scope.
Use the [human decision points](../../shared-references/research-autonomy.md#human-participation-at-consequential-decisions)
for consequential choices; do not add approval stops at every stage transition.

## 子 Agent 与中间产物

Research-stage decisions and team assignments share one record in the project's
existing plan or tracker. Keep the execution mode, requested endpoint, current
stage, dependencies, responsible agent, artifact path/version, acceptance result,
decisions and remaining work together. Use an existing schema when available;
for a small on-demand task, working context and the deliverable are sufficient.
Do not create separate research-control and team-control ledgers.

Carry constraint origins and decision sources through compaction and recovery.
Consult the referenced originals when a summary cannot distinguish a user
requirement from an agent suggestion or delegated choice. Resume accepted work
within its scope; do not promote a provisional choice into a lasting user preference.

主 Agent 在项目现有计划/跟踪器中记录最终交付、阶段状态、负责人、产物路径、验收结论
及下一步。遵循子项目已有目录结构，不新建一套与现有台账并行的必填模板。
派单给出相关输入及版本、可修改范围、产物位置和验收条件。子 Agent 返回提交物，
主 Agent 核实后才记为已验收；“提交了”不等于“通过了”。科学负结果也可构成合格交付。

压缩上下文或恢复会话后，读取已记录产物和未完成节点继续；不凭简略摘要重新选题，
也不把尚未完成的阶段误记为完成。上游输入变化只重验受影响的下游产物。
若本次已有 /goal，复用其目标与预算；本规则不自行创建 goal，也不宣称运行时不存在的
后台续跑、跨进程恢复或定时能力。

An existing /goal does not activate automatic mode or widen its task. Switching
to explicitly authorized execution in automatic mode reuses the same artifacts and
record; it does not restart the research or create a competing goal.

## 结束条件

Apply these conditions to the authorized scope. Finishing a requested plan or
single-stage revision completes that on-demand task; it does not claim completion
of a full research project. In automatic mode, assess the full agreed endpoint.

技术预检与科学判据分开：执行、输出格式或测量异常只阻塞依赖该输出的分支，
不能据此判定机制无效。先诊断，按实验计划在授权范围和剩余预算内做有界开发修复；
保留失败记录，修复后冻结配置，不使用正式测试结果调参。不得为通过判据无限重试。
Agent 自定的运行参数不等于用户限制；调整前记录理由和适用范围，不突破用户预算或权限。

- **完成**：全部适用阶段均有验收过的实际产物，达到本次最终交付条件，未解决项不妨碍该条件。
- **等待选题确认**：选题汇报已交付，状态为 `AWAITING_TOPIC_APPROVAL`；等待用户明确选择，
  不启动依赖该选题的后续阶段，不以超时、自动模式授权或模型代选绕过，也不记为全流程完成。
- **提前止损**：有效测量下最小实验未达到事先约定的继续条件，或对应预算耗尽。停止依赖性的大规模研究，
  保存原始结果、可复用成果和停止依据，列出未执行阶段；不把这称为论文全流程完成。
- **等待真实依赖**：需要尚未取得的权限、数据、资源或外部反馈。先完成不依赖该条件的工作，
  记录可恢复位置及所需输入，准确报告尚未完成；普通澄清卡无人回复不单独构成这种阻塞。

结束整轮前，列明停止原因的作用范围、被阻塞的阶段和仍可独立推进的必要工作。
仍有后者时继续完成；若只剩无法在现有授权内解决的依赖、已止损的分支或等待选题确认，
交付真实状态即可，不为避免停止而扩大目标或虚构进展。已有工作稿不是跳过此核对的理由。

最终汇报简明说明完成、验证、未解决和发生过的默认决定。不能以“计划已列好”、
“下阶段可以开始”或子 Agent 自报成功结束仍可推进的全流程任务。
