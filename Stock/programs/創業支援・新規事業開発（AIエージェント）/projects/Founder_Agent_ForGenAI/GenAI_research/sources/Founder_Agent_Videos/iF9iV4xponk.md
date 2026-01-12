---
title: "I think back to when I first started learning coding, I was the kid that sat in the back of math cla..."
video_id: "iF9iV4xponk"
video_url: "https://www.youtube.com/watch?v=iF9iV4xponk"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
  - "Agents"
  - "LLM"
  - "Anthropic"
  - "MCP"
  - "Automation"
  - "Programming"
  - "Tutorial"
  - "Startup"
topics:
  - "AI Agents"
  - "LLM Development"
  - "Prompt Engineering"
  - "Tool Integration"
  - "Workflow Automation"
summary: |
  I think back to when I
  first started learning coding,
  I was the kid that sat in the back
key_points:
  - "that I can actually program the answers"
  - "and the future of software engineering."
  - "And I'm joined by my colleague Boris."
  - "and things are moving very, very fast,"
  - "and where are we standing currently?"
  - "is now when you code, you use an agent,"
  - "is this continuing into the future."
  - "or whatever we call this thing,"
category: "AI Agent Development"
confidence_level: "high"
---

# Transcript: iF9iV4xponk

- URL: https://www.youtube.com/watch?v=iF9iV4xponk
- Retrieved at: 2025-12-30T15:53:54+09:00

## Text

