---
title: "- URL: https://www.youtube.com/watch?v=lx813D-mb7Y"
video_id: "lx813D-mb7Y"
video_url: "https://www.youtube.com/watch?v=lx813D-mb7Y"
speaker: ""
channel: ""
date: ""
duration: ""
tags: ["AI", "machine_learning", "investment", "funding"]
topics: ["資金調達", "AI技術"]
summary: |
  - URL: https://www.youtube.com/watch?v=lx813D-mb7Y
  - Retrieved at: 2025-12-30T16:09:09+09:00
  - [00:11] As we progress in all directions of
key_points:
  - "- [02:18] orchestrator must decide whether to"
category: "AI技術"
confidence_level: "high"
---


# Transcript: lx813D-mb7Y

- URL: https://www.youtube.com/watch?v=lx813D-mb7Y
- Retrieved at: 2025-12-30T16:09:09+09:00

## Text

- [00:11] As we progress in all directions of
- [00:13] research at MSR, we stay true to a core
- [00:15] part of our mission, advancing AI
- [00:18] responsibly by understanding not just
- [00:20] what these systems can do, but how and
- [00:23] why they sometimes fail. Tyler Payne, a
- [00:26] senior research software engineer with
- [00:29] Microsoft Research AI Frontiers in New
- [00:31] York City, is investigating how AI
- [00:34] agents perform when they're given access
- [00:36] to multiple tools, from calculators to
- [00:39] code interpreters. Surprisingly, his
- [00:42] findings show that adding more tools can
- [00:45] sometimes hurt performance, introducing
- [00:47] tool space interference. Over to you,
- [00:50] Tyler.
- [01:02] Hi, my name is Tyler and I'm a research
- [01:04] engineer at Microsoft Research AI
- [01:06] Frontiers. Today I'm going to be talking
- [01:08] about an emerging problem for LLM agents
- [01:11] that we call toolspace interference.
- [01:14] This was an exploration done over the
- [01:15] summer of 2025 in collaboration with my
- [01:17] colleagues here at AI Frontiers. AI
- [01:20] agents powered by LLMs have become a
- [01:22] popular topic in both research and
- [01:24] industry. In general, an agent is a
- [01:27] system that can sense and affect its
- [01:28] environment in pursuit of a goal. LLM
- [01:31] agents are usually software systems that
- [01:33] equip LLM with tools they can use to
- [01:35] understand and manipulate their
- [01:37] environment to complete tasks on behalf
- [01:39] of their users. Often, these agents act
- [01:42] in computer environments where they can
- [01:44] browse the web, write code, and
- [01:46] manipulate the file system. For example,
- [01:49] Magentic 1 is a popular generalist agent
- [01:51] developed by my collaborators here at
- [01:53] MSR. It is designed as a multi- aent
- [01:56] system which is a useful programming
- [01:58] abstraction that delegates certain
- [02:00] capabilities to sub aents. Specifically
- [02:02] in Magentic 1, these sub aents are the
- [02:05] coder, terminal, web surfer, and file
- [02:08] surfer. All of which are coordinated by
- [02:10] a top level orchestrator agent. Now
- [02:13] let's imagine you ask Magentic 1 to
- [02:15] solve a git related task. First, the
- [02:18] orchestrator must decide whether to
- [02:19] delegate that task to the terminal agent
- [02:21] or the web server agent. But when
- [02:24] building a system like Magentic 1, we
- [02:26] can evaluate its behavior on such tasks
- [02:28] and fix issues by adjusting any part of
- [02:30] the system. So for example, we can
- [02:32] provide in context examples to the
- [02:34] orchestrator if it decides to delegate
- [02:36] to the wrong sub agent. Likewise, we can
- [02:39] adjust the tools and prompts of these
- [02:41] sub aents directly. In this way, Magent
- [02:44] 1 is a vertically integrated system. But
- [02:47] in the past year, the model context
- [02:49] protocol or MCP has exploded in
- [02:51] popularity. MCP enables developers to
- [02:54] bundle their tools into a server that
- [02:56] can be easily shared and consumed by LLM
- [02:58] agents. Most popular LLM agents like
- [03:01] Cloud Code, Cursor, and GitHub Copilot
- [03:04] already support MCP servers. This lets
- [03:07] any user extend their agent at runtime,
- [03:10] breaking the assumptions of vertical
- [03:11] integration. Now while this horizontal
- [03:14] extensibility is exciting in principle,
- [03:16] in practice we observed that it can
- [03:18] actually reduce LLM agents performance.
- [03:21] We call this phenomenon toolspace
- [03:23] interference.
- [03:25] In order to study toolspace
- [03:26] interference, we developed MCP
- [03:28] interviewer, a CLI tool that
- [03:30] automatically analyzes MCP servers,
- [03:32] collecting descriptive statistics like
- [03:34] the number of tools they provide, the
- [03:36] depth and length of those tool schemas,
- [03:38] and many more features. It can also use
- [03:40] an LLM to generate a functional test
- [03:42] plan that invokes each of the servers
- [03:44] tools to test that they behave as
- [03:46] expected. You can also use MCP
- [03:48] interviewer to do qualitative LLM as a
- [03:50] judge evaluation of the server. We're
- [03:53] excited that MSR enables us to share
- [03:54] these tools with the world and we've
- [03:56] open sourced the MCP interviewer on
- [03:58] GitHub. Back to the research, we
- [04:00] collected nearly 1500 real MCP servers
- [04:03] from public registries including
- [04:04] smithy.ai and Docker MCPhub. We then ran
- [04:08] the MCP interviewer on each of these
- [04:10] servers and analyzed the results which
- [04:12] we lay out in detail in our blog post on
- [04:14] the MSR blog. To recap our main
- [04:16] findings, we identified a few common
- [04:18] issues that can cause tool space
- [04:20] interference. First of all is tool name
- [04:22] collisions. Two tools cannot have the
- [04:24] same name and LLM provider APIs will
- [04:27] reject requests if there are name
- [04:29] collisions between tools. MCB provides
- [04:32] no formal guidance on namespacing and so
- [04:35] clients have had to develop each develop
- [04:36] their own strategies like prefixing the
- [04:38] server name before the tool name. Beyond
- [04:41] exact collisions though, tool names can
- [04:43] also have significant semantic overlap
- [04:45] like search, web search, Bing search,
- [04:47] and Google search. This can also confuse
- [04:49] agents. Next, we identified servers that
- [04:52] expose too many tools. OpenAI's API
- [04:55] accepts a maximum of 128 tools, and
- [04:58] their documentation recommends keeping
- [04:59] that number well below 20, but we
- [05:02] observe many servers above this 20 tool
- [05:04] threshold. Long contexts can also
- [05:07] degrade LLM tool calling performance,
- [05:09] and MCP provides no limit on the length
- [05:11] of tool responses. We identified some
- [05:13] tools that returned more than 128,000
- [05:16] tokens in a single response, overflowing
- [05:18] the available context of models like
- [05:20] GPT40 and reducing the number of
- [05:22] possible tool calls for other long
- [05:24] context models like Gemini. Finally,
- [05:27] different models need to be prompted
- [05:28] differently. For example, OpenAI
- [05:30] recommends providing incontext examples
- [05:32] of tool calls for chat completion
- [05:34] models, but discourages them for
- [05:36] reasoning models. An MCP server
- [05:38] generally does not know what model is
- [05:40] connected to its client. And so its tool
- [05:43] descriptions may work better for some
- [05:44] models than others. So what can you do?
- [05:47] As a user of MCP servers, you can use
- [05:49] the MCP interviewer tool to test servers
- [05:52] before using them. As the developer of
- [05:54] an MCP client, you can intercept long
- [05:56] tool responses before submitting them to
- [05:58] your LLM provider. As an MCP server
- [06:01] developer, you should expose as few
- [06:03] tools as possible, have short tool
- [06:05] responses, unique and descriptive tool
- [06:07] names, and you should report what models
- [06:09] and clients you tested your server with.
- [06:11] MCP marketplaces should also test
- [06:13] uploaded servers and report their
- [06:15] findings and even reject servers not
- [06:18] meeting certain minimum criteria like
- [06:20] exceeding maximum tool counts. To learn
- [06:22] more, please read our blog post and
- [06:24] check out the MCP interviewer on GitHub.
