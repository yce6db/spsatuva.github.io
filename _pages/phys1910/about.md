---
layout: page
title: PHYS 1930
---

# PHYS 1930 - Physics in the 21st Century

PHYS 1930 is a 2-credit seminar course held during the Fall which is intended to help students get a grasp on what a physics major is about, along with what research is being performed in the physics department. The course features guest lectures by various professors in the department, who will discuss research opportunities in their field. Enrolling in PHYS 1930 will help you meet many of the professors in the department and will help break the ice in introducing yourself.


PHYS 1910 is a student-run course meant to introduce physics majors to the variety of research opportunities available to them within physics. The course is a run as a speaker series, featuring a talk from a professor in the UVA Physics Department about the research they perform and the research opportunities they have for students enrolled in this course. Speakers in the series are drawn from both experimental and theoretical diciplines of the main areas of physics research currently being pursued at UVA:
- Atomic, Molecular, and Optical (AMO) Physics
- Condensed Matter Physics
- High Energy Physics
- Medical Physics
- Nuclear and Particle Physics

Many lectures are able to be recorded, and an archive of them from the current and previous years can be found on the [course lecture page]({{ site.url }}{{ site.baseurl }}/phys1910/lectures/).

# Syllabus / Course Schedule

Below you can find the current and previous syllabi and course schedules for PHYS 1910.

{% for item in site.data.phys1910.syllabus %}
- **{{ item.year }}**: {% if item.pdf %} [PDF]({{ item.pdf }}) {% else %} Nothing yet! {% endif %}
{% endfor %}

# Course Organizers

<div class="years-1910" id="1910-years">
    {% for year in site.data.phys1910.years %}
    {%- capture year_no_space -%}
        {{ year.year | remove: " " }}
    {%- endcapture -%}
    {% if site.data.phys1910.current-year == year.year %}
        {% assign expanded = true %}
    {% else %}
        {% assign expanded = false %}
    {% endif %}
    {% include collapse-list-heading.html 
       heading=year.year
       heading-type='h2'
       expanded=expanded
       target-id=year_no_space
    %}
    <div class="info-container-1910 collapse {% if site.data.phys1910.current-year == year.year %} show {% endif %}" id="{{ year_no_space }}" aria-labelledby="{{ year_no_space }}" data-parent="#1910-years">
        {% for person in year.people %}
            {% assign image = person.image %}
            {% assign name = person.name %}
            {% assign title = person.title %}
            {% assign email = person.email %}
            <div class="image-item-1910">
                {% include lazy-image.html
                    image=image
                    base-path='pages/phys1910'
                    image-class="image-1910"
                %}
                <h2 class="image-name-1910"> {{ name }} </h2>
                <h3 class="image-title-1910"> {{ title }} </h3>
                {% if site.data.phys1910.current-year == year.year %}
                <a href="mailto:{{ email }}"> {{ email }} </a>
                {% endif %}
                <hr class="image-separator-1910">
            </div>
        {% endfor %}
    </div>
    {% endfor %}
</div>
