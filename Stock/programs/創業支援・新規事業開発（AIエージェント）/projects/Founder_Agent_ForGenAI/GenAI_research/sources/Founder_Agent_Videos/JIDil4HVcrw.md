---
title: "Joining us from our New York City lab, Ada Mujad is exploring how neuroscience can inform artificial intelligence."
video_id: "JIDil4HVcrw"
video_url: "https://www.youtube.com/watch?v=JIDil4HVcrw"
speaker: "Idamo"
channel: "Unknown"
date: ""
duration: ""
tags: ["AI", "Agents", "LLM", "Tutorial", "Development"]
topics: ["AI", "Agents", "LLM", "Tutorial", "Development"]
summary: |
  Joining us from our New York City lab, Ada Mujad is exploring how neuroscience can inform artificial intelligence
  Her research on brain inspired agenic architectures shows how multiple LLMs can collaborate like neurons in the brain, improving reasoning, planning, and even reducing hallucinations
  This is the kind of curiositydriven science that lays the foundation for future breakthroughs
key_points:
  - "Covers ai agents concepts and applications"
  - "Discusses AI, Agents, LLM"
  - "Suitable for learning and reference"
category: "AI Agents"
confidence_level: "medium"
source: "Founder_Agent_Videos"
retrieved_at: "2025-12-30T10:24:13+09:00"
---

# Transcript: JIDil4HVcrw

- URL: https://www.youtube.com/watch?v=JIDil4HVcrw
- Retrieved at: 2025-12-30T10:24:13+09:00

## Text

