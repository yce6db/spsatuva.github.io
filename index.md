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
            <div class="hero lazyload" data-bg="{{ site.url }}{{ site.baseurl }}/assets/img/slider/{{ image.file }}" {% if image.align %}style="background-position: {{ image.align }};"{% endif %}> 
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

### New Updates! List of professors looking for students:

Here you will find a list of professors who have specific research projects to advertise to undergraduate students. Simply click on any projects that sound interesting to you to find out more about the project and to find out information on how to contact them.

<div class="project_list" id="project_list">
    {% for project in site.data.research-opportunities.project-list %}
    <a href="#" class="project" data-toggle="collapse" data-target="#{{ project.short-name }}" aria-expanded="false" aria-controls="{{ project.short-name }}">
        {{ project.name }} - {{ project.title }}
    </a>
    <div class="project_container collapse" id="{{ project.short-name }}" aria-labelledby="{{ project.short-name }}">
        <iframe style="width:100%;height:500px" src="{{ project.url }}?embeded=true"></iframe>
    </div>
    {% endfor %}
</div>

<div class="div-calendar" align="center">
    <iframe src="https://calendar.google.com/calendar/embed?src=d55hnepu6qjp8q3krgeh1kvlb0%40group.calendar.google.com&ctz=America%2FNew_York" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe> 
</div>
