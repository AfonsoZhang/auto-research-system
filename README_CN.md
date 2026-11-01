<p align="center">
  <img src="assets/banner.png" alt="Auto-Research System：一群人把一座石门逐块拆掉，门后学生们拿着带图表的论文走向城市和产业园区。" width="100%">
</p>

# Auto-Research System 🔨（自动科研系统）

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat)](LICENSE) · [![README English](https://img.shields.io/badge/README-English-blue?style=flat)](README.md) · [![Skills](https://img.shields.io/badge/🧰_技能-37_个-7C3AED?style=flat)](#-里面有什么) · [![诚信对照表](https://img.shields.io/badge/🛡️_诚信对照-A–H_八族-2E7D32?style=flat)](.claude/skills/shared-references/integrity-patterns.md) · [![Runtime](https://img.shields.io/badge/运行于-Claude_Code-blue?style=flat)](#-快速开始)

<div align="center">

### 🔨 科研的门槛，吾辈来拆 —— 让每个想去工业界的人都拿得出一篇站得住的论文。

***Research should not be a gate. We take it down, so everyone heading into industry can bring a paper that holds up.***

</div>

> 一套跑在 Claude Code 上的端到端科研系统：从一个研究目标出发，到选定的题目、核实过的
> 文献、设计好并跑过 pilot 的实验、诚实的分析，再到一篇带配图、引用和复现材料、可以投稿的
> 论文。37 个技能、一个科研主控，在要紧的决定处设人工关口。

它能给你什么：

- **整条路，而不是某一步。**选题、文献与新颖性核查、选会议和 benchmark、实验设计、实现与
  pilot、分析、写作、配图、局限与 AI 使用声明草稿、审稿与 rebuttal。每个阶段都是可以单独
  调用的技能，也可以交给主控按顺序跑。
- **先有证据，再有结论。**每个数字都能追到原始结果文件，每条引用都经过核实，结论只说到
  证据撑得住的强度。
- **决定权在你。**选题批准、花钱、租算力、投稿和一切对外动作都等你点头。
- **不绑定厂商。**生图服务和外部评审在本地配置里自选；已授权的常规决策由主 agent 直接处理。

---

## 🧭 里面有什么

| | |
|---|---|
| **技能** | 37 个 Claude Code 技能，在 `.claude/skills/`。 |
| **共享科研规则** | 结论保真、按贡献类型分流、目标会议校准、选题、发表/版本规则、科研自主边界、摘要与结论写法、拆分审查，以及[诚信对照表](.claude/skills/shared-references/integrity-patterns.md)。在 `.claude/skills/shared-references/` 下。 |
| **科研主控** | `.claude/skills/research-agent-team/`：一个主 agent 在当前请求范围内协调各阶段；只有你明确开启时，自动模式才跑完整流程。 |
| **决策卡** | 自动模式下主 agent 直接选择并执行已授权方案，在现有任务记录中留下依据、理由和后续影响。 |
| **专职 agent** | `.claude/agents/`（分析、架构、实现、质检、编辑、需求；头脑风暴、选题批评、策略）。 |
| **文献工具** | arXiv、OpenAlex、Semantic Scholar、Exa（`.agents/aris/tools/`）。 |
| **Codex 评审桥** | `.agents/mcp-servers/codex-exec/` 下的 MCP 服务，用于跨模型评审（可选，需要 Codex CLI）。 |
| **路由规则** | `CLAUDE.md`。 |

---

## 📰 动态

- **2026-11-01** — 🚀 **v1.0。** 37 个 Claude Code 技能和科研主控；人工关口写进路由规则；
  生图服务、外部评审不绑定厂商；[诚信对照表](.claude/skills/shared-references/integrity-patterns.md)
  把每类论文缺陷对应到负责预防它的阶段；`paper-claim-audit` 开头新增确定性预检（增量算术、
  摘要数字在表里找不到、GRIM、不可能的标准差、p 值与统计量矛盾、重复表格、残留模板串）。

---

## 🗺️ 工作流

```mermaid
flowchart TD
    U(["你的研究目标"]) --> T["1 · 选题<br/>brainstorming-research-ideas · research-companion<br/>idea-evaluator · novelty-check"]
    T --> H{"👤 选题批准<br/>只能由你决定，模型、<br/>默认值、超时都不行"}
    H -- 修改 --> T
    H -- 批准 --> L["2 · 文献与证据<br/>research-lit · deep-research<br/>nature-reader · nature-ref-verifier"]
    L --> D["3 · 会议、benchmark 与实验设计<br/>select-venue · benchmark-research-skill<br/>experiment-plan"]
    D --> P["4 · 实现与最小 pilot<br/>experiment-bridge · run-experiment"]
    P --> G{"pilot 关卡<br/>analyze-results"}
    G -- "停止或重新设计" --> D
    G -- 继续 --> M["5 · 主实验与分析<br/>run-experiment · analyze-results<br/>失败和缺失的实验照样保留"]
    M --> W["6 · 论证与写作<br/>good-story · ts-paper-plan · paper-writer<br/>nature-figure · ts-paper-cite"]
    W -. "发现证据缺口" .-> M
    W --> X["7 · 局限与声明草稿<br/>limitation-and-risk-writer · ai-use-drafter"]
    X --> V["8 · 修订与核查<br/>诚信预检 → paper-claim-audit<br/>pre-submission-reviewer · paper-polish"]
    V -. "改证据，<br/>不改措辞" .-> M
    V --> F(["9 · 交付<br/>论文、复现材料、<br/>核查结果、遗留问题"])
    F --> O{"👤 投稿、发布、推送<br/>须经你授权"}

    classDef human fill:#FFF4CC,stroke:#B45309,color:#000
    classDef gate fill:#E8F5E9,stroke:#2E7D32,color:#000
    class H,O human
    class G gate
```

默认情况下，每个请求只跑它需要的阶段，做完就停；技能建议的下一步不等于允许继续。
自动模式会沿着这张图跑到约定的终点，但仍会在两个 👤 关口停下等你。综述、理论、立场和
复现类论文会跳过不适用的阶段。

---

## 🚀 快速开始

```bash
git clone <本仓库> research && cd research
./install.sh                 # WITH_DIAGRAMS=1 ./install.sh 会顺带装好示意图渲染
claude
```

`install.sh` 从 `config/*.example.json` 在 `.tools/` 下生成本地配置（不进版本库），
生成对应宿主的 MCP 配置；Codex 安装会准备 Claude 外审桥依赖。无需独立决策模型。
需要 Python 3.10+、生图需要 Node 18+，以及 Claude Code。Codex CLI 可选：外部评审和内置生图工具
要靠它。

### 配置（全部可选）

| 组件 | 文件 | 可选项 | 不配置时 |
|---|---|---|---|
| 生图 | `.tools/image-provider.json` | Codex 内置 `image_gen`（默认）或 Antigravity 内置 `generate_image`（Nano Banana，`"provider": "antigravity"`）；任何返回图片的 OpenAI 兼容对话端点；另有 Poe、OpenRouter 适配器 | 经 Codex 桥调用内置 `image_gen` 工具；Codex 或该工具不可用时如实报告无法生成 |
| 外部评审 | `.tools/reviewer.json` | Codex MCP（服务商随你的 Codex CLI），或人工评审 | 如实报告外部评审不可用，绝不拿自评顶替 |
| 语言润色（可选） | 无；只在你要求时使用 | 默认 Gemini 4 Argon，经会话中可用的 Gemini 工具调用（Antigravity `agy` MCP 或 Gemini CLI）；只改语言，每处改动审核后才采用 | 由 Claude 润色 |
| 文献 API | 环境变量 | `EXA_API_KEY`、`SEMANTIC_SCHOLAR_API_KEY`、`OPENALEX_EMAIL` | 用免密钥来源，并报告覆盖缺口 |

密钥一律从配置里指定的环境变量读取。手动运行辅助脚本时，把 `RESEARCH_ROOT` 设为仓库
路径。自动模式的常规决策由主 agent 直接处理，无需单独配置决策模型。

---

## 🎯 为什么做这个

很多想去工业界的人卡在第一篇论文上：方法都懂，但把想法变成经过检查的实验、诚实的
分析、审稿人愿意接收的论文，这套本事很少有人系统地教。agent 能干掉其中很大一部分活，
但放任不管，它也会产出看着写完了、其实站不住的论文：摘要里的数字哪张表都没有、"提升 16%"实际只有
6.7%、baseline 根本没调参、引用查无此文。

这套系统的设计目标是：速度永远不从这些捷径里来。

## 🔒 怎么保证诚实

1. **先有证据，再有结论。** 论文里每个数字都能追到原始结果文件。`paper-claim-audit` 用
   一个全新的、零上下文的跨模型评审，只给它论文源码和原始结果。
2. **改证据，不改措辞。** 一条问题的解决方式只能是：改正数字、补上缺的实验或 baseline、
   或把结论收窄到证据范围内（[结论保真](.claude/skills/shared-references/claim-preservation.md)）。
   改写措辞让检查对不上、缺陷却还在，不算修复。
3. **每类缺陷都有人管。**[诚信对照表](.claude/skills/shared-references/integrity-patterns.md)
   写明每类缺陷（数字、范围、baseline、实验、引用、表面呈现、证明、评测设计）由哪个阶段
   预防、投稿前由哪项检查查出。
4. **预先定好的标准不改。** 看到结果后不经披露不改标准；pilot 失败就停止后续花费；失败和
   缺失的实验留在分析里。
5. **要紧的决定留给人。** 新选题的批准永远等你，任何超时、默认值或模型都放行不了。超出
   授权预算的花费、租算力、推代码、投稿和其他对外动作，也都要你点头。

## 🧭 行为方式

- **一个请求，一个范围。** 技能做完被要求的工作和必要检查就停；技能里写的"下一步"不等于
  允许继续。
- **自动模式**只有你为某个任务明确开启（输入 `/research-auto [任务与终点]`）时才跑完整流程。主 agent 直接推荐并执行已有授权内的常规选择，记录依据和理由。
  选题批准和新增授权仍由你决定，独立外审保留。

---

## ⚠️ 局限（信任任何一次运行之前必读）

- **已测试：**宿主适配（Codex 视图、Claude 外审桥、决策模型退役；codex-exec 外审桥和 `/research-auto`）、生图适配器（13 项）、诚信预检（干净样例加 8 种
  注入缺陷，以及不带前导零的小数）、nature-response（7 项）和
  nature-shared（5 项）包检查。大多数技能是说明文件，没有自动化行为测试。
- **诚信预检基于正则抽取。**只能查到抽取器认出的内容，零发现不等于没问题。没装 scipy 时
  只复核 z 检验的 p 值。
- **诚信对照表是预防，不是证明。**所有检查都过了不等于论文正确，审稿人仍可能查出问题。
- **会议规则、截稿日期和排名**必须对照官方页面重新核实。

---

## 🧬 致谢

本项目建立在开源社区的工作之上，改编、并在部分地方直接复用了以下项目。衷心感谢各位作者和贡献者：

| 来源 | 用于 |
|---|---|
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) (ARIS) | research-review、paper-claim-audit、research-lit、novelty-check、experiment-plan、experiment-bridge、run-experiment、analyze-results、文献工具、codex-exec 评审桥 |
| [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | paper-writer、paper-polish、intro-drafter、deep-research、idea-evaluator、pre-submission-reviewer、figure-designer、rebuttal-guidance 等写作类技能 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | nature-figure、nature-reader、nature-ref-verifier、nature-response |
| [andrehuang/research-companion](https://github.com/andrehuang/research-companion) | research-companion 及 brainstormer、idea-critic、research-strategist 三个代理 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | brainstorming-research-ideas、creative-thinking-for-research |
| [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | ts-paper-plan、ts-paper-cite 及论文模板 |
| [wanshuiyin/Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch) | 诚信预检的 4 个脚本、诚信地图依据的缺陷分类；README 版式 |
| [wanshuiyin/HERO-Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense) | README 版式 |
| [ShaishavMaisuria/research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) | select-venue |
| [Rimagination/good-story](https://github.com/Rimagination/good-story) | good-story |
| [EternalWavee/benchmark-research-skill](https://github.com/EternalWavee/benchmark-research-skill) | benchmark-research-skill |
| [UKGovernmentBEIS/inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) | 基准有效性检查清单 |
| [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | limitation-and-risk-writer |
| [Airjiannan05/research-paper-workflow-skill](https://github.com/Airjiannan05/research-paper-workflow-skill) | 实验记录规范 |
| [panbibliotekar/gaidet-declaration](https://github.com/panbibliotekar/gaidet-declaration) | AI 使用声明术语（ai-use-drafter） |
| [blader/humanizer](https://github.com/blader/humanizer) | paper-polish、paper-writer 的去 AI 腔检查 |
| [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | paper-polish、paper-writer 的去 AI 腔检查 |
| [acl-org/acl-style-files](https://github.com/acl-org/acl-style-files) | ACL LaTeX 样式文件 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 选题方法的思路（未复制原文） |
| [joshzyj/open-scholar-skill](https://github.com/joshzyj/open-scholar-skill) | 范文知识库的思路（未复制原文） |

选题方法部分还参考了 Fischbach, *Cell* 2024（[doi:10.1016/j.cell.2024.03.012](https://doi.org/10.1016/j.cell.2024.03.012)）。各组件保留原有声明，版本与许可证见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。如有遗漏或标注不准，请告诉我，我会马上改正。

## 🙋 欢迎批评指正

我在科研和工程上都还是小白，这是第一次做这样的系统，错误和不完善之处一定不少，恳请各位大佬批评指正。非常欢迎提 [Issue](../../issues) 和 [PR](../../pulls)，大小都行：报 bug、指出规则错误、文档不清楚、更好的思路都可以。

## ⚖️ 许可证

CC BY-NC-SA 4.0（[`LICENSE`](LICENSE)）：可在非商业目的下分享和改编，需署名并以相同许可证
发布。改编自其他项目的组件保留原有声明，见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

## Codex 版本

保留 Claude 原版，同时提供 Codex 宿主适配。Codex 负责执行、写作和默认润色；
外部审查交给 Claude。全面审查仍拆为材料审计与论文审查，分别由 Codex 子代理和
Claude 执行。选题人工确认、证据要求、产物格式和流程阶段保持原样。

```bash
bash install.sh --host codex
codex
```

在可信项目中重启 Codex，使项目 MCP 和技能生效。使用 `$paper-polish`、
`$research-review`；明确输入 `$research-auto` 才开启当前任务的自动模式。
`AGENTS.md` 是 Codex 入口，`.agents/skills/` 是生成目录；更新原技能后运行
`python3 scripts/build_codex.py`，不要直接编辑生成文件。原有 37 个可加载技能
全部保留，另补齐 `research-auto` 入口。

Claude 审查需要已登录的 Claude CLI，并支持 `--print --output-format json`、
`--effort`、`--tools` 和 `--strict-mcp-config` 等参数。配置写在
`.tools/reviewer-codex.json`，默认 `opus`，深审/常规 effort 为 `high`/`medium`；
可用 `CLAUDE_REVIEW_MODEL`、`CLAUDE_REVIEW_EFFORT_DEEP`、
`CLAUDE_REVIEW_EFFORT_REGULAR` 覆盖。Claude 原版仍使用 `.tools/reviewer.json`，
两者互不覆盖。审查桥只开放读取工具，不开放命令执行、写入或嵌套 MCP。
调用方声明的执行模型会如实标注，不能冒充宿主认证的独立性证据。

安装保留已有本地配置，新增项目级 `.codex/config.toml` 的缺失 MCP 表，
不修改用户级 Codex 配置。宿主接口差异集中在
[Codex 适配约定](config/codex/host.md)；科研规则和辅助脚本仍取自原版。
生图优先使用当前 Codex 会话的原生图像工具，不绕到审查器。

适配验证：`python3 -m unittest discover -s tests -v`。
