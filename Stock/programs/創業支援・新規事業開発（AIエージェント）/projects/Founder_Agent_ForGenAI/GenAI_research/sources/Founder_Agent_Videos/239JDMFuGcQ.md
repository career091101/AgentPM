---
title: "YouTube Video: 239JDMFuGcQ"
video_id: "239JDMFuGcQ"
video_url: "https://www.youtube.com/watch?v=239JDMFuGcQ"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "YouTube"
  - "Transcript"
  - "AI Agent"
  - "LLM"
  - "Technical"
  - "Tutorial"
topics:
  - "AI Agent"
  - "LLM"
  - "Technical"
  - "Tutorial"
summary: |
  Claude Code recently released this new feature called sub agents. And I have seen a few videos on sub agents. I end up clicking off because they just go into too much jargon. So I'm going to break it ...
key_points:
  - "動画トランスクリプトの内容を参照"
category: "Tutorial"
confidence_level: "medium"
transcript_type: "YouTube Auto-generated"
language: "en-ja-mixed"
source: "Founder_Agent_Videos"
---


# Transcript: 239JDMFuGcQ

- URL: https://www.youtube.com/watch?v=239JDMFuGcQ
- Retrieved at: 2025-12-30T09:19:43+09:00

## Text

- [00:00] Claude Code recently released this new
- [00:02] feature called sub agents. And I have
- [00:05] seen a few videos on sub agents. I end
- [00:08] up clicking off because they just go
- [00:09] into too much jargon. So I'm going to
- [00:11] break it down for you in layman's terms
- [00:13] just like Perplexity broke it down for
- [00:16] me. And then I'm going to show you the
- [00:17] two I've created, how you can create
- [00:19] them, and what you can get them to do.
- [00:21] So these new sub aents let you create
- [00:24] specialized mini AI assistants inside
- [00:26] your main Claude Code instance. And they
- [00:28] each have their own job, personality,
- [00:30] and tools. So instead of you using
- [00:32] claude code and telling the terminal to
- [00:35] manage everything, writing the code,
- [00:37] reviewing, debugging, documenting, you
- [00:39] can delegate these specific, very, very,
- [00:41] very specific jobs to expert helpers. So
- [00:44] each sub agent is one of those expert
- [00:47] helpers. They have their own focus. In
- [00:49] this example, you could create a code
- [00:51] reviewer agent, a bug fixer agent, or a
- [00:53] testr runner agent. And again, each one
- [00:55] is tailored to a specific task or area
- [00:58] of expertise. And this allows you to
- [01:00] really zero in on one thing. So each of
- [01:03] these agents are working together in
- [01:05] unison, but with a superpower. So each
- [01:07] of these agents have separate memory,
- [01:09] which is their context window. And each
- [01:11] sub agent operates its own workspace. So
- [01:14] again, this keeps everything clean. one
- [01:16] agent is only working on that one thing
- [01:18] and it's not mixing up information,
- [01:20] instructions, knowledge bases with other
- [01:23] agents doing different tasks. Another
- [01:25] thing I found quite cool is that you get
- [01:27] to decide what the agent has access to.
- [01:29] So if you don't want it to have access
- [01:30] to specific commands, plugins, tools,
- [01:34] MCPs, files, you can set it up in a way
- [01:36] that it only calls the tools that you
- [01:38] need it to or it can have access to
- [01:40] everything. Now, when you're in the
- [01:41] terminal vibe coding talking to Claude
- [01:44] code, it will decide when a job fits
- [01:46] that sub agent. Claude code hands that
- [01:49] task off to that agent and that agent
- [01:51] does the work in its own headsp space
- [01:53] and then reports back to the main
- [01:55] conversation so you can stay organized.
- [01:57] And you can set different color schemes
- [01:59] so you know which agent is doing what
- [02:01] and when. I think this feature is going
- [02:03] to be a gamecher because you can now
- [02:04] work on much more complex projects, AI
- [02:07] workflows, build bigger teams because
- [02:10] now you can chain or parallelize tasks
- [02:12] with special agents. So no more
- [02:14] one-sizefits-all because you've got this
- [02:16] entire AI team just for your workflow.
- [02:19] So this front-end integration tester has
- [02:22] been created and designed to run anytime
- [02:27] I've told Claude Code to create the DMG.
- [02:30] So to update a new file. So this was the
- [02:33] prompt I gave it. Update the DMG. And
- [02:36] it's gone ahead to do that. It's looking
- [02:38] at everything it needs to do. And then
- [02:39] before it updates the DMG, it's going to
- [02:42] run this agent to get it to test the
- [02:44] front-end functions and make sure that
- [02:46] all the backend code for these
- [02:48] corresponding things like the buttons
- [02:50] and everything are all working. So it's
- [02:52] really cool that you don't have to
- [02:53] constantly tag the agent, although you
- [02:55] can if you need to. So I'm going to go
- [02:57] ahead and create a new agent. I'll start
- [02:59] a new terminal. Type in claude and then
- [03:02] I'm going to do forward slash agents
- [03:06] and then there we go. We've got create
- [03:08] new agent. And then you have to decide
- [03:10] whether you want it to be for that
- [03:12] specific project or the entire claude
- [03:15] code instance that you've got installed.
- [03:16] I'm going to do project and then you can
- [03:19] manually set it up, but you can generate
- [03:21] it with claude which means you just
- [03:22] describe what you want the agent to do
- [03:24] and then it creates all of the prompt
- [03:26] the system prompt and everything else.
- [03:27] I'm going to go with it suggestion this
- [03:29] time. I've already created two separate
- [03:31] agents. Um, there might be a bit of
- [03:34] overlap, but I'm going to still go ahead
- [03:36] with it. And then I'm going to tell it
- [03:37] when I want it to call this agent. So,
- [03:39] as I showed in my example, when I told
- [03:41] it to update the DMG, it automatically
- [03:44] called that agent. So, I'm going to say
- [03:46] expert software engineer that helps
- [03:48] review my code on best practices. I'm
- [03:52] going to say for a Mac app and I'm going
- [03:56] to say run whenever whenever I ask it to
- [04:01] review the app. It's quite simple. I'm
- [04:03] probably going to delete this agent
- [04:04] because it's quite similar to my front
- [04:06] end testing agent. And as I said, you
- [04:08] really want to hone in on one specific
- [04:11] thing. Otherwise, you're just going to
- [04:12] have a bunch of overlapping agents. In
- [04:15] some cases, it's going to make sense.
- [04:16] Other times, it's probably going to be
- [04:18] overkill. And but for the purpose of
- [04:20] this video, I'm going to go ahead and
- [04:21] make this. So, enter. And now it's going
- [04:23] to generate all the configuration for
- [04:25] me.
- [04:28] Now, step four allows you to set the
- [04:30] tools that you want it to be able to
- [04:32] have access to. So, we've got all tools,
- [04:34] readonly tools, edit tools, execution
- [04:37] tools, MCP tools, show advanced options.
- [04:40] We go into here. We've got individual
- [04:41] tools that you can select or deselect.
- [04:44] Um, if you don't understand what most of
- [04:46] these are, that's absolutely fine. and
- [04:49] just give it access to everything as you
- [04:52] learn, as you figure this out. You can
- [04:53] always delete the agent after. If you
- [04:56] want to go back, you just go to escape.
- [04:58] I think I've actually skipped the step
- [05:00] by doing that. Uh, nonetheless, let's uh
- [05:02] choose a color for it and crack on. So,
- [05:05] this is what it's doing. This is the
- [05:07] final step. And it's given it a name. I
- [05:09] could have told it why I wanted to name
- [05:11] it, but we've got Mac app code reviewer.
- [05:14] Shows me where it's located. It's in a
- [05:16] markdown file. It tells me the tools it
- [05:18] has access to. So, it looks like I did
- [05:20] deselect all tools, although it has them
- [05:23] all listed individually. I'm not sure
- [05:24] because I don't remember if it done this
- [05:26] the first time. And then the description
- [05:28] is Claude telling Claude what this agent
- [05:31] does, when to use it. And then you've
- [05:32] got the system prompt. It looks like
- [05:34] this is all truncated. So, let me go
- [05:36] ahead and press enter. And now we've got
- [05:39] our list of agents. So, whenever you
- [05:41] type forward slash agents, you're going
- [05:43] to see this menu where you can create a
- [05:45] new agent uh or check out your project
- [05:47] agents or your personal agents for your
- [05:49] entire Claude code instance. And then
- [05:52] you've got built-in agents which are
- [05:54] always available general purpose. Um but
- [05:56] again, you can just go into the code
- [05:58] here, view, edit, delete. I'll go back
- [06:01] and come out of that and it tells me
- [06:03] that's the agent I've created. Again, I
- [06:06] can at and call that agent.
- [06:12] Okay, it's been running tests in the
- [06:13] background. So, that's awesome because
- [06:15] the agent I had running has been working
- [06:18] and I've opened up another terminal and
- [06:21] just been cracking on and the agent was
- [06:23] in the back fixing things. So, that
- [06:26] works. That's awesome. Um, so back over
- [06:29] here, as I said, I can call that agent.
- [06:31] I typed in ma. There it is down there.
- [06:35] Agent Mac app. So, I can just tag that
- [06:37] agent and then give it a specific task I
- [06:39] want it to do. So, that's it. If you are
- [06:41] already using these sub agents, let me
- [06:44] know in the comments how you're using
- [06:45] them because I know in the next few days
- [06:48] and weeks, people are going to come up
- [06:50] with some amazing hacks for how they are
- [06:52] setting up very, very complex workflows.
- [06:55] And I definitely want to be in the know.
- [06:57] So, drop a comment, like and subscribe
- [06:58] if you want to see more content like