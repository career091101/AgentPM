---
title: "I have shot a video before about using GPUs in Cloud Run. Viewers asked in the comments about a real..."
video_id: "knT3kN4EpOo"
video_url: "https://www.youtube.com/watch?v=knT3kN4EpOo"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
  - "Agents"
  - "LLM"
  - "Programming"
topics:
  - "AI Agents"
  - "LLM Development"
  - "Tool Integration"
  - "Workflow Automation"
  - "Product Development"
summary: |
  I have shot a video before about using
  GPUs in Cloud Run. Viewers asked in the
  comments about a realistic application
key_points:
  - "comments about a realistic application"
  - ">> Yes, I agree. Let's dive in. My app is a"
  - "smart health agent that will create"
  - "including exercises and diet. To do"
  - "say that I live in San Francisco. I'll"
  - "are dummy records for John Doe created"
  - ">> We can see that the app responded. It"
  - ">> And it looks like you can ask follow-up"
category: "AI Agent Development"
confidence_level: "high"
---

# Transcript: knT3kN4EpOo

- URL: https://www.youtube.com/watch?v=knT3kN4EpOo
- Retrieved at: 2025-12-30T16:04:00+09:00

## Text

- [00:00] I have shot a video before about using
- [00:02] GPUs in Cloud Run. Viewers asked in the
- [00:06] comments about a realistic application
- [00:08] using that setup. I built one. Let me
- [00:11] show you.
- [00:12] [Music]
- [00:21] >> Hi Jay, welcome. You work at Nvidia,
- [00:24] right? Uh what do you do there?
- [00:27] >> Thanks for having me, Martin. Yes, I
- [00:29] work at Nvidia as a developer advocate.
- [00:32] I help AI engineers harness the power of
- [00:35] Nvidia GPUs for building LLM
- [00:37] applications.
- [00:39] >> Very good. And you wrote a sample
- [00:41] application that uses Nvidia GPUs in
- [00:44] Google Cloud, right?
- [00:46] >> That's right. NVIDIA GPUs integrates
- [00:48] seamlessly with the open-source AI
- [00:51] ecosystem and Google Cloud provides
- [00:53] excellent cloud infrastructure. Together
- [00:56] they make a great combo. And when
- [00:59] talking to developers, it's always
- [01:01] better to show code than slides.
- [01:05] >> Yes, I agree. Let's dive in. My app is a
- [01:09] smart health agent that will create
- [01:12] personalized wellness recommendation
- [01:14] including exercises and diet. To do
- [01:18] that, it asks me for my current daily
- [01:20] routine. I'll enter that. I work at a
- [01:24] desk, take daily walks, and go to bed
- [01:27] around midnight.
- [01:29] >> An hour of walking every day. That's
- [01:31] impressive.
- [01:33] >> Yes, I I try to do my best. Then I'll
- [01:36] say that I live in San Francisco. I'll
- [01:40] upload the medical records. Now, these
- [01:43] are dummy records for John Doe created
- [01:45] for the demo.
- [01:47] Then I'll click on the activate button
- [01:50] and the AI agent takes over.
- [01:52] >> I love those AI agent workflows.
- [01:55] >> We can see that the app responded. It
- [01:58] considered my daily routine and the
- [02:00] medical records. It even included the
- [02:03] current weather when crafting a
- [02:05] personalized recommendation.
- [02:08] >> And it looks like you can ask follow-up
- [02:10] questions.
- [02:12] >> Yes, that's right. I'll ask about my
- [02:14] cholesterol levels.
- [02:17] And here's the answer. It looks like I
- [02:19] may have to watch my cholesterol.
- [02:23] >> Very nice application, Jay. And uh what
- [02:26] AI model is it using?
- [02:28] >> It uses Gemma 3 model uh made by Google
- [02:31] deep mind and it is GPU optimized
- [02:35] >> and then it runs some sort of agent
- [02:37] workflow.
- [02:39] >> Yes, let's have a look. Here is the
- [02:42] Google cloud console. We are looking at
- [02:44] cloud run logs. Here is the routine that
- [02:47] I entered
- [02:49] here where it says rag. It starts
- [02:52] looking at the medical records that I
- [02:54] uploaded. It found five documents and it
- [02:57] split them up into chunks. Then it
- [03:00] vectorized those chunks and added them
- [03:03] into the vector store. in the
- [03:06] vectorization. That's a fancy way of
- [03:08] saying that you made the medical records
- [03:11] searchable by the AI.
- [03:13] >> Exactly. Now that the data is in place,
- [03:16] it's time for the agents to start.
- [03:19] First, the weather agent is called to
- [03:22] get the current weather in San
- [03:23] Francisco. That's the city I entered.
- [03:27] >> And then it says something about an
- [03:29] agent workflow.
- [03:31] Yes, the routine analysis agent
- [03:34] processes the entered information about
- [03:37] the user's daily activities. The
- [03:39] knowledge agent processes the medical
- [03:41] reports and together they come up with a
- [03:44] personalized health plan. That plan is
- [03:47] streamed in real time to the user
- [03:49] interface
- [03:51] >> and all this runs as a service in Cloud
- [03:54] Run.
- [03:55] >> Yes, it uses two services in Cloud Run.
- [03:59] Here they are. The smart health app CPU
- [04:02] service displays the user interface and
- [04:05] takes the input from the user. It is a
- [04:08] traditional web app without any AI. It
- [04:11] uses CPUs only, no GPUs.
- [04:15] >> Got it.
- [04:16] >> I've named the other service Olama
- [04:18] Gemma. It runs Gemma 3 on Olama. Ola is
- [04:23] a tool that makes it easy to download
- [04:25] and run large language models. I split
- [04:28] my application into two services as they
- [04:31] need different hardware and different
- [04:34] scaling behavior.
- [04:36] >> And the Olama Gemma service, that's the
- [04:39] one that uses GPUs.
- [04:41] >> Yes, it does. I'll click it. Then I'll
- [04:45] click the pen icon here. So we can look
- [04:48] at the details of the service.
- [04:50] Here in the resources section, it shows
- [04:53] that the service is using single Nvidia
- [04:56] L4 GPU.
- [04:58] >> Thanks for showing us this, Jay. I have
- [05:00] some questions for you.
- [05:02] >> Go ahead, Martin.
- [05:04] >> I'm a developer, so I like to see code.
- [05:07] I'm especially interested in how the
- [05:09] multiple agents work together.
- [05:12] >> I have open sourced this application, so
- [05:14] anyone can download it and adapt it to
- [05:17] their needs.
- [05:19] Here you can see how I use the line
- [05:21] graph library to put the agents together
- [05:24] in a workflow.
- [05:26] >> I will include a link to your repo uh
- [05:28] from the video description below. So
- [05:31] another option for agent orchestration
- [05:34] would have been to use Google's ADK
- [05:36] agent development kit. Right.
- [05:39] >> That's right. Uh but I'm more familiar
- [05:41] with Langraph so I use that framework.
- [05:44] Yeah, it's a good idea to use the tools
- [05:47] we have experience with. Now, uh why is
- [05:50] your application using its own copy of
- [05:53] Gemma? Because another option would have
- [05:55] been to call the Gemini API and not host
- [05:59] your model yourself.
- [06:01] The Gemini API works well for many
- [06:04] application, but if you want more
- [06:06] control, you are better off hosting the
- [06:09] model inside your own GPU cluster or
- [06:12] cloudr run service like I did. For
- [06:14] example, you may want to fine-tune your
- [06:17] model for federated learning.
- [06:19] >> Makes sense. How did you generate that
- [06:22] user interface? Uh, it looked pretty
- [06:24] good.
- [06:25] >> Oh, thank you. I wanted to keep things
- [06:28] simple, so I used Gradio library. I like
- [06:31] it because it lets you define a web user
- [06:34] interface in Python.
- [06:36] >> Cool. Uh I hadn't heard about Gradio
- [06:38] before. How was your developer
- [06:40] experience uh building this app?
- [06:43] >> It was pretty easy. Cloud Run is
- [06:46] serverless, so I didn't have to reserve
- [06:48] GPUs or provision any infrastructure.
- [06:51] Nvidia GPUs integrate seamlessly with
- [06:55] open-source AI ecosystem and Google uh
- [06:58] cloud provides excellent cloud
- [07:00] infrastructure. Together they make a
- [07:03] developer's life simple.
- [07:05] >> I like hearing that. Thank you for
- [07:07] joining me today, Jay.
- [07:09] >> Thanks for having me, Martin.
- [07:11] >> And thank you everyone for watching. If
- [07:13] you have any questions for Jay or me,
- [07:16] ask in the comments below. Also, please
- [07:18] let me know what you thought of this
- [07:20] episode. I love hearing from you and I
- [07:23] read every single comment. Now, go build
- [07:27] some great AI applications.
- [07:32] [Music]
