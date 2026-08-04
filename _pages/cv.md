---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
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

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Resume download -->
    <div class="mb-8 flex justify-center">
        <a href="https://drive.google.com/file/d/1-BkKK9OD12Yq5J6TGXAQr53f1jmGQXwN/view?usp=sharing" target="_blank" class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-8 py-3 rounded-lg font-medium hover:from-blue-600 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl inline-flex items-center" style="text-decoration: none;">
            <i class="fas fa-file-pdf mr-2"></i>
            My Resume
        </a>
    </div>

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
                <input type="text" id="search-input" placeholder="Title or venue..." class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
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
</div>

<script>
    const publications = [
        {% assign pubs = site.publications | sort: 'date' | reverse %}
        {% for post in pubs %}
        {
            title: {{ post.title | jsonify }},
            venue: {{ post.venue | jsonify }},
            year: {{ post.date | date: "%Y" }},
            description: {{ post.excerpt | jsonify }},
            url: {{ post.url | jsonify }},
            acronym: {{ post.carousel.acronym | jsonify }},
            tagline: {{ post.carousel.tagline | jsonify }},
            gradient: {{ post.carousel.gradient | default: "" | jsonify }},
            image: {{ post.carousel.image | default: "" | jsonify }}
        }{% unless forloop.last %},{% endunless %}
        {% endfor %}
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

    // Cover image or gradient placeholder
    function coverHTML(pub) {
        if (pub.image) {
            return `<div class="w-full overflow-hidden" style="aspect-ratio: 8.5 / 11;">
                        <img src="/images/${pub.image}" alt="${pub.title}" class="w-full h-full object-cover object-top" loading="lazy">
                    </div>`;
        }
        return `<div class="w-full h-56 bg-gradient-to-br ${pub.gradient} flex items-center justify-center">
                    <span class="text-white text-center px-4"><strong>${pub.acronym}</strong><br/>${pub.tagline}</span>
                </div>`;
    }

    // Create carousel items
    function createCarouselItems() {
        const carouselPublications = publications.filter(pub => pub.image);
        const doubledPublications = [...carouselPublications, ...carouselPublications];
        carouselInner.innerHTML = '';
        doubledPublications.forEach(pub => {
            const item = document.createElement('div');
            item.className = 'flex-shrink-0 w-96 mx-2';
            item.style.width = '400px';
            item.innerHTML = `
                <a href="${pub.url}" class="block bg-white rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300 h-full no-underline">
                    ${coverHTML(pub)}
                    <div class="p-4">
                        <h3 class="font-semibold text-gray-900 text-sm line-clamp-2 mb-2">${pub.title}</h3>
                        <p class="text-gray-600 text-xs mb-1">${pub.year}</p>
                        <p class="text-gray-500 text-xs">${pub.venue}</p>
                    </div>
                </a>
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
            const searchMatch = (pub.title || '').toLowerCase().includes(searchTerm) ||
                                (pub.venue || '').toLowerCase().includes(searchTerm);
            return yearMatch && searchMatch;
        });
        resultsCount.textContent = `${filtered.length} of ${publications.length} publications`;
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
                    <div class="lg:w-1/4 flex-shrink-0">
                        <div class="w-full h-64 rounded-lg overflow-hidden">${coverHTML(pub)}</div>
                    </div>
                    <div class="lg:w-3/4">
                        <h3 class="text-xl font-semibold text-gray-900 mb-3 leading-tight">${pub.title}</h3>
                        <div class="space-y-3">
                            <div>
                                <span class="text-gray-700 font-medium">Published in: </span>
                                <span class="text-gray-600 italic">${pub.venue}</span>
                            </div>
                            <div>
                                <span class="text-gray-700 font-medium">Year: </span>
                                <span class="text-gray-600">${pub.year}</span>
                            </div>
                            <div class="prose prose-gray max-w-none">
                                <p class="text-gray-700 leading-relaxed">${pub.description}</p>
                            </div>
                            <div class="flex flex-wrap gap-3 pt-2">
                                <a href="${pub.url}" class="inline-flex items-center px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-md hover:bg-blue-700 transition-colors">Details</a>
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
