---
title: "Convolutional Xformers for Vision"
collection: publications
permalink: /publication/cxv
excerpt: 'CXV is a new convolutional transformer hybrid architecture that outperforms other architectures in image classification, especially in scenarios with limited data and GPU resources.'
date: 2026-07-10
venue: 'GlobalSouthML Workshop at International Conference on Machine Learning (ICML) 2026, Seoul, South Korea'
image: 'cxv.jpg'
width: '800'
carousel:
  acronym: "CXV"
  tagline: "CNN-Transformer Hybrid"
  image: "papers/cxv.jpg"
  tags:
    - "Hybrid Architecture"
    - "Vision"
---
Vision transformers (ViTs) have found only limited practical use in processing images, in spite of their state-of-the-art accuracy on certain benchmarks. The reason for their limited use include their need for larger training datasets and more computational resources compared to convolutional neural networks (CNNs), owing to the quadratic complexity of their self-attention mechanism. We propose a linear attention-convolution hybrid architecture -- Convolutional X-formers for Vision (CXV) -- to overcome these limitations. We replace the quadratic attention with linear attention mechanisms, such as Performer, Nyströmformer, and Linear Transformer, to reduce its GPU usage. Inductive prior for image data is provided by convolutional sub-layers, thereby eliminating the need for class token and positional embeddings used by the ViTs. We also propose a new training method where we use two different optimizers during different phases of training and show that it improves the top-1 image classification accuracy across different architectures. CXV outperforms other architectures, token mixers (e.g. ConvMixer, FNet and MLP Mixer), transformer models (e.g. ViT, CCT, CvT and hybrid Xformers), and ResNets for image classification in scenarios with limited data and GPU resources (cores, RAM, power).

<iframe width="560" height="315" src="https://www.youtube.com/embed/-qBu8HDUQkM?si=h6tpdlPBDjUjD_kh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Paper Link](https://arxiv.org/abs/2201.10271)

Recommended citation: Jeevan, P., & Sethi, A. (2022). Convolutional Xformers for Vision. ArXiv, abs/2201.10271.