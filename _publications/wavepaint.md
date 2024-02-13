---
title: "WavePaint: Resource-efficient Token-mixer for Self-supervised Inpainting"
collection: publications
permalink: /publication/wavepaint
excerpt: 'WavePaint is a new resource-efficient neural architecture for image inpainting that achieves comparable or better performance than the current state-of-the-art models without using adversarial training or diffusion.'
date: 2023-07-01
venue: 'Arxiv'
image: 'wavepaint.jpg'
width: '800'
---

![Architecture](https://private-user-images.githubusercontent.com/15833382/251272215-5f414f26-44f7-4a90-83d8-a35500e21f20.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc3ODM4NTcsIm5iZiI6MTcwNzc4MzU1NywicGF0aCI6Ii8xNTgzMzM4Mi8yNTEyNzIyMTUtNWY0MTRmMjYtNDRmNy00YTkwLTgzZDgtYTM1NTAwZTIxZjIwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjEzVDAwMTkxN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBjMWQ1MGQzMDYxZWU5OTJlNmVlOTY5YmI0MzIwZGFmZjgyNmM4Zjg4YzM3NTQ2M2JkODFhYjQxZDFjZTU5MjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.SQEwruYWE26b5zfi-IP4uKvqICITq9nMl2E3UhWUjJ0)

Image inpainting, which refers to the synthesis of missing regions in an image, can help restore occluded or degraded areas and also serve as a precursor task for self-supervision. The current state-of-the-art models for image inpainting are computationally heavy as they are based on transformer or CNN backbones that are trained in adversarial or diffusion settings. This paper diverges from vision transformers by using a computationally-efficient WaveMix-based fully convolutional architecture -- WavePaint. It uses a 2D-discrete wavelet transform (DWT) for spatial and multi-resolution token-mixing along with convolutional layers. The proposed model outperforms the current state-of-the-art models for image inpainting on reconstruction quality while also using less than half the parameter count and considerably lower training and evaluation times. Our model even outperforms current GAN-based architectures in CelebA-HQ dataset without using an adversarially trainable discriminator. Our work suggests that neural architectures that are modeled after natural image priors require fewer parameters and computations to achieve generalization comparable to transformers.

[Paper Link](https://arxiv.org/abs/2307.00407v1)

Recommended citation: Jeevan, P., Kumar, D.S., & Sethi, A. (2023). WavePaint: Resource-efficient Token-mixer for Self-supervised Inpainting.