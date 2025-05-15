---
title: "Evaluation Metric for Quality Control and Generative Models in Histopathology Images"
collection: publications
permalink: /publication/rl2
excerpt: 'Our study introduces ResNet-L2 (RL2), a novel metric using ResNet features and a normalizing flow for evaluating generative models in histopathology, offering reliable assessments with fewer images and quicker assessments than traditional metrics, effectively handling diverse degradation types and diffusion processes.'
date: 2025-04-14
venue: 'Proceedings of the 2025 IEEE International Symposium on Biomedical Imaging (ISBI), Huston TX, USA'
image: 'wavepaint.jpg'
width: '800'
---

Our study introduces ResNet-L2 (RL2), a novel metric for evaluating generative models and image quality in histopathology, addressing limitations of traditional metrics, such as Frechet inception distance (FID), when the data is scarce. RL2 leverages ResNet features with a normalizing flow to calculate RMSE distance in the latent space, providing reliable assessments across diverse histopathology datasets. We evaluated the performance of RL2 on degradation types, such as blur, Gaussian noise, salt-and-pepper noise, and rectangular patches, as well as diffusion processes. RL2's monotonic response to increasing degradation makes it well-suited for models that assess image quality, proving a valuable advancement for evaluating image generation techniques in histopathology. It can also be used to discard low-quality patches while sampling from a whole slide image. It is also significantly lighter and faster compared to traditional metrics and requires fewer images to give stable metric value.

[Paper Link](https://ieeexplore.ieee.org/document/10981064)

Recommended  Citation: P. Jeevan, N. Nixon, A. Patil and A. Sethi, "Evaluation Metric for Quality Control and Generative Models in Histopathology Images," 2025 IEEE 22nd International Symposium on Biomedical Imaging (ISBI), Houston, TX, USA, 2025, pp. 1-4, doi: 10.1109/ISBI60581.2025.10981064. 

