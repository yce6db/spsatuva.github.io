---
layout: docs
title: Making Collapsible Elements
---

See documentation for Boostrap collapse elements [here](http://getbootstrap.com/docs/4.0/components/collapse/).

# Simple example

```html
<!-- This is the wrapper for the whole collapsible list. Give it a class name so you can style it and give it a unique ID to reference later -->
<div class="collapse-list-wrapper" 
     id="wrapper-id">
    <!-- This is the thing that you click on -->
    <!-- The attributes 'data-toggle', 'data-target', 'aria-controls' and 'aria-expanded' are required by Bootstrap to make the collapse work -->
    <!-- 'aria-expanded' when set to true means that the collapsible content pointed to by 'target-id' will be expanded upon loading -->
    <!-- 'target-id' should be the unique ID of the element that will be collapsed upon clicking the heading -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#target-id" 
         aria-controls="target-id" 
         aria-expanded="true">
        <!-- This is the arrow element. It MUST be before the heading. -->
        <!-- The arrow includes an h1arrow class to indicate what size it should be -->
        <!-- h1arrow, h2arrow, and h3arrow classes are all available to match the size of h1, h2, and h3 -->
        <i class="arrow h1arrow"></i>
        <!-- This is the heading name. You can change to anything you want, but h1 is a good size for a title -->
        <h1> Heading Name </h1>
    </div>
    <!-- This is what gets collapsed -->
    <!-- Give this a unique ID 'target-id' so that Bootstrap knows what gets collapsed when you click on the corresponding heading -->
    <!-- include the attribute 'data-parent' and give it the ID of the list wrapper if you only want one item in the collapse list to be open at once. If 'data-parent' is not included in each target element, then all collapsible elements can be open at once -->
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

<div class="tutorial-wrapper">
<!-- This is the wrapper for the whole collapsible list. Give it a class name so you can style it and give it a unique ID to reference later -->
<div class="collapse-list-wrapper" 
     id="wrapper-id">
    <!-- This is the thing that you click on -->
    <!-- The attributes 'data-toggle', 'data-target', 'aria-controls' and 'aria-expanded' are required by Bootstrap to make the collapse work -->
    <!-- 'aria-expanded' when set to true means that the collapsible content pointed to by 'target-id' will be expanded upon loading -->
    <!-- 'target-id' should be the unique ID of the element that will be collapsed upon clicking the heading -->
    <div class="collapse-list-heading" 
         data-toggle="collapse" 
         data-target="#target-id" 
         aria-controls="target-id" 
         aria-expanded="true">
        <!-- This is the arrow element. It MUST be before the heading. -->
        <!-- The arrow includes an h1arrow class to indicate what size it should be -->
        <!-- h1arrow, h2arrow, and h3arrow classes are all available to match the size of h1, h2, and h3 -->
        <i class="arrow h1arrow"></i>
        <!-- This is the heading name. You can change to anything you want, but h1 is a good size for a title -->
        <h1> Heading Name </h1>
    </div>
    <!-- This is what gets collapsed -->
    <!-- Give this a unique ID 'target-id' so that Bootstrap knows what gets collapsed when you click on the corresponding heading -->
    <!-- include the attribute 'data-parent' and give it the ID of the list wrapper if you only want one item in the collapse list to be open at once. If 'data-parent' is not included in each target element, then all collapsible elements can be open at once -->
    <div class="collapse-list-target collapse show" 
         id="target-id" 
         aria-labelledby="target-id" 
         data-parent="#wrapper-id">
        <p> Content goes here </p>
        <h3> It can be anything, as long as it's wrapped in the collapsible div </h3>
        <img src="https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"/>
    </div>
</div>
</div>

# With liquid tags and external data

We can make this more complex by generating the list with liquid tags. Examine the data in `_data/docs/test-collapse.yml`, which has the structure:

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
    <!-- We loop over each item in the list specified with site.data.docs.test-collapse.data -->
    {% for item in site.data.docs.test-collapse.data %}
    <!-- We're going to make a unique HTML5-friendly (no spaces) target ID to use from the data -->
    <!-- Here, we just use the heading name to uniquely identify each item in the collapse list -->
    <!-- The capture tag takes whatever is rendered inside it and puts it in a string contained in the variable 'target-id' to use later -->
    {%- capture target-id -%}
        {{ item.heading-name | remove: " " }}
    {%- endcapture -%}
    <!-- We check which item in the list we are currently examining with forloop.index -->
    <!-- If it is the first element, we want it to be expanded. -->
    <!-- If it is any other element, we want the content to be hidden -->
    <div class="collapse-list-heading {% unless forloop.index == 1 %} collapsed {% endunless %}" 
         data-toggle="collapse" 
         data-target="#{{ target-id }}" 
         aria-controls="{{ target-id }}" 
         aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
        <!-- If it is the first element, we want the arrow pointing up -->
        <!-- If it is any other element, we want the arrow pointing down -->
        <i class="arrow h1arrow"></i>
        <!-- Put in a heading with the name specified -->
        <h1> {{ item.heading-name }} </h1>
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
    {% for item in site.data.docs.test-collapse.data %}
    {%- capture target-id -%}
        {{ item.heading-name | remove: " " }}
    {%- endcapture -%}
    <!-- The controller -->
    <div class="collapse-list-heading {% unless forloop.index == 1 %} collapsed {% endunless %}" 
         data-toggle="collapse" 
         data-target="#{{ target-id }}" 
         aria-controls="{{ target-id }}" 
         aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
        <!-- The arrow -->
        <i class="arrow h1arrow"></i>
        <!-- The heading -->
        <h1> {{ item.heading-name }} </h1>
    </div>
    <!-- What is hidden / shown -->
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

<div class="tutorial-wrapper">
    <div class="collapse-list-wrapper" 
        id="complex-wrapper-id">
        {% for item in site.data.docs.test-collapse.data %}
        {%- capture target-id -%}
            {{ item.heading-name | remove: " " }}
        {%- endcapture -%}
        <div class="collapse-list-heading {% unless forloop.index == 1 %} collapsed {% endunless %}" 
            data-toggle="collapse" 
            data-target="#{{ target-id }}" 
            aria-controls="{{ target-id }}" 
            aria-expanded="{% if forloop.index == 1 %} true {% else %} false {% endif %}">
            <i class="arrow h1arrow"></i>
            <h1> {{ item.heading-name }} </h1>
        </div>
        <div class="collapse-list-target collapse {% if forloop.index == 1 %} show {% endif %}" 
            id="{{ target-id }}" 
            aria-labelledby="{{ target-id }}" 
            data-parent="#complex-wrapper-id">
            {{ item.content }}
            {% if item.image %}
            <img src="{{ item.image }}"/>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</div>

# Templated heading and content

It can get complicated making the collapse list heading and content and making sure it all works together. To prevent having to repeat complicated code, there is a template that takes care making these for you. You can make a heading with the template found found in `_includes/collapse-list-heading.html` which is used as follows:

```liquid
{% raw %}{% include collapse-list-heading.html
   <!-- Required. Can also be a liquid variable. -->
   heading="My Heading"
   <!-- Required. Can also be a liquid variable -->
   target-id="my-target-id"
   <!-- Optional. Either true or false -->
   expanded=true
   <!-- Optional. Default = h1 -->
   heading-type='h3'
   <!-- Optional. Include all of the CSS classes you want here as a space separated string -->
   classes="class-one class-two"
%}{% endraw %}
```

This heading can be paired with an accompanying target include found in `_includes/collapse-list-target.html` and is used as follows:

```liquid
<!-- We have to capture all of the HTML we want inside of the collapse target div before we actually include it. We capture it all using the capture liquid tag, which stores everything between the tag into the variable 'content'. 'content' is then passed onto the target template HTML and included inside the div. -->
{% raw %}{%- capture content -%}
 <p> I am inside this div. </p>
{%- endcapture -%}
{% include collapse-list-target.html
   <!-- Required. Pass the ID of the target element here. -->
   id="my-target-id"
   <!-- Required. Either true or false. -->
   expanded=true
   <!-- Required. A string containing all of the content to put inside the target. -->
   content=content
   <!-- Optional. Used for when there are multiple items to control. Pass the ID of the div that wraps all the collapse-lists. -->
   parent-id=""
   <!-- Optional. Pass all of the CSS classes that you want in one string separated by spaces. -->
   classes=""
%}{% endraw %}
```

So in total we have:

```liquid
{% raw %}{% include collapse-list-heading.html
   <!-- Required. Can also be a liquid variable. -->
   heading="My Heading"
   <!-- Required. Can also be a liquid variable -->
   target-id="my-target-id"
   <!-- Optional. Either true or false -->
   expanded=true
   <!-- Optional. Default = h1 -->
   heading-type='h3'
   <!-- Optional. Include all of the CSS classes you want here -->
   classes="class-one class-two"
%}

{%- capture content -%}
 <p> I am inside this div. </p>
{%- endcapture -%}
{% include collapse-list-target.html
   id="my-target-id"
   expanded=true
   content=content
   parent-id=""
   classes=""
%}{% endraw %}
```

which renders out to the following html

```html
<!-- The heading -->
{% include collapse-list-heading.html heading="My Heading" target-id="my-target-id" expanded=true heading-type='h3' %}
{%- capture content -%}
<p> I am inside this div </p>
{%- endcapture -%}
<!-- The target -->
{% include collapse-list-target.html id="my-target-id" expanded=true content=content parent-id="" classes="" %}
```

which finally renders to:
<div class="tutorial-wrapper">
    {% include collapse-list-heading.html 
    heading="My Heading"
    target-id="my-target-id"
    expanded=true
    heading-type='h3'
    %}
    {%- capture content -%}
    <p> I am inside this div </p>
    {%- endcapture -%}
    {% include collapse-list-target.html 
       id="my-target-id"
       expanded=true
       content=content
       parent-id=""
       classes=""
    %}
</div>

Of course this gets a bit cumbersome, especially with using `collapse-list-target.html` which requires capturing **all** of the content we wish to be inside the dropdown *before* we actually make the div. The `collapse-list-heading.html` template is more self-contained and can be used independently as long as you remember to properly ID your collapse targets and pass them to `collapse-list-heading.html`.

# Templated headings, content, and external data

We're going to combine each of the tutorials above to show how to completely automate and modularize this process. We will be using the same data stored in `_data/docs/test-collapse.yml`:

```yaml
data:
  - heading-name: One
    content: "This is the content of heading one"
  - heading-name: Two
    content: "The is the content of heading two"
  - heading-name: Three
    content: "This is the content of heading three. It has an image as well"
    image: https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940
```

We first wrap the whole thing in a parent div, with ID "full-parent", then loop through each item in the above list, making a friendly ID for the target content (we append "-full-example" to not conflict with the elements above on this same page), generate the header div with the template, capture all of the content in a variable, and then pass the content to the target template to generate the target div.

```liquid
{% raw %}<div id="full-parent">
    {% for item in site.data.docs.test-collapse.data %}
        <!-- Make unique target ID -->
        {%- capture target-id -%}
            {{ item.heading-name | remove: " " | append: "-full-example" }}
        {%- endcapture -%}
        <!-- Check if expanded -->
        {% if forloop.index == 1 %}
            {% assign expanded = true %}
        {% else %}
            {% assign expanded = false %}
        {% endif %}
        <!-- Heading -->
        {% include collapse-list-heading.html 
            heading=item.heading-name
            target-id=target-id
            expanded=expanded
            heading-type='h1'
        %}
        <!-- Target content -->
        {%- capture content -%}
            {{ item.content }}
            {% if item.image %}
                <img src="{{ item.image }}"/>
            {% endif %}
        {%- endcapture -%}
        <!-- The target div template -->
        {% include collapse-list-target.html
            id=target-id
            expanded=expanded
            content=content
            parent-id="full-parent"
        %}
    {% endfor %}
</div>{% endraw %}
```

This generates the following HTML:

```html
<div id="full-parent">
    {% for item in site.data.docs.test-collapse.data %}
        {%- capture target-id -%}
            {{ item.heading-name | remove: " " | append: "-full-example" }}
        {%- endcapture -%}
        {% if forloop.index == 1 %}
            {% assign expanded = true %}
        {% else %}
            {% assign expanded = false %}
        {% endif %}{% include collapse-list-heading.html 
            heading=item.heading-name
            target-id=target-id
            expanded=expanded
            heading-type='h1'
        %}{%- capture content -%}
            {{ item.content }}
            {% if item.image %}
                <img src="{{ item.image }}"/>
            {% endif %}
        {%- endcapture -%}{% include collapse-list-target.html
            id=target-id
            expanded=expanded
            content=content
            parent-id="full-parent"
        %}
    {% endfor %}
</div>
```

You can see that using the templated HTML makes some poorly formatted code (new lines and spaces everywhere). This doesn't really matter though, since the syntax is valid and it renders perfectly to:

<div class="tutorial-wrapper">
    <div id="full-parent">
        {% for item in site.data.docs.test-collapse.data %}
            {%- capture target-id -%}
                {{ item.heading-name | remove: " " | append: "-full-example" }}
            {%- endcapture -%}
            {% if forloop.index == 1 %}
                {% assign expanded = true %}
            {% else %}
                {% assign expanded = false %}
            {% endif %}
            {% include collapse-list-heading.html 
                heading=item.heading-name
                target-id=target-id
                expanded=expanded
                heading-type='h1'
            %}
            {%- capture content -%}
                {{ item.content }}
                {% if item.image %}
                    <img src="{{ item.image }}"/>
                {% endif %}
            {%- endcapture -%}
            {% include collapse-list-target.html
                id=target-id
                expanded=expanded
                content=content
                parent-id="full-parent"
            %}
        {% endfor %}
    </div>
</div>