
---
layout: page
title: About
---

# Who We Are

The Society of Physics Students at UVa is a group dedicated to the academic and personal enrichment of the physics majors at the University of Virginia. We have three focuses: social inclusion within our chapter, providing access to [research]( {{ site.baseurl }}/research ) and [academic resources]( {{ site.baseurl }}/courses ), and representing the voice of undergraduates in the UVA physics department.

Although this organization has members who are University of Virginia students and may have University employees associated or engaged in its activities and affairs, the organization is not a part of or an agency of the University. It is a separate and independent organization, which is responsible for and manages its own activities and affairs. The University does not direct, supervise or control the organization and is not responsible for the organization's contracts, acts or omissions.

___

# Faculty Advisor

<div class="fac_advisor" id="fac_advisor">
    <div class="exec_board_info_container">
        <div class="exec_board_info">
            <h2>
                Professor Jency Sundararajan
            </h2>
        </div>
        {% include lazy-image.html
           image='Stefan.png'
           base-path='exec'
           container-class="exec_board_image"
           image-class="exec_board_image"
        %}
        <p>
            <strong>Email</strong>: <a href="mailto:zey9gt@virginia.edu">zey9gt@virginia.edu</a>
        </p>
    </div>
    <div class="exec_board_description">
        Jency Sundararajan is an Assistant Professor at the University of Virginia. 
    </div>
</div>

# Executive Board

<div class="exec_board" id="exec_board">
    {% for year in site.data.exec-board.exec-boards %}
    {%- capture year_no_space -%}
        {{ year.year | remove: " " }}
    {%- endcapture -%}
    {% if year.year == site.data.exec-board.current-year %}
        {% assign expanded = true %}
    {% else %}
        {% assign expanded = false %}
    {% endif %}
    {% include collapse-list-heading.html 
       heading=year.year
       target-id=year_no_space
       expanded=expanded
    %}
    <div class="exec_board_container collapse {% if year.year == site.data.exec-board.current-year %} show {% endif %}" id="{{ year_no_space }}" aria-labelledby="{{ year_no_space }}" data-parent="#exec_board">
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
                    {% include lazy-image.html
                       image=image 
                       base-path='exec'
                       container-class="exec_board_image"
                       image-class="exec_board_image"
                    %}
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