- [00:00] - I think back to when I
first started learning coding,
- [00:03] I was the kid that sat in the back
- [00:05] of math class in middle school,
- [00:07] and I had my little TI-83 Plus calculator.
- [00:10] And we just program it with BASIC,
- [00:12] 'cause at some point I realized
- [00:14] that I can actually program the answers
- [00:16] for the math test into the calculator .
- [00:24] Hey, I'm Alex.
- [00:25] I lead Claude Relations here at Anthropic.
- [00:28] Today we're gonna be
talking about Claude Code
- [00:30] and the future of software engineering.
- [00:31] And I'm joined by my colleague Boris.
- [00:33] - I'm Boris.
- [00:34] I'm a member of technical
staff here at Anthropic
- [00:37] and creator of Claude Code.
- [00:39] - A lot has happened
in the past 12 months,
- [00:40] and things are moving very, very fast,
- [00:42] especially in the coding domain.
- [00:44] For folks that, you know,
- [00:46] maybe aren't following
the news every single day
- [00:48] or even staying on top of the latest,
- [00:50] and I have trouble myself sometimes,
- [00:52] can you kind of catch us
up here on what's happened,
- [00:55] and where are we standing currently?
- [00:57] - Yeah, a year ago coding
was totally different
- [01:00] than what it is today.
- [01:02] A year ago, if you want to write code,
- [01:04] you have a IDE,
- [01:05] you have some sort of
autocomplete in the IDE,
- [01:08] and then there's some sort of chat app,
- [01:09] and you might like copy and paste code
- [01:11] back and forth a little bit.
- [01:13] And that was the state of the
art, that was AI in coding.
- [01:17] And I think maybe
sometime around a year ago
- [01:20] we started to see agents appear
- [01:22] as a thing that people
earnestly use in coding.
- [01:25] It's like a part of the workflow.
- [01:27] It's not like a gimmick or a prototype.
- [01:29] It's actually part of the inner
loop when you're doing dev.
- [01:32] And I think this is the thing
- [01:34] that's changed the most in the last year,
- [01:36] is now when you code, you use an agent,
- [01:40] you don't directly manipulate
text in an IDE anymore.
- [01:43] It's not just about tab;
- [01:45] it's about the model writing code for you.
- [01:48] And I think what we've started to see
- [01:49] is the shift from directly
manipulating texts
- [01:53] to having the model do the
text manipulation for you.
- [01:57] And I think projecting it out,
- [01:58] this is sort of the
trajectory that we're on,
- [02:01] is this continuing into the future.
- [02:04] - I see, so we've gone from
- [02:07] it all being within a web app
- [02:09] where you're copy and pasting the code out
- [02:11] and you're making like very
targeted edits, almost,
- [02:13] to just being a lot more hands-off
- [02:15] and telling an agent
what you want it to do,
- [02:18] and then trusting it to
go make tons of edits
- [02:21] and create whole apps
sometimes even by itself.
- [02:23] - Yeah, exactly.
- [02:24] And this was something that
- [02:27] I think the reason we
couldn't do it a year ago,
- [02:30] and, you know, like, people
have tried to make AI do coding
- [02:33] for the longest time and to, you know,
- [02:34] just like automate more and
more of coding in various ways.
- [02:37] And it hasn't really worked, I think,
- [02:38] probably for a couple of reasons:
- [02:39] one is the models weren't
really good enough,
- [02:42] and the second one is
that like the scaffolding,
- [02:44] the thing on top of the
model, wasn't good enough.
- [02:47] And when we initially
launched Claude Code,
- [02:49] the very, very first
versions late last year,
- [02:52] I think it was still using Sonnet 3.5.
- [02:55] This wasn't even 3.6,
- [02:57] or whatever we call this thing,
- [02:59] the new Sonnet 3.5.
- [03:00] - Yeah, upgraded Sonnet.
- [03:02] - Yeah. It wasn't even this.
- [03:03] And it like sort of worked, you know?
- [03:05] Like, I used it for maybe 10% of my code
- [03:07] or something like that.
- [03:08] But even then, I remember
when we launched it,
- [03:11] we gave it to the core team.
- [03:13] And it was just me
- [03:14] and like a few other people
on the team at the time.
- [03:16] And I remember walking in one morning,
- [03:18] and kind of on the way to to my desk,
- [03:21] there was a few engineers sitting there;
- [03:22] and one of them was Robert,
- [03:23] and there was a couple of other engineers.
- [03:25] And I just walked in,
- [03:27] and I saw Claude Code on
their screen the first time.
- [03:29] And like I just gave this
to them the day before
- [03:32] and they're already using it.
- [03:33] And it was just the craziest thing.
- [03:34] And the model wasn't very good.
- [03:35] The harness wasn't very good.
- [03:37] But even in this early version,
- [03:39] it was already a little bit useful.
- [03:41] And I think that over the last year
- [03:43] what's happened is the
model has gotten way better
- [03:46] at agentic coding,
- [03:47] and that's happened with like
3.7 and now 4.0 and Opus 4.1.
- [03:53] And the harness has also
gotten a lot better.
- [03:55] And, you know, obviously
the harness is Claude Code,
- [03:57] because the way you
interact with the model,
- [04:00] you can't just like
directly use the model:
- [04:01] you have to use a harness.
- [04:02] It's sort of like, you know,
- [04:03] like if you're riding a horse,
you need some sort of saddle.
- [04:06] And like that saddle
makes a giant difference
- [04:08] when you're riding a horse.
- [04:10] I'm not a horse rider.
- [04:13] - I like that analogy, though.
- [04:14] I mean, it is kind of
like Claude is the horse,
- [04:18] and as the engineer you're trying to
- [04:21] get it to go in a certain direction
- [04:23] and you're trying to guide it,
- [04:23] and like you need some sort
of scaffolding around it
- [04:27] to be able to steer it correctly.
- [04:30] And the harness in this case,
- [04:32] just so we're on the same page,
- [04:33] is everything from like
the tools we're giving it
- [04:36] to how we handle like the
context and everything
- [04:39] for the model.
- [04:39] - Exactly, exactly.
- [04:40] It's like all of Claude Code.
- [04:41] Like, the model is the
thing behind the API,
- [04:44] and then Claude Code,
it's the system prompt,
- [04:46] it's context management,
- [04:48] it's tools, it's the
ability for, you know,
- [04:51] to plug in MCP servers,
- [04:53] settings, permissions,
all this kind of stuff.
- [04:55] All of this interfaces with the model.
- [04:58] And the model sees all the context,
- [05:00] all the output from this stuff,
- [05:01] and it makes a giant difference
in the way that it performs.
- [05:03] And I think over the last year
- [05:05] we've learned how exactly
we build for the model.
- [05:08] And the model has kind of coevolved
- [05:11] with not just Claude Code
- [05:13] but all these different products
- [05:14] that are using Anthropic models
- [05:16] to build agentic coding tools.
- [05:19] - Maybe let's speak more on that.
- [05:20] When you say coevolve,
- [05:22] is that because it's
like a deliberate thing
- [05:24] in which we're doing with the training, or
- [05:27] how is the model also getting better
- [05:29] at these sorts of things?
- [05:30] as we make the product
features itself better.
- [05:32] - It's pretty organic, honestly.
- [05:34] Like, you know, at Anthropic,
everyone uses Claude Code.
- [05:37] And that includes the researchers.
- [05:39] And so every day the
people building the models
- [05:42] are using the model in
order to do their job.
- [05:45] And I think as part of that
- [05:46] you kind of see these natural limits
- [05:48] that you hit with a model.
- [05:50] So, you know, as an example,
- [05:52] maybe the model's really bad
- [05:54] at doing certain kinds of edits.
- [05:55] And sometimes when you use Claude Code,
- [05:56] you see like, oh, failed
to replace string,
- [05:58] failed to replace string.
- [05:59] Like, this is a model capability,
- [06:01] and we can improve this
if we learn from it.
- [06:03] Or another example,
- [06:04] maybe something like higher level
- [06:06] is if you just let the model
cook for like 30 minutes,
- [06:10] with 3.5, it could kind
of do it for a little bit,
- [06:13] maybe for like a minute or
something it would stay on track.
- [06:16] And then with newer models
- [06:17] it kind of gets longer and longer
- [06:20] this amount of time the model
can operate autonomously.
- [06:24] And I think this is really
based on experience,
- [06:25] because you use the model,
- [06:27] you kind of see where as a human
- [06:28] you have to course correct and steer it.
- [06:30] And then we've learn from that,
- [06:31] and we can kind of incorporate
that into the model
- [06:33] and teach it better to do this itself.
- [06:36] - When you're evaluating a new model,
- [06:39] do you kind of have a vibe
check set of tests that you run?
- [06:43] Or if it's like a new feature
that we're rolling out
- [06:44] to make something better in the harness,
- [06:46] how do you personally evaluate
- [06:48] if the performance is getting better?
- [06:51] - I just do my work that day.
- [06:52] - Interesting.
- Yeah.
- [06:54] Like, my perfect day is
I'm just coding all day.
- [06:57] And, you know, whatever the model is,
- [07:00] whatever is the new thing we're testing,
- [07:01] I'll just code using that
and see what the pipe is.
- [07:03] There isn't like a specific thing I do.
- [07:05] - Right, you just see how
does it actually work for me
- [07:08] in my day to day?
- [07:09] - Yeah. Exactly, exactly.
- [07:10] And, you know, like in day-to-day work
- [07:12] you do all sorts of stuff.
- [07:13] Like, you're writing new code,
- [07:15] you're maybe like fixing bugs,
- [07:16] you're maybe reading Slack messages
- [07:18] or GitHub issues to respond to feedback.
- [07:21] And I think more and more
- [07:22] the model is able to do
more and more of this.
- [07:24] So actually, in a way, if
you had maybe one thing
- [07:27] that you always use the model for,
- [07:28] you would miss out on some
of these newer capabilities,
- [07:31] like pulling in context through MCP,
- [07:32] like reading your Slack messages.
- [07:34] Or, you know, automatically
debugging stuff,
- [07:36] 'cause you can pull in
Sentry logs automatically.
- [07:39] - Yeah, so the best eval in some sense
- [07:41] is the one that most looks like real life.
- [07:44] And in that case, just using it
- [07:46] gives you the best result.
- [07:48] - We tried really hard,
when building Claude Code,
- [07:50] to build a product evals.
- [07:52] - Yeah.
- [07:53] - You know, just like to
have some sort of benchmark;
- [07:55] like, when we change a
system prompt or whatever,
- [07:57] is the model getting better?
- [07:58] And we have a little bit of this,
- [08:00] but honestly it's just like
so hard to build evals.
- [08:02] And by far the biggest
signal is just the vibes.
- [08:05] Like, does it feel smarter?
- [08:07] 'Cause there's such a broad
range of tasks they use it for.
- [08:10] - Yeah, that's actually a question
- [08:11] I hear from developers all the time,
- [08:13] is they would appreciate more guidance on
- [08:15] how we go about prompt
testing and iterating.
- [08:21] I know for different products
- [08:22] we have like various sorts of evals
- [08:23] that we've tried to create,
- [08:24] but for Claude Code it really is
- [08:26] just kind of this tight feedback loop
- [08:28] that almost gives us like
more immediate signal
- [08:30] than any hardcoded set of evals.
- [08:33] - I wonder if people kind of want to hear
- [08:34] a better answer from an AI.
- [08:37] But yeah, man, it's all vibes.
- [08:39] I think at this point we're, you know,
- [08:41] the models are doing so good
on evals, like SWE-bench.
- [08:43] You know, we're just trying
to find these harder evals.
- [08:46] And now there's like T-bench,
- [08:47] which is like a little bit
less kind of saturated.
- [08:50] But I think it's just really
hard to find synthetic evals
- [08:52] that capture all the complexity
in software engineering.
- [08:54] - Right, right.
- [08:56] Do you think there's something we did
- [08:58] uniquely to set up that
feedback loop internally?
- [09:01] 'Cause I feel like Claude
Code has like the best
- [09:04] dogfooding cycle I've seen
of like any type of product.
- [09:07] - Initially, I built it the way
that I do any other product,
- [09:11] which is just listen to users
- [09:13] and make it as easy as
possible to listen to users.
- [09:17] And I think one part of it
- [09:18] is when we built Claude Code,
- [09:20] there was just like a single
feedback channel in Slack.
- [09:22] And anytime anyone had feedback,
- [09:23] I would just direct them to that,
- [09:25] just be like, "Yeah, post there."
- [09:26] And I feel like people hesitated
sometimes a little bit.
- [09:29] 'Cause sometimes when you give feedback,
- [09:32] you expect that no one listens
- [09:34] and it kind of goes into this
black hole, like into a void.
- [09:37] And I think one of the things
that we did really right was,
- [09:39] from the beginning, whenever
someone gave feedback,
- [09:42] I would try to fix it as fast as I can.
- [09:44] And sometimes I would
kind of go into the office
- [09:46] and then just spend like three hours
- [09:47] or two hours or whatever,
- [09:48] just go through as many bugs as I can
- [09:50] and fix them as fast as I can,
- [09:52] and then every time comment
back and tell people it's fixed.
- [09:55] And this kind of encourages
them to keep giving feedback.
- [09:57] And to this day the Claude Code
feedback channel internally
- [10:00] is just this fire hose, just nonstop.
- [10:02] - Oh, totally.
- [10:03] I remember, on those
early days, and still do,
- [10:06] dropping in there, posting something,
- [10:08] and immediately your emoji reacting.
- [10:10] Or you're asking for more
clarification and more questions,
- [10:14] and you do feel like, oh, okay,
my feedback's being heard.
- [10:17] And then you're able to like actually be,
- [10:19] you know, incentivized
- [10:20] to go post more feedback in the future.
- [10:23] - Yeah, 'cause, you know,
- [10:24] honestly, like, I don't
know what I'm doing.
- [10:25] Like, no one really knows
what they're doing with AI.
- [10:27] Like, we're kind of discovering
this thing as we build it.
- [10:30] And the best indicator
is what the users want.
- [10:33] So you gotta listen.
- [10:34] - Right, switching gears slightly,
- [10:38] what is like the current state
of Claude Code as a product?
- [10:42] What are the latest features?
What are you excited about?
- [10:45] Some things that you're seeing
folks do with it right now?
- [10:47] - Claude Code, from the start,
- [10:49] was built to be the simplest thing it can
- [10:51] and to be as hackable as possible.
- [10:53] And I think the hackability is something
- [10:55] that we've been developing a lot,
- [10:57] and that's something I'm
really excited about.
- [10:59] So originally, the way to hack Claude Code
- [11:01] is adding to its CLAUDE.md.
- [11:04] That was the original extension point.
- [11:06] And CLAUDE.md, as you
know, is like this file.
- [11:09] You can put it in the root directory,
- [11:11] you can put it in child directories.
- [11:12] There's kind of different
places you can put it.
- [11:14] And it's just additional
context to give Claude Code,
- [11:17] and it kind of goes with your repo.
- [11:18] You often check it into your code base.
- [11:20] So it's kind of, you know,
- [11:21] a little bit more
information about the code.
- [11:23] But over time we've added a
lot more extension points.
- [11:26] So now there's a very
sophisticated setting system
- [11:28] and permission system.
- [11:30] There's hooks now which Dixon built.
- [11:34] Dixon's an engineer on our team,
- [11:36] and he just kind of saw all
these different user asks
- [11:38] coming in for: "I want
to extend it this way.
- [11:40] I want to hook into this, hook into this."
- [11:41] And so he built a super
extensive hook system.
- [11:45] MCP, obviously, this is a
really great extension point.
- [11:48] and now there's slash
commands and subagents.
- [11:51] And user-defined slash commands
- [11:53] is something we've invested in a lot.
- [11:55] And the idea is it's just a workflow:
- [11:56] it's like a markdown file.
- [11:57] You put it in your code,
- [11:59] and it's something that
you can reuse a lot.
- [12:01] So for example,
- [12:03] I have a slash command for making commits.
- [12:07] And I have some instructions in there:
- [12:09] here's how you write a good git commit.
- [12:11] I pre-allow the git commit Bash command
- [12:13] so I don't have to accept it every time,
- [12:16] and the model can just do it.
- [12:19] So I think slash commands
are really interesting,
- [12:21] and agents are kind of a
different view of slash commands.
- [12:23] Like, it's like a slash command,
- [12:25] but it has a forked context window.
- [12:29] And so you can kind of think
of agents and slash commands
- [12:31] as two sides of the same thing.
- [12:33] And this is also very exciting.
- [12:34] It's just another way
to extend Claude Code.
- [12:37] And so when I look at the future,
- [12:38] I think a lot of it is just about
- [12:40] like how do we extend Claude Code more?
- [12:43] How do we make it easier for
other people to build on top?
- [12:46] How do we make the SDK
more useful for people?
- [12:48] So it's useful for code if you
want to build a coding agent,
- [12:51] but also you can use it for other stuff.
- [12:52] Like, anything that you need an agent for,
- [12:54] you can just use the SDK for.
- [12:56] And I think these are the things
- [12:58] that I'm the most excited about.
- [12:59] And obviously all of this benefits
- [13:00] from all the other work we're doing
- [13:02] to make the model more autonomous,
- [13:03] to make it work for
longer periods of time,
- [13:05] to make it better adhere to instructions,
- [13:07] to make it remember things better.
- [13:09] And so everything along
the way it benefits.
- [13:11] - So I'm using Claude Code,
- [13:13] or whatever form of it,
in six to 12 months;
- [13:17] what does my work actually look like?
- [13:19] Am I reviewing PRs all day,
- [13:22] or what does it day to day break down to?
- [13:27] - Yeah, I think there's gonna be a mix
- [13:28] of more hands-on coding.
- [13:30] I don't think that's going away.
- [13:32] And maybe it'll look different, though.
- [13:34] So maybe hands-on coding today
- [13:35] is directly manipulating text,
- [13:37] but in the future it might be using Claude
- [13:39] to manipulate the text for you.
- [13:42] And then I think there's
gonna be this other bucket
- [13:43] of maybe less direct coding
- [13:46] where Claude proactively does something,
- [13:48] and maybe Claude even reviewed it.
- [13:51] And it's your job to
decide if this is a change
- [13:53] that you want or not.
- [13:56] And I think maybe 12 or 24 months from now
- [13:59] we're gonna start seeing
Claude that's more about goals
- [14:02] and more about these higher
level things that it needs to do
- [14:07] and less about the specific
tasks that go into it.
- [14:09] The same way that, as an engineer,
- [14:11] I think about what is it that I want to do
- [14:13] over the next month.
- [14:14] And I kind of make small
changes to work towards that.
- [14:17] Maybe Claude will go
through the same thing.
- [14:19] - Right, sort moving up and
up the stack, to some degree,
- [14:22] of these like abstraction
levels of getting Claude
- [14:25] to make individual changes to files,
- [14:27] to getting Claude to make
changes to a whole PR,
- [14:30] to getting Claude to think
about a goal of building an app
- [14:33] or whatever else it is.
- [14:35] - Yeah.
- Okay.
- [14:37] That's interesting.
- [14:38] If I'm an engineer and I'm hearing that,
- [14:41] it seems like there's
gonna be a lot changing
- [14:44] in a very short amount of time,
- [14:46] especially with my role
and what I should be doing.
- [14:49] What's your advice for folks out there
- [14:51] that are looking to prepare themselves
- [14:52] and adapt to this world?
- [14:53] about what they should be learning
- [14:55] or what skills they should be developing.
- [14:57] - I think back to when I
first started learning coding;
- [15:00] I was the kid that sat in the back
- [15:02] of math class in middle school,
- [15:04] and I had my little TI-83 Plus calculator.
- [15:07] It was like a transparent gray one;
- [15:09] you can kind of see the circuit.
- [15:11] And we just program it with BASIC,
- [15:14] because at some point I realized that
- [15:16] I can actually program the answers
- [15:18] for the math test into the calculator .
- [15:21] And you can get better grades that way.
- [15:24] And
- [15:26] there's just something about
kind of this visceral feeling
- [15:29] of being able to hack,
and having this idea
- [15:31] of maybe there's this
one program I can make;
- [15:33] and just I go into my
calculator and I code it,
- [15:34] and then I can just restart
and use it really quick:
- [15:37] this kind of feedback cycle
that was really amazing.
- [15:39] And it made it possible
for me to build stuff
- [15:41] that I never could have before.
- [15:44] And it was just so easy to get started.
- [15:47] And I think about the difference
- [15:50] between that world and the
world before agentic coding,
- [15:53] where stacks just got
way, way too complicated.
- [15:58] You know, if I wanted
to make a JavaScript,
- [16:00] you know, like website,
- [16:02] I had to learn about
React and maybe Next.js,
- [16:05] and then three different build
systems and a deploy system.
- [16:08] And it was just so complicated.
- [16:11] And I think one really
cool thing about agents
- [16:13] is that they're changing this.
- [16:15] So with coding agents
- [16:17] it makes it really easy to get started.
- [16:19] And if you have an idea
you can just build it.
- [16:21] And it's a lot more about the idea now
- [16:23] than it is about the details,
- [16:24] because just like Claude Code,
- [16:27] you can rewrite the code over and over.
- [16:29] And, you know, Claude Code
itself, we rewrite all the time.
- [16:30] And I think this is just something
- [16:32] that coding agents enable.
- [16:34] The code itself is no longer precious.
- [16:36] And there's still an art to writing it,
- [16:38] and, you know, all stone
code by hand sometimes.
- [16:41] And one of the engineers
on the team, Lena,
- [16:43] she was talking about how on the weekends
- [16:45] she still sometimes writes C++ by hand,
- [16:47] just 'cause it's fun.
- [16:49] And, you know, as a coder,
- [16:51] it can be a really
joyous thing to do this.
- [16:54] But I think more and more
- [16:55] it's gonna be about the thing you make
- [16:56] and not about the process
of making it as much.
- [17:00] And I think my advice for
people learning to code today
- [17:04] is you still have to learn the craft.
- [17:07] So you still have to learn
to code, learn languages,
- [17:09] learn compilers, runtimes,
how to build web apps,
- [17:13] how to build programs,
- [17:15] system design.
- [17:16] You still have to know all the stuff,
- [17:18] but also just start to get more creative.
- [17:22] And, you know, if you
have an idea for a startup
- [17:23] or an idea for a product,
you can just build it now
- [17:26] in a way that you just couldn't before.
- [17:27] And we don't really
understand what this means,
- [17:29] but there's just so much potential
- [17:31] that's about to be unlocked because of it.
- [17:33] - Yeah, I love that.
- [17:35] I think that's great advice too.
- [17:37] Ideas suddenly become
something you can action on in,
- [17:41] you know, a span of a few minutes almost;
- [17:44] whereas before it could be
just in your backlog forever.
- [17:49] Before we wrap, I want to ask you,
- [17:52] as the creator of Claude Code,
- [17:54] what are your best practices
for using Claude Code?
- [17:56] And any tips or tricks.
- [17:58] - Yeah, I think the biggest
thing that I recommend,
- [18:01] okay, maybe two tricks.
- [18:03] So one thing I recommend
- [18:04] is that if you're brand new to Claude Code
- [18:06] and you haven't used it before,
- [18:08] don't use it to write code.
- [18:13] I know it sounds crazy.
- Yeah, explain, explain.
- [18:15] - But you gotta stop yourself.
- [18:16] Like, don't use it to write code yet.
- [18:18] The thing to start with
is use it to ask questions
- [18:20] about the code base.
- [18:22] So you can ask, you
know, if I want to make,
- [18:24] if I want to add a new
logger, how do I do that?
- [18:27] And then ask Claude Code
to explore the code base
- [18:29] and figure it out for you.
- [18:31] Or why is this function
designed the way that it is?
- [18:35] Claude Code can go in and it
can look through Git history
- [18:37] and it can answer this stuff for you.
- [18:40] So I think ask Claude Code
questions about the code base
- [18:42] and just don't code yet.
- [18:43] And then once you feel comfortable
- [18:44] with using Claude Code this way
- [18:46] and you get comfortable
with this idea of an agent
- [18:48] that's doing this research for you,
- [18:50] then start to use it to code.
- [18:53] I think the second thing is
- [18:54] when you are using Claude
Code to write code,
- [18:57] think about what kind of
work do you want to do
- [19:00] and like how big is the task?
- [19:01] So for something that's really easy,
- [19:03] I kind of, in my mind,
- [19:05] I have these three categories:
- [19:06] easy, medium, and hard, very roughly.
- [19:08] And so easy tasks are something
- [19:09] that Claude can write in one shot;
- [19:11] like one prompt, it'll
get it pretty much right.
- [19:13] And nowadays I'll just go to GitHub
- [19:15] and I'll tag @Claude on an issue
- [19:16] and just have Claude write the PR for me.
- [19:18] And this is how I do easy tasks,
- [19:20] 'cause that frees up my terminal.
- [19:21] I don't have to kind of spend it on this.
- [19:23] Medium tasks, I'll start
it in the terminal,
- [19:26] and I'll start in plan mode.
- [19:27] So just Shift + Tab into plan,
- [19:29] and I'll align on a
plan with Claude first.
- [19:32] And then once I feel good about the plan,
- [19:34] I'll go into auto-accept and
I'll have it implemented.
- [19:37] And then for really hard tasks,
- [19:38] I'm still the one driving,
- [19:39] and Claude is more of a tool.
- [19:41] And I'm kind of pairing with it.
- [19:43] But really I'm the one
in the driver's seat,
- [19:44] not Claude for this.
- [19:46] And so I'll use Claude maybe
to do some code-based research,
- [19:49] maybe prototype a few ideas,
- [19:51] maybe I'll just like
vibe code a few options
- [19:53] to understand the boundaries of the system
- [19:55] and what works well.
- [19:56] But I'll still mostly implemented myself.
- [19:58] And maybe Claude will
write the unit tests,
- [20:01] but it's still mostly me doing the coding.
- [20:04] So I think that'll be the second advice,
- [20:05] is just think about what's
the task that you're doing
- [20:07] and what's the right way to
use Claude Code to do it.
- [20:10] - Those are great tips.
- [20:12] Really, really appreciate the time, Boris.
- [20:14] This has been awesome. Thank you.
- [20:15] - Yeah, thanks, Alex.
