---
title: "WaveMix: A Resource-efficient Neural Network for Image Analysis"
collection: publications
permalink: /publication/wavemix
excerpt: 'WaveMix is a new resource-efficient and scalable neural architecture for computer vision that achieves comparable or better accuracy than the state-of-the-art in multiple-computer vision tasks.'
date: 2026-07-10
venue: 'GlobalSouthML Workshop at International Conference on Machine Learning (ICML) 2026, Seoul, South Korea'
image: 'wavemix.jpg'
width: '800'
carousel:
  acronym: "WaveMix"
  tagline: "Token Mixer"
  image: "papers/wavemix.jpg"
  venue: "ICML 2026"
  tags:
    - "Token Mixer"
    - "Efficiency"
---

We propose WaveMix -- a novel neural architecture for computer vision that is resource-efficient yet generalizable and scalable. WaveMix networks achieve comparable or better accuracy than the state-of-the-art convolutional neural networks, vision transformers, and token mixers for several tasks, establishing new benchmarks for segmentation on Cityscapes; and for classification on Places-365, five EMNIST datasets, and iNAT-mini. Remarkably, WaveMix architectures require fewer parameters to achieve these benchmarks compared to the previous state-of-the-art. Moreover, when controlled for the number of parameters, WaveMix requires lesser GPU RAM, which translates to savings in time, cost, and energy. To achieve these gains we used multi-level two-dimensional discrete wavelet transform (2D-DWT) in WaveMix blocks, which has the following advantages: (1) It reorganizes spatial information based on three strong image priors -- scale-invariance, shift-invariance, and sparseness of edges, (2) in a lossless manner without adding parameters, (3) while also reducing the spatial sizes of feature maps, which reduces the memory and time required for forward and backward passes, and (4) expanding the receptive field faster than convolutions do. The whole architecture is a stack of self-similar and resolution-preserving WaveMix blocks, which allows architectural flexibility for various tasks and levels of resource availability. Our code and trained models are publicly available.

<iframe width="560" height="315" src="https://www.youtube.com/embed/r30EP54bNsM?si=ag57GCl7XSDvyxRc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Paper Link](https://arxiv.org/abs/2205.14375)

Recommended citation: Jeevan, P., Viswanathan, K., AnanduA, S., & Sethi, A. (2022). WaveMix: A Resource-efficient Neural Network for Image Analysis.