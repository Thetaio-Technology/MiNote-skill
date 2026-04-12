<div align="center">

# minote-skill

### 不是再造一个浏览器驱动。

### 是把小米云笔记待办，变成 AI 和人都能直接调用的能力。

[![Layer Skill](https://img.shields.io/badge/Layer-Skill-8A2BE2.svg)](#minote-skill)
[![Runtime minote--driver](https://img.shields.io/badge/Runtime-minote--driver-111827.svg)](#它和-minote-driver-是什么关系)
[![Local First](https://img.shields.io/badge/Local-First-0EA5E9.svg)](#它适合谁)
[![Todo Ready](https://img.shields.io/badge/MiNote-Todo_Ready-22C55E.svg)](#当前能力)

</div>

<div align="center">

**你不该每次都从 Selenium、选择器、登录态开始。**

**你需要的是一个已经能跑、能调、能接进 agent 的 skill 层。**

</div>

---

<div align="center">

你想让 AI 帮你读待办？`minote-skill` 直接给你入口。

你想让 AI 帮你新建待办？`minote-skill` 直接给你协议。

你想把小米云笔记接进自己的产品或工作流？`minote-skill` 直接给你一层可调用封装。

你不需要先理解整套浏览器自动化细节，才能把这项能力用起来。

</div>

---

## 它是什么

`minote-skill` 把 `minote-driver` 的底层自动化能力，包装成更适合 agent、产品集成方和终端体验层使用的 skill 能力。

它的目标不是再造一个浏览器驱动，而是把已经验证过的执行能力，变成：

- 一句能力描述能理解
- 一个统一入口能调用
- 一份结构化结果能返回

换句话说：

- `minote-driver` 负责把事做成
- `minote-skill` 负责把这件事变得更容易被调用

## 当前能力

当前第一个能力包是：

- `minote-todo`

它已经能完成：

- 读取未完成待办
- 读取已完成待办
- 创建待办
- 修改待办标题
- 标记完成
- 恢复待办
- 删除待办

## 它适合谁

适合：

- 想把小米云笔记待办接进 agent 的开发者
- 想做个人工作流自动化的人
- 想把待办操作封装成产品能力的人
- 想要一个本地、可控、真实可跑的执行后端的人

## 它和 minote-driver 是什么关系

当前策略是明确分层：

- `minote-driver`：执行层、CLI、验证脚本、运行时约束
- `minote-skill`：skill 定义、调用协议、上层能力包装

driver 负责真实执行，skill 负责稳定暴露能力。

## 仓库内容

这个仓库是 skill-facing 仓库，主要包含：

- `README.md`：展示页和定位说明
- `SKILL.md`：顶层 skill 定义
- `skills/minote-todo/SKILL.md`：具体能力包定义
- `skills/minote-todo/interface.md`：接口契约
- `skills/minote-todo/examples.md`：调用示例
- `skills/minote-todo/checklist.md`：执行检查项

## 运行时说明

`minote-skill` 自身不是浏览器自动化 runtime。

底层执行由 `minote-driver` 提供。这个仓库更适合：

- 对外展示 skill 能力
- 承载 agent 集成文档
- 承载机器可读 manifest
- 作为从 `minote-driver` 同步发布出来的 skill 仓库
