---
layout: home
---

{% comment %}
<!-- Hero Slider -->
{% endcomment %}
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

{% comment %}
<!-- Main content -->
{% endcomment %}
<main class="site__content">
    <section class="blog">
    </section>
</main>

<div class="div-calendar" align="center">
    <iframe src="https://calendar.google.com/calendar/b/1/embed?height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=virginia.edu_2n5ng0l77qnkib1b4o731sb6ag%40group.calendar.google.com&amp;color=%236B3304&amp;ctz=America%2FNew_York" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe> 
</div>