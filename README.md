# Project Template

这个目录是单个项目的标准模板，适合执行型项目，也适合探索型项目。

将此目录复制后，重命名为：

`YYYY-MM-DD-project-name`

例如：

`2026-04-01-llm-infra`

## 推荐使用方式

如果是执行型项目：

- 先明确目标
- 判断任务是简单任务还是复杂任务
- 复杂任务先在 `tasks/milestones.md` 定义完整的 `M1` 到 `Mn`
- 按 `M1.1` 子目标和 `M1.1.1` 可执行任务逐层分解
- 按任务编号推进并更新状态、决策、测试和工作日志

如果是探索型项目：

- 先补背景知识
- 再整理术语、问题地图和研究笔记
- 最后再进入方案设计和实施

## 复制后优先修改

- `README.md`
- `AGENTS.md`
- `context/project-overview.md`
- `context/research-notes.md`
- `tasks/active.md`
- `tasks/milestones.md`

## 目录说明

- `context/`：背景知识、架构、术语、研究笔记
- `tasks/`：里程碑、任务、待办、决策
- `prompts/`：可复用提示词
- `logs/`：工作过程记录
