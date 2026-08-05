---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<style>
  .pubs-carousel-wrap {
    margin: 0 0 2.5rem 0;
  }
  .pubs-carousel-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #111827;
    text-align: center;
    margin-bottom: 0.75rem;
  }
  .pubs-carousel-sub {
    text-align: center;
    color: #4b5563;
    max-width: 48rem;
    margin: 0 auto 1.5rem;
  }
  .pubs-carousel-viewport {
    overflow: hidden;
    position: relative;
    padding: 2rem 0;
  }
  .paper-carousel {
    display: flex;
    width: max-content;
    animation: scrollPapers 60s linear infinite;
  }
  @keyframes scrollPapers {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
  }
  .paper-card {
    flex-shrink: 0;
    width: min(320px, 78vw);
    margin: 0 16px;
    background: #fff;
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    transition: all 0.3s ease;
    opacity: 0.9;
    text-decoration: none;
    color: inherit;
    display: block;
  }
  .paper-card:hover {
    transform: scale(1.05);
    opacity: 1;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  }
  .paper-card-img {
    width: 100%;
    overflow: hidden;
    aspect-ratio: 8.5 / 11;
  }
  .paper-card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    display: block;
  }
  .paper-card-body {
    padding: 1rem;
  }
  .paper-card-title {
    font-weight: 700;
    color: #111827;
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .paper-card-venue {
    color: #dc2626;
    font-weight: 600;
    font-size: 0.75rem;
    margin: 0.75rem 0 0 0;
  }
  .paper-card-year {
    font-size: 0.75rem;
    color: #6b7280;
    margin-bottom: 0.75rem;
  }
  .paper-card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
  }
  .tag {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 0.25rem;
    background: #f3e8ff;
    color: #7e22ce;
    transition: all 0.2s;
  }
  .tag:hover {
    transform: scale(1.1);
  }
  html[data-theme="dark"] .pubs-carousel-title {
    color: #f1f5f9;
  }
  html[data-theme="dark"] .pubs-carousel-sub {
    color: #94a3b8;
  }
  html[data-theme="dark"] .paper-card {
    background-color: #1e293b;
  }
  html[data-theme="dark"] .paper-card:hover {
    background-color: #334155;
  }
  html[data-theme="dark"] .paper-card-title {
    color: #f1f5f9;
  }
  html[data-theme="dark"] .paper-card-venue {
    color: #f87171;
  }
  html[data-theme="dark"] .paper-card-year {
    color: #94a3b8;
  }
  html[data-theme="dark"] .tag {
    background-color: rgba(139, 92, 246, 0.15);
    color: #c4b5fd;
  }
</style>

<div class="pubs-carousel-wrap">
  <h3 class="pubs-carousel-title">Recent Publications</h3>
  <p class="pubs-carousel-sub">Scroll through my recent research publications. Click on any paper to learn more.</p>
  <div class="pubs-carousel-viewport">
    <div class="paper-carousel">
      {% assign pubs = site.publications | sort: 'date' | reverse %}
      {% for i in (0..1) %}
        {% for post in pubs %}
          {% if post.carousel.image %}
          <a href="{{ post.url }}" class="paper-card">
            <div class="paper-card-img">
              <img src="/images/{{ post.carousel.image }}" alt="{{ post.title }}" loading="lazy" />
            </div>
            <div class="paper-card-body">
              <h5 class="paper-card-title">{{ post.title }}</h5>
              <p class="paper-card-year">{{ post.date | date: "%Y" }}</p>
              <div class="paper-card-tags">
                {% for tag in post.carousel.tags %}
                <span class="tag">{{ tag }}</span>
                {% endfor %}
              </div>
              {% if post.carousel.venue %}<p class="paper-card-venue">{{ post.carousel.venue }}</p>{% endif %}
            </div>
          </a>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </div>
  </div>
</div>

<script>
  /* Pause carousel on hover */
  document.addEventListener('DOMContentLoaded', function () {
    var carousel = document.querySelector('.paper-carousel');
    if (carousel) {
      carousel.addEventListener('mouseenter', function () {
        carousel.style.animationPlayState = 'paused';
      });
      carousel.addEventListener('mouseleave', function () {
        carousel.style.animationPlayState = 'running';
      });
      carousel.addEventListener('touchstart', function () {
        carousel.style.animationPlayState = 'paused';
      });
      carousel.addEventListener('touchend', function () {
        carousel.style.animationPlayState = 'running';
      });
    }
  });
</script>

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
