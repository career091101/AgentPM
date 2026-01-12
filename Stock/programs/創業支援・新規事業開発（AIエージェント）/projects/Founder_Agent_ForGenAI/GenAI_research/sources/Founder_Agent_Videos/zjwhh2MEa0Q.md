---
title: "- URL: https://www.youtube.com/watch?v=zjwhh2MEa0Q"
video_id: "zjwhh2MEa0Q"
video_url: "https://www.youtube.com/watch?v=zjwhh2MEa0Q"
speaker: ""
channel: ""
date: ""
duration: ""
tags: ["AI", "machine_learning"]
topics: ["AI技術"]
summary: |
  - URL: https://www.youtube.com/watch?v=zjwhh2MEa0Q
  - Retrieved at: 2025-12-30T16:47:55+09:00
  - [00:00] Yes, Python has a ternary operator.
key_points:
  - "- [01:09] But importantly, the condition"
  - "- [01:15] which is important in a case like this"
  - "- [02:36] But today they should not"
category: "AI技術"
confidence_level: "high"
---


# Transcript: zjwhh2MEa0Q

- URL: https://www.youtube.com/watch?v=zjwhh2MEa0Q
- Retrieved at: 2025-12-30T16:47:55+09:00

## Text

- [00:00] Yes, Python has a ternary operator.
- [00:04] The ternary operator in many languages since 1960 
has looked something like this, using the question mark.
- [00:11] But Python is way too cool for that. 
So in Python, it's written using "if"
- [00:16] And to top it all off, it's not even referred to 
as a ternary operator, even though it totally is!
- [00:23] Instead, an expression like this in Python
- [00:25] "a if some condition else b" is technically 
referred to as a conditional expression.
- [00:32] But anyone will know what you mean if you 
say ternary operator or if expression.
- [00:36] Side note: Why is it called ternary 
and not trinary?
- [00:39] I don't know, maybe if 
you're an English expert,
- [00:42] you can comment down 
below, and I'll pin the answer.
- [00:45] The way it works is it 
first evaluates the condition,
- [00:47] and then if it's true, gives you the 
first thing; otherwise, the second thing.
- [00:50] This is kind of out of 
order of the way that it's written.
- [00:53] But it's more in line with how 
you might say it out loud in English.
- [00:57] The value is "x" if "x" is bigger 
than 0, otherwise, negative "x."
- [01:02] A lot of different alternatives were
 considered, but they literally held a vote.
- [01:05] And this "if" syntax won 
out over using a question mark.
- [01:09] But importantly, the condition 
is the first thing that's evaluated.
- [01:12] And the expression that's 
not returned doesn't get evaluated at all
- [01:15] which is important in a case like this 
where we don't want to divide by 0.
- [01:19] It's a similar idea as 
short-circuiting for "and" and "or."
- [01:23] It's basically just syntactic sugar for a 
full "if" statement, but it also returns a value.
- [01:29] And keep in mind that 
this is Python.
- [01:31] And in Python, it usually doesn't check
 whether a value is literally "equals equals true."
- [01:36] Instead, Python uses its 
notion of truthiness
- [01:38] where something like a non-empty 
list would be considered true,
- [01:42] but an empty list would 
be considered false.
- [01:44] In general, it's good for short definitions, like 
setting the default value of a mutable argument.
- [01:49] But do your best not 
to go overboard.
- [01:51] It quickly becomes unreadable if you try 
to stuff too much stuff into one expression.
- [01:56] Just like with any other operators,
 beware of operator precedence.
- [01:59] Where you put or don't put 
parentheses can change the answer.
- [02:02] The ternary operator has the lowest
 precedence of any operator in the language.
- [02:06] So the parentheses, if you were
 to put them in, look like this:
- [02:11] Now for the surprising part, the Stack 
Overflow answers for this question.
- [02:17] Luckily, the first answer 
is the one that I would recommend.
- [02:21] But number two with 
over 900 upvotes.
- [02:24] And number three with over 400 upvotes 
tell you to do something completely bonkers.
- [02:30] These answers are 
from 2008 and 2009.
- [02:33] Back when these answers were written,
 they served a completely legitimate purpose.
- [02:36] But today they should not 
appear anywhere in your code.
- [02:40] I wish Stack Overflow 
had a way to flag an answer
- [02:43] as severely out of date without 
hurting the reputation of the original poster.
- [02:47] After all, if you tried to ask this 
question again today to get a modern answer,
- [02:51] it would surely be 
closed as a duplicate.
