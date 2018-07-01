---
#
# You don't need to edit this file, it's empty on purpose.
# Edit sleeks's default layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: default
title: Sleek Jekyll Theme
---

<div id="hero-carousel" class="carousel slide" data-ride="carousel" data-pause="false" data-interval="7000">
    <div class="carousel-inner">
    {% for image in site.data.front-page-slider.images %}
    <div class="carousel-item {% if forloop.index == 1 %} active{% endif %}">
        <div class="hero lazyload" data-bg="{{ site.url }}{{ site.baseurl }}/assets/img/slider/{{ image.file }}.jpg">
        <div class="hero__wrap">
            <h1 class="hero__title">{{ site.title | escape }}</h1>
            <p class="hero__meta">{{ site.tagline }}</p>
        </div>
        </div>        
    </div>
    {% endfor %}
    </div>
</div>
    
<main class="site__content">
    <section class="blog">
    <div class="container">
        <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

        {% for post in site.posts %}
            {% include card.html %}
        {% endfor %}

        <!-- {% include pagination.html %} -->
        </div>
    </div>
    </section>
</main>