---
layout: page
title: Making collapsible elements
permalink: /docs/test-collapse/
---

See documentation for Boostrap collapse elements [here](http://getbootstrap.com/docs/4.0/components/collapse/).

# Simple example

```html
<!-- This is the wrapper for the whole collapsible list. Give it a class name so you can style it and give it a unique id to reference later -->
<div class="collapse-list-wrapper" 
     id="wrapper-id">
    <!-- This is the thing that you click on -->
    <!-- The attributes 'data-toggle', 'data-target', 'aria-controls' and 'aria-expanded' are required by Bootstrap to make the collapse work -->
    <!-- 'aria-expanded' when set to true means that the collapsible content pointed to by 'target-id' will be expanded upon loading -->
    <!-- 'target-id' should be the unique id of the element that will be collapsed upon clicking the heading -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#target-id" 
         aria-controls="target-id" 
         aria-expanded="true">
        <!-- This is the heading name. You can change to anything you want, but h1 is a good size for a title -->
        <h1> Heading Name </h1>
        <!-- This is the arrow element -->
        <i class="arrow up"></i>
    </div>
    <!-- This is what gets collapsed -->
    <!-- Give this a unique id 'target-id' so that Bootstrap knows what gets collapsed when you click on the corresponding heading -->
    <!-- include the attribute 'data-parent' and give it the id of the list wrapper if you only want one item in the collapse list to be open at once. If 'data-parent' is not included in each target element, then all collapsible elements can be open at once -->
    <div class="collapse-list-target collapse show" 
         id="target-id" 
         aria-labelledby="target-id" 
         data-parent="#wrapper-id">
        <p> Content goes here </p>
        <h3> It can be anything, as long as it's wrapped in the collapsible div </h3>
        <img src="https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"/>
    </div>
</div>
```

This renders to:

<div style="background-color: #f8f8f8; border-color: rgb(222, 226, 230); border-radius: 0.3rem; border: solid 1px; padding: 5px;">
<!-- This is the wrapper for the whole collapsible list. Give it a class name so you can style it and give it a unique id to reference later -->
<div class="collapse-list-wrapper" 
     id="wrapper-id">
    <!-- This is the thing that you click on -->
    <!-- The attributes 'data-toggle', 'data-target', 'aria-controls' and 'aria-expanded' are required by Bootstrap to make the collapse work -->
    <!-- 'aria-expanded' when set to true means that the collapsible content pointed to by 'target-id' will be expanded upon loading -->
    <!-- 'target-id' should be the unique id of the element that will be collapsed upon clicking the heading -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#target-id" 
         aria-controls="target-id" 
         aria-expanded="true">
        <!-- This is the heading name. You can change to anything you want, but h1 is a good size for a title -->
        <h1> Heading Name </h1>
        <!-- This is the arrow element -->
        <i class="arrow up"></i>
    </div>
    <!-- This is what gets collapsed -->
    <!-- Give this a unique id 'target-id' so that Bootstrap knows what gets collapsed when you click on the corresponding heading -->
    <!-- include the attribute 'data-parent' and give it the id of the list wrapper if you only want one item in the collapse list to be open at once. If 'data-parent' is not included in each target element, then all collapsible elements can be open at once -->
    <div class="collapse-list-target collapse show" 
         id="target-id" 
         aria-labelledby="target-id" 
         data-parent="wrapper-id">
        <p> Content goes here </p>
        <h3> It can be anything, as long as it's wrapped in the collapsible div </h3>
        <img src="https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"/>
    </div>
</div>
</div>

# With liquid tags and external data

We can make this more complex by generating the list with liquid tags. Examine the data in `_data/test-collapse.yml`, which has the structure:

```yml
data:
  - heading-name: One
    content: "This is the content of heading one"
  - heading-name: Two
    content: "The is the content of heading two"
  - heading-name: Three
    content: "This is the content of heading three. It has an image as well"
    image: https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940
```

With the following HTML + Liquid code

```html
{% raw %}<div class="collapse-list-wrapper" 
     id="complex-wrapper-id">
    <!-- We loop over each item in the list specified with site.data.test-collapse.data -->
    {% for item in site.data.test-collapse.data %}
    <!-- We're going to make a unique HTML5-friendly (no spaces) target id to use from the data -->
    <!-- Here, we just use the heading name to uniquely identify each item in the collapse list -->
    <!-- The capture tag takes whatever is rendered inside it and puts it in a string contained in the variable 'target-id' to use later -->
    {%- capture target-id -%}
        {{ item.heading-name | remove: " " }}
    {%- endcapture -%}
    <!-- We check which item in the list we are currently examining with forloop.index -->
    <!-- If it is the first element, we want it to be expanded. -->
    <!-- If it is any other element, we want the content to be hidden -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#{{ target-id }}" 
         aria-controls="{{ target-id }}" 
         aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
        <!-- Put in a heading with the name specified -->
        <h1> {{ item.heading-name }} </h1>
        <!-- If it is the first element, we want the arrow pointing up -->
        <!-- If it is any other element, we want the arrow pointing down -->
        <i class="arrow {% if forloop.index == 1 %} up {% else %} down {% endif %}"></i>
    </div>
    <!-- If it is the first element, we want the content to be shown  -->
    <!-- If it is any other element, we want the content to be hidden -->
    <div class="collapse-list-target collapse {% if forloop.index == 1 %} show {% endif %}" 
         id="{{ target-id }}" 
         aria-labelledby="{{ target-id }}" 
         data-parent="#complex-wrapper-id">
        <!-- Copy in the content specified from the data with {{ item.content }} -->
        {{ item.content }}
        <!-- Check if we specified an image in the data -->
        {% if item.image %}
        <!-- If so, include an image -->
        <img src="{{ item.image }}"/>
        {% endif %}
    </div>
    {% endfor %}
</div>{% endraw %}
```

Which, when the Liquid tags renders out gives this code:

```html
<div class="collapse-list-wrapper" 
     id="complex-wrapper-id">
    {% for item in site.data.test-collapse.data %}
    {%- capture target-id -%}
        {{ item.heading-name | remove: " " }}
    {%- endcapture -%}
    <!-- Note the automatically generated element ids -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#{{ target-id }}" 
         aria-controls="{{ target-id }}" 
         aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
        <!-- The heading -->
        <h1> {{ item.heading-name }} </h1>
        <i class="arrow {% if forloop.index == 1 %} up {% else %} down {% endif %}"></i>
    </div>
    <div class="collapse-list-target collapse {% if forloop.index == 1 %} show {% endif %}" 
         id="{{ target-id }}" 
         aria-labelledby="{{ target-id }}" 
         data-parent="#complex-wrapper-id">
        <!-- The content -->
        {{ item.content }}
        {% if item.image %}
        <!-- The image -->
        <img src="{{ item.image }}"/>
        {% endif %}
    </div>
    {% endfor %}
</div>
```

We can make a collapse list that renders to:

<div style="background-color: #f8f8f8; border-radius: 0.3rem; border: solid 1px; padding: 5px;">
    <div class="collapse-list-wrapper" 
         id="complex-wrapper-id">
        <!-- We loop over each item in the list specified with site.data.test-collapse.data -->
        {% for item in site.data.test-collapse.data %}
        <!-- We're going to make a unique HTML5-friendly (no spaces) target id to use from the data -->
        <!-- Here, we just use the heading name to uniquely identify each item in the collapse list -->
        <!-- The capture tag takes whatever is rendered inside it and puts it in a string contained in the variable 'target-id' to use later -->
        {%- capture target-id -%}
            {{ item.heading-name | remove: " " }}
        {%- endcapture -%}
        <!-- We check which item in the list we are currently examining with forloop.index -->
        <!-- If it is the first element, we want it to be expanded. -->
        <!-- If it is any other element, we want the content to be hidden -->
        <div class="collapse-list-heading" 
             data-toggle="collapse" 
             data-target="#{{ target-id }}" 
             aria-controls="{{ target-id }}" 
             aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
            <!-- Put in a heading with the name specified -->
            <h1> {{ item.heading-name }} </h1>
            <!-- If it is the first element, we want the arrow pointing up -->
            <!-- If it is any other element, we want the arrow pointing down -->
            <i class="arrow {% if forloop.index == 1 %} up {% else %} down {% endif %}"></i>
        </div>
        <!-- If it is the first element, we want the content to be shown  -->
        <!-- If it is any other element, we want the content to be hidden -->
        <div class="collapse-list-target collapse {% if forloop.index == 1 %} show {% endif %}" 
             id="{{ target-id }}" 
             aria-labelledby="{{ target-id }}" 
             data-parent="#complex-wrapper-id">
            <!-- Copy in the content specified from the data with {{ item.content }} -->
            {{ item.content }}
            <!-- Check if we specified an image in the data -->
            {% if item.image %}
            <!-- If so, include an image -->
            <img src="{{ item.image }}"/>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</div>