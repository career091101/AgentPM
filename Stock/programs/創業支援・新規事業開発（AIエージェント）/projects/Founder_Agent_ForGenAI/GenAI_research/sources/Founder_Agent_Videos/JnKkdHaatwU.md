---
title: "[music] Hello everyone."
video_id: "JnKkdHaatwU"
video_url: "https://www.youtube.com/watch?v=JnKkdHaatwU"
speaker: "the"
channel: "Unknown"
date: ""
duration: ""
tags: ["AI", "Agents", "LLM", "Tutorial", "Development"]
topics: ["AI", "Agents", "LLM", "Tutorial", "Development"]
summary: |
  In the last series, we deep dive into the foundation of multi- aent system
  And today we are introducing a game changer, the model context protocol, the MCP and this is the start of two episode series
  By the end of the series, you will know everything you need to know to get started with ADK agents and MCP, including how to connect an ADK agent to an MCP server and also how to use ADK to build your own MCP server
key_points:
  - "episode, we will cover three things"
  - "is what is an MCP server and why is a universal adapter for all AI agents"
  - "is why do you need to use MCP"
  - "part is what is an MCP server"
  - "part of today's video is why do we want to connect ADK agents with an MCP server"
  - "since MCP server expose tools, your agent now can access huge external capabilities"
  - "it give you modularity and reusability"
  - "concepts in the setup"
category: "AI Agents"
confidence_level: "medium"
source: "Founder_Agent_Videos"
retrieved_at: "2025-12-30T10:29:14+09:00"
---

# Transcript: JnKkdHaatwU

- URL: https://www.youtube.com/watch?v=JnKkdHaatwU
- Retrieved at: 2025-12-30T10:29:14+09:00

## Text

