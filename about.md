---
layout: page
title: About
permalink: /about/
---

# Who We Are

The Society of Physics Students at UVa is a group dedicated to the academic and personal enrichment of the physics majors at the University of Virginia. We have three focuses: social inclusion within our chapter, providing access to [research]( {{ site.baseurl }}/research ) and [academic resources]( {{ site.baseurl }}/courses ), and representing the voice of undergraduates in the UVA physics department.

___

# Executive Board

<div class="exec_board" id="exec_board">
    {% for year in site.data.exec-board.exec-boards %}
    <div class="image_list_year" data-toggle="collapse" data-target="#{{ year.year }}" {% if year.year == site.data.exec-board.current-year %} aria-expanded="true" {% else %} aria-expanded="false" {% endif %} aria-controls="{{ year.year }}">
        <h1>
            {{ year.year }}
        </h1>
    </div>
    <div class="image_list_container collapse {% if year.year == site.data.exec-board.current-year %} show {% endif %}" id="{{ year.year }}" aria-labelledby="{{ year.year }}" data-parent="#exec_board">
        {% for person in year.board %}
        <div class="image_list_item">
            <div class="image_list_info_container">
                <div class="image_list_info">
                    <h2>
                        {{ person.name }}
                    </h2>
                    <h3>
                        {{ person.role }}
                    </h3>
                </div>
                {% if person.img %}
                <div class="image_list_image">
                    <img class="image_list_image lazyload" data-src="{{ site.baseurl}}/assets/img/exec/{{ person.img }}">
                </div>
                {% endif %}
            </div>
            <div class="image_list_description">
                {% for paragraph in person.description %}
                    {{ paragraph | markdownify }}
                {% endfor %}
            </div>
            {% if person.site or person.email %}
            <div class="image_list_item_footer_container">
                <div class="image_list_item_footer">
                    {% if person.site %}
                    <p>
                         <strong>Homepage</strong>: <a href="{{ person.site }}"> {{ person.site }} </a>
                    </p>
                    {% endif %}
                    {% if person.email %}
                    <p>
                        <strong>Email</strong>: <a href="mailto:{{ person.email }}"> {{ person.email }} </a>
                    </p>
                    {% endif %}
                </div>
            </div>
            {% endif %}
        </div>
        <div class="image_list_hr_container">
            <hr>
        </div>
        {% endfor %}
    </div>
    {% endfor %}
</div>