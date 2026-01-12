---
title: "Transcript: Udx7SLFDsxo"
video_id: "Udx7SLFDsxo"
video_url: "https://www.youtube.com/watch?v=Udx7SLFDsxo"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: "00:04:32"
tags:
  - "AI"
  - "Agents"
topics:
  - "AI Agents"
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

# Transcript: Udx7SLFDsxo

- URL: https://www.youtube.com/watch?v=Udx7SLFDsxo
- Retrieved at: 2025-12-30T11:05:28+09:00

## Text

- [00:03] [music]
- [00:05] Welcome back to Real Terms for AI with
- [00:07] me, Aza, and Jason. And Jason, we've
- [00:10] been talking a lot about how to design
- [00:12] agents and how to build agents and
- [00:13] agents and agents and agents. I want to
- [00:15] talk about something different today. Do
- [00:17] you have any ideas?
- [00:18] >> I was thinking we should talk about
- [00:20] systems for agents.
- [00:21] >> Not sure that many agents is actually
- [00:23] that different than talking about one
- [00:25] agent, but sure. But you got to promise
- [00:27] me you're not just going to lob a whole
- [00:29] bunch of technical terms at us and that
- [00:30] you're actually going to like use the
- [00:32] board and draw a picture so that we can
- [00:34] all follow along with what's going on in
- [00:35] your head. Deal?
- [00:37] >> Maybe. Well, remains to be seen.
- [00:39] >> Okay,
- [00:40] >> let's talk about system. So, to do this,
- [00:42] I think we should go back to the pet
- [00:44] shop agent that we first talked about,
- [00:46] right?
- [00:47] >> Okay.
- [00:47] >> And let's go ahead and get this drawing
- [00:49] going because I need to draw it out. So,
- [00:52] we have our order agent here.
- [00:54] >> Okay.
- [00:56] And this is for our pet shop. So, say
- [00:59] buy cat food or you maybe place an order
- [01:02] for a new toy.
- [01:03] >> Yeah.
- [01:04] >> And if you also remember, we talked
- [01:05] about memory
- [01:07] >> that our agent has.
- [01:08] >> And we talked about different kinds of
- [01:10] memory. We had working memory for the
- [01:11] current task or the current prop the
- [01:13] agent was working with. We had
- [01:15] short-term memory for some of the things
- [01:16] that the agent had done recently. And
- [01:18] then we had long-term memory, which we
- [01:20] talked about as being used like across
- [01:22] user sessions. Right.
- [01:24] >> Exactly.
- [01:24] >> Okay. Now, let's say we want to add
- [01:27] another agent, a different type of
- [01:29] agent. So, maybe we've taken the time
- [01:32] and we have a customer service agent.
- [01:35] >> Okay, that agent has memory.
- [01:39] >> It has connectors for memory, but we
- [01:42] need to get these memories for that
- [01:44] agent also
- [01:45] >> because this agent needs to know about
- [01:47] my orders.
- [01:48] >> Exactly.
- [01:48] >> So, how do we get these two agents to
- [01:50] share memory?
- [01:52] So in the application development world,
- [01:54] what we're almost talking about is just
- [01:56] managing state over long periods of time
- [01:58] and things that we know. And this is
- [02:00] where we start to think about systems
- [02:02] that are helping our agents out.
- [02:04] >> Okay. So this memory system supports our
- [02:07] agents.
- [02:10] >> It does.
- [02:11] >> And then each of our agents can connect
- [02:13] to that and pull the information that
- [02:15] they need for short-term or long-term
- [02:17] memory. And we also may have agents
- [02:19] adding to those memories. So for
- [02:22] example, our service agent if it has a
- [02:25] tool call failure, it may go through and
- [02:28] add memories about the right thing that
- [02:29] it should do in the future or correcting
- [02:31] maybe a bad tool call that it had in the
- [02:34] past.
- [02:34] >> Okay, but this memory can't exist in
- [02:38] like just a markdown file or an XML file
- [02:40] or anything if we're going to share it
- [02:41] across systems because each of these
- [02:43] systems needs different memories to do
- [02:45] their jobs.
- [02:46] >> We could do that. That would probably be
- [02:47] the very simple way. But coming back
- [02:49] again to application development
- [02:50] principles, we could use a database
- [02:54] and we could store those memories in a
- [02:57] database and we could even have
- [02:59] different pieces of code which help us
- [03:02] with things like harvesting the most
- [03:03] important information from those
- [03:05] memories or even you know creating
- [03:07] different types of memories that we can
- [03:09] share with our different agents. So each
- [03:11] agent is responsible for using this
- [03:13] memory system that we've created to get
- [03:15] the types of memories it needs out of
- [03:17] our data store, whatever format that is,
- [03:19] >> when it needs to run them and then
- [03:21] writing back memory information that
- [03:23] other agents or it may need at a later
- [03:25] date.
- [03:25] >> Exactly. And we could even think about
- [03:27] as we add agents. So let's maybe say
- [03:30] that we want to create a inventory agent
- [03:35] that this agent would also interact with
- [03:38] this memory and maybe learn things like
- [03:41] you know this one type of cat food is
- [03:43] always out of stock and the supplier
- [03:45] never delivers it on time. We can use
- [03:47] this memory to improve other agents that
- [03:49] we may choose to add to the system. So
- [03:51] the inventory agent could write that
- [03:52] fact in some way to the memory and then
- [03:54] the service agent could use that when
- [03:56] people call in complaining about not
- [03:58] getting their cat food and the order
- [04:00] agent could use that information to give
- [04:02] a better predicted date of when the cat
- [04:04] food might arrive.
- [04:05] >> Yep. And it's all powered by a shared
- [04:07] system that our agents are using. And in
- [04:09] this case it's just our memory system
- [04:11] for it. Kind of like a micros service.
- [04:13] >> It's a bunch of microservices.
- [04:15] Microservices all the way down.
- [04:16] >> It is. And if you'd like to learn more
- [04:18] about getting started with building your
- [04:20] own systems, like a memory system for
- [04:22] your agents, we've put some links down
- [04:24] in the comments below that you can get
- [04:26] to.
- [04:27] >> And with that, this is Aza and Jason
- [04:29] signing off for Real Terms for AI.
- [04:32] >> Happy prompting. [music]