- [00:01] [music]
- [00:04] Hello everyone. In the last series, we
- [00:07] deep dive into the foundation of multi-
- [00:09] aent system. And today we are
- [00:12] introducing a game changer, the model
- [00:14] context protocol, the MCP
- [00:18] and this is the start of two episode
- [00:20] series. By the end of the series, you
- [00:22] will know everything you need to know to
- [00:24] get started with ADK agents and MCP,
- [00:27] including how to connect an ADK agent to
- [00:31] an MCP server and also how to use ADK to
- [00:34] build your own MCP server. So for this
- [00:37] first episode, we will cover three
- [00:39] things. The first is what is an MCP
- [00:43] server and why is a universal adapter
- [00:46] for all AI agents. And secondly is why
- [00:49] do you need to use MCP? And lastly, we
- [00:53] will walk through two examples of
- [00:55] connecting an ADK agents to an MCP
- [00:58] server. We will also have a detailed
- [01:00] written tutorial from the link on the
- [01:02] screen so that you can try yourself. All
- [01:04] right, let's dive in. So the first part
- [01:07] is what is an MCP server? At its core,
- [01:11] the model context protocol is an open
- [01:14] standard. It defines how large language
- [01:17] model and AI agents can talk to the
- [01:19] external world. Think of it as MCP is a
- [01:23] USBC port for AI. Instead of building a
- [01:27] custom connector for every single tool,
- [01:31] you get one universal way of plugging
- [01:34] in. And there are two important concepts
- [01:36] in the setup. The MCP client and MCP
- [01:40] server. And here is how it works. So
- [01:43] when it comes to MCP server expose tools
- [01:48] for example it can connect to data
- [01:50] sources APIs or custom actions so that
- [01:54] we can do data fetching calling API or
- [01:57] customized logics with actions and then
- [02:00] we have this MCP client. It discovers
- [02:04] and use those tools and in most cases
- [02:07] your ADK agent acts as an MCP client and
- [02:11] it connects to MCP servers to gain new
- [02:15] capabilities. And the second part of
- [02:18] today's video is why do we want to
- [02:20] connect ADK agents with an MCP server?
- [02:24] Basically, why bother with this
- [02:27] universal adapter? Why not just connect
- [02:30] directly to those tools? And the answer
- [02:32] is very simple. MCP makes your agents
- [02:36] more powerful, more reliable, and more
- [02:39] practical. And here is what you get with
- [02:42] MCP. Firstly, since MCP server expose
- [02:46] tools, your agent now can access huge
- [02:49] external capabilities. For example, it
- [02:52] can read or write files on a local or
- [02:55] remote file system. It can query
- [02:58] database like BigQuery or MongoDB. It
- [03:01] can also connect a realtime directions
- [03:04] from Google maps and has many more. For
- [03:07] example, it can use generative media
- [03:09] tools like imaging for image
- [03:11] generations.
- [03:13] And secondly, it give you modularity and
- [03:16] reusability. An MCP server can be a
- [03:19] standalone service and any MCP compliant
- [03:22] client including ADK agent can plug in
- [03:26] and there's no custom glue code
- [03:28] required. This means less custom
- [03:31] integration code and more reusable
- [03:34] components. It can also offer security
- [03:36] and control. MCP allows you to define
- [03:40] clear boundaries. And last but not
- [03:42] least, a simplified deployment strategy.
- [03:45] With remote server you can decouple
- [03:47] tools from your agent and that makes
- [03:49] scaling a lot easier in environment like
- [03:51] cloud run or GKE. So the bottom line is
- [03:56] connecting ADK with MCP can allow your
- [03:59] ADK agent to interact with the real
- [04:02] world and make a true agentic system.
- [04:05] And now the third part of this video is
- [04:08] how to connect an ADK agent to an MCP
- [04:11] server. How do we actually do it? And
- [04:14] ADK makes it really simple with
- [04:16] something called MCP tool set. And you
- [04:19] can think of it as ADK's built-in bridge
- [04:22] to the MCP world. And here is what it
- [04:25] does behind the thing. So first it set
- [04:28] up the connection with the MCP server.
- [04:31] And this can be a local process or a
- [04:34] remote HTTP server. And then you will
- [04:38] load all the available tools from MCP
- [04:41] server. And while you're doing that, it
- [04:43] translate those MCP tools into ADK
- [04:46] compatible version so that it can handle
- [04:49] communication back and forth. When your
- [04:51] agent decided to use an MCP tool, the
- [04:54] MCP tool set forward a request to the
- [04:57] MCP server and send a response back to
- [05:00] your agent. And let's take a look at
- [05:02] this two quick example. For the first
- [05:05] example, file system MCP server.
- [05:08] Remember your agent is a model as a
- [05:11] brain and select a tool from the toolbox
- [05:13] and make a decision right. So what if
- [05:16] you want your agent to equip this tools
- [05:19] like listing or reading files from this
- [05:22] folder. So in this Python example the
- [05:26] MCP tool set is configured to launch an
- [05:29] MPX command that runs the file system
- [05:32] MCP server. It pass a target folder path
- [05:36] as arguments and giving server access to
- [05:39] that specific directory. By using MCP2
- [05:43] set, your agent now can use tools like
- [05:47] this directory and read file right in
- [05:50] this toolbox. You can follow the
- [05:52] instruction on the screen or scan the QR
- [05:54] code for more details about how to
- [05:56] connect to your MCP server. All right,
- [05:59] let's take a look at the second example.
- [06:01] Google Map MCP server. You can think of
- [06:04] a situation like okay you want to figure
- [06:06] out the direction from San Francisco to
- [06:08] New York. How do you figure out the
- [06:10] direction with your agent? You can
- [06:12] easily do that by connecting to MCP
- [06:15] Google map. With MCP tool set after
- [06:19] setting up your API key and enabling all
- [06:22] the necessary Google map APIs, your
- [06:25] agent now can respond to prompts like
- [06:28] tell me the direction from New York to
- [06:30] San Francisco. Again the link on the
- [06:32] screen will provide you with more
- [06:34] information of how to connect into this
- [06:36] MCP server. All right let's wrap up. So
- [06:40] firstly MCP is a universal connector for
- [06:43] AI agents and secondly connecting ADK
- [06:47] agents to MCP servers give them real
- [06:50] world capabilities stronger modularities
- [06:53] and more control. And lastly, with ADK
- [06:57] MCP2 set, the setup is really
- [07:00] straightforward.
- [07:02] So, this is the foundation for making
- [07:05] your agents truly powerful. If you want
- [07:08] to try yourself, check the links in the
- [07:10] description. And in the next episode, we
- [07:13] will flip the script and I will show you
- [07:15] how to build our own MCP server with ADK
- [07:20] tools. [music] And see you in next
- [07:22] episode. Bye. Heat. Heat. N.
- [07:35] >> [music]
