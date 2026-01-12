---
title: "- URL: https://www.youtube.com/watch?v=sMQ5R92F86o"
video_id: "sMQ5R92F86o"
video_url: "https://www.youtube.com/watch?v=sMQ5R92F86o"
speaker: ""
channel: ""
date: ""
duration: ""
tags: ["hiring", "machine_learning", "marketing", "PMF", "AI", "team_building", "product_development", "growth"]
topics: ["成長戦略", "プロダクト開発", "組織構築", "AI技術"]
summary: |
  - URL: https://www.youtube.com/watch?v=sMQ5R92F86o
  - Retrieved at: 2025-12-30T16:28:37+09:00
  - [00:00] Most AI agents don't fail because of weak models. They fail because of the data behind them. More
key_points:
  - "- [00:25] 1% of enterprise data makes its way into generative AI projects today. And here's the key:"
  - "- [03:35] data management goes beyond just integration. We also need to understand the data and trus"
  - "- [04:10] extract key entities like names, dates, topics, transforming raw files into structured ana"
category: "AI技術"
confidence_level: "high"
---


# Transcript: sMQ5R92F86o

- URL: https://www.youtube.com/watch?v=sMQ5R92F86o
- Retrieved at: 2025-12-30T16:28:37+09:00

## Text

- [00:00] Most AI agents don't fail because of weak models. They fail because of the data behind them. More
- [00:05] than 90% of enterprise data is unstructured. Things like contracts, PDFs, Word documents,
- [00:12] emails, transcripts, images, audio, video, and so much more. Unlike rows in a database,
- [00:19] this content can't be easily searched, queried or fed directly into a model. That's why less than
- [00:25] 1% of enterprise data makes its way into generative AI projects today. And here's the key:
- [00:32] public data is already baked into foundation models, so the real differentiator for AI is
- [00:36] unlocking and harnessing enterprise data. Caroline, what makes unstructured data so difficult to
- [00:42] leverage? The challenge with unstructured data is that it's scattered across systems, inconsistent
- [00:48] in format, and often full of sensitive information. So, handing it straight to an AI agent risks
- [00:53] hallucinations, inaccurate answers or even leaks. To cope, data engineering teams have relied on
- [00:59] tedious manual work, sifting through disparate documents, stripping out sensitive details and
- [01:05] stitching together custom scripts. This does not make our engineer happy. The process can take
- [01:10] weeks. But the landscape is changing. That's why today we'll talk about two essential concepts: unstructured
- [01:16] data integration, which transforms raw content into AI-ready datasets in minutes, and
- [01:22] unstructured data governance, which ensures those datasets can be discovered, catalog and trusted.
- [01:28] Together, they enable reusable, unstructured pipelines alongside structured ones, unlocking a
- [01:33] goldmine of data to power new use cases and address the technical challenges of integrating
- [01:38] unstructured data into AI workloads. This makes our engineers' lives a lot easier. Let's start with
- [01:45] integration. Adrian, can you describe what that looks like in practice? Of course. Integration is
- [01:50] about transforming messy, raw, unstructured data into structured, machine-readable datasets. Think
- [01:56] of it as extending the familiar principles of structured data integration to a new modality.
- [02:01] Like ETL pipelines for structured sources, unstructured data integration creates repeatable
- [02:05] pipelines that ingest, process, and prepare high volumes of content. Only this time it's documents, emails,
- [02:12] chats, audio and more. The result? Users can automate in minutes what previously
- [02:18] required weeks of custom scripting and maintenance. Here's how it works: We first ingest
- [02:24] data from sources like SharePoint, Box, Slack, Filestores and more, using prebuilt connectors.
- [02:32] We then transform using prebuilt operators for text extraction, deduplication, language annotation, personally
- [02:38] identifiable information removal, chunking content into usable segments and
- [02:43] vectorizing those segments into embeddings. We finally then load embeddings into a vector
- [02:50] database where they fuel retrieval augmented generation or RAG, AI agents, document
- [02:56] classification, intelligence search and more, all without requiring deep machine learning expertise.
- [03:02] So, something like this? Yes, exactly. But what happens if a document changes?
- [03:08] Updates don't require rerunning the entire pipeline. Only the delta is captured and pushed
- [03:13] downstream, keeping pipelines current at scale without costly reprocessing. And for security. native
- [03:19] access control lists support prev ... preserves document-level permissions so users and agents
- [03:25] only see what they're authorized to, ensuring compliance and trust throughout the pipeline.
- [03:30] Unstructured data integration is a game changer, but it is only the first step. True unstructured
- [03:35] data management goes beyond just integration. We also need to understand the data and trust it.
- [03:42] Caroline, how does that work? Integration focuses on data delivery and usability, but governance is
- [03:48] what makes unstructured data truly discoverable, organized and trustworthy. Just as structured data
- [03:54] has long benefited from data governance solutions, we now have end-to-end governance designed
- [03:59] specifically to address the complexities of unstructured data. Let's walk through the steps. First,
- [04:04] we connect to unstructured assets across the enterprise using prebuilt connectors. We then
- [04:10] extract key entities like names, dates, topics, transforming raw files into structured analyzable
- [04:16] data. Next enrichment pipelines classify content, assess quality and add contextual
- [04:23] metadata. Documents are tagged with topics, people or sentiment to make them easier to
- [04:28] organize and interpret. Results appear in simple validation tables with configurable rules and
- [04:33] alerts that flag low-confidence metadata, helping ensure accuracy and trust. Assets then move
- [04:39] through workflows into a central catalog, improving organization and discoverability. With
- [04:45] technical and contextual metadata in place, users can now search and filter intelligently across
- [04:50] all assets. And finally, data lineage tracks how documents move from source to target, providing
- [04:56] full visibility, compliance and auditability. With this governance layer, data teams deliver reliable,
- [05:02] structured datasets that enable accurate AI model outputs and ensure compliance. Adrian, can
- [05:08] these two technologies, unstructured data integration and governance, be used together?
- [05:13] Unstructured data integration and governance close the reliability gap by giving AI agents
- [05:18] high-quality, contextualized domain knowledge. With embeddings stored in a vector database, agents
- [05:24] retrieve precise information instead of guessing, fueling more accurate RAG, copilots and domain-specific
- [05:30] assistants. But the power doesn't stop with AI. The same foundation supports high-value
- [05:37] use cases such as analytics and reporting. Teams can mine customer calls for sentiment trends, scan
- [05:44] contracts to track compliance risks, or analyze field reports to uncover operational insights, all
- [05:50] without manually sifting through thousands of files. Caroline, how do you see this shifting the
- [05:55] enterprise AI story? It's a huge shift. Reliable AI agents require more than just smart models.
- [06:02] They require smart data pipelines. Integration makes the data usable, and governance makes it
- [06:08] trustworthy. But together, they unlock the 90% of enterprise data that's historically been out of
- [06:14] reach. And this isn't just about AI agents. It's about giving enterprises new visibility into
- [06:21] unstructured content. That's how teams can transition AI projects from prototypes to
- [06:26] scalable production-grade systems.
