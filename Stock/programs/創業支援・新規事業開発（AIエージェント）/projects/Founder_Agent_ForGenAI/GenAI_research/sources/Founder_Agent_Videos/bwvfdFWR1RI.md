---
title: "So, normally when I build a prompt using and using LLM, I usually start with a, a smaller LLM. And i..."
video_id: "bwvfdFWR1RI"
video_url: "https://www.youtube.com/watch?v=bwvfdFWR1RI"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
  - "Agents"
  - "LLM"
topics:
  - "AI Agents"
  - "LLM Development"
  - "Prompt Engineering"
  - "Workflow Automation"
summary: |
  So, normally when I build a prompt using and using LLM, I usually start with a, a smaller
  LLM. And if I can't get that to work, I move to a slightly larger one. I can't get that to work, I
  move to a bigger one and a bigger one and a bigger one. But what happens if you've got, if
key_points:
  - "LLM. And if I can't get that to work, I move to a slightly larger one. I can't get that to work, I"
  - "you're using the biggest LLM you have available and you still can't get it to work? One"
  - "option is to use an agentic workflow instead of a single prompt to a single"
  - "LLM. This actually happened to me recently. I was working on a problem, and I was using the biggest,"
  - "will, what we're going to do in this video is we're going to walk through that problem, and I'll"
  - "information. The first piece of information was a list of items that were not included in the order."
  - "was not an explanation, put that into a file like a text file that would look something like this."
  - "issues with edge cases. You know, for example, let's say that the explanation here for"
category: "AI Agent Development"
confidence_level: "high"
---

# Transcript: bwvfdFWR1RI

- URL: https://www.youtube.com/watch?v=bwvfdFWR1RI
- Retrieved at: 2025-12-30T11:36:09+09:00

## Text

- [00:00] So, normally when I build a prompt using and using LLM, I usually start with a, a smaller
- [00:06] LLM. And if I can't get that to work, I move to a slightly larger one. I can't get that to work, I
- [00:12] move to a bigger one and a bigger one and a bigger one. But what happens if you've got, if
- [00:17] you're using the biggest LLM you have available and you still can't get it to work? One
- [00:23] option is to use an agentic workflow instead of a single prompt to a single
- [00:30] LLM. This actually happened to me recently. I was working on a problem, and I was using the biggest,
- [00:35] baddest LLM I had available to me, and I could not solve the problem with a single prompt. So what
- [00:42] will, what we're going to do in this video is we're going to walk through that problem, and I'll
- [00:46] show you how I shifted from a single LLM to an agentic workflow. So the
- [00:52] problem was it seemed pretty straightforward at the beginning. I was given two pieces of
- [00:58] information. The first piece of information was a list of items that were not included in the order.
- [01:04] So imagine you've submitted a grocery request to a grocery store, and an employee goes through and
- [01:11] kind of does your shopping for you. So the first piece of items was, the first piece of information
- [01:17] were the items that were not included in the order.
- [01:26] The second piece of information were notes from the employee, and the employee, if he's not able to
- [01:31] find an item, he's supposed to mention that in the notes.
- [01:42] So the request that was made of me was to look at the items in column B, the items that were not
- [01:49] included in the order, and make sure that there was an explanation in column A. And if there
- [01:56] was not an explanation, put that into a file like a text file that would look something like this.
- [02:08] Cheese- No explanation. So I was able to get it to work for the most part, but I had, I had
- [02:15] issues with edge cases. You know, for example, let's say that the explanation here for
- [02:21] cheese is meh. Okay, that's really not a good reason not to get the cheese.
- [02:28] And because the reasons had to be valid in this column, um, sometimes I had trouble telling
- [02:35] which reads, I could identify the reasons, but I couldn't really tell if they were valid or not. So
- [02:40] again, because I wasn't able to solve this problem with a single prompt to the largest LLM, I moved
- [02:46] to an agentic workflow. Here's what my agentic workflow basically looked like.
- [03:00] So I had the first prompt. I had one prompt that extracted items
- [03:09] from B with an explanation.
- [03:18] The second prompt took the information from the first prompt and
- [03:25] determined whether or not those reasons were valid. The third prompt, and it probably didn't have to
- [03:31] be a prompt, but you could use a prompt or an LLM to do it, is compare.
- [03:41] P2 output to
- [03:48] B, to column B. And then, the fourth would be just to
- [03:55] output the text. So again, maybe you do this in three prompts. Maybe maybe do it in
- [04:02] four. Maybe these actually aren't prompts in an LLM. There's some other function, text function. Um,
- [04:08] that's really not the point here. The point is that I tried to do this with a single prompt, and
- [04:14] I couldn't get it to work. This worked. And if you look at these prompts kind of individually,
- [04:19] they're really doing different things. Like this first one, I would say it's more of an extraction
- [04:25] function. It's extracting information from the text. This one is doing some, it's more of a
- [04:30] classification. It's looking at the reasons and trying to determine whether or not that reason is
- [04:36] valid or not. Um, the third one, you're just doing a comparison. So I guess that's kind of a
- [04:40] classification. And then the output of text, that's more of a generation. So we were trying to do. It
- [04:45] didn't seem that way at first, but because we were trying to do all these different types of prompts
- [04:51] or these types of functions inside the prompt, I think the, the original LLM trying to do this in
- [04:56] one big bite was getting confused. So let's take this and go back to our original example to see
- [05:02] how it would work in the, in the, in the workflow. So P1 here,
- [05:09] you know would look at this information right here and extract something like this. Ham:
- [05:17] Old Cheese: May.
- [05:24] The second prompt would look at this information right here and determine that, you
- [05:30] know, meh is not a really a good reason not to fill an order. So it would be something like this.
- [05:39] The third prompt would compare this to this, and we would end up with something that
- [05:46] looked like this. Because again, cheese is the item in here without a valid explanation for not
- [05:52] being filled. And then the fourth would basically be output
- [05:59] this into the final format. So again, sometimes, the biggest baddest LLM is not going
- [06:06] to do everything. And sometimes, you have to break the problem into several steps and use multiple
- [06:12] LLMcalls, multiple prompts, or multiple functions to get to where you need to be. And doing that is
- [06:17] called an agentic workflow.
