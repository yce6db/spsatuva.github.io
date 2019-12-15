---
layout: page
title: PHYS 1910 Lectures
---

Here you can find an archive of lecture recordings for the PHYS 1910 course, which you can find out more about [here]( {{ site.url }}{{ site.baseurl }}/phys1910/about/ ).

<div class="lectures-years" id="lectures-years">
    {% for year in site.data.phys1910.lectures %}
    {%- capture year_no_spaces -%}
        {{ year.year | remove: " " }}
    {%- endcapture -%}
    {% if year.year == site.data.phys1910.current-year %}
        {% assign expanded = true %}
    {% else %} 
        {% assign expanded = false %}
    {% endif %}
    {% include collapse-list-heading.html
       heading=year.year
       target-id=year_no_spaces
       heading-type='h1'
       expanded=expanded
    %}
    <div class="recordings collapse {% if year.year == site.data.phys1910.current-year %} show {% endif %}" id="{{ year_no_spaces }}" aria-labelledby="{{ year_no_spaces }}" data-parent="#lectures-years">
        {% if year.recordings %}
        {% for recording in year.recordings %}
            {% if recording.id and recording.id != "NA" %}
                {% assign div_id = recording.id %}
            {% else %}
                {% comment %} This will generate a pseudo-random number based on the time of generation to use as an id for the collapsible div element {% endcomment %}
                {% capture time_seed %}{{ 'now' | date: "%s" }}{% endcapture %}
                {% assign div_id = time_seed | times: 1103515245 | plus: 12345 | divided_by: 65536 | modulo: 32768 %}
            {% endif %}
            <div class="collapse-list-heading collapsed" data-toggle="collapse" data-target="#{{ div_id }}" aria-expanded="false" aria-controls="{{ div_id }}">
                <h3>
                    <a class="recording-info"> 
                        {{ recording.speaker }} - {{ recording.title }} 
                    </a>
                </h3>
            </div>
            <div class="recording-container collapse" id="{{ div_id }}" aria-labelledby="{{ div_id }}">
                {% if recording.slides %}
                <h4>
                    Slides can be found <a href="{{ recording.slides }}">here</a>.
                </h4>
                {% endif %}
                {% if recording.id and recording.id != "NA" %}
                <iframe class="recording-video" src="https://uva.hosted.panopto.com/Panopto/Pages/Embed.aspx?id={{ div_id }}&v=1" frameborder="0" allowfullscreen allow="autoplay">
                </iframe>
                {% endif %}
            </div>
        {% endfor %}
        {% else %}
            <p> Oops...doesn't look like there are any videos for {{ year.year }}. Try checking out the archive of previous years' videos below. </p>
        {% endif %}
    </div>
    {% endfor %}
</div>