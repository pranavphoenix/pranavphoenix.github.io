---
title: "Normalizing Flow Based Metric for Image Generation"
collection: publications
permalink: /publication/fld
excerpt: 'We propose two efficient flow-based metrics, FLD and D-FLD, that provide accurate realness assessment of generated images with significantly fewer parameters and samples than FID, making them ideal for evaluating small image sets in diverse domains.'
date: 2024-10-02
venue: 'Arxiv'
image: 'wavepaint.jpg'
width: '800'
---

We propose two new evaluation metrics to assess realness of generated images based on normalizing flows: a simpler and efficient flow-based likelihood distance (FLD) and a more exact dual-flow based likelihood distance (D-FLD). Because normalizing flows can be used to compute the exact likelihood, the proposed metrics assess how closely generated images align with the distribution of real images from a given domain. This property gives the proposed metrics a few advantages over the widely used Fréchet inception distance (FID) and other recent metrics. Firstly, the proposed metrics need only a few hundred images to stabilize (converge in mean), as opposed to tens of thousands needed for FID, and at least a few thousand for the other metrics. This allows confident evaluation of even small sets of generated images, such as validation batches inside training loops. Secondly, the network used to compute the proposed metric has over an order of magnitude fewer parameters compared to Inception-V3 used to compute FID, making it computationally more efficient. For assessing the realness of generated images in new domains (e.g., x-ray images), ideally these networks should be retrained on real images to model their distinct distributions. Thus, our smaller network will be even more advantageous for new domains. Extensive experiments show that the proposed metrics have the desired monotonic relationships with the extent of image degradation of various kinds.

[Paper Link](https://arxiv.org/abs/2410.02004)

Recommended  Jeevan, P., Nixon, N., & Sethi, A. (2024). Normalizing Flow Based Metric for Image Generation.