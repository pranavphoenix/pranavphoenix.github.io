---
title: "FLD+: Data-efficient Evaluation Metric for Generative Models"
collection: publications
permalink: /publication/fld
excerpt: 'FLD+ is a new, more efficient and reliable image quality metric using normalizing flows that outperforms FID, especially with fewer images and on specialized domains.**'
date: 2025-10-19
venue: 'Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops 2025, Honolulu, Hawaii, US'
image: 'wavepaint.jpg'
width: '800'
---

We introduce a new metric to assess the quality of generated images that is more reliable, data-efficient, compute-efficient, and adaptable to new domains than the previous metrics, such as Frechet Inception Distance (FID). The proposed metric is based on normalizing flows, which allows for the computation of density (exact log-likelihood) of images from any domain. Thus, unlike FID, the proposed Flow-based Likelihood Distance Plus (FLD+) metric exhibits strongly monotonic behavior with respect to different types of image degradations, including noise, occlusion, diffusion steps, and generative model size. Additionally, because normalizing flow can be trained stably and efficiently, FLD+ achieves stable results with two orders of magnitude fewer images than FID (which requires more images to reliably compute Frechet distance between features of large samples of real and generated images). We made FLD+ computationally even more efficient by applying normalizing flows to features extracted in a lower-dimensional latent space instead of using a pre-trained network. We also show that FLD+ can easily be retrained on new domains, such as medical images, unlike the networks behind previous metrics -- such as InceptionNetV3 pre-trained on ImageNet.

[Paper Link](https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Jeevan_FLD_Data-efficient_Evaluation_Metric_for_Generative_Models_ICCVW_2025_paper.html)

Recommended Citation: Pranav Jeevan, Neeraj Nixon, Amit Sethi; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops, 2025, pp. 1649-1657
