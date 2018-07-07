---
layout: page
title: Events
permalink: /events/
container: false
---

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
