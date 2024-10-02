---
title: "WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency"
collection: publications
permalink: /publication/wavemixsrv2
excerpt: 'WaveMixSR is a new neural network for image super-resolution that uses the WaveMix architecture, which is based on a 2D-discrete wavelet transform for spatial token-mixing, and achieves higher performance while requiring fewer resources and training data than transformer-based models.'
date: 2024-09-16
venue: 'arxiv'
image: 'wavemixsr.jpg'
width: '800'
---
Recent advancements in single image super-resolution have been predominantly driven by token mixers and transformer architectures. WaveMixSR utilized the WaveMix architecture, employing a two-dimensional discrete wavelet transform for spatial token mixing, achieving superior performance in super-resolution tasks with remarkable resource efficiency. In this work, we present an enhanced version of the WaveMixSR architecture by (1) replacing the traditional transpose convolution layer with a pixel shuffle operation and (2) implementing a multistage design for higher resolution tasks (4×). Our experiments demonstrate that our enhanced model -- WaveMixSR-V2 -- outperforms other architectures in multiple super-resolution tasks, achieving state-of-the-art for the BSD100 dataset, while also consuming fewer resources, exhibits higher parameter efficiency, lower latency and higher throughput. 


[Paper Link](https://arxiv.org/abs/2409.10582)

Recommended citation: Jeevan, P., Nixon, N., & Sethi, A. (2024). WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency.