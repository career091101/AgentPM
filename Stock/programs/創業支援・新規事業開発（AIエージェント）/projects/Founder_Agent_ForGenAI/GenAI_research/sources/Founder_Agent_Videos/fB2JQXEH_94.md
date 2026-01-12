---
title: "I think it's fair to say that some of the most used AI buzzwords in recent times have been, well, on..."
video_id: "fB2JQXEH_94"
video_url: "https://www.youtube.com/watch?v=fB2JQXEH_94"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
  - "Agents"
  - "LLM"
  - "MCP"
  - "Programming"
topics:
  - "AI Agents"
  - "LLM Development"
  - "Prompt Engineering"
  - "Tool Integration"
  - "Workflow Automation"
summary: |
  I think it's fair to say that some of the most used AI buzzwords in recent times have
  been, well, one of them is certainly agentic AI, and... let me
  guess another one, right? Probably RAG. Yeah. Retrieval augmented generation. And with those
key_points:
  - "been, well, one of them is certainly agentic AI, and... let me"
  - "how the primary use case for agentic AI today is coding. Exactly. Or that RAG is always the best"
  - "are we saying that these things are not the case? Oh, Cedric. You know, this is where we wheel out"
  - "the consultant's default answer, right? Well, I guess I do. Is RAG always the best"
  - "let's start off by explaining what these terms agentic AI and RAG really mean. And then you can"
  - "get your practitioner viewpoint out where these buzzy technologies are actually going to be put"
  - "decisions and they execute actions towards achieving a goal. And all of this happens with"
  - "environment, they can consult memory, they can"
category: "AI & Technology"
confidence_level: "high"
---

# Transcript: fB2JQXEH_94

- URL: https://www.youtube.com/watch?v=fB2JQXEH_94
- Language: en
- Retrieved at: 2025-12-30T12:58:32+09:00

## Text

