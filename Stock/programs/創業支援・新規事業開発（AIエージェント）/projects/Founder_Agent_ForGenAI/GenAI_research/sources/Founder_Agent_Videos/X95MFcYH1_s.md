---
title: "Transcript: X95MFcYH1_s"
video_id: "X95MFcYH1_s"
video_url: "https://www.youtube.com/watch?v=X95MFcYH1_s"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: "00:08:13"
tags:
  - "AI"
  - "Agents"
  - "LLM"
topics:
  - "AI Agents"
  - "Large Language Models"
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

# Transcript: X95MFcYH1_s

- URL: https://www.youtube.com/watch?v=X95MFcYH1_s
- Retrieved at: 2025-12-30T11:16:04+09:00

## Text

- [00:00] Imagine you're short on time and need to use an AI agent to help you answer some questions
- [00:05] quickly and accurately. You grab your mobile device, type in the first question, and
- [00:11] nuhhh! The agent replies, "Sorry! I don't know enough to answer your question." Aren't AI
- [00:18] agents supposed to know everything on the internet? You've probably heard someone say large
- [00:24] language models are powerful, but on their own, they're kind of like brilliant interns with
- [00:30] literally no memory and no access to your systems. They can talk, but they don't know your data, and
- [00:36] they certainly cannot act on your behalf. You know how everyone's always saying AI is only
- [00:43] as good as the data you give it? They're actually totally right. Today, we're going to unpack
- [00:50] two different ways to give agents access to data. I hope you're excited for more acronyms because
- [00:57] we're talking about RAG and MCP. Now both aim to make models
- [01:03] smarter and more useful but in very different ways. RAG helps models no more by pulling in the
- [01:10] right information, while MCP helps models do more by connecting them to tools and systems that
- [01:17] drive work. Retrieval augmented generation and model context protocol, or RAG and MCP,
- [01:24] are two methods that allow AI to be able to provide more insight, answer questions, help users
- [01:31] while being grounded in actual information. That information could be all kinds of things:
- [01:37] documents, PDFs, videos, websites, even systems or
- [01:42] applications. While these two seem similar at first glance, they have some significant
- [01:48] differences that set them apart. Let's use an example to explore this. Imagine: you're using
- [01:55] AI to get assistance because you are going on vacation as an employee. Yes, I've been needing a
- [02:02] vacation. You'll probably need to get some information about the vacation policy.
- [02:09] Perhaps check how much information that you have, review the vacation accrual policy and even
- [02:15] request time off so that it's logged correctly. Based on this example, let's dig into how
- [02:22] MCP and RAG are similar and different. We're going to double click on three different categories: purpose,
- [02:28] of course, then data, and lastly, process.
- [02:36] Let's talk similarities first. I'll bill-build these into let's say a Venn diagram. I'll put the
- [02:41] similarities in the middle. RAG and MCP are very similar in many ways, some of which we just talked
- [02:48] about. For example, they aim to provide information, of course. And the data they're accessing doesn't
- [02:54] actually live in the large language model, but is instead provided by outside knowledge.
- [03:02] Both can also reduce hallucinations by grounding the model in real-time or specialized information.
- [03:09] But, these same areas are where they truly start to differ. We're going to start with RAG
- [03:16] and then, we'll talk about MCP. Now RAG's main purpose is to
- [03:22] add information, okay? I'm talking about providing large language models with additional
- [03:28] information living inside context. It allows large language models to access and reference
- [03:35] proprietary or specialized knowledge bases, so that the generated responses are grounded in up-to-date
- [03:42] and authoritative information. RAG is all about getting data that's static,
- [03:47] semi-structured, or even unstructured, like documents, manuals, PDFs, and more.
- [03:54] RAG also provides the user with the source of information from an answer, helping ensure that
- [03:59] the answer can be checked and verified. RAG works in five different steps. I'll outline them
- [04:05] over here. We'll start with ask, of course. This is when the user submits their question or prompt to
- [04:11] the system. Leaning on our vacation example, this would be, for example, "What is our vacation policy?"
- [04:17] Next, we'll go into retrieval. This is when the system transforms that prompt into a
- [04:24] search query and retrieves the most relevant data from a knowledge base, perhaps from an employee
- [04:30] handbook. Let's assume it's in PDF format. The next piece is all about return.
- [04:37] This is one that return passage that was received, right, or sent back to the integration layer for
- [04:44] use in context building. Then we'll move to augmentation. This step is all about when the
- [04:50] system is building an enhanced prompt for the large language model, combining the user's
- [04:55] question with all that retrieved content. Andlastly, of course, the part that we know the most
- [05:01] and well: generation. This is when the large language model is going to use that augmented
- [05:06] prompt to produce a grounded answer and returns it to the user. For example, let's say there's a
- [05:11] passage in that handbook that says employees accrue one day of vacation time every pay period.
- [05:18] Building on our example of vacation time for an employee, RAG would help us read through the
- [05:23] employee handbook, any payroll documentation to understand maybe the company's vacation policy,
- [05:29] how it works, how employees accrued time off, and more. MCP, on the other hand, is different. MCP's
- [05:36] main purpose is to take action. It's a communication protocol that allows the agent to
- [05:42] connect to an external system, either to gather information, update systems with new information,
- [05:48] execute actions. It's even orchestrating workflows or going to get live data. So I'll put systems
- [05:54] here. MCP works in a different set of five steps.
- [06:01] We'll start with discover. This is when the large language model is connecting to an MCP server, and
- [06:08] takes a look at what tools, APIs, and more are available. For example, if you asked for our
- [06:14] vacation story, "How many vacation days do I have?" it would take a look and see if it had access to
- [06:19] maybe the payroll system or wherever that information lives. The next step is all about
- [06:25] understanding. This is when it's reading each tool's schema. I'm talking about the inputs
- [06:31] and outputs to know how to call it, how to reach out. Then we'll go into plan. This is when the
- [06:38] large language model is deciding which tools to use and in what order to answer the user's
- [06:42] request. Moving along, we'll go to execute. In this phase, it's all about sending
- [06:49] structured calls through the secure MCP runtime, which runs the tools and returns the results.
- [06:56] And lastly, integrate. This is when the large language model is using those results I was just
- [07:02] talking about to keep reasoning, make more calls if needed, or of course, finalize an answer or an
- [07:08] action. When it comes to the process of vacation time for an employee, the AI would use MCP to
- [07:15] pull the employee's open number of vacation days from an HR system and perhaps even submit a
- [07:20] request to their manager for additional days off through that same system. We've unpacked the
- [07:27] similarities and differences between RAG and MCP today, and it all comes down to their end goal,
- [07:34] data and how they work. RAG is all about knowing more. While on the
- [07:40] other hand, MCP is about doing more. If you're thinking ahead, you may be
- [07:47] wondering 'Could these ever work together?' AI use cases need all kinds of data after all. You're
- [07:54] on the right track. There are times that MCP uses RAG as a tool to be even
- [08:01] more effective at information return for a user. If you're planning your next AI project, the key
- [08:07] isn't choosing one pattern or the other. It's understanding when to retrieve knowledge, when to
- [08:13] call tools and how to architect both for things like security, governance and scale.
