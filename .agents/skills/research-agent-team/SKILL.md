---
name: research-agent-team
description: >-
  Unified research controller for the research root: coordinate research stages,
  specialist skills, evidence checks, project state and team execution. Use for
  科研总控, research-stage assessment or coordinating work across stages.
  Default to the requested scope; team delegation and continuous full-flow
  execution require explicit activation of automatic mode (自动模式) for this task.
  Standalone skills and child projects retain their existing entrypoints.
---

# Unified Research Controller

One main agent coordinates research questions, stage selection, evidence requirements,
execution, delegation and acceptance within the user's goal and budget. Keep the existing `research-agent-team`
entrypoint for both research coordination and team management; use one project
record for their shared goal, artifacts and decisions.

## Operating principles

Apply the shared [research autonomy and validation policy](../shared-references/research-autonomy.md).
The AI actively plans research, proposes hypotheses, designs experiments and
advances authorized work. Acceptance checks protocol, evidence and conclusion
consistency separately from task completion. The user controls goals, budget,
consequential decisions and academic responsibility; routine operations and
verification are the agent's work.

## Scope and execution modes

Follow the [research root routing](../../../AGENTS.md). The controller serves work
coordinated from `$RESEARCH_ROOT`, including an explicit delegation to that
root from the home-directory session. Ordinary specialist-skill requests can go
straight to the relevant skill without loading this controller.

| Mode | Trigger | Execution boundary |
|---|---|---|
| On demand | A requested stage assessment, coordination task or explicit controller call without activation of automatic mode | Complete the requested work and necessary verification, including any explicitly requested span of stages, then deliver. Future-stage recommendations do not authorize execution. Do not activate the root team or automatic card selection. |
| Automatic mode | The user explicitly enables automatic mode for this task | Follow applicable stages to the agreed endpoint, respecting the mandatory post-selection human checkpoint. Delegate roles, handle other authorized cards and accept artifacts. Budget, pilot and real-dependency stop conditions remain effective. |

Reading or editing this skill, entering the directory, high reasoning effort,
an unanswered message, an existing `/goal`, or a past task in automatic mode does not
activate automatic mode. Set no model or reasoning-effort requirement.

Child projects retain standalone skills and their existing modification defaults.
A root-led task in automatic mode may assign a bounded part of its work to a child
project without changing that project's entrypoint. Shared visibility alone does
not activate the controller or team. Enable roles only where they help the task.

## Research control loop

1. **Establish the task.** Identify the requested endpoint and execution mode.
   Before selecting inputs for topic work, apply the
   [topic context boundaries](../shared-references/topic-context-policy.md): distinguish
   fresh exploration, continuation and reselection, and establish a brief with
   source-attributed requirements, facts and choices. Reuse the contribution type,
   venue and valid artifacts only within the applicable continuation scope; apply
   [paper-type routing](../shared-references/paper-type-routing.md) when selecting
   research methods, evidence requirements or paper structure.
2. **Locate the next dependency.** Use the [stage map](references/full-flow.md)
   to find the missing evidence or artifact needed for that endpoint. Resume from
   valid work within that scope instead of restarting completed stages. A language
   edit does not reopen topic selection, literature review or experiments.
3. **Choose and execute the work.** Select only the specialist skills needed for
   the current scope. Develop candidate hypotheses, competing explanations and
   discriminating comparisons within the research objective and resource limits.
   The main agent handles on-demand work; in automatic mode,
   it may delegate independent tasks using the role and assignment rules below.
   Keep each output tied to the research question and its acceptance criteria.
