---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<!-- {% include base_path %} -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Publications</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .line-clamp-2 {
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
    </style>
</head>
<body class="min-h-screen bg-white">
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <!-- Paper Carousel -->
        <div class="mb-8">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Recent Publications</h2>
            <div id="paper-carousel" class="overflow-hidden rounded-lg shadow-lg" style="height: 500px;">
                <div id="carousel-inner" class="flex" style="transform: translateX(0px); transition: transform 0.1s linear;">
                    <!-- Papers will be added dynamically -->
                </div>
            </div>
        </div>
        <!-- Filters -->
        <div class="bg-white rounded-lg shadow-sm border p-6 mb-8">
            <div class="flex flex-col lg:flex-row gap-4 items-start lg:items-center justify-between mb-6">
                <h2 class="text-xl font-semibold text-gray-900">Filter Publications</h2>
                <button id="reset-filters" class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                    Reset
                </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <!-- Search -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Search</label>
                    <input type="text" id="search-input" placeholder="Title, author, or venue..." class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                </div>
                <!-- Year Filter -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Year</label>
                    <select id="year-filter" class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                        <option value="All">All</option>
                        <!-- Options will be added dynamically -->
                    </select>
                </div>
                <!-- Results Count -->
                <div class="flex items-end">
                    <p id="results-count" class="text-sm text-gray-600">0 of 0 publications</p>
                </div>
            </div>
        </div>
        <!-- Publications List -->
        <div id="publications-list" class="space-y-8">
            <!-- Publications will be added dynamically -->
        </div>
    </main>
    <!-- Footer -->
    <footer class="bg-gray-50 border-t mt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="text-center text-gray-600">
                <p>© 2024 Pranav Singh. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script>
        const publications = [
            {
                id: 1,
                title: "Evaluation Metric for Quality Control and Generative Models in Histopathology Images",
                authors: "Pranav Singh, Faisal Mahmood",
                venue: "Proceedings of the 2025 IEEE International Symposium on Biomedical Imaging (ISBI), Huston TX, USA",
                year: 2025,
                description: "Our study introduces ResNet-L2 (RL2), a novel metric using ResNet features and a normalizing flow for evaluating generative models in histopathology, offering reliable assessments with fewer images and quicker assessments than traditional metrics, effectively handling diverse degradation types and diffusion processes.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/e3f2fd/1976d2?text=ISBI+2025"
            },
            {
                id: 2,
                title: "Self-Supervised Contrastive Learning for Digital Pathology",
                authors: "Faisal Mahmood, R. Chen, D. Hashmi",
                venue: "Nature Machine Intelligence, 2023",
                year: 2023,
                description: "We present a self-supervised contrastive learning framework for digital pathology that achieves state-of-the-art performance on multiple histopathology datasets without requiring labeled data, demonstrating the potential of contrastive learning in medical imaging applications.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/fff3e0/f57c00?text=Nature+MI"
            },
            {
                id: 3,
                title: "Weakly Supervised Instance Segmentation in Histopathology",
                authors: "Faisal Mahmood, N. Chaudhary, M. Ali",
                venue: "IEEE Transactions on Medical Imaging, 2022",
                year: 2022,
                description: "A novel weakly supervised approach for instance segmentation in histopathology images using only image-level labels, significantly reducing annotation burden while maintaining competitive performance compared to fully supervised methods.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/e8f5e8/388e3c?text=IEEE+TMI"
            },
            {
                id: 4,
                title: "Transformer-Based Models for Whole Slide Image Analysis",
                authors: "Faisal Mahmood, K. Zhang, L. Wang",
                venue: "Medical Image Analysis, 2022",
                year: 2022,
                description: "We propose a transformer-based architecture specifically designed for whole slide image analysis in digital pathology, leveraging self-attention mechanisms to capture long-range dependencies across gigapixel images.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/fff8e1/ffa000?text=MedIA"
            },
            {
                id: 5,
                title: "Generative Adversarial Networks for Medical Image Synthesis",
                authors: "Faisal Mahmood, J. Patel, S. Kumar",
                venue: "IEEE Journal of Biomedical and Health Informatics, 2021",
                year: 2021,
                description: "A comprehensive study on GAN architectures for medical image synthesis, with applications in data augmentation, domain adaptation, and anomaly detection in various medical imaging modalities.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/f3e5f5/7b1fa2?text=JBHI"
            },
            {
                id: 6,
                title: "Multi-Modal Fusion for Cancer Diagnosis",
                authors: "Faisal Mahmood, A. Thompson, B. Lee",
                venue: "International Journal of Computer Assisted Radiology and Surgery, 2021",
                year: 2021,
                description: "A deep learning framework for multi-modal fusion of histopathology and radiology images for improved cancer diagnosis, demonstrating the complementary nature of different imaging modalities in clinical decision support.",
                pdf: "#",
                code: "#",
                slides: "#",
                image: "https://placehold.co/400x500/e0f7fa/0097a7?text=IJCARS"
            }
        ];
        // DOM elements
        const carouselInner = document.getElementById('carousel-inner');
        const yearFilter = document.getElementById('year-filter');
        const searchInput = document.getElementById('search-input');
        const resultsCount = document.getElementById('results-count');
        const publicationsList = document.getElementById('publications-list');
        const resetFilters = document.getElementById('reset-filters');
        // Initialize years filter
        const years = [...new Set(publications.map(p => p.year).sort((a, b) => b - a))];
        years.forEach(year => {
            const option = document.createElement('option');
            option.value = year;
            option.textContent = year;
            yearFilter.appendChild(option);
        });
        // Create carousel items
        function createCarouselItems() {
            const doubledPublications = [...publications, ...publications];
            carouselInner.innerHTML = '';
            doubledPublications.forEach(pub => {
                const item = document.createElement('div');
                item.className = 'flex-shrink-0 w-96 mx-2';
                item.style.width = '400px';
                item.innerHTML = `
                    <div class="bg-white rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300 h-full">
                        <img src="${pub.image}" alt="${pub.title}" class="w-full h-64 object-cover">
                        <div class="p-4">
                            <h3 class="font-semibold text-gray-900 text-sm line-clamp-2 mb-2">${pub.title}</h3>
                            <p class="text-gray-600 text-xs mb-1">${pub.authors}</p>
                            <p class="text-gray-500 text-xs">${pub.venue}</p>
                        </div>
                    </div>
                `;
                carouselInner.appendChild(item);
            });
        }
        // Filter publications
        function filterPublications() {
            const selectedYear = yearFilter.value;
            const searchTerm = searchInput.value.toLowerCase();
            const filtered = publications.filter(pub => {
                const yearMatch = selectedYear === 'All' || pub.year.toString() === selectedYear;
                const searchMatch = pub.title.toLowerCase().includes(searchTerm) || 
                                    pub.authors.toLowerCase().includes(searchTerm) ||
                                    pub.venue.toLowerCase().includes(searchTerm);
                return yearMatch && searchMatch;
            });
            // Update results count
            resultsCount.textContent = `${filtered.length} of ${publications.length} publications`;
            // Update publications list
            renderPublicationsList(filtered);
            return filtered;
        }
        // Render publications list
        function renderPublicationsList(publicationsToRender) {
            publicationsList.innerHTML = '';
            if (publicationsToRender.length === 0) {
                const emptyMessage = document.createElement('div');
                emptyMessage.className = 'text-center py-12';
                emptyMessage.innerHTML = '<p class="text-gray-500 text-lg">No publications found matching your criteria.</p>';
                publicationsList.appendChild(emptyMessage);
                return;
            }
            publicationsToRender.forEach(pub => {
                const pubElement = document.createElement('div');
                pubElement.className = 'bg-white rounded-lg shadow-sm border p-6 hover:shadow-md transition-shadow';
                pubElement.innerHTML = `
                    <div class="flex flex-col lg:flex-row gap-6">
                        <!-- Paper Image -->
                        <div class="lg:w-1/4 flex-shrink-0">
                            <img src="${pub.image}" alt="${pub.title}" class="w-full h-64 object-cover rounded-lg">
                        </div>
                        <!-- Content -->
                        <div class="lg:w-3/4">
                            <h3 class="text-xl font-semibold text-gray-900 mb-3 leading-tight">${pub.title}</h3>                          
                            <div class="space-y-3">
                                <div>
                                    <span class="text-gray-700 font-medium">Authors: </span>
                                    <span class="text-gray-600">${pub.authors}</span>
                                </div>    
                                <div>
                                    <span class="text-gray-700 font-medium">Published in: </span>
                                    <span class="text-gray-600 italic">${pub.venue}</span>
                                </div>
                                <div class="prose prose-gray max-w-none">
                                    <p class="text-gray-700 leading-relaxed">${pub.description}</p>
                                </div>
                                <!-- Links -->
                                <div class="flex flex-wrap gap-3 pt-2">
                                    <a href="${pub.pdf}" class="inline-flex items-center px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-md hover:bg-blue-700 transition-colors">PDF</a>
                                    <a href="${pub.code}" class="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 text-sm font-medium rounded-md hover:bg-gray-50 transition-colors">Code</a>
                                    <a href="${pub.slides}" class="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 text-sm font-medium rounded-md hover:bg-gray-50 transition-colors">Slides</a>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                publicationsList.appendChild(pubElement);
            });
        }
        // Auto-scroll effect for paper covers
        let scrollPosition = 0;
        function startCarousel() {
            setInterval(() => {
                const container = document.getElementById('paper-carousel');
                const inner = document.getElementById('carousel-inner');
                if (!container || !inner) return;
                scrollPosition += 1;
                const maxScroll = inner.scrollWidth - container.clientWidth;
                if (scrollPosition >= maxScroll) {
                    scrollPosition = 0;
                }
                inner.style.transform = `translateX(-${scrollPosition}px)`;
            }, 50);
        }
        // Event listeners
        yearFilter.addEventListener('change', filterPublications);
        searchInput.addEventListener('input', filterPublications);
        resetFilters.addEventListener('click', () => {
            yearFilter.value = 'All';
            searchInput.value = '';
            filterPublications();
        });
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            createCarouselItems();
            filterPublications();
            startCarousel();
        });
    </script>
</body>
</html>
