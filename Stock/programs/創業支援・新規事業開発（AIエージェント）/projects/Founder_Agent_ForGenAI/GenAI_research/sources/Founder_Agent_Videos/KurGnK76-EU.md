---
title: "Let me explain what is agentic rag using a very simple real life example we will also see the difference between rag and"
video_id: "KurGnK76-EU"
video_url: "https://www.youtube.com/watch?v=KurGnK76-EU"
speaker: "a"
channel: "Unknown"
date: ""
duration: ""
tags: ["AI", "Agents", "RAG", "LLM", "Technology", "Tutorial", "Development"]
topics: ["AI", "Agents", "RAG", "LLM", "Technology", "Tutorial", "Development"]
summary: |
  Let me explain what is agentic rag using a very simple real life example we will also see the difference between rag and agentic rag
  We all know that when we have llm like GPT gemini etc it is trained on a general internet knowledge
  So if you ask this question plan a three day trip to Australia it will be able to answer it
key_points:
  - "Covers ai agents concepts and applications"
  - "Discusses AI, Agents, RAG"
  - "Suitable for learning and reference"
category: "AI Agents"
confidence_level: "medium"
source: "Founder_Agent_Videos"
retrieved_at: "2025-12-30T10:31:02+09:00"
---

# Transcript: KurGnK76-EU

- URL: https://www.youtube.com/watch?v=KurGnK76-EU
- Retrieved at: 2025-12-30T10:31:02+09:00

## Text

