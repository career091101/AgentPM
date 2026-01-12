---
title: "YouTube Video: 1WImBwiA7RA"
video_id: "1WImBwiA7RA"
video_url: "https://www.youtube.com/watch?v=1WImBwiA7RA"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "YouTube"
  - "Transcript"
  - "AI Agent"
  - "Technical"
  - "Tutorial"
topics:
  - "AI Agent"
  - "Technical"
  - "Tutorial"
summary: |
  Cloud just introduced this concept called agent skills. It might look complicated but it's actually really simple ideas but super powerful and many things that it might be even bigger than MCP. So a c...
key_points:
  - "consistent result. But more importantly"
category: "Tutorial"
confidence_level: "medium"
transcript_type: "YouTube Auto-generated"
language: "en-ja-mixed"
source: "Founder_Agent_Videos"
---


# Transcript: 1WImBwiA7RA

- URL: https://www.youtube.com/watch?v=1WImBwiA7RA
- Retrieved at: 2025-12-30T09:18:34+09:00

## Text

- [00:00] Cloud just introduced this concept
- [00:01] called agent skills. It might look
- [00:02] complicated but it's actually really
- [00:04] simple ideas but super powerful and many
- [00:06] things that it might be even bigger than
- [00:08] MCP. So a cloud skill you can almost
- [00:10] consider as a combination of both a prom
- [00:12] instruction to teach agent how to do
- [00:14] certain skills as well as a list of
- [00:16] assets and tools like predefined
- [00:18] functions and templates guidelines to
- [00:20] make it produce more consistent result.
- [00:22] But tool and assets are kind of
- [00:23] optional. It can be as simple as just
- [00:25] one single prompt as well. For example,
- [00:27] for brand guideline skill, literally
- [00:29] just one single prompt including very
- [00:30] specific brand guidelines that you want
- [00:32] agent to follow. Same thing here. I also
- [00:34] have a UI design skills that just one
- [00:37] single prompt. So all the skills start
- [00:39] with a skill.md file including this
- [00:41] short description explain to agent when
- [00:43] to use this skill and this description
- [00:44] will always be added to the agent
- [00:46] context. So you will know what type of
- [00:48] skills it has access to and when agent
- [00:50] decide to call the skill this where the
- [00:52] rest of context below will be loaded. So
- [00:54] this part almost feel like cloud code
- [00:56] commands. So skill.mmd is the most
- [00:58] necessary part of skill. For more
- [01:00] complex skill you can also include more
- [01:02] resource. For example for this skill to
- [01:03] generate algorithm art. They also
- [01:05] include resource like example
- [01:06] implementation and get agent to raise
- [01:09] those example reference before they
- [01:10] implement to making sure we have more
- [01:12] consistent result. But more importantly
- [01:14] you can also include some predefined
- [01:15] functions like in this slack give
- [01:17] creator skill. They already import
- [01:19] packages and predefined functions and
- [01:21] the instruction here basically tell the
- [01:22] agent how to use those functions to
- [01:24] create a nice gift out of the box. And
- [01:26] here's why I think skills might be even
- [01:28] better than MCPS. So MCP has been
- [01:30] awesome way to extend agents capability
- [01:32] by connecting agent with new MCPS can
- [01:35] suddenly do new things that it couldn't
- [01:36] do before. The problem is that MCP in
- [01:38] practical is not that easy to use.
- [01:40] Firstly, MCP can consume a whole bunch
- [01:42] of token that is unnecessary because
- [01:43] each MCP can contain a bundle of
- [01:46] different tools and each tool here
- [01:47] including the description about when to
- [01:49] use this tool as well as input schema
- [01:51] and all those token will be loaded to
- [01:53] agent context regardless whether this is
- [01:55] useful or not and more importantly quite
- [01:57] often MCP builder will want to build the
- [01:59] tools in a more kind of modular way so
- [02:01] it's reusable and more composable but
- [02:03] that also means most of MCP is not
- [02:05] something you just connect and use you
- [02:06] want to give agent more detailed
- [02:08] instruction about the order of when to
- [02:10] use which tool and that may set up more
- [02:12] complicated. But on the other hand, the
- [02:13] way skill is set up allow you to consume
- [02:15] much less token but perform much more
- [02:17] complicated tasks. Let's take chassis
- [02:19] and MCP as example. At default, it has
- [02:21] seven different tools for different
- [02:23] purpose. If I load the context, you will
- [02:25] see those chassis MCP tools already take
- [02:27] about 4.2,000 token. But you can imagine
- [02:30] if we turn that into a chassine skill,
- [02:32] we can probably reduce token from
- [02:34] 4.2,000 to just 70. And that means your
- [02:36] agent can be equipped with many more
- [02:38] skills and it should just work out of
- [02:40] box because skill.md can already contain
- [02:42] all the referencing instructions. But
- [02:44] without further ado, let's show you
- [02:45] example. So here under docloud/sklls
- [02:48] we have loaded a list of different
- [02:49] skills and there's one skill called
- [02:50] slack gift creator which including the
- [02:52] description the four details about how
- [02:54] to create a gift as well as some
- [02:56] predefined functions. So if I ask it to
- [02:58] create a gift for my slack around daily
- [03:00] stand up time, you will see that it will
- [03:02] try to call this command slack give
- [03:04] creator with a custom prompt. As I
- [03:05] mentioned before, this skill is
- [03:06] basically reuse the command
- [03:08] infrastructure. If you click yes, it
- [03:10] will start loading all skills here. Then
- [03:11] it will create this Python code and run
- [03:14] this Python code which gener
- [03:20] pipeline by just improving those
- [03:21] predefined functions. There's another
- [03:23] skill called algorithm art. If I tell it
- [03:25] to help me create animated Zen style
- [03:26] mountain algorithm art again it recall
- [03:28] this command. It will firstly create MD
- [03:30] file to really design and plan the
- [03:32] artwork read the template file that we
- [03:34] defined here as example reference. Then
- [03:36] just generate this animated art using
- [03:38] p5GS. Meanwhile another really cool
- [03:40] thing about skill is that you can also
- [03:42] start using skill for your own codebase
- [03:44] as a way to make agent self-improving.
- [03:46] So here's how I create skills for my own
- [03:48] codebase. So I'm building this cloud
- [03:49] platform for super design and we have
- [03:51] this fairly large motor ripple and what
- [03:53] I do is that I load a skill creator
- [03:54] skill inside cloud folder. So I can give
- [03:57] a prompt we have the front end in this
- [03:58] folder and also share package here.
- [04:00] Please go investigate our current
- [04:01] convention and tell me what's the best
- [04:03] practice for adding new UI component.
- [04:05] Great. So we did a quite deep
- [04:06] investigation and come back with the
- [04:08] convention. Now let's create skill
- [04:09] called front end including all the best
- [04:10] practice for front end implementation
- [04:12] for our codebase. Let's start with how
- [04:14] to add UI components. So it will try to
- [04:16] call the skill initiate skew front end
- [04:18] which will be created here include this
- [04:20] file that generates gener description
- [04:22] obviously you can update that also it
- [04:23] start including those best practice
- [04:25] about our front end UI implementation it
- [04:27] even create a further reference file for
- [04:29] the component guide as well as style
- [04:31] guide with this one next time if I ask
- [04:32] you to create new UI component like
- [04:34] let's create a new UI component for
- [04:35] emoji and image picker in our front end
- [04:37] it will firstly call the skills to get a
- [04:39] best practice and coding convention in
- [04:41] our codebase first and then start
- [04:42] building things properly following the
- [04:44] best practice So this how you can use
- [04:46] skill feature to really extend agent
- [04:48] capability and make it continuously
- [04:50] improving. I just started this ripple
- [04:51] called awesome cloud skills and moment
- [04:53] most of them is from official cloud but
- [04:54] I start adding some stuff like UI design
- [04:56] which including very specific prompt
- [04:58] I've been using and I'll keep adding new
- [04:59] stuff also feel free to contribute and
- [05:01] create PRs and meanwhile if you're
- [05:02] interested to dive into cloud skills
- [05:04] more I will dive a bit deeper in our
- [05:06] upcoming weekly workshop at AI builder
- [05:08] cup. So you can click on the link below
- [05:09] to join if you're interested. I hope you
- [05:11] enjoy this video. Thank you and I see
- [05:12] you next