- [00:00] I think it's fair to say that some of the most used AI buzzwords in recent times have
- [00:06] been, well, one of them is certainly agentic AI, and... let me
- [00:13] guess another one, right? Probably RAG. Yeah. Retrieval augmented generation. And with those
- [00:20] buzzwords has come plenty of hype and preconceived notions. Preconceived notions like
- [00:27] how the primary use case for agentic AI today is coding. Exactly. Or that RAG is always the best
- [00:34] way to incorporate specific, up-to-date information into a model's context window. Wait, so
- [00:40] are we saying that these things are not the case? Oh, Cedric. You know, this is where we wheel out
- [00:47] the consultant's default answer, right? Well, I guess I do. Is RAG always the best
- [00:53] option? Well, here it comes. It depends. It depends. There you go. You know, I spent seven
- [01:00] years as a technical consultant, and no matter what the question, a good old "it depends," that
- [01:05] always seems to work. Well, I have an idea. How about we explain what it depends on. Right. So,
- [01:11] let's start off by explaining what these terms agentic AI and RAG really mean. And then you can
- [01:18] get your practitioner viewpoint out where these buzzy technologies are actually going to be put
- [01:22] into action. Now, AI multi-agent workflows, they perceive their environment, they make
- [01:29] decisions and they execute actions towards achieving a goal. And all of this happens with
- [01:34] minimal human intervention. Now, architecturally, these components, they kind of form a loop. So, the
- [01:41] first thing on the loop might be to perceive. And once they've perceived their
- [01:47] environment, they can consult memory, they can
- [01:54] reason, they can act along a particular path,
- [02:00] and then they can go through the final stage, which is to observe what happened, and kind of
- [02:06] round and round we go in a loop. the key here is that each agent operates at the application
- [02:13] level. They're making decisions, they're using tools and they can communicate with each other.
- [02:18] Now Martin, that's great. But if I had to pick the most common use case for agentic AI, I think it has
- [02:24] to be coding agents, right? Uh, yeah. You mean like, uh, like code assistants and copilots? Precisely.
- [02:30] And these are examples of agents that can help plan and architect new ideas that can
- [02:37] help write code straight to our repository, and even help review the code that we've generated—with
- [02:43] minimal human guidance and by using LLMs that have larger context windows with reasoning
- [02:49] capabilities. This, this kind of looks like a, like a mini developer team, like where you have maybe a,
- [02:55] an architect agent that kind of plans out the feature. And then we've got the
- [03:01] implementer that's going to come along and actually write the code. And then we've got the
- [03:06] reviewer that checks out that code, and then maybe send some feedback in a loop like this.
- [03:12] Exactly. And this agentic pattern still needs human intervention. But our job is to be more of a
- [03:19] conductor of an orchestra, right, than play a single instrument. Now, let's also think about
- [03:25] another use case for agentic AI. Think about enterprises with the need to handle support
- [03:30] tickets or HR requests. Or, for example, customers who have some particular query where specialized
- [03:37] agents can autonomously filter and query this to the right agent that's able
- [03:44] to then use tool calling in order to use services or an API, using some type of
- [03:51] protocol like model context protocol, which standardizes the interaction between our LLMs and
- [03:57] the tools that we use every day. Cool. So instead of using a chat window with an LLM to kick off an
- [04:04] action, agents can be responsive in their own environment. Exactly. But, but there is a
- [04:10] challenge, right? Because without reliable access to external information, these agents, they can
- [04:16] quickly hallucinate, or they can make misinformed decisions. And one way we can limit
- [04:23] those misinformed decisions is with retrieval augmented generation or
- [04:30] RAG. Right. And RAG is essentially a two-phase system because you've got a offline phase where
- [04:36] you ingest and index your knowledge, and an online phase where you retrieve and generate on demand.
- [04:41] And the offline part, it's pretty straightforward. So, we start off with, well, let's start it over
- [04:47] here. We're going to start with some documents. So, these are your documents. That could be Word files, it
- [04:52] could be PDFs, whatever. And we're going to break them into chunks and create vector
- [04:58] embeddings for each chunk using something called an embedding model. Now,
- [05:04] these embeddings, they get stored into a special type of database called
- [05:11] a vector database. So, now you have a searchable index of your knowledge. And when a query
- [05:18] hits the system—so we've got perhaps here a prompt from the user—that's where the
- [05:24] online face kicks in. So, the prompt goes to a RAG retriever, and that takes
- [05:31] the user question and it turns it into vector embeddings using the same embedding model. And
- [05:38] then it performs a similarity search in your vector database. Now, that's going to return back
- [05:45] to you the top K most relevant document chunks, perhaps 3 to 5 passages that are most likely to
- [05:51] contain the answer. And that is what is going to be received by the large language
- [05:58] model at the end of this. Wow, Martin! And this is really powerful. But when we start to scale things
- [06:05] up with more data, right, from our organization, or perhaps allow more users to start using
- [06:12] this RAG application, this is where it gets really tricky. Because the more documents or tokens that
- [06:18] our large language model is going to retrieve, well, the harder it is for the LLM to recall that
- [06:24] information, in addition to increased cost for our AI bill and wait times. And if we actually plot
- [06:30] this out roughly, when we talk about accuracy and the amount of tokens retrieved by our RAG
- [06:36] application, well, the more we add sometimes can have a marginal increase in performance or
- [06:41] accuracy, but afterwards can in ... result in degraded performance because of noise or redundancy.
- [06:47] So, maybe not everything should be dumped into the context of an LLM with RAG. But going back to
- [06:53] Martin's point about the two phases of RAG, let's start to talk about ingestion. Because we need to
- [06:59] be really intentional about our data curation, using perhaps open-source tools like Docling
- [07:05] that can help us do document confersion ... conversion to get it ready for our RAG
- [07:09] application. That means starting from, for example, PDF types to m-machine-readable and LLM-readable
- [07:16] types like Markdown, with their associated metadata. And this means not just the text from
- [07:22] our PDFs and documents or spreadsheets, but also tables, graphs, images, pages that are
- [07:28] truncated and much, much more. So here we can enrich your data before we write it to that
- [07:34] vector database or a similar storage. But after ingestion, the next step is retrieval or also
- [07:41] known as context engineering. So, context engineering, as the name implies, allows us to
- [07:48] form our context for the LLM for RAG applications into a compressed and
- [07:54] prioritized uh,result. So, this starts with hybrid recall from databases, right? So, if the user is
- [08:01] asking, "Hey, what is agentic AI?" what we're going to do is use both the semantic meaning of
- [08:07] our question, but also do keyword search, specifically in this example, for agentic AI. Now,
- [08:14] when we do the recall to get that information from our database, what we're also going to do
- [08:19] when we get those top K chunks, as Martin mentioned, is re-rank them for relevance,right, to
- [08:25] prioritize them for our LLM. When we get this back, well we can also do combination of
- [08:32] chunks. So if these two chunks are related, well, we'll put them together and piece this, so at the
- [08:37] end of the day, when we provide the context and the question for our LLM, we have one single
- [08:43] coherent source of truth. This results in higher accuracy, faster inference and cheaper AI cost. Now
- [08:50] that sounds great. And speaking of costs, I hear that local models can power
- [08:57] RAG and agentic AI. Is that, is that the case? Yes, the rumors are true because instead of paying for
- [09:03] an LLM, lots of developers have already been using open-source models, using open-source tools
- [09:10] like vLLM or Llama C++. And this allows us to maintain the same API as
- [09:17] a proprietary model but have the added benefit of data sovereignty—so, keeping everything on premise—and
- [09:23] tweaking our model runtime for KV cache in order to have big uh, improvements that could
- [09:30] speed up our RAG or agentic AI applications. Yeah, so that is AI agents with the
- [09:36] help of RAG, a winning combination. Always, right? Well, maybe not
- [09:43] always, but, you know, of course, it depends.