- [00:00] Let me explain what is agentic rag using
- [00:02] a very simple real life example we will
- [00:05] also see the difference between rag and
- [00:06] agentic rag. We all know that when we
- [00:10] have llm like GPT gemini etc it is
- [00:14] trained on a general internet knowledge.
- [00:15] So if you ask this question plan a three
- [00:18] day trip to Australia it will be able to
- [00:21] answer it. But let's say you are
- [00:22] creating a chatboard for a car insurance
- [00:25] company called Gerto
- [00:28] and if you take a general GPT and if you
- [00:32] ask a question okay I have car insurance
- [00:34] what is the process to file a claim it
- [00:36] will not know that let's say this is a
- [00:38] new company and GPT or claude has not
- [00:42] scrapped the data from their website
- [00:44] it's a new company so it doesn't know
- [00:46] the process of how to file a claim so
- [00:49] let's say if you're working as an AI
- [00:51] engineer in this Gerti Deco company and
- [00:52] if you're building a chat board which
- [00:55] can assist your customer one thing you
- [00:57] can do is you can provide access of your
- [01:00] policy documents to this LLM this is
- [01:03] policy knowledge base okay and when you
- [01:07] provide access of this knowledge to LLM
- [01:10] it will be able to retrieve the answer
- [01:13] now as an AI engineer you will build a
- [01:16] rag application retrieval augmented
- [01:18] generation application where for this
- [01:22] question you will retrieve the relevant
- [01:25] chunk. See this database might be very
- [01:27] big. Okay, let's say 1 TBTE
- [01:30] 1 GB let's say. Now in LLM we have a
- [01:34] context window limitation. So you can't
- [01:35] feed all the PDF. So you will do
- [01:38] semantic search. Okay, you will do
- [01:40] semantic search and for this people use
- [01:42] vector databases. So what they do is all
- [01:45] these PDF they will index into a vector
- [01:47] database. Let's say this is your vector
- [01:49] database and in vector database you will
- [01:53] do your semantic search and whatever
- [01:56] relevant chunks or relevant policy
- [01:58] document information that you have you
- [02:01] provide it in a context. So when you ask
- [02:03] a question to LLM uh what you do is you
- [02:07] provide your question here okay and you
- [02:11] will say provide me the answer based on
- [02:13] this context. So in this context
- [02:16] whatever relevant chunks you have
- [02:17] retrieved you will provide it and then
- [02:20] it will be able to uh provide you the
- [02:23] answer. This is traditional rag. Now
- [02:27] let's say you ask this question why did
- [02:29] my invoice go up this month? This is a
- [02:32] different question. And as an AI
- [02:33] engineer now you want to build something
- [02:37] uh intelligent something which is
- [02:39] agentic. Okay, see previously all these
- [02:42] things you have coded it up in your
- [02:44] Python code. Let's say maybe you use
- [02:46] lang chain. Okay, and Python and you
- [02:49] have done coding of all of this. So it
- [02:52] will do just one retrieval. Whatever
- [02:54] chunks come you will have to find the
- [02:57] answer. But now you are building an
- [02:59] agent. So in agent you will provide a
- [03:02] number of tools. So these tools can be
- [03:05] see you can have your knowledge base you
- [03:08] can have your billing database you can
- [03:10] provide access to your API for usage
- [03:13] data and this entire system that you're
- [03:17] here that you're seeing here right this
- [03:20] entire thing is actually an agent
- [03:25] and you leave it up to this LLM to make
- [03:28] a decision when to call policy knowledge
- [03:31] base when to call billing database etc.
- [03:33] So when you ask this question now LLM
- [03:35] has a brain it's intelligent it will
- [03:38] first decide okay now first I need to
- [03:40] get some policy document data I need to
- [03:43] also get billing information for this
- [03:45] customer so it will identify okay this
- [03:47] this customer ID is a 3459
- [03:51] for which it will make a call you are
- [03:53] not doing this in Python by the way LLM
- [03:56] is making a call you are just setting up
- [03:59] an agent using langraph agno whatever is
- [04:02] the framework network but LLM is making
- [04:05] autonomous decision to call to a
- [04:08] specific knowledge source for a given
- [04:10] need and for the usage it might call
- [04:14] API. Okay, not only that it might call
- [04:18] these things multiple times. So see here
- [04:21] also a retrieval augmented generation is
- [04:24] happening. It is retrieving records from
- [04:26] this PDF from this database etc. But
- [04:29] compared to rag here the selection of
- [04:33] database LLM is making autonomously. So
- [04:36] there is autonomous behavior. There is
- [04:38] agentic behavior here. Second difference
- [04:40] is in a rag you just make one call one
- [04:44] call retrieve chunk and that's it. Here
- [04:46] you might make multiple calls. So first
- [04:49] it will make API call it will retrieve
- [04:52] the data. Then it will call building
- [04:54] database get some data. Now let's say if
- [04:57] it doesn't find satisfactory answer, it
- [05:00] might call API again. It might call
- [05:02] billing database again. It's a multiple
- [05:05] iterative approach until the goal is
- [05:08] satisfied. So eventually it will have an
- [05:10] answer that your users exceeded this. So
- [05:12] your invoice increase this. Now this is
- [05:15] simple Q&A. It can also perform an
- [05:18] action. Customer might say upgrade my
- [05:20] plan to this. It will actually upgrade.
- [05:23] So agentic rag is little smarter
- [05:26] compared to traditional rag. So to
- [05:29] summarize in rag you are retrieving
- [05:31] context. Agentic rag also you are
- [05:33] retrieving context. Okay but in rag you
- [05:37] don't plan next steps. You don't do
- [05:39] multi-turn reasoning. You don't uh you
- [05:42] rarely use tools and APIs. Okay. You
- [05:44] have knowledge source and there is no
- [05:46] task autonomy. Here in agentic you can
- [05:50] actually complete the task. You can
- [05:52] upgrade the plan also you know and you
- [05:54] can use multi-turn approach. So folks
- [05:58] that's what it is. Agentic rag is
- [06:00] basically agentic in nature. It can have
- [06:03] multi-turn approach. LLM has autonomy to
- [06:06] select which database to call etc.
- [06:09] Whereas rag is more rigid. It is all
- [06:12] done through coding and it's not agentic
- [06:14] in nature. I hope this video gave you
- [06:17] some clarity on the difference between
- [06:19] the two. If you have any question, post
- [06:21] in the comment box below. If you like
- [06:22] this video, give it a thumbs up. Share
- [06:24] it with your friends.
