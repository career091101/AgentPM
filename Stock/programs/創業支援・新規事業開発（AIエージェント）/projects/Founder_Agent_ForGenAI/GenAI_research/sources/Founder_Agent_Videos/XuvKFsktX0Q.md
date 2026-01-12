---
title: "Transcript: XuvKFsktX0Q"
video_id: "XuvKFsktX0Q"
video_url: "https://www.youtube.com/watch?v=XuvKFsktX0Q"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: "00:22:04"
tags:
  - "AI"
  - "Agents"
  - "Interview"
  - "Product Development"
topics:
  - "AI Agents"
  - "Product Development"
  - "Team Building"
  - "Data"
summary: |
  creativity ends at some point. a way to go do that thing.
key_points:
  - "a way to go do that thing."
  - "Relations here at Anthropic."
  - "Claude Developer Platform."
  - "Claude Developer Platform."
  - "why we made that change"
category: "Technology"
confidence_level: "high"
---

# Transcript: XuvKFsktX0Q

- URL: https://www.youtube.com/watch?v=XuvKFsktX0Q
- Retrieved at: 2025-12-30T11:17:37+09:00

## Text

- [00:00] - Because as a developer, my
creativity ends at some point.
- [00:04] I can only think of so many use cases.
- [00:06] But the model, like anything,
- [00:08] anything somebody comes with,
- [00:10] the model will figure out
a way to go do that thing.
- [00:16] - Hey, I'm Alex. I lead Claude
Relations here at Anthropic.
- [00:19] Today we're talking about
- [00:20] building the future of agents with Claude,
- [00:22] and I'm joined by my colleagues.
- [00:23] - I'm Brad.
- [00:24] I run the PM team on the
Claude Developer Platform.
- [00:27] - I'm Katelyn, I lead the engineering team
- [00:29] for the Claude Developer Platform.
- [00:30] - Let's talk about the
Claude Developer Platform.
- [00:32] - Yeah, let's start with that.
- [00:33] - Let's start with that.
- Start there.
- [00:35] - It used to be called the Anthropic API.
- [00:37] - Yeah.
- We just went through
- [00:38] a big name change.
- [00:40] Can you walk me through
why we made that change
- [00:42] and also what this new platform
is and what it encompasses?
- [00:45] - Yeah, totally.
- [00:46] So the Claude Developer Platform
- [00:48] really encompasses our APIs,
our SDKs, our documentation,
- [00:53] all of our experiences within the console,
- [00:55] and really everything
that a developer needs
- [00:57] to actually build on top of Claude.
- [00:59] We're really humbled, proud to serve
- [01:02] some really awesome
customers around the world
- [01:04] who are trying to, what we like to say,
- [01:06] raise the ceiling of
intelligence using Claude.
- [01:09] And the platform really
enables them to do that.
- [01:12] And I would say one of my
favorite parts about it
- [01:14] is the platform doesn't just
serve customers externally,
- [01:18] the platform actually serves
our internal products.
- [01:21] So we love telling people,
Claude Code, for example,
- [01:24] is actually built directly
on our public platform.
- [01:27] - I see.
- Yeah, I mean,
- [01:29] I think when we started,
- [01:30] we were just the Anthropic APIs
- [01:32] very simple access to the model,
- [01:34] but over the last year or so,
- [01:36] we've added so many features to it.
- [01:38] We added prompt caching,
- [01:39] we added a whole separate batch of API,
- [01:43] we added web search, web fetch,
- [01:45] we have this context management
support, the code execution.
- [01:48] So all these tools, you
know, now this kind of,
- [01:50] we feel like, yeah, it's aspirationally,
- [01:53] it's a platform now.
- [01:54] - I see, so there's just
a lot more to it now.
- [01:56] It's evolved in a pretty
drastic way over the past year.
- [01:59] - Yeah, yeah.
- Better, I think so.
- [02:00] - And I think that's what developers
- [02:03] were sort of calling it anyway.
- [02:04] You know, so it's always
natural to just sort of go
- [02:06] with what developers were saying.
- [02:07] - We were a little late to the game there.
- [02:09] It's always had it, right?
- [02:10] - It's okay.
- We've made our amends.
- [02:14] One of the cool things you can do now
- [02:16] as we're moving from
the sort of chat model
- [02:18] to maybe this more agentic future
- [02:20] is building agents as part
of this developer platform.
- [02:24] Before we get into how
we're actually doing that
- [02:26] on the platform, can we talk
about what even is an agent
- [02:29] to begin with?
- [02:30] - Yeah, I mean, agents is,
- [02:32] it's almost sort of a buzzword, right?
- [02:33] Like everybody you talk
to now is building agents
- [02:36] and whenever a industry tech
term gets to that level,
- [02:40] you know, the definition gets very gray.
- [02:42] Everything everybody builds is an agent.
- [02:44] But Anthropic, what we
really think about agent
- [02:47] is where the model is taking some autonomy
- [02:51] to be able to choose what tools to call,
- [02:53] to call those tools,
to handle the results,
- [02:56] and kind of choose the next step.
- [02:57] So as a foundational research lab,
- [03:01] leaning into the model
and what its reasoning,
- [03:05] how it decides what to do,
- [03:07] we think that's a really important element
- [03:09] of what an agent is.
- [03:10] - Mm, so it's kind of like the aspect
- [03:13] of it being autonomous in some sense.
- [03:14] - Yeah.
- Charting towards-
- [03:15] - I mean, I think there's also,
- [03:17] I mean, we have customers
doing really useful workflows
- [03:20] where they're sort of predefining the path
- [03:23] that Claude should walk
- [03:24] and that is a super-useful thing to do.
- [03:27] But what's nice about the agentic thing is
- [03:29] as the model gets better every
couple of months, you know,
- [03:32] we release a new model
- [03:33] and with a true agentic pattern, you know,
- [03:36] those services are just gonna get better.
- [03:38] Where if you build a workflow
- [03:41] with a lot of scaffolding in it,
- [03:42] you kind of put bounds on the model,
- [03:44] which is maybe okay in some use cases,
- [03:46] but that means that you
may not take advantage
- [03:49] of the next level of intelligence
- [03:51] that a next model release gets.
- [03:53] - Yeah, so it seems like
there's this interesting trend
- [03:55] with agents, at least
over the past 6-12 months,
- [03:58] where like you've said, the scaffolding
- [04:00] has been a bit of a hindrance,
- [04:01] and maybe we're dropping some of that.
- [04:04] Can you explain the
intuitions behind that around
- [04:08] is this actually the future
- [04:09] is we give less and less
things to the model?
- [04:12] - Yeah, I mean, I think over time
- [04:14] what we're seeing is the
scaffolding the model needs
- [04:17] to be able to accomplish
tasks is it's needing less
- [04:21] as the level of intelligence
of the model goes up.
- [04:25] And we believe is gonna keep going up
- [04:28] that basically the model has
more contextual understanding
- [04:32] of the high level task that
it's trying to accomplish.
- [04:35] So therefore it doesn't need
as many sort of guardrails,
- [04:38] And in fact, those
guardrails in some cases
- [04:41] become some like a liability to have.
- [04:44] We've had customers try out new models
- [04:47] and say, "Oh, well, it's actually only
- [04:49] just a little bit better."
- [04:50] And then we kinda look into it with them
- [04:52] about what's going on.
- [04:53] And it turns out well,
- [04:54] yeah, they were constraining it in ways
- [04:56] that makes it harder for them to see
- [04:58] the intelligence of the model.
- [04:59] - Ah, does this match
what we see in the field
- [05:02] with our customers
- [05:03] where they're also
following these same trends?
- [05:06] I know at the limit we
have customers exploring
- [05:08] all sorts of innovative
techniques for managing Claude.
- [05:12] - Yeah, totally.
- [05:12] And there's actually a lot of discourse
- [05:15] about this right now, right?
- [05:16] Like, what is an agent
and what does it need?
- [05:18] What do you need to build?
- [05:19] And there are people saying, you know,
- [05:21] "It's just a wild loop."
- [05:22] Like, "You don't have to try that hard."
- [05:24] And I think ultimately there's
been a lot of evolution
- [05:29] of frameworks that people
are putting around the model
- [05:32] that are helping them
orchestrate their agents,
- [05:35] try to get the most outta the model.
- [05:36] And I think what the industry
- [05:39] is maybe kind of circling around is
- [05:41] a lot of that has become maybe too heavy
- [05:43] and maybe too opinionated
- [05:45] and which is why you
kind of get the people
- [05:48] coming back to like,
"It's just a wild loop
- [05:50] and that is all you need."
- [05:52] And I think what we're
trying to do there is to say
- [05:55] maybe in a lot of ways it is a wild loop,
- [05:57] but the things we can more uniquely do
- [06:00] to help people get the
most out of the model
- [06:02] is a lot of those tools,
those features and otherwise.
- [06:05] And so what we wanna do is put, you know,
- [06:07] frameworks and tools
and platform out there
- [06:09] that is opinionated
- [06:11] to some extent on how people
should use those tools.
- [06:15] But it's not this super-heavy framework
- [06:18] that really to Brad's
point gets in the way
- [06:20] of what the model's
ultimately trying to do.
- [06:22] So it's strike the right balance.
- [06:23] It's like, you know, we've
seen what a lot of people
- [06:25] have tried to do, so we know
we can be opinionated there,
- [06:28] but we wanna be lightweight in
the way that we're doing that
- [06:31] and make sure that the
real thing we're doing
- [06:33] is helping you get the
most out of the model
- [06:35] without, you know, bogging you down
- [06:37] in some super-heavy framework.
- [06:39] - Right, so would you describe
- [06:40] part of the strategy here then
- [06:41] as providing these
auxiliary tools and things
- [06:46] that we can give to the model,
- [06:47] but we're not necessarily
placing the bumper
- [06:51] spawn the model itself?
- [06:53] - Yeah, we think about it as like,
- [06:54] how do you unhobble the model?
- [06:56] The model already has
a lot of capabilities.
- [06:58] In fact, I'm convinced that
- [06:59] even if you take your
current generation of models,
- [07:02] there's way more intelligence in there
- [07:03] than we've been able to unlock.
- [07:05] But anyway, that intuition
is if you just give the model
- [07:10] tools it needs and set it free,
- [07:12] let it be able to use
those in the right way,
- [07:15] you'll get great results.
- [07:16] And I think a good example of that
- [07:19] is we launched this
server-side web search tool
- [07:23] and web fetch tools.
- [07:24] And it's been interesting to
watch customers use those.
- [07:28] And you know, all we did really,
- [07:30] I mean it's a very minimal
prompt that we have.
- [07:32] We just give it the web search tool
- [07:34] and all of a sudden deep research tasks
- [07:37] are almost completely done
- [07:40] with just turning on
that switch on the API,
- [07:43] because the model will call that tool,
- [07:45] it'll look at its results,
it'll say, consider it
- [07:48] and say, okay, maybe I
need to call, you know,
- [07:50] do these other searches
- [07:51] and then, oh, that fourth link you return,
- [07:53] that's the great one.
- [07:54] It'll do a web fetch on that
link and bring that data back.
- [07:57] And really all that very
autonomously on its own
- [08:00] kind of deciding.
- [08:01] - Right, I think it's almost kind of like
- [08:03] an interesting shift in
where the intelligence
- [08:06] of a system is being applied.
- [08:07] - Exactly, yeah.
- From the developer
- [08:09] having to apply their
intelligence to guiding
- [08:11] towards the model now, figuring it out.
- [08:13] - Right, and it's so exciting
what the model does it,
- [08:16] because as a developer,
- [08:18] my creativity ends at some point.
- [08:20] I can only think of so many use cases,
- [08:22] but the model, like anything,
- [08:24] anything somebody comes with
the model will figure out a way
- [08:27] to go do that thing.
- [08:28] So it's great, great
to unhobble the model.
- [08:31] - Yeah, so if I'm a developer today
- [08:33] and I'm getting started building
- [08:35] with the developer platform,
what do you recommend?
- [08:38] What are some best practices
or ways for me to get started?
- [08:41] - Yeah, so super-tactically,
actually the number one thing
- [08:44] that we recommend right
now is the Claude Code SDK.
- [08:48] And what's really, really interesting
- [08:49] about the Claude Code SDK
- [08:50] is we essentially built an agent harness
- [08:54] an agentic harness around the
model to run that loop, right?
- [08:58] And automate a lot of that tool calling
- [09:00] and otherwise feature use.
- [09:01] And obviously originally was
built for coding purposes.
- [09:05] And what the team really
quickly figured out was like,
- [09:07] actually this is an excellent
- [09:09] general purpose agentic harness.
- [09:12] And so what the SDK does is
it gives people a perfect
- [09:16] out-of-the-box solution
- [09:17] to actually just start prototyping agents
- [09:20] without having to go and build, you know,
- [09:22] the loop with all the tool
calling and otherwise.
- [09:25] It's built on top of the messages API
- [09:27] and all those same tools
that we're mentioning.
- [09:30] But it kind of gives you that
really great starting place
- [09:32] right out-of-the-box.
- [09:33] - Right, I feel like this is
a pretty common misconception,
- [09:35] at least when I talk to developers
- [09:37] about the Claude Code SDK.
- [09:39] So I'm not building a coding application.
- [09:42] Why would I wanna use this?
- [09:44] But you can kind of remove
the coding-specific parts,
- [09:47] - Yeah, I mean I think
that's a great example
- [09:50] of what we were talking about
- [09:51] removing scaffolding on the model.
- [09:53] It's like once we got done
removing things from Claude Code
- [09:57] to really unhobble the model,
- [09:59] it turns out there was
nothing coding left.
- [10:01] When you remove everything else,
- [10:03] then it's just agentic loop
- [10:05] and you're really a
minimalistic thing to give
- [10:08] Claude access to a file system,
- [10:12] to a set of Linux command line tools
- [10:15] to the ability to, you know,
- [10:17] write code and execute that code.
- [10:19] So those are all very
generic kind of capabilities
- [10:22] it turns out could solve a
wide variety of problems.
- [10:24] - Right, yeah.
- [10:25] I feel like something
I've been running up to
- [10:28] in my own side projects
- [10:29] and also seeing with
projects within Anthropic
- [10:32] is before the Claude Code SDK,
- [10:34] everybody's implementing some form of
- [10:36] managing prompt caching
- [10:38] or some form of managing their tool calls
- [10:40] and that loop.
- [10:42] And now it's like, oh, just
start at this base point,
- [10:45] and then build from there.
- [10:46] - You start a little bit higher up.
- [10:47] - Yeah.
- Yeah, yeah, yeah.
- [10:48] - So it's like a further
level abstraction.
- [10:50] I think that's super-interesting.
- [10:51] - I mean, I think the other
really interesting thing
- [10:53] to think about, especially for
businesses looking at agents
- [10:57] is what use case to go target.
- [11:00] So thinking beyond the technology,
- [11:02] what is the actual problem to go solve?
- [11:05] And I think, you know,
we see a lot of customers
- [11:07] and doing a lot of
things we love all of it,
- [11:10] but where, you know,
the biggest impacts are
- [11:12] is where a customer has thought hard about
- [11:15] what's the business value of this?
- [11:18] Will it actually save this
many engineering hours
- [11:22] or will it help us remove this
much manual work or whatnot?
- [11:28] And being able to articulate
what you expect the outcome
- [11:31] of the agent project to be,
- [11:33] I think is really helpful
- [11:34] in defining the scope of the agent.
- [11:37] - Right, and tying back
one more time to the SDK.
- [11:41] So it seems like it's been
really, really useful for
- [11:44] individual developers
like myself, you know,
- [11:46] starting out and just
wanting to get hacking
- [11:48] on something really fast
- [11:50] for these customers, for enterprises
- [11:52] that are actually trying
to get real business value
- [11:54] on these things.
- [11:56] Should they be using the SDK?
- [11:57] Is it ready for them?
- [11:58] Is it ready for scaled use like that?
- [12:01] - Yeah, so I think in a lot of ways it is,
- [12:04] in a lot of ways if you are
in a spot where you can,
- [12:08] like, you can deploy that runtime,
- [12:10] essentially, that's what
you get outta the SDK
- [12:12] is an agentic loop runtime.
- [12:15] You can go and deploy that
runtime wherever you want,
- [12:17] whenever you're ready to do so.
- [12:19] But I think what we're really trying to do
- [12:20] is take the spirit of what
the SDK unlocks for people,
- [12:24] go kind of up to that
higher order abstraction
- [12:27] where we give you the loop,
- [12:28] we give you a lot of the tool
calling in an automated way
- [12:31] and say, how can we learn from that
- [12:33] and give people out-of-the-box
solutions that at scale
- [12:37] will really be able to
solve for their use cases.
- [12:40] And I think that's a lot of
where we're kind of trying to go
- [12:43] with our roadmap throughout
the rest of the year.
- [12:45] And one really important
bit when we think about that
- [12:48] is if the entire goal
here is to help our users
- [12:52] really raise that ceiling of intelligence,
- [12:54] get the absolute best
outcome outta the models,
- [12:56] then higher order abstractions
are not just make it easier,
- [13:00] because you don't have to
write all that code yourself.
- [13:02] It's actually like, how can
we really, truly help you
- [13:05] get the best outcome?
- [13:07] Because we're in the room with research,
- [13:09] we're in the room with inference,
- [13:10] we know how to make sure
that our abstractions,
- [13:13] our agentic loop is going
to be extremely powerful
- [13:16] and extremely good at working with Claude.
- [13:19] And the last thing that
I would add in there is,
- [13:21] especially as these
things get longer running
- [13:24] and as we provide more and more tooling
- [13:25] to help people get at
those longer running tasks,
- [13:28] another big problem that our users
- [13:30] we know are gonna keep trying to solve
- [13:32] is observability within
those longer running tasks.
- [13:36] And so that's one of
the most common things
- [13:39] that comes up for folks is, you know,
- [13:41] I have these long running tasks,
- [13:42] I'm trying to get these
really great outcomes,
- [13:45] but you know, I might
need to do some steering
- [13:48] or I might need to tune my prompt,
- [13:49] or I might need to
think about tool calling
- [13:51] a little differently.
- [13:52] And that's something that
we know we can give people
- [13:55] that observability through
the platform over time.
- [13:58] And that's another big
area of focus for us.
- [14:00] - Mm, okay, that's really interesting.
- [14:02] I mean, this has been a huge issue
- [14:04] that's starting to come
to a head with agents-
- [14:07] - I think so.
- [14:08] - ... especially as you trust
them to go work in some,
- [14:11] you know, other application
in the background,
- [14:13] how do you make sure they're
actually doing the right thing
- [14:15] and then if you're deploying them.
- [14:17] - Yeah, how do you audit it?
- [14:18] Like if we're gonna give
some level of autonomy
- [14:20] to the system, there needs
to be a way to audit it
- [14:22] and make sure the right
things are happening,
- [14:24] so that you can tune things and whatnot.
- [14:26] So I think observability is
really a key piece of this.
- [14:31] - And putting a pin there that
I wanna ask a question on,
- [14:34] just the future of how
we're gonna address that.
- [14:37] Before I do, is there other
tools that exist right now
- [14:41] that folks should be aware of
- [14:42] when they're getting started
with the developer platform,
- [14:45] things that you've
found helpful or useful?
- [14:48] - Yeah, I mean, I think there's a,
- [14:49] so we mentioned web search and web fetch.
- [14:52] I think an another big
thing that we're seeing
- [14:56] is customers right now
have to do a lot of work
- [15:01] to manage the context window.
- [15:02] So by default, Claude has
200 K tokens of context.
- [15:06] We have a million token
available now in beta on Sonnet,
- [15:11] which is great, but even a
million, there's a limit there.
- [15:14] And what many customers have told us
- [15:17] is that they get better
outputs, higher intelligence
- [15:20] if they even use a smaller
part of the context.
- [15:24] And so we've done, we have
a couple of cool features
- [15:27] that are just coming out
- [15:29] to help developers manage that context.
- [15:31] So in these agentic loops,
a lot of times you're doing
- [15:35] 10, 15, 100 tool calls
and you edit this file
- [15:40] or look up data in this database
- [15:41] or you know, send this email
- [15:44] and each of those tool calls takes up
- [15:47] 100, 200, 1,000 tokens.
- [15:49] And so we have this cool feature
- [15:51] that lets the model actually remove
- [15:55] some of the older tool calls
that are not needed anymore.
- [15:58] - Interesting.
- And that gives,
- [16:00] just like you, if you declutter your desk
- [16:02] and declutter your notebook,
- [16:03] you can focus a little bit better.
- [16:05] So if you declutter the prompt actually,
- [16:07] the model can actually
focus a little bit better.
- [16:09] - Ah, interesting.
- [16:10] So okay, we're moving unnecessary context.
- [16:12] Is there a risk that we
remove necessary context?
- [16:16] - Yeah.
- How does that work?
- [16:17] - Yeah, yeah, yeah.
- [16:17] So we have some guardrails
and some bounds around it,
- [16:22] but the general rule is
- [16:26] we try to remove the tools
that are several turns back,
- [16:30] that the model's already made decisions
- [16:31] based on those tools.
- [16:33] Yeah, I was playing with it recently
- [16:35] and I removed the tools
that it was just called
- [16:39] and it's, oh, my tool results are gone,
- [16:41] I don't know what to do.
- [16:42] And then, but the model,
the Sonnet doesn't give up.
- [16:44] It's like, I'm just gonna call
this tool again, you know?
- [16:46] - Yeah, yeah, yeah, yeah.
- [16:47] - But yeah, so generally we
have put some bounds on that,
- [16:50] because of that experience.
- [16:51] So we do preserve the
most recent set of tools.
- [16:53] - I see, okay.
- [16:54] - And then the other cool
thing we do is tombstone it.
- [16:58] So by that we mean when
we remove the tool calls,
- [17:02] we put a note in there
to the model that say,
- [17:04] oh, the tool results for
the search call were here.
- [17:08] - Oh, okay.
- And they've been removed.
- [17:09] - So the model's not
completely memory wiped.
- [17:11] - Exactly.
- [17:12] I think we found the model does better
- [17:14] if we just give it a little more context
- [17:16] about what is happening.
- [17:19] And so that's a key feature.
- [17:22] And the other one is
- [17:23] this kind of agentic memory feature
- [17:28] that we've added.
- [17:30] And there we have seen
- [17:33] that the model does,
- [17:36] right now, if you give
a task to the model,
- [17:38] say a deep research task
or play Pokemon or whatnot,
- [17:42] the model does about the
same every time it runs.
- [17:46] But if you give a human a task,
- [17:49] the fifth time the human does a task,
- [17:50] they do it way better,
- [17:52] because they've learned, okay,
- [17:53] if I'm gonna do this search, okay,
- [17:55] probably the Wikipedia site is better
- [17:58] than this other site or whatever.
- [17:59] They learn which thing, so
they get better over time.
- [18:03] So we've given this memory
tool to the model now,
- [18:05] so that the model can
actually take some notes
- [18:08] while it's going and say,
- [18:09] oh, I realize that this website
maybe isn't the right one,
- [18:13] or if I'm doing a search,
it should be like this,
- [18:15] or if I'm looking up, I
should use this database,
- [18:18] not that database or whatnot.
- [18:20] And it makes those notes.
- [18:21] And then when it's stumped,
- [18:23] it can actually go back
and review its notes
- [18:25] and say, okay, oh, I'm starting this task,
- [18:28] let me go read the notes,
so I can figure it out.
- [18:30] - Ah, cool.
- [18:31] So we're handling all of that
for the developer to say.
- [18:34] - Yeah, yeah, well, we're giving the model
- [18:36] this core capability to do memory,
- [18:39] and right now we're letting the
developer manage the memory.
- [18:42] So, because, you know,
different developers,
- [18:43] they might wanna store
it in some cloud storage
- [18:46] or they might wanna
store it somewhere else.
- [18:47] So we're letting developers
figure out exactly
- [18:49] where to store the memory.
- [18:51] That way they have more control over that.
- [18:54] - But exposing the tool.
- But expose the tool.
- [18:56] Yeah, we expose the tool.
- [18:57] - So going back again to
a roadmap question here.
- [19:00] So it sounds like there's
a ton of new features
- [19:02] that we've recently launched.
- [19:03] There's a lot of momentum,
- [19:04] and now there's other offerings as well,
- [19:06] like the Claude Code SDK
and things coming out soon.
- [19:10] What are you most excited about, Katelyn?
- [19:12] What's the future looking like
here in the next 6-12 months?
- [19:15] - Yeah, so we talked a little bit about
- [19:17] these higher orders of abstraction
- [19:18] where we can really just make it
- [19:22] as simple as possible
- [19:23] for you to get the absolute
best outcomes out of Claude.
- [19:27] And we wanna pair that
with the observability
- [19:29] that we talked about,
- [19:30] so that you can really, you know,
- [19:32] see the data and take those insights
- [19:34] from those longer running tasks.
- [19:37] And if you can combine
these things together
- [19:38] and start to think about
some of the capabilities
- [19:40] like memory that Brad just talked about,
- [19:42] you can really start to see this flywheel
- [19:44] where over time we're
not just able to help you
- [19:46] get the best outcomes out of Claude,
- [19:48] but we can help you get self-improving
- [19:50] and continuously improving
outcomes out of Claude.
- [19:53] And that to me is kind
of the galaxy brain magic
- [19:56] of the roadmap is get to
a point where, you know,
- [19:59] we have people coming to us,
they're building on Claude,
- [20:02] they have their tasks, they
know what they're trying to do,
- [20:05] and they get these really like aha moments
- [20:08] where over time it's getting
better and better and better.
- [20:12] And you know, that's
kind of the biggest thing
- [20:15] that in everything that we're doing,
- [20:16] we're trying to make
sure we're going after.
- [20:18] - That's awesome.
- [20:19] - Yeah, I mean, I guess I'd have to say
- [20:21] I'm always excited about model launches.
- [20:23] It's like Christmas, wow,
- [20:25] what will be possible now?
- [20:28] So I love playing with the model launches
- [20:30] they come out, just
unlocks more use cases,
- [20:32] some use cases that, you know,
we've been working hard on
- [20:35] and trying to improve,
which is satisfying to see,
- [20:38] but also some things I
had no idea the model
- [20:41] would be able to do this thing.
- [20:42] You know, now it draws ASCII
pictures so much better
- [20:45] or what, you know, whatever.
- [20:46] - The important things.
- Very important things.
- [20:48] But beyond that, the other
thing I'm really excited about
- [20:51] is we're in the early stages
of giving Claude a computer.
- [20:56] You know, I think about
if we hire an employee
- [20:59] here at Anthropic and we welcome 'em,
- [21:01] "Here's your first day."
- [21:02] But we don't give them a computer.
- [21:04] They would not be very
successful at Anthropic.
- [21:07] So right now, essentially
everybody is using Claude
- [21:10] and it doesn't have a computer.
- [21:12] So I'm really excited about
giving Claude a computer
- [21:15] and you see the very baby steps of that
- [21:18] with the code execution tool,
- [21:20] where the model can write
code executed on the VM
- [21:24] and get the results back.
- [21:26] So it can zoom in on images
- [21:30] or take a Excel spreadsheet
- [21:32] and create amazing data
analysis with charts and graphs.
- [21:36] And that's just the baby step.
- [21:38] What if I had a persistent computer
- [21:39] that was always there
- [21:41] and it could organize the files
in there the way it needed
- [21:44] and get the tools set
up the way it wanted.
- [21:47] And I just think there's a lot
of headroom to that scenario.
- [21:51] - Yeah, and I guess that all
ties back into this unhobbling
- [21:54] into this too.
- Exactly, exactly.
- [21:55] It's all about unhobbling the model.
- [21:57] That's exactly, just
give Claude the tools.
- [21:59] - Yeah.
- Yeah.
- [22:00] - Well, I'm excited for that future.
- [22:02] Thanks so much for this conversation.
- [22:03] - All right, cool.
- [22:04] Yeah, thank you.
- Thanks.
