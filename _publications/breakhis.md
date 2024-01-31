---
title: "Magnification Invariant Medical Image Analysis: A Comparison of Convolutional Networks, Vision Transformers, and Token Mixers"
collection: publications
permalink: /publication/breakhis
excerpt: 'This study evaluates the robustness of different deep learning architectures for breast cancer histopathological image classification across magnification scales.'
date: 2024-02-21
venue: 'Proceedings of the 17th International Joint Conference on Biomedical Engineering Systems and Technologies 2024, Rome, Italy'

---
Convolution Neural Networks (CNNs) are widely used in medical image analysis, but their performance degrade when the magnification of testing images differ from the training images. The inability of CNNs to generalize across magnification scales can result in sub-optimal performance on external datasets. This study aims to evaluate the robustness of various deep learning architectures in the analysis of breast cancer histopathological images with varying magnification scales at training and testing stages. Here we explore and compare the performance of multiple deep learning architectures, including CNN-based ResNet and MobileNet, self-attention-based Vision Transformers and Swin Transformers, and token-mixing models, such as FNet, ConvMixer, MLP-Mixer, and WaveMix. The experiments are conducted using the BreakHis dataset, which contains breast cancer histopathological images at varying magnification levels. We show that performance of WaveMix is invariant to the magnification of training and testing data and can provide stable and good classification accuracy. These evaluations are critical in identifying deep learning architectures that can robustly handle changes in magnification scale, ensuring that scale changes across anatomical structures do not disturb the inference results.

[Paper Link](https://arxiv.org/abs/2302.11488)

Recommended citation: Jeevan, P.; Kurian, N. and Sethi, A. (2024). Magnification Invariant Medical Image Analysis: A Comparison of Convolutional Networks, Vision Transformers, and Token Mixers.  In Proceedings of the 17th International Joint Conference on Biomedical Engineering Systems and Technologies - Volume 1, ISBN 978-989-758-688-0, ISSN 2184-4305, pages 218-224. 