---
title: "Transcript: S6wc6yvoZLY"
video_id: "S6wc6yvoZLY"
video_url: "https://www.youtube.com/watch?v=S6wc6yvoZLY"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: "00:04:47"
tags:
  - "AI"
  - "Agents"
  - "Product Development"
topics:
  - "AI Agents"
  - "Product Development"
summary: |
  動画の内容を分析中...
key_points:
  - "AI and technology discussion"
  - "Industry insights"
  - "Future perspectives"
category: "AI Agents"
confidence_level: "high"
---

# Transcript: S6wc6yvoZLY

- URL: https://www.youtube.com/watch?v=S6wc6yvoZLY
- Retrieved at: 2025-12-30T10:52:22+09:00

## Text

- [00:00] Earlier this year, online payments
- [00:01] changed forever, and you probably didn't
- [00:03] even notice. Every internet user has
- [00:05] heard of the HTTP status code 404 not
- [00:08] found. But if you're a web developer,
- [00:10] you might have nightmares about status
- [00:12] code 500, internal server error, which
- [00:14] happens when your shoddy deployed code
- [00:16] breaks in production. But there's one
- [00:18] HTTP status code that's just been
- [00:20] sitting there since 1997, waiting for
- [00:22] its moment to shine, 402, payment
- [00:25] required. It was reserved for future use
- [00:27] back when the web was young and
- [00:28] optimistic. But now, three decades
- [00:30] later, we're still figuring out how to
- [00:31] handle money on the internet without
- [00:33] giving platforms like Stripe a 3% cut
- [00:35] before the privilege of pressing some
- [00:37] buttons. Well, that's about to change
- [00:39] thanks to a new protocol developed by
- [00:40] Coinbase called X42 that enables micro
- [00:43] payments that can turn every API request
- [00:46] into a tiny cash register with zero
- [00:48] fees. And what's especially crazy is
- [00:50] that these payments are instantaneous,
- [00:52] frictionless, and open the door for
- [00:54] machine toachine payments. Like, imagine
- [00:56] an entire AI economy where AI agents are
- [00:59] paying other AI agents to do whatever AI
- [01:01] agents do. What could possibly go wrong?
- [01:04] In today's video, we'll find out by
- [01:05] taking a closer look at X42 and its
- [01:07] promise to revolutionize the way money
- [01:09] moves on the internet. It is November
- [01:11] 26, 2025, and you're watching the Code
- [01:14] Report. One thing that sucks about
- [01:15] platforms like Stripe is that they
- [01:17] charge a 30 cent fee per transaction,
- [01:19] which makes them overly complex for
- [01:21] certain use cases. Like if you have an
- [01:23] API where you charge one penny per
- [01:25] request you'd be running at a negative
- [01:26] 3,000% profit margin. That's not
- [01:29] acceptable even by Silicon Valley
- [01:30] standards. So the solution is to force
- [01:33] users to authenticate OOTH to verify a
- [01:35] credit card, then either buy
- [01:36] subscriptions or credits on your
- [01:38] platform for a higher dollar amount and
- [01:39] then replenish them when they run out.
- [01:41] It's complicated, but X42 dramatically
- [01:44] simplifies this workflow. In fact, it
- [01:46] only takes one line of middleware code
- [01:47] in Node.js to get up and running. If a
- [01:49] buyer makes a request to a paid API
- [01:51] endpoint, the server responds with an
- [01:53] HTTP 402 code, which means a payment is
- [01:56] required to complete the request. The
- [01:58] user would then see a page like this
- [01:59] asking them to connect a wallet at which
- [02:01] point the transaction can be completed
- [02:03] without subscriptions, authentication,
- [02:05] or any other friction. In addition, the
- [02:07] process can be done programmatically on
- [02:09] the buyer side using handwritten code or
- [02:11] even AI agents. Pretty cool. But now,
- [02:14] let's actually deploy our own monetized
- [02:15] API from scratch. Before doing that
- [02:18] though, we need a reliable back-end
- [02:19] server to run our code, like Hostinger,
- [02:22] the sponsor of today's video. Their
- [02:23] virtual private servers give you the
- [02:25] power and flexibility to run whatever
- [02:27] you want without locking you into
- [02:28] someone else's platform. And for less
- [02:30] than 10 bucks a month, you get a
- [02:32] respectable two CPUs and 8 GB of RAM.
- [02:35] And right now, you can save a ton of
- [02:36] money with their Black Friday deal and
- [02:38] then save even more money after that by
- [02:40] stacking it with the Fire Ship discount
- [02:41] code. In this demo, we'll build both
- [02:43] client and server apps. So, I'm choosing
- [02:45] a Docker VPS. What's especially awesome
- [02:48] about this VPS is its Docker Compose
- [02:50] Manager where you can deploy, run, and
- [02:52] monitor multiple apps with a highly
- [02:54] efficient, streamlined interface, which
- [02:56] is provided free of charge from
- [02:58] Hostinger. But now that we have a server
- [02:59] lined up, let's take a look at the code.
- [03:01] Here I have a dead simple Node.js JS app
- [03:03] using hono to build a restful API. When
- [03:06] someone navigates to this protected
- [03:08] route, it will give them some highly
- [03:09] secret esoteric knowledge only known to
- [03:12] 33rd degree Freemasons. This knowledge
- [03:14] is so valuable that we must require a
- [03:16] payment of exactly one bitcoin to access
- [03:18] it. Although with X42, you can handle
- [03:20] payments of less than 1 cent and use
- [03:22] stable coins like USDC. Right now,
- [03:25] anybody can access this route, but we
- [03:27] can change that by simply installing the
- [03:28] X42 SDK from npm. Most importantly, it
- [03:32] contains a middleware function that will
- [03:34] put a payw wall in front of this route.
- [03:35] The first argument to this function is
- [03:37] your wallet address where the funds will
- [03:39] be sent. Then the second argument
- [03:40] contains an object with some
- [03:42] configuration values like the route you
- [03:44] want to protect, the price, the amount
- [03:46] of time allowed to complete the purchase
- [03:47] and the decentralized network that will
- [03:49] handle the transaction. And as a seller,
- [03:51] that's basically all there is to it. If
- [03:53] we now open up the app on localhost as a
- [03:55] potential customer and hit that URL, we
- [03:57] get a 402 response that will require us
- [03:59] to make a payment. In a web app, the end
- [04:01] user can use a wallet extension like
- [04:03] MetaMask or Coinbase wallet to complete
- [04:05] the transaction. Then once that's
- [04:07] complete, they'll receive a response
- [04:08] with the knowledge of a 33rd degree
- [04:10] Freemason. That's cool and all, but
- [04:12] buyers can also make payments
- [04:13] programmatically. If we go back to the
- [04:15] code, we can use the X42 fetch library,
- [04:17] which can do all sorts of things,
- [04:19] including handle the payment request
- [04:20] automatically. And that's pretty awesome
- [04:22] if you're building a paid API where AI
- [04:24] agents can access paid resources on
- [04:27] someone else's behalf. And now we can
- [04:28] deploy everything together by
- [04:30] dockerizing it, pushing it to GitHub,
- [04:32] and then let our Hostinger VPS run it in
- [04:34] production. I'm not sure I'm ready to
- [04:35] let AI make live payments for me, but
- [04:37] hey, at least when it drains my bank
- [04:39] account, it'll do it efficiently. Huge
- [04:41] thanks to Hostinger for sponsoring, and
- [04:42] make sure to lock in the discount while
- [04:44] there's still time. This has been the
- [04:45] Code Report. Thanks for watching, and I
- [04:47] will see you in the next one.
