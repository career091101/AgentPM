---
title: "Our AI agent works perfectly when I'm the only one using it."
video_id: "ESIL0Rzl5VQ"
video_url: "https://www.youtube.com/watch?v=ESIL0Rzl5VQ"
speaker: "the"
channel: "Unknown"
date: ""
duration: ""
tags: ["AI", "Agents", "Tutorial", "Development"]
topics: ["AI", "Agents", "Tutorial", "Development"]
summary: |
  Our AI agent works perfectly when I'm the only one using it
  But what happens when the rest of the internet shows up
  So today we simulate that nightmare scenario with a load test to see if our architecture scales gracefully or just starts crying
key_points:
  - "create a session with the agent and then in a loop it will repeatedly send one of several random questions just like a real person would"
  - "Covers ai agents concepts and applications"
  - "Discusses AI, Agents, Tutorial"
category: "AI Agents"
confidence_level: "medium"
source: "Founder_Agent_Videos"
retrieved_at: "2025-12-30T10:12:17+09:00"
---

# Transcript: ESIL0Rzl5VQ

- URL: https://www.youtube.com/watch?v=ESIL0Rzl5VQ
- Retrieved at: 2025-12-30T10:12:17+09:00

## Text

- [00:00] Our
- [00:05] AI agent works perfectly when I'm the
- [00:08] only one using it. But what happens when
- [00:10] the rest of the internet shows up? So
- [00:11] today we simulate that nightmare
- [00:13] scenario with a load test to see if our
- [00:15] architecture scales gracefully or just
- [00:17] starts crying.
- [00:19] Welcome back. So far we've deployed a
- [00:21] GPU powered a Gemma model and a separate
- [00:24] ADK agent that talks to it. To simulate
- [00:26] traffic, we're going to use an open-
- [00:28] source tool called Locust to simulate a
- [00:30] flood of users and watch how our two
- [00:32] Cloud Run services scale or don't scale
- [00:35] independently. To simulate traffic, we
- [00:37] need a script that acts like a real
- [00:39] user. So, let's take a look at load
- [00:41] test. py. This is a Locust script.
- [00:43] Locust is a Python package that allows
- [00:45] us to simulate user queries. Our user
- [00:48] will first create a session with the
- [00:50] agent and then in a loop it will
- [00:52] repeatedly send one of several random
- [00:54] questions just like a real person would.
- [00:57] We'll run this from the command line to
- [00:59] generate the traffic. The command tells
- [01:02] Locust to use our script target the
- [01:04] agents URL and ramp up to three
- [01:06] concurrent users over 3 seconds. It
- [01:09] doesn't sound like much, but for a GPU,
- [01:11] this could be a real workout. Okay,
- [01:13] here's a setup. On the left I have the
- [01:15] metrics for our lightweight ADK agent
- [01:17] and on the right the metrics for our
- [01:19] heavyduty GPU powered a Gemma 3 service.
- [01:22] Both services are currently idle with
- [01:25] one instance running. Now I'm going to
- [01:27] start the load test in my terminal. Keep
- [01:29] your eyes on the instance count graphs.
- [01:32] The test is running. Users are sending
- [01:34] messages and the GPU service is scaling
- [01:36] up. Cloudr run detected the high demand
- [01:39] for model inference and automatically
- [01:41] provisioned more GPU servers to handle
- [01:43] it. But now look at the left. The ADK
- [01:45] agent instance count is rock steady at
- [01:47] one. It's barely breaking a sweat
- [01:49] because all it's doing is passing
- [01:51] messages. It doesn't need to scale. This
- [01:53] is the whole point of our architecture.
- [01:55] We are only scaling the expensive
- [01:57] resource inensive part of the system
- [01:59] while the lightweight part remains
- [02:00] efficient and cheap. So what have we
- [02:02] learned? Here are some key points.
- [02:04] Decoupling is key. Separating your agent
- [02:06] logic from your model server is critical
- [02:08] for production. Scaling the bottleneck.
- [02:10] Our GPU backend was the bottleneck and
- [02:12] it scaled beautifully to meet demand.
- [02:14] Cost efficiency. By only scaling the GPU
- [02:17] service when needed, we saved a ton of
- [02:19] money. Cloud Runs scale to zero or one
- [02:22] behavior is perfect for this. You've now
- [02:24] seen the full journey from deploying a
- [02:26] model to building an agent to stress
- [02:28] testing the final productionready
- [02:30] architecture.
- [02:31] I hope this series gave you the
- [02:32] confidence to take your own AI projects
- [02:34] into production. You now have a
- [02:36] powerful, scalable, and cost-effective
- [02:38] pattern you can use for your own
- [02:40] applications. Thanks so much for
- [02:41] watching.
- [02:52] [Music]
