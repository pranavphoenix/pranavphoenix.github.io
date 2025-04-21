---
title: "WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency"
collection: publications
permalink: /publication/wavemixsrv2
excerpt: 'WaveMixSR-V2, an enhanced version of WaveMixSR, incorporating pixel shuffle and a multistage design, achieving state-of-the-art super-resolution performance on the BSD100 dataset with improved resource efficiency, lower latency, and higher throughput.'
date: 2025-02-25
venue: 'Proceedings of the 2025 AAAI Conference on Artificial Intelligence (AAAI-25), Philadelphia, PA, USA'

---
Recent advancements in single image super-resolution have been predominantly driven by token mixers and transformer architectures. WaveMixSR utilized the WaveMix architecture, employing a two-dimensional discrete wavelet transform for spatial token mixing, achieving superior performance in super-resolution tasks with remarkable resource efficiency. In this work, we present an enhanced version of the WaveMixSR architecture by (1) replacing the traditional transpose convolution layer with a pixel shuffle operation and (2) implementing a multistage design for higher resolution tasks (4×). Our experiments demonstrate that our enhanced model -- WaveMixSR-V2 -- outperforms other architectures in multiple super-resolution tasks, achieving state-of-the-art for the BSD100 dataset, while also consuming fewer resources, exhibits higher parameter efficiency, lower latency and higher throughput. 

Accepted as Oral Presentation.

<iframe width="560" height="315" src="https://www.youtube.com/embed/w4wmDxZVPR4?si=JtVBAqkFIc_dMvjB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Paper Link](https://ojs.aaai.org/index.php/AAAI/article/view/35262)

Recommended citation: Jeevan, P., Nixon, N., & Sethi, A. (2025). WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency (Student Abstract). Proceedings of the AAAI Conference on Artificial Intelligence, 39(28), 29390-29392. https://doi.org/10.1609/aaai.v39i28.35262