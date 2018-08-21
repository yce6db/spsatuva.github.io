---
layout: page
title: Outreach Guides
permalink: /outreach/guides/
---

Here you will find an organized list of written guides for performing outreach demonstrations for schools. These guides were written by a combination of our Outreach Managers, Jillian Ticatch and Pedrom Zadeh, and our Outreach Volunteers, mainly Michael Worcester.

<div id="guide-list-wrapper">
    {% for guide in site.data.outreach-guides.guides %}
        {% comment %}
            NOTE: This is extremely hacky. It uses the google docs url to determine a unique id for each element. This only works if the google doc document id stays HTML id safe (no spaces or special characters other than '.', '-', and '_'). It also makes the source HTML on the rendered page unreadable.
        {% endcomment %}
        {% assign url_split = guide.url | split: "/" %}
        {%- capture target-id -%}
            {{ url_split[-2] }}
        {%- endcapture -%}
        <a class="guide-list-heading" data-toggle="collapse" data-target="#{{ target-id }}" aria-controls="{{ target-id }}" aria-expanded="false">
            {{ guide.title }}
        </a>
        <div class="collapse" id="{{ target-id }}" aria-labelledby="{{ target-id }}">
            <iframe style="width:100%; height:500px;" src="{{ guide.url }}?embeded=true"></iframe>
        </div>
    {% endfor %}
</div>