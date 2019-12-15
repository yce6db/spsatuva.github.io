---
layout: docs
title: Home Page
doc-title: Home
source-files:
- "index.md"
- "_config.yml"
- "_data/front-page-slider.yml"
---

The home page is located in the file `index.md` and consists of two elements: 1) an image slider with an overlay on top of it with the site title and 2) a Google calendar with upcoming events.

# Image Slider Overlay

The overlay text shows the site title and the site description, stored in `_config.yml` under the keys `title` and `tagline`. To change the overlay, change the content of these fields in `_config.yml`.

# Image Slider

The image slider is controlled by the following HTML and Liquid. You can see that the variables `site.title` and `site.tagline` (set from `_config.yml`) are referenced in this snippet.
```html
{% raw %}
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
{% endraw %}
```

The images that will appear in the image slider on the front page are specified in the file `_data/front-page-slider.yml` and are accessed above as `site.data.front-page-slider.images`. Each image has a field `file` which specifies the filename of the image and an optional field `align` which will change how the image is positioned within the slider (for centering the image without cropping for example). Each image is expected to reside in the folder `/assets/img/slider`. 

To add a new image to the slider, add your image to the folder `_img/slider/` and then run the `img-resize.py` script (see [here])(/docs/sites/images/)). Next, add the image to `_data/front-page-slider.yml` under the `images` list with at least a `file` field with the name of the file you added.

# Google Calendar

The Google Calendar is embeded into the front page with the following HTML:

```html
<div class="div-calendar" align="center">
    <iframe src="https://calendar.google.com/calendar/b/1/embed?height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=virginia.edu_2n5ng0l77qnkib1b4o731sb6ag%40group.calendar.google.com&amp;color=%232952A3&amp;ctz=America%2FNew_York" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe> 
</div>
```
