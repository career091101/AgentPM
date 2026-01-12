---
title: "Say you're watching tennis, and you want to know what's going on within a close match."
video_id: "FqF4b7Uemfc"
video_url: "https://www.youtube.com/watch?v=FqF4b7Uemfc"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags: ["AI", "Agents", "RAG", "LLM", "Tutorial", "Development", "Data Science"]
topics: ["AI", "Agents", "RAG", "LLM", "Tutorial", "Development", "Data Science"]
summary: |
  Say you're watching tennis, and you want to know what's going on within a close match
  Well, that's where an agent-oriented architecture comes in
  It's a real-time, interactive AI assistant powered by an agentic graph
key_points:
  - "Covers ai agents concepts and applications"
  - "Discusses AI, Agents, RAG"
  - "Suitable for learning and reference"
category: "AI Agents"
confidence_level: "medium"
source: "Founder_Agent_Videos"
retrieved_at: "2025-12-30T10:13:53+09:00"
---

# Transcript: FqF4b7Uemfc

- URL: https://www.youtube.com/watch?v=FqF4b7Uemfc
- Retrieved at: 2025-12-30T10:13:53+09:00

## Text

- [00:00] Say you're watching tennis, and you want to know what's going on within a close match. Well, that's
- [00:04] where an agent-oriented architecture comes in. It's a real-time, interactive AI assistant powered
- [00:10] by an agentic graph. Such a system was debuted at the 2025 Wimbledon Championships and the US
- [00:16] Open 2025. Now this assistant, it allows fans to ask live questions during singles matches and to
- [00:23] get instant and insightful answers right at your fingertips. Now here's an example path to the
- [00:29] experience. So as the user, what we can do is we can select a match that's either in play or scheduled
- [00:36] to play. Now the system, it supports conversations about in progress, retired, suspended and even
- [00:41] complete matches. But when the system is available, that any fan can then begin a dialog. They can
- [00:47] start a dialog by pushing one of these buttons. And let's say we want to push a Match Chat button
- [00:53] underneath the tennis match that has the score. You can also follow live or view a recap if you
- [00:58] want, but in all of these cases, we follow an evidence-based user experience. Now the real fun
- [01:04] really begins. So upon entry, the user is then gently nudged into a conversation with two pre-curated entry-level
- [01:11] questions, often around match-defining skills or even pivotable plays. This is
- [01:18] called classic UX priming, so we want to lower the barrier for engagement but spark your curiosity
- [01:24] and invite participation throughout a match. But of course, the more inquisitive minds, they might
- [01:30] want to ask any question. And this is where this open field comes in, where you can click and then
- [01:35] it'll open up, and you can put in any query that you can think of. With the user's question in hand
- [01:40] or maybe even this button pushed, the system transitions into this agentic experience,
- [01:45] launching this decision tree interaction. The user selects a primary category from the following, right?
- [01:52] Now, a user doesn't have to select this because again, they can enter any question that
- [01:56] they would like to, right. And whatever query you entered, it's dispatched to a scaled out cloud-based
- [02:02] system of systems, and it's really optimized for this real-time analysis and insight
- [02:08] generation. But even if no subcategory subcategory is chosen, we do invite a, you know, the
- [02:14] user to maybe have a dialog or a question-answer with the system to ensure that no curiosity goes
- [02:20] unanswered here. Now comes the moment of computational ingenuity. So here, a visual
- [02:25] indicator, it appears whenever you submit a query, showing that the LLM is either thinking
- [02:34] or it could be running, that this is where you have the chains of thoughts that are being fed
- [02:39] back into the model itself. Um, another aspect or a state that happens is called fact
- [02:45] checking. So we want to make sure that anything that's returned back by this real-time system,
- [02:50] it's accurate. But this small touch, it really adds what's called transparency to the AI's cognitive
- [02:56] process and maintains all the user's engagement throughout. Butimportantly, this experience is
- [03:02] also seamlessly mirrored across both mobile and desktop. So, it provides you this consistent and
- [03:07] device-agnostic interaction model, whether you're maybe sitting on the phone in a bleacher or
- [03:13] stadium or you're in a laptop at home, but the system is anywhere you are, it's ready on the go,
- [03:18] and it's right here for you. Now let's take a look at the architecture behind this system, where it
- [03:23] balances scale, response time and AI accuracy. So here's the masterpiece. So, at the foundation lies
- [03:30] a robust, event-driven architecture that's built on this publish subscribe messaging system. So as
- [03:36] a match progresses here, it ingests scoring and performance data all the way through to create
- [03:41] these different feeds. Now this data is immediately published to on-demand topics
- [03:45] enabling this near real-time availability. So simultaneously, the system writes dozens of these
- [03:52] JSON files into these cloud object storage buckets that are fronted by CDNs. This ensures
- [03:58] high-speed global distribution and caching. Now, once a user submits a query here, the message
- [04:05] traverses the secure firewall CDNs, and it finally lands in this containerized application known as
- [04:11] a middleware app. This is deployed across a distributed cloud infrastructure across multiple
- [04:16] regions, and it has 30 active replicas. The middleware app, what it does is it takes the
- [04:22] question, and it first analyzes and it interprets it. So first, we have this mini LM, L6 v2.
- [04:29] It's this model that has embeddings, and it transforms the query into numeric, to numerical
- [04:34] vectors. Now these embeddings are then passed through a random force of 100 different decision
- [04:40] trees, which classify the question into specific tennis categories, such as the player stats, the
- [04:45] match logistics. You might even have questions about live insights, but based on this confidence,
- [04:51] the thresholds that we have empirically determined, we then in turn go through, and we want
- [04:56] to know how, how confident is this model that this question is about a particular topic. So, as it
- [05:02] goes through the pipeline, we then need to ensure that the conversation, it remains safe and respectful.
- [05:09] So this is where we screen all the questions through this HAP, which stands for hateful abusive
- [05:15] profanity filters. And we then take that when we go through. And once we've classified and
- [05:22] we've gone through that moderation step through all those gates, we then can go to the next step.
- [05:26] And this is where the system, it reaches a decision point. If the question fits in a known
- [05:31] confidently classified category, we then go into this custom extension that's right here. Now,
- [05:38] if the, if the confidence is low or the anomaly detector flags ambiguity or the question is
- [05:44] then can be routed to this knowledge-based system, which is almost like a fallback system. And this
- [05:50] is deployed into two different regions. But here, this fallback system, it consults a library of
- [05:57] about 50 different intents that are mapped to topics, which then return thoughtful and
- [06:01] pre-trained responses. Forexample, if you're asking, where can I go find a place to get tickets, or
- [06:07] where can I find shade? That might go to our knowledge base, but in most cases, this includes a
- [06:12] deep link to the relevant tennis data, and it closes the loop so that the UX, it shows and
- [06:18] renders the appropriate context. So when a query does meet all these routing criteria, it's then sent
- [06:23] to this custom extension application here. And this is a powerhouse house app. It runs on over 60
- [06:29] replicas across a multi-region Kubernetes platform. So here is where then the traffic is
- [06:35] routed to this lane graph. It's pulled from a queue. So we we initialize many lane graphs at the
- [06:41] same time, right. And if one isn't ready, the system then waits until one does become available. But once
- [06:47] initialized and we have this agentic framework, we then can execute the following steps. Right.
- [06:54] And these steps, it uses a bunch of tools to go out, and it pulls in information such that we
- [07:00] can extract the relevant information that's about the question that we've already classified. Now,
- [07:06] this data is formatted in two different ways by the tool. We can have raw JSON, which preserves the
- [07:11] original schema and the keys that came from the tennis information. We also have an LLM JSON, which
- [07:17] is more of a decorative type text, and it helps to prime and, and optimize LLM comprehension of what
- [07:24] this data is about. And then we go into the generative agent part. And this is where the
- [07:29] structured data to the formulation of the answers comes into play. So if the agents determine that
- [07:35] they can't confidently respond from all this information, maybe it could be due to insufficient
- [07:41] data, or maybe the play hasn't caught up to what the person is asking about. Then we will notify
- [07:47] the middleware application. This is when there's no structured or generative agent can really
- [07:52] provide a cohesive answer. We then go to what's called a light synthesizer that's invoked as a
- [07:58] last resort. This is what we call a lightweight LLM prompt, where we attempt a final synthesis of the
- [08:05] information with any data fragments that still remain throughout this pipeline. And through all
- [08:10] of this, the architecture balances scale, speed, safety as well as accuracy to provide a nice
- [08:17] experience to you. At the core of this lies an agentic system architected as a directed graph.
- [08:23] Now in this graph, each agent is represented by a discrete computational agent that looks like a
- [08:30] node, and each of these nodes is connected by an edge. And the edge means information flows in
- [08:36] between the agents here. Now the process begins at this initialization agent here. This
- [08:42] creates, and it propagates a state variable. So this is a dynamic context object that goes
- [08:48] throughout this entire graph. But one of the earliest agent, it's called the tool agent here. It
- [08:54] interprets the conversational category signal, and it selects the appropriate data feeds for
- [09:00] extraction. Now this feed, it drives data from all the tennis state, and it then saves it into the
- [09:07] shared state for downstream agents. Now the next critical node in all of this is called the facts
- [09:13] agent. This performs parallel inference operations using two different types of thread right. So you
- [09:19] have thread one and thread two right. So the first thread, what it does is it constructs a prompt. It
- [09:25] includes a persona, right. So it tells it how to act and how to respond, the style it's supposed to
- [09:30] use for the extracted JSON data that it pulls out. It then submits it to an LLM to produce a
- [09:37] paragraph interpretation directly from the input. Now your thread two here, what this does is it
- [09:43] uses a synthesizer, right, that generates standalone factual sentences. And these sentences
- [09:48] are then fed into another LLM. And it's almost like a race. So the first one that
- [09:55] wins is then used in the propagated piece of the graph here. Now to manage the response latency and
- [10:01] ensure that the system responsiveness, each path of these, it operates with strict timeouts because
- [10:07] we want to be really fast so that users can see what the output is going to be. So the framework,
- [10:12] it allows for up to three different potential outputs in order of preference. So the first one
- [10:16] would be the direct JSON interpretation into a coherent paragraph. Now the next one that we try
- [10:22] to achieve would be a summarized paragraph from multiple factual sentences from one of these
- [10:27] threads that, again, is racing over time. And that's what one of these summarized agents what it does.
- [10:34] Now a collection of these goes to a judge here. Right. So that we then, in turn, can figure out what
- [10:40] is it supposed to say, what is it supposed to do. Right. And if it determines wait a minute, this
- [10:45] content isn't exactly right, then it's going to feed back into a corrective type agent here, right?
- [10:52] So we have these four agents all working together to produce this said output. Right.
- [11:00] And all the candidate outputs are then routed, right, all throughout down into this lower section
- [11:06] here, so that we then in turn can produce the content. But I want to revisit this judge agent
- [11:12] because what it does is it then, in turn, it evaluates the content on two primary dimensions.
- [11:18] The first one, it needs to make sure that the content that's produced is factual, right. But it's
- [11:23] also relevant to what the user has been asking about from the initialization to the tools agent. Now,
- [11:29] if the judge if it does identify uncertainty and the preferred output, it may pre-append, you
- [11:35] know, confidence adjusting a preamble, right, to the response. And then once judged, it might go into a
- [11:42] corrective type agent here. Right. And the corrective agent is enforce the textual
- [11:47] consistency by aligning the response to predefined stylistic guidelines that might have
- [11:52] been supplied by the tennis user, that if the agent pipeline, if it fails to produce a valid,
- [11:58] even a confident output due to maybe missing data, it could either be an ambiguity or even timeouts
- [12:05] of these threads that are constantly running in the background and erase the system. It can
- [12:09] activate a fallback search mechanism across a knowledge base, but should this too return no
- [12:14] useful result? the system performs this final synthesis using a lightweight LLM-based
- [12:19] synthesizer to generate informative responses. Now these final informative responses, they sometimes
- [12:26] go down here, right? And when this does happen, we then can return that back right to the user But
- [12:32] these final contingencies ensure that the system maximizes response coverage. But it also is highly
- [12:38] accurate so that we can provide to the user and answer that aligns towards what they're asking
- [12:44] for. So now let's look at some of the streaming data. The real-time Live Likelihood to Win
- [12:49] estimation within our system is enabled by a streaming data architecture and probabilistic
- [12:55] modeling framework. Now this system integrates predictive analytics, live match dynamics, and
- [13:00] event based computation to generate and update this Likelihood to Win estimates all throughout
- [13:06] the duration of a match. Now what happens is, prior to the first serve, we have a pre-match Likelihood
- [13:12] to Win. That looks very much like this a donut plot, but this model, it's a predictive model, right?
- [13:19] And it gives you a probability of a player winning before a match starts for each of the
- [13:23] players. Now we have a model that's been built on a couple features, right. Some of them are around
- [13:29] head to head history between the players. Now if they have the head to head history, if not then
- [13:34] we'll go to other predictors. Now we also have forecasted play indicators and historical match
- [13:39] outcomes that all go into this So for example in a specific match scenario, you know I might have a
- [13:45] model that predicts player A to have a 53% Likelihood to Win. And I might have player B that
- [13:51] has a 47% chance Likelihood to Win. Now this close distribution, it indicates a statistically
- [13:57] balanced match. Right. That could happen. And what the models are doing is it's applying this
- [14:02] probabilistic equation, where we want to make sure that we can get the odds of a player winning,
- [14:07] given the evidence that I just showed you. Now, as the match progresses, we have this Likelihood
- [14:12] to Win that looks like this. Now the system transitions to this Live Likelihood to Win every
- [14:19] single point. So it's continuously updating the probability model using this real-time
- [14:23] performance metrics. Now the the Live Likelihood the model. It is a time defined model
- [14:30] which we have a decayed pre-match probability which gradually diminishes the pre-Likelihood to
- [14:36] Win pieces. Right. So as the match unfolds we then in turn say the match data that's happening
- [14:43] in real time matters more. And then we also have a booster function that's activated by critical
- [14:49] match events. This approach, it enables a system to account for both the historical expectation
- [14:56] and the real time player dominance that's happening now in this five set match. As you can
- [15:01] see the score right here. The player with the pre-match edge up here had a 53% and ultimately
- [15:08] did win three sets to two. But you can see the story as it was unfold that it wasn't just a
- [15:14] linear win, right? That one of the players was had more momentum and then it shifted back. It shifted
- [15:20] back again. And then finally we get it right because we then in turn converge to what the
- [15:25] ultimate player who won, which is player A, right. And this happened after a tie break and this
- [15:29] dramatic sequence of events. Now, this visualization of serves not only as a statistical
- [15:34] output, but also as a narrative of the matches momentum. It captures competitive tension as well
- [15:40] as the turning points within this high fidelity, message driven architecture. These insights are
- [15:45] made possible by this messaging and for structure that you can see here. And it's a pub sub piece
- [15:51] that uses what's called MQTT pieces. Some of this, it uses what's called a broker application that
- [15:57] subscribes to match specific topics upon scheduling. And then as each of these scoring
- [16:02] events occurs. The data is published to each of the relevant topics that we have. So it's highly
- [16:09] parallelized so that it's very fast and we retrieve these messages here. Right? And then we
- [16:15] pass it to an engine. And this engine is what uses some of these equations that I went over to
- [16:21] create. Right. These numbers here that we have. But each scoring updated triggers the recalculation
- [16:28] of this Live Likelihood to Win at that moment in time of play. The resulting value is
- [16:34] serialized and stored right over into a CDN and a cloud object storage, enabling this
- [16:40] asynchronous access from our fans all around the world So when a fan asked a question, you know,
- [16:46] through our agentic system about live or past win probabilities, the system performs some of the
- [16:52] following steps. So first we'll go and we'll retrieve the relevant JSON Likelihood to Win data
- [16:58] that's been created by this system here. And this utilizes the data extractor agents to transform
- [17:05] the data into the semantic objects and we in turn, submit all of the summarized data to an LLM,
- [17:11] and this integration ensures that fans now receive intelligible, data-driven responses
- [17:16] grounded in the probabilistic analytics and powered by this real-time computational system
- [17:22] that we have here. Now the agent-oriented system, it delivers a real-time, intuitive experience by
- [17:28] combining the live scoring data with this AI pipeline that interprets fan queries and updates
- [17:34] the match insights like momentum shifting and the wind predictions. But by this blending the AI
- [17:41] and streaming data, and we combine gen AI with predictive modeling with this smart UX. This is
- [17:48] how we transform that raw data into clear, engaging narratives for tennis fans all around
- [17:53] the world.
