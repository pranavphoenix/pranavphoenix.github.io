---
title: "WaveMixSR: A Resource-efficient Neural Network for Image Super-resolution"
collection: publications
permalink: /publication/wavemixsr
excerpt: 'WaveMixSR is a new neural network for image super-resolution that uses the WaveMix architecture, which is based on a 2D-discrete wavelet transform for spatial token-mixing, and achieves higher performance while requiring fewer resources and training data than transformer-based models.'
date: 2024-04-01
venue: 'Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikaloa, HI, USA'
image: 'wavemixsr.jpg'
width: '800'
---
Image super-resolution research recently been dominated by transformer models which need higher computational resources than CNNs due to the quadratic complexity of self-attention. We propose a new neural network -- WaveMixSR -- for image super-resolution based on WaveMix architecture which uses a 2D-discrete wavelet transform for spatial token-mixing. Unlike transformer-based models, WaveMixSR does not unroll the image as a sequence of pixels/patches. It uses the inductive bias of convolutions along with the lossless token-mixing property of wavelet transform to achieve higher performance while requiring fewer resources and training data. We compare the performance of our network with other state-of-the-art methods for image super-resolution. Our experiments show that WaveMixSR achieves competitive performance in all datasets and reaches state-of-the-art performance in the BSD100 dataset on multiple super-resolution tasks. Our model is able to achieve this performance using less training data and computational resources while maintaining high parameter efficiency compared to current state-of-the-art models.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YVb0lp2fSeY?si=xz0Y5RoQyMcUDLHA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[Paper Link](https://openaccess.thecvf.com/content/WACV2024/html/Jeevan_WaveMixSR_Resource-Efficient_Neural_Network_for_Image_Super-Resolution_WACV_2024_paper.html)

Recommended citation: Jeevan, P., Srinidhi, A., Prathiba, P., & Sethi, A.; Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2024, pp. 5884-5892