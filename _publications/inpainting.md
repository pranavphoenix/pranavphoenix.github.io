---
title: "Resource-efficient Image Inpainting"
collection: publications
permalink: /publication/inpainting
excerpt: 'The paper proposes a computationally-efficient WaveMix-based fully convolutional architecture for image inpainting that outperforms the current state-of-the-art models while using less parameters and lower training and evaluation times.'
date: 2023-05-05
venue: ' Tiny Papers @ ICLR 2023'

---
Image inpainting refers to the synthesis of missing regions in an image, which can help restore occluded or degraded areas and also serve as a precursor task forself-supervision. The current state-of-the-art models for image inpainting are computationally heavy as they are based on vision transformer backbones in adversarial or diffusion settings. This paper diverges from vision transformers by using a computationally-efficient WaveMix-based fully convolutional architecture, which uses a 2D-discrete wavelet transform (DWT)for spatial and multi-resolution token-mixing along with convolutional layers. The proposed model outperforms the current state-of-the-art models for large mask inpainting on reconstruction quality while also using less than half the parameter count and considerably lower training and evaluation times.

[Paper Link](https://dblp.org/rec/conf/iclr/KumarJS23.html)

Recommended citation: Kumar, D.S., Jeevan, P., & Sethi, A. (2023). Resource-efficient image inpainting. Tiny Papers @ ICLR.