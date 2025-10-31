---
title: "WavePaint: Resource-efficient Token-mixer for Self-supervised Inpainting"
collection: publications
permalink: /publication/wavepaint
excerpt: 'WavePaint is a new resource-efficient neural architecture for image inpainting that achieves comparable or better performance than the current state-of-the-art models without using adversarial training or diffusion.'
date: 2025-10-19
venue: 'Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops 2025'
image: 'wavepaint.jpg'
width: '800'
---

Image inpainting, which refers to the synthesis of missing regions in an image, can help restore occluded or degraded areas and also serve as a precursor task for self-supervision. The current state-of-the-art models for image inpainting are computationally heavy as they are based on transformer or CNN backbones that are trained in adversarial or diffusion settings. This paper diverges from vision transformers by using a computationally-efficient WaveMix-based fully convolutional architecture -- WavePaint. It uses a 2D-discrete wavelet transform (DWT) for spatial and multi-resolution token-mixing along with convolutional layers. The proposed model outperforms the current state-of-the-art models for image inpainting on reconstruction quality while also using less than half the parameter count and considerably lower training and evaluation times. Our model even outperforms current GAN-based architectures in CelebA-HQ dataset without using an adversarially trainable discriminator. Our work suggests that neural architectures that are modeled after natural image priors require fewer parameters and computations to achieve generalization comparable to transformers.

[Paper Link](https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Jeevan_WavePaint_Resource-efficient_Token-mixer_for_Self-supervised_Inpainting_ICCVW_2025_paper.html)

Recommended citation: Pranav Jeevan, Dharshan Sampath Kumar, Amit Sethi; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops, 2025, pp. 1639-1648