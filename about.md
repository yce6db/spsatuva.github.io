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
    <div class="exec_board_year" data-toggle="collapse" data-target="#{{ year.year }}" {% if year.year == site.data.exec-board.current-year %} aria-expanded="true" {% else %} aria-expanded="false" {% endif %} aria-controls="{{ year.year }}">
        <h1>
            {{ year.year }}
        </h1>
    </div>
    <div class="exec_board_container collapse {% if year.year == site.data.exec-board.current-year %} show {% endif %}" id="{{ year.year }}" aria-labelledby="{{ year.year }}" data-parent="#exec_board">
        {% for person in year.board %}
            {% assign image = false %}
            {% assign email = false %}
            {% assign homepage = false %}
            {% assign description = false %}
            {% for member in site.data.exec-board.members %}
                {% if member.name == person.name %}
                    {% assign image = member.img %}                        
                    {% assign email = member.email %}
                    {% assign homepage = member.homepage %}
                    {% assign description = member.description %}
                {% endif %}
            {% endfor %}
        <div class="exec_board_item">
            <div class="exec_board_info_container">
                <div class="exec_board_info">
                    <h2>
                        {{ person.name }}
                    </h2>
                    <h3>
                        {{ person.role }}
                    </h3>
                </div>
                {% if image %}
                <div class="exec_board_image">
                    <img class="exec_board_image lazyload" data-src="{{ site.baseurl}}/assets/img/exec/{{ image }}">
                </div>
                {% endif %}
                {% if homepage or email %}
                {% if homepage %}
                <p>
                    <strong>Homepage</strong>: <a href="{{ homepage }}"> {{ homepage }} </a>
                </p>
                {% endif %}
                {% if email %}
                <p>
                    <strong>Email</strong>: <a href="mailto:{{ email }}"> {{ email }} </a>
                </p>
                {% endif %}
                {% endif %}
            </div>
            <div class="exec_board_description">
                {% for paragraph in description %}
                    {{ paragraph | markdownify }}
                {% endfor %}
            </div>
        </div>
        <div class="exec_board_hr_container">
            <hr>
        </div>
        {% endfor %}
    </div>
    {% endfor %}
</div>