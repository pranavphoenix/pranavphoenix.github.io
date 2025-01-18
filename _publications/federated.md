---
title: "FLeNS: Federated Learning with Enhanced Nesterov-Newton Sketch"
collection: publications
permalink: /publication/federated
excerpt: 'FLeNS combines Nesterov acceleration with adaptive Hessian sketching to achieve super-linear convergence in federated learning while significantly reducing communication overhead.'
date: 2024-12-15
venue: 'Proceedings of the 2024 IEEE International Conference on Big Data (IEEE BigData), Washington, DC, USA'
image: 'wavepaint.jpg'
width: '800'
---

Federated learning faces a critical challenge in balancing communication efficiency with rapid convergence, especially for second-order methods. While Newton-type algorithms achieve linear convergence in communication rounds, transmitting full Hessian matrices is often impractical due to quadratic complexity. We introduce Federated Learning with Enhanced Nesterov-Newton Sketch (FLeNS), a novel method that harnesses both the acceleration capabilities of Nesterov's method and the dimensionality reduction benefits of Hessian sketching. FLeNS approximates the centralized Newton's method without relying on the exact Hessian, significantly reducing communication overhead. By combining Nesterov's acceleration with adaptive Hessian sketching, FLeNS preserves crucial second-order information while preserving the rapid convergence characteristics. Our theoretical analysis, grounded in statistical learning, demonstrates that FLeNS achieves super-linear convergence rates in communication rounds - a notable advancement in federated optimization. We provide rigorous convergence guarantees and characterize tradeoffs between acceleration, sketch size, and convergence speed. Extensive empirical evaluation validates our theoretical findings, showcasing FLeNS's state-of-the-art performance with reduced communication requirements, particularly in privacy-sensitive and edge-computing scenarios. 

[Paper Link](https://ieeexplore.ieee.org/abstract/document/10825820)

Recommended citation: S. Gupta, M. Jindal, P. Kashyap, P. Jeevan and A. Sethi, "FLeNS: Federated Learning with Enhanced Nesterov-Newton Sketch," 2024 IEEE International Conference on Big Data (BigData), Washington, DC, USA, 2024, pp. 7774-7783, doi: 10.1109/BigData62323.2024.10825820.