---
title: "Resource-Efficient Hybrid X-Formers for Vision"
collection: publications
permalink: /publication/vixwacv22
excerpt: 'We developed a resource-efficient architecture for vision by making three modifications on ViT to address their shortcomings, which significantly improved their performance and made them more accessible.'
date: 2022-01-04
venue: 'Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA'
image: 'vix.jpg'
width: '800'
---
Although transformers have become the neural architectures of choice for natural language processing, they require orders of magnitude more training data, GPU memory, and computations in order to compete with convolutional neural networks for computer vision. The attention mechanism of transformers scales quadratically with the length of the input sequence, and unrolled images have long sequence lengths. Plus, transformers lack an inductive bias that is appropriate for images. We tested three modifications to vision transformer (ViT) architectures that address these shortcomings. Firstly, we alleviate the quadratic bottleneck by using linear attention mechanisms, called X-formers (such that, X in Performer, Linformer, Nystromformer ), thereby creating Vision X-formers (ViXs). This resulted in up to a seven times reduction in the GPU memory requirement. We also compared their performance with FNet and multi-layer perceptron mixers, which further reduced the GPU memory requirement. Secondly, we introduced an inductive prior for images by replacing the initial linear embedding layer by convolutional layers in ViX, which significantly increased classification accuracy without increasing the model size. Thirdly, we replaced the learnable 1D position embeddings in ViT with Rotary Position Embedding (RoPE), which increases the classification accuracy for the same model size. We believe that incorporating such changes can democratize transformers by making them accessible to those with limited data and computing resources.

<iframe width="560" height="315" src="https://www.youtube.com/embed/J8ooadqugZU?si=GKNBkYaHTnSLE4VA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[Paper Link](https://openaccess.thecvf.com/content/WACV2022/papers/Jeevan_Resource-Efficient_Hybrid_X-Formers_for_Vision_WACV_2022_paper.pdf)

Recommended citation: P. Jeevan and A. Sethi, "Resource-efficient Hybrid X-formers for Vision," 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA, 2022, pp. 3555-3563, doi: 10.1109/WACV51458.2022.00361.