- [00:11] Joining us from our New York City lab,
- [00:13] Ada Mujad is exploring how neuroscience
- [00:16] can inform artificial intelligence. Her
- [00:19] research on brain inspired agenic
- [00:22] architectures shows how multiple LLMs
- [00:25] can collaborate like neurons in the
- [00:27] brain, improving reasoning, planning,
- [00:29] and even reducing hallucinations. This
- [00:32] is the kind of curiositydriven science
- [00:34] that lays the foundation for future
- [00:36] breakthroughs. Over to you, Ida.
- [00:51] Hello, I'm Idamo Manad, principal
- [00:54] researcher at Microsoft Research New
- [00:56] York City. Today I will talk to you a
- [00:58] little bit about how brain inspired
- [01:00] agentic architectures built with LLMs
- [01:02] can improve multi-step reasoning.
- [01:05] Large language models demonstrate
- [01:07] impressive performance on a variety of
- [01:08] tasks like writing emails or answering
- [01:11] questions.
- [01:13] But LLMs and agentic AI systems often
- [01:16] struggle with tasks that require
- [01:17] multi-step reasoning or goal- directed
- [01:19] planning, which are necessary skills in
- [01:22] many real world applications. Think
- [01:24] about planning a trip, coordinating a
- [01:26] project, or enforcing safety rules in a
- [01:29] sequence of steps. Those are problems
- [01:32] that require multi-step reasoning and
- [01:34] planning. You need to keep track of
- [01:35] where you are,
- [01:38] what's allowed, and what you're trying
- [01:40] to achieve. And this way you take
- [01:42] actions and track your goals. These
- [01:44] skills are crucial for users,
- [01:46] organizations, and Microsoft customers
- [01:48] who wish to deploy generative AI in
- [01:50] their work. In our earlier work, we have
- [01:52] rigorously shown failure modes of large
- [01:54] language models in solving simple
- [01:56] multi-step reasoning tasks like
- [01:58] navigating a building described in text
- [02:01] or passing a message in a network of
- [02:03] colleagues. While the models often sound
- [02:06] confident, we found that they commonly
- [02:07] propose illegal moves and hallucinate
- [02:10] paths that get stuck in loops or wander
- [02:12] off detours. For users and Microsoft
- [02:15] customers, improving multi-step
- [02:17] reasoning and planning is not just
- [02:18] academic, it's a necessity.
- [02:22] This is why we propose a modular agentic
- [02:25] planner or map inspired by the brain to
- [02:28] solve these problems.
- [02:30] To address these challenges, we took
- [02:32] inspiration from the human brain in
- [02:34] which planning is accomplished via
- [02:36] component processes that are
- [02:37] predominantly associated with specific
- [02:39] brain regions. These processes include
- [02:42] task decomposition, task coordination,
- [02:45] conflict monitoring, [clears throat]
- [02:46] state prediction, and evaluation.
- [02:49] A key insight from our research was that
- [02:51] when testing LLMs on individual
- [02:54] functions or processes, we find that
- [02:56] they are often capable of carrying out
- [02:58] these functions in isolation. However,
- [03:00] they struggle to autonomously coordinate
- [03:02] them in the service of a goal. Inspired
- [03:05] by these findings, we designed a brain
- [03:08] inspired architecture with specific
- [03:10] brain inspired modules.
- [03:13] Here is how map or our modular agentic
- [03:15] planner works.
- [03:18] It is designed with functional rules,
- [03:20] communication protocols, and iterative
- [03:22] algorithmic steps for collaborative
- [03:24] problem solving inspired by the brain.
- [03:27] The brain inspired interactions include
- [03:29] the actor proposing actions in response
- [03:32] to a prompt to solve a task. The monitor
- [03:35] checking whether those actions are valid
- [03:37] or hallucinations and gating them. The
- [03:40] predictor and evaluator then taking the
- [03:42] actions that pass that first stage and
- [03:45] then doing its research to predict its
- [03:47] future and evaluate whether it's the
- [03:48] right outcome and the orchestrator
- [03:50] determining when the goals are achieved.
- [03:53] This is implemented with specialized
- [03:55] prompting of LLM instances where roles
- [03:58] and interaction protocols are all
- [04:00] inspired by the brain.
- [04:02] What we found is that MAP yields
- [04:05] significant improvement over both
- [04:06] standard LLMs at zeroshot and multi-shot
- [04:11] examples and competitive agentic
- [04:14] baselines. For instance, on tower of
- [04:16] Hanoi, we show that map improves
- [04:19] performance from 11% for GPT4 zeroot
- [04:23] to 74% for map that's been designed with
- [04:27] all GPT4 agents.
- [04:29] Graph traversal was improved from 50%
- [04:32] for our best baseline to 95% on a
- [04:35] fourstep path. In terms of errors and
- [04:38] hallucinations, map had 0% invalid moves
- [04:42] even in out of distribution tasks
- [04:46] whereas the other methods had up to 31%
- [04:49] hallucination. MAP also shows superior
- [04:51] transfer learning between tasks and out
- [04:54] of distribution. A notable outcome was
- [04:56] that when we built map with a smaller
- [04:59] and more costefficient LLM, meaning
- [05:01] Llama 7TB as opposed to GPT4,
- [05:05] we saw superior performance and transfer
- [05:07] across tasks. So as a summary, map can
- [05:10] improve accuracy, reliability, and
- [05:13] potentially safety in AI systems. In
- [05:16] parallel work published in artificial
- [05:18] life, we explored topologies of
- [05:20] multi-agent architectures for collective
- [05:23] innovation. Together, this line of
- [05:25] research findings offers a blueprint to
- [05:28] advance future end-to-end architectures
- [05:30] beyond transformers that readily
- [05:32] incorporate MAP's multi-level and
- [05:34] multi-rule computations to improve
- [05:36] performance, reliability, and safety.
- [05:40] This has implications for customers real
- [05:42] world needs and their trust way beyond
- [05:45] our toy research tasks. Together, we can
- [05:49] use human- centered and brain inspired
- [05:51] methods in the service of mitigating
- [05:53] inaccuracies and risks and improving
- [05:56] performance of our AI systems with
- [05:58] rigorous methods. Thank you.