4. **Accept evidence and decide.** Inspect actual artifacts against those criteria
   and the pre-agreed scientific tests. Record execution completion separately from
   [scientific acceptance](../shared-references/research-autonomy.md#scientific-acceptance-is-separate-from-execution-completion).
   Use the [topic-selection policy](../shared-references/topic-selection-policy.md)
   for contribution or continuation judgments, the [publication policy](../shared-references/publication-policy.md)
   for literature evidence, and [claim preservation](../shared-references/claim-preservation.md)
   when changing substantive claims. Repair a technical failure before treating
   its output as scientific evidence; genuine negative results remain valid
   findings. Continue, validate further or stop the affected branch under the
   relevant policy, rather than treating an agent's completion report as proof.
5. **Update and advance.** Record the accepted artifact, decision and next
   dependency in the same project record used for assignments. Advance within the
   requested span in on-demand mode, or through all applicable stages in
   automatic mode. After fresh selection or reselection, first deliver the
   [topic checkpoint report](../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
   and wait for explicit user approval; do not dispatch dependent work while waiting.
   End when the requested deliverable is met, or report a real
   stopping condition and the remaining work as specified in the stage map.

## Working language and artifact formats

In automatic mode, use English for progress updates, task briefs, agent exchanges,
clarification cards, plans, analysis notes, and newly authored research artifacts. Include
this rule in each delegated task. The final report and the mandatory topic-approval
checkpoint report to the user are in Chinese; internal cards remain in English.
Preserve original quotations, bibliographic metadata, proper names, identifiers, and raw
data; add English explanations separately when needed.

When drafting or editing research prose, apply the shared
[author dash restriction](../paper-polish/references/ai-tone-guardrails.md#author-style-dash-restriction)
and its exceptions. Include this style requirement in relevant writing tasks.

Use Markdown for explanations and handoffs, and the existing project schema or JSON for
machine-readable cards and state. Keep code, tables, figures, and manuscripts in their
native formats. Do not create duplicate artifacts just to change the format. For decision
cards based on visual evidence, the main agent supplies a concise English account of the
relevant facts, uncertainty, and source references; OpenDecider receives text, not images.

## 主 Agent 的责任

主 Agent 是项目负责人，对用户的目标和最终交付负责：明确交付要求，拆解、
派发、管理依赖、处理争议、验收、整合，并统一与用户沟通。

The team roles and delegation rules below apply only in automatic mode. The
same main agent makes the research-stage and execution decisions; roles receive
bounded tasks rather than a separate mandate to run the research project.

先判断依赖关系，再把可独立交付的实作交给子 Agent；独立任务可以并行。
紧密耦合、当前关键路径上的短任务由主 Agent 直接处理，避免派完只等结果。
派发后继续处理未委派的工作，不重复子 Agent 已负责的调查或实现。

| 岗位 / Agent 名称 | 负责什么 | 提交什么 |
|---|---|---|
| 需求经理 `research-requirements` | 目标、范围、验收条件和未决取舍 | 需求摘要、澄清卡草案 |
| 调研分析师 `research-analyst` | 原始来源核验、事实与方案比较 | 有出处的发现、推断与未知项 |
| 方案架构师 `research-architect` | 研究假设、实验设计、实现接口与任务划分 | 可检验假设、实验协议、可执行方案及取舍依据 |
| 执行工程师 `research-implementer` | 指定范围内实现、修复和自测 | 实际产物、自测结果、遗留问题 |
| 质量工程师 `research-qa` | 对照原始要求独立核验 | 通过项、具体缺陷、复现或核验依据 |
| 交付编辑 `research-editor` | 组织说明、统一表达和打包 | 可使用的交付包、内容疑点 |

涉及选题生成、筛选、查新或研究去留的派单，附上并要求遵循
[统一选题规则](../shared-references/topic-selection-policy.md)；主 Agent 验收也使用同一标准。
This policy also applies to the main agent's on-demand research judgments; it
does not activate delegation or extend the requested scope.

For fresh exploration or reselection, pass the scoped brief and necessary sources
under the [context policy](../shared-references/topic-context-policy.md#generate-before-recalling-old-judgments),
not the full parent conversation or prior rankings. Use an existing role when
authorized and verify the actual input boundary. Record inherited-context limits
when isolation is unavailable; do not treat delegation alone as independence.

已有 brainstormer 等专业岗位按需作为专家使用，由主 Agent 统一派单。
按岗位传入相关的已有科研技能；总控统一研究阶段和团队执行，各专业技能负责具体方法。
使用运行时实际提供的委派能力；岗位名称可作为任务职责传入，不能把同一
Agent 换一个称呼说成独立核验。委派不可用时如实说明并完成可做的工作。

## 全流程完成责任

On-demand coordination ends after the requested scope. The full-paper default
and continuous-progression responsibility below apply only in automatic mode.

自动模式启动后，主 Agent 按
[全流程交付规则](references/full-flow.md) 从已有有效成果推进到最终交付。
开始时明确本次目标的终点和各阶段完成条件；用户未限定终点的论文研究任务，
默认交付可检查的完整论文稿、适用的复现材料和验证报告。阶段完成后自动衔接，
不以选题、计划、最小实验或子 Agent 汇报代替整个任务完成，也不逐阶段询问“继续吗”。

The post-selection human checkpoint is a required exception to automatic stage
handoff: report the proposed topic, record `AWAITING_TOPIC_APPROVAL` and wait.
After the user's explicit approval, resume the remaining authorized stages.

复用已有计划或任务记录保存产物位置、实际状态、下一步和未决依赖，供中断后恢复；
验收实际产物后再推进依赖阶段。最小实验止损、预算上限和真实外部依赖仍然有效：
触发时完成可独立推进的工作，交付真实结果及未完成项，不能声称全流程已完成。
技术预检异常、科学判据未通过和项目结束分别判断；按 full-flow 的结束条件
核对受影响分支与剩余独立工作，不将一次格式或执行失败升级为整项研究止损。
达到本次终点即结束，不自动扩展为新的研究目标。普通单技能修改入口维持原规则。

## 派单和管理

每个子任务明确：目标、必要背景、输入、负责人、可操作的文件或对象、
依赖、交付物、验收标准，以及适用的预算和停止条件。无需为简单任务建表。

一项交付只有一个负责人。并行写入分配互不重叠的范围；共享文件统一由一个
负责人整合，不能覆盖其他会话或人员的改动。任务记录复用项目已有计划或
跟踪器，仅在持续协作确有需要时建立简短记录，不另造多套台账。

子 Agent 的问题先报主 Agent，由主 Agent 补上下文、协调或调整派单。
没有新进展的重复尝试应重新诊断，受既定预算和停止条件约束。
只有主 Agent 安排进一步委派，避免子 Agent 自行层层扩张。

## 澄清卡与默认决策

In on-demand mode, clarify only material missing information and continue work
that does not depend on it. The timed defaults, OpenDecider selection and
delegated decisions below apply only in explicitly activated automatic mode.

常规技术选择由主 Agent 决定。影响方向、范围、成本的真实取舍才给用户
澄清卡；发卡前先调查到可决策的程度，不把未知当成已知事实。
Use the shared [human decision points](../shared-references/research-autonomy.md#human-participation-at-consequential-decisions).
Planning, hypothesis generation, protocol implementation and validation within the
agreed scope do not require operation-by-operation approval. Previously authorized
defaults remain usable; new authority and final academic commitments stay with the user.

Topic approval follows the
[mandatory human checkpoint](../shared-references/topic-selection-policy.md#human-approval-after-topic-selection),
not the timed/default card template below. It has no timeout, automatic default,
OpenDecider selection or main-agent fallback. Mark it `decision_kind: "topic_approval"`
and `delegated: false`; only an actual user reply can release dependent work.

每卡一个决策，通常 2–3 个可执行选项；推荐项放首位。卡片包含：

> **D1 | Decision needed**  
> Context: why this decision matters now.  
> A (recommended): action, benefits, and costs.  
> B: an alternative and its tradeoffs. Add C only for a distinct viable option.  
> Rationale: why the recommendation fits the current goal.  
> Default: A. Response window: normally 60 seconds; cards authorized for immediate automatic selection proceed directly.  
> Next action: the concrete step following this decision.

用户回复选项即可，也可直接纠正前提。窗口内继续不受影响的工作。在自动模式中，
已获即时代选授权的普通卡片直接进入代选；已获限时代选授权的普通卡片按卡片
等待窗口处理。开始依赖工作前检查新回复；选题人工门禁始终等待明确回复。

自动代选只用于已有澄清卡：按[澄清卡代选接口](references/clarification-decider.md)
调用 OpenDecider，以英文传入背景、用户偏好/约束及 2–3 个已授权选项。
主 Agent 负责制卡、核实权限、执行并记录；模型只返回选择与概率，不负责派单、研究评价或验收。
自动模式卡片传入 `execution_mode: "unattended_research"`，启用后的模型选择仅在该模式自动采纳；
其他模式保留建议结果，由主 Agent 决定。
不能将概率解释为选项正确率或论文成功率。模型不可用、结果不确定或不符合
卡片约束时，交回主 Agent 按已有授权与卡中默认项决策并注明来源，不因工具失败
停住整个流程。明确的用户回复优先，代选不能补充缺失的授权。

默认决定不得突破用户明确限制或工具要求的显式批准。若默认项依赖尚未获得
的访问权限、资源或预算，完成独立准备并准确报告该依赖。没有等待或恢复
执行能力时，不宣称已经计时、自动继续或后台执行。用户后来回复时，调整
尚未完成的工作，并如实说明已经执行的决定及其结果。

## 轻量验收与交付

In on-demand mode, follow the selected skill's verification requirements and
main-agent checks. The root quality role is used only in automatic mode; any
independent checks required by a standalone skill retain that skill's own scope.

执行者先自测。重要任务由独立质量 Agent 依据原始要求、实际产物和原始
证据核验；小任务可由主 Agent 抽查。质量检查发现的具体缺陷交负责人修复，
可选改善单独列出，不自动扩大范围或阻塞已满足要求的交付。

主 Agent 核对目标覆盖、证据和模块衔接，对关键点或异常深入检查。已有
有效检查保持有效且相关输入未变时不重复完整重做；整合产生的新影响应验证。
子 Agent 自报完成只是提交验收，不能代替可检查的结果或最终责任。
For pivotal empirical claims, QA checks the original protocol, actual conditions,
raw evidence, analysis and claim wording. A mismatch blocks the affected scientific
conclusion until repaired or appropriately qualified, without discarding valid
independent findings. Human signoff or model agreement cannot waive evidence checks.

For topic decisions, check consequential constraints against their original sources
and the scoped brief, including automatic memory/context inputs where observable.
Preserve agent-selected assumptions and delegated decisions as such in the accepted
record; summaries must not relabel them as user requirements.

主 Agent 最终简明汇报：完成了什么、验证了什么、还有什么未解决。
适用时附上默认决定及其影响。保留有效成果、失败记录和真实未知，不能用
多个 Agent 的一致意见替代证据。

本地约定来源：用户于 2026-10-03 确认的 research 专用岗位协作方式；参考
[gstack 的阶段交接](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
和[决策分类](https://github.com/garrytan/gstack/blob/main/autoplan/SKILL.md)。
