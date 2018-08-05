---
layout: home
---

<!-- Hero Slider -->
<div id="hero-carousel" class="carousel slide" data-ride="carousel" data-pause="false" data-interval="7000">
    <div class="carousel-inner">
    {% for image in site.data.front-page-slider.images %}
    <div class="carousel-item {% if forloop.index == 1 %} active {% endif %}">
        <div class="hero lazyload" data-bg="{{ site.url }}{{ site.baseurl }}/assets/img/slider/{{ image.file }}.jpg" {% if image.align %}style="background-position: {{ image.align }};"{% endif %}> 
        </div>
    </div>
    {% endfor %}
    <div class="hero__wrap">
        <h1 class="hero__title">{{ site.title | escape }}</h1>
        <p class="hero__meta">{{ site.tagline }}</p>
    </div>
    </div>
</div>

<!-- Main content   -->
<main class="site__content">
    <section class="blog">
    </section>
</main>