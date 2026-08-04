---
title: "Survival Modeling from Whole Slide Images via Patch-Level Graph Clustering and Mixture Density Experts"
collection: publications
permalink: /publication/graphclust
excerpt: 'A modular framework for cancer-specific survival prediction from whole-slide images, combining quantile-based patch filtering, graph-regularized patch clustering, hierarchical feature aggregation, and expert-guided mixture density modeling.'
date: 2026-04-08
venue: 'Proceedings of the 2026 IEEE 23rd International Symposium on Biomedical Imaging (ISBI), London, UK'
carousel:
  acronym: "GraphClust"
  tagline: "Survival Analysis"
  image: "papers/graphclust.jpg"
  tags:
    - "Histopathology"
    - "Survival Analysis"
---

We present a modular framework for predicting cancer-specific survival from whole-slide pathology images (WSIs). The approach integrates four main components: (i) Quantile-Based Patch Filtering, which employs quantile-based thresholding to identify prognostically informative tissue regions; (ii) Graph Regularized Patch Clustering using k-NN graph to model phenotype-level heterogeneity through spatial-morphological coherence; (iii) Hierarchical Feature Aggregation for learning intra- and inter-cluster dependencies; and (iv) an Expert-Guided Mixture Density Modeling module to estimate complex survival distributions using Gaussian distributions. The proposed model achieves a concordance index of 0.653 ± 0.037 on TCGA-LUAD, 0.719 ± 0.011 on TCGA-KIRC, and 0.733 ± 0.037 on TCGA-BRCA, surpassing current state-of-the-art methods.

[Paper Link](https://arxiv.org/abs/2507.16476)

Recommended citation: A. Sekhar, V. Soni, K. Aske, G. Jain, P. Jeevan and A. Sethi, "Survival Modeling from Whole Slide Images via Patch-Level Graph Clustering and Mixture Density Experts," 2026 IEEE 23rd International Symposium on Biomedical Imaging (ISBI), London, UK, 2026. Preprint: arXiv:2507.16476.
