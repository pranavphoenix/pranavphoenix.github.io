---
title: "“So You Think You’re Funny?”: Rating the Humour Quotient in Standup Comedy"
collection: publications
permalink: /publication/emnlp
excerpt: 'A new dataset and model for computational humor are proposed, which can automatically rate the humor quotient of stand-up comedy clips.'
date: 2021-11-07
venue: 'Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, Punta Cana, Dominican Republic'

---
Computational Humour (CH) has attracted the interest of Natural Language Processing and Computational Linguistics communities. Creating datasets for automatic measurement of humour quotient is difficult due to multiple possible interpretations of the content. In this work, we create a multi-modal humour-annotated dataset (~40 hours) using stand-up comedy clips. We devise a novel scoring mechanism to annotate the training data with a humour quotient score using the audience’s laughter. The normalized duration (laughter duration divided by the clip duration) of laughter in each clip is used to compute this humour coefficient score on a five-point scale (0-4). This method of scoring is validated by comparing with manually annotated scores, wherein a quadratic weighted kappa of 0.6 is obtained. We use this dataset to train a model that provides a ‘funniness’ score, on a five-point scale, given the audio and its corresponding text. We compare various neural language models for the task of humour-rating and achieve an accuracy of 0.813 in terms of Quadratic Weighted Kappa (QWK). Our ‘Open Mic’ dataset is released for further research along with the code.

[Paper Link](https://aclanthology.org/2021.emnlp-main.789)

Recommended citation: Anirudh Mittal, Pranav Jeevan P, Prerak Gandhi, Diptesh Kanojia, and Pushpak Bhattacharyya. 2021. “So You Think You’re Funny?”: Rating the Humour Quotient in Standup Comedy. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 10073–10079, Online and Punta Cana, Dominican Republic. Association for Computational Linguistics.