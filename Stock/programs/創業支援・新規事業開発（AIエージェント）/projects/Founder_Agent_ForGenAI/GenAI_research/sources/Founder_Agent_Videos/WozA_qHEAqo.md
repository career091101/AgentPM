---
title: "Transcript: WozA_qHEAqo"
video_id: "WozA_qHEAqo"
video_url: "https://www.youtube.com/watch?v=WozA_qHEAqo"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: "00:06:24"
tags:
  - "AI"
  - "Agents"
  - "LLM"
  - "Interview"
  - "Product Development"
topics:
  - "AI Agents"
  - "Large Language Models"
  - "Product Development"
  - "Data"
summary: |
  動画の内容を分析中...
key_points:
  - "AI and technology discussion"
  - "Industry insights"
  - "Future perspectives"
category: "AI Agents"
confidence_level: "high"
---

# Transcript: WozA_qHEAqo

- URL: https://www.youtube.com/watch?v=WozA_qHEAqo
- Retrieved at: 2025-12-30T11:14:18+09:00

## Text

- [00:00] Today, we're going past surface-level conversation about how tools enable LLMs to take action beyond
- [00:06] just generating text. Instead, we'll dive under the hood to see exactly how the BeeAI framework, which is
- [00:13] an open-source AI agent framework built for developers, actually implements and executes tools
- [00:18] in production. We're going to cover the whole tool lifecycle, from creating the tool to executing it
- [00:24] and observing its actions, to how the tool output is consumed by the LLM. And then at the end, we're
- [00:30] going to see it in action. In the BeeAI framework, a tool is an executable component that extends an
- [00:36] LLM's capabilities. This could be a procedural code function, an API call to an external
- [00:42] service, a database query or a file system operation, or an MCP or a model context protocol
- [00:49] server, or any custom business logic. Each tool has a name, description, and usually an input
- [00:56] schema that an LLM uses to pick the right tool call. The BeeAI framework provides some built-in tools,
- [01:02] so you don't need to recreate the wheel for common tools like internet search, running Python
- [01:08] code in a safe, sandboxed environment and encouraging the agent to think using a react
- [01:13] pattern. But you can also create your own custom tools if needed. There are two primary ways to
- [01:19] create custom tools in BeeAI. For simpler functions, you can add a tool decorator like this.
- [01:25] The framework automatically extracts the function signature to create a Pydantic input schema, uses
- [01:32] the docstring as the description and wraps everything in a proper tool class. But for more
- [01:37] complex tool calls, you can extend the tool class by providing a data model for the tool, setting
- [01:42] the run options, and providing the expected tool output. Once tools are created, they are passed to
- [01:49] the agent as a list. Then the agent passes the allowed tools to the LLM to make a selection on
- [01:55] what tools should be called. So next, the framework executes the tool call, handling input validation,
- [02:01] execution, error handling, result collection, and much more. And lastly, the agent adds the
- [02:08] tool results to memory and loops back to the LLM for the next decision, unless a final answer is
- [02:14] triggered. Next, we have the MCP tool. MCP tools are external services that
- [02:21] expose endpoints following the Model Context Protocol, a standard from Anthropic that allows
- [02:26] language models to call tools. They are handled mostly the same way and follow the same tool
- [02:31] calling pattern. The framework's built-in retry and error handling becomes even more valuable
- [02:37] with MCP tools, since they involve network calls that can fail. So the same retry logic that
- [02:43] handles the local tool errors also handles MCP connection issues, timeouts, and server errors.
- [02:50] So from the agent's perspective, MCP tools are just tools in the list. All in all, the BeeAI
- [02:56] framework includes many features that make it production ready, but some of the most important
- [03:01] ones when it comes to tool calling are the built-in observability, so you can understand and even
- [03:06] log your agent's actions; cycle detection, that prevents infinite tool call loops, built-in retry
- [03:13] logic, and memory persistence, and lastly, type validation. So the entire agent run doesn't
- [03:19] accidentally break from an invalid input. Now, let's walk through a quick demo to see it all in
- [03:24] action. In this scenario, we have a company analysis agent that has access to three tools to
- [03:30] help complete its task.
- [03:38] It has a built-in think tool, which is a reasoning module forcing the agent to follow a ReAct or
- [03:44] reasoning and acting pattern with chain of thought reasoning. It also has an MCP internet
- [03:51] search tool, and we've given it a custom tool that performs retrieval to gather context from an
- [03:57] internal database that we've preceded with some synthetic documents. This process is also known as
- [04:03] RAG or retrieval augmented generation.
- [04:11] So now, I'm going to run the script.
- [04:25] And I'm going to give it the question: When is the next pilot and what
- [04:32] is it on? And it should know what I'm talking about, even though it doesn't have context from
- [04:38] the system prompt. So as the agent runs, we can see that the agent first checks its conditional tools.
- [04:45] And because of the requirement, it forces the think tool call first.
- [04:52] So we can see it thinking there. Then it
- [04:59] goes back to the LLM to make another tool choice based on its allowed tools for this specific
- [05:04] iteration. So the LLM decides to call the internal search tool. So this is a custom RAG tool that
- [05:10] searches a database for relevant internal documents.
- [05:29] It also realizes that it needs to do a more broad internet search. So it calls the MCP internet search
- [05:34] tool, which is running on a local MCP server, with access to the Tavily search tool on
- [05:40] my device. And we can see that's running on standard
- [05:47] IO because it's running locally on my device. And then once the LLM
- [05:54] feels like it's had enough information, it provides the final answer. And the framework is
- [05:59] responsible for returning that to the user. So, what have we learned from going under the
- [06:06] hood of the BeeAI framework? That the LLM is just a small piece of the puzzle. The framework actually
- [06:13] handles a lot of the orchestration and execution logic, so you can focus on the business logic. So
- [06:18] if you're ready to give the BeeAI framework a try for your AI agents, you can find the GitHub and
- [06:24] documentation links in the show notes below. Happy building!
