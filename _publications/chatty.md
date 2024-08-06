---
title: "CHATTY: Coupled Holistic Adversarial Transport Terms with Yield for Unsupervised Domain Adaptation"
collection: publications
permalink: /publication/chatty
excerpt: 'The new technique, CHATTY, enhances unsupervised domain adaptation by introducing a novel transport loss that displaces classifier outputs to reduce class confusion and improve domain-invariant representations, leading to superior UDA results on benchmark datasets.'
date: 2023-04-19
venue: 'Proceedings of the 27th International Conference on Pattern Recognition, Kolkata, India'

---
We propose a new technique called CHATTY: Coupled Holistic Adversarial Transport Terms with Yield for Unsupervised Domain Adaptation. Adversarial training is commonly used for learning domain-invariant representations by reversing the gradients from a domain discriminator head to train the feature extractor layers of a neural network. We propose significant modifications to the adversarial head, its training objective, and the classifier head. With the aim of reducing class confusion, we introduce a sub-network which displaces the classifier outputs of the source and target domain samples in a learnable manner. We control this movement using a novel transport loss that spreads class clusters away from each other and makes it easier for the classifier to find the decision boundaries for both the source and target domains. The results of adding this new loss to a careful selection of previously proposed losses leads to improvement in UDA results compared to the previous state-of-the-art methods on benchmark datasets. We show the importance of the proposed loss term using ablation studies and visualization of the movement of target domain sample in representation space.

[Paper Link](https://arxiv.org/abs/2304.09623)

Recommended citation: Chirag, P., Wagle, M., Gupta, R., Jeevan, P., & Sethi, A. (2023). CHATTY: Coupled Holistic Adversarial Transport Terms with Yield for Unsupervised Domain Adaptation. ArXiv, abs/2304.09623.