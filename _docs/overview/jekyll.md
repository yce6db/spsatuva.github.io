---
layout: docs
title: Jekyll, Liquid, and YAML
doc-title: Jekyll
---

Jekyll is a static website *generator* which GitHub pages uses natively to build and publish our website. You should take a look at the [Jekyll documentation](https://jekyllrb.com/docs/) to get a feel for how it works. Jekyll is built using the programming language [Ruby](https://www.ruby-lang.org/), which is popular for web applications. However, you won't need to know how to use Ruby to use Jekyll.

# What is Jekyll?

Many website are built out of fundamental pieces that all look similar to one another. For example, on many websites there will be a navigation bar at the top, left, or right of the page that lets you get around the website. While each page of a website is a single separate HTML file, the set of HTML, CSS, and JavaScript that describes that navigation bar will be the same on each page. Instead of hard-coding in this navigation bar into hundreds of the HTML files on your site, it would make a lot more sense to *template* in the navigation bar instead so it gets included automatically when the site is *built*. When a website grows beyond a few pages, it becomes cumbersome, confusing, and challenging to manage any part of it and keep it all looking and functioning in a consistent way without templating and generating dynamically the HTML that manages each page. 

Jekyll allows you to do this. It uses the [Liquid templating langauge](https://shopify.github.io/liquid/) to build individual pages of a website by using page templates (or *layouts*) and HTML / CSS / JavaScript snippets that can be *included* into each page. Each page on your website corresponds to single [Markdown](https://www.markdownguide.org/) file. Markdown lets you create the page without being burdened by the cumbersome syntax of HTML. Pages can be grouped into collections of similar pages, most notably blog *posts*. Additionally, pages can be generated using *data*, lists and dictionaries of values specified using [YAML](https://yaml.org/), that can be used to generate HTML / CSS / JavaScript. Finally, Jekyll allows for users to build plugins (called *Gems* in Ruby). The directory structure of a new Jekyll project that describes and allows you to build a website will look like the following:
```
_data        # contains YAML files that specify external data that can be used by Jekyll
_includes    # the set of HTML snippets that can be included by Jekyll
_layouts     # the set of HTML layouts that Jekyll is aware of
_pages       # a place to put individual pages
_posts       # a place to put blog posts
Gemfile      # specifies which Jekyll plugins to use
_config.yaml # data that specifies site configuration
```

# How does Jekyll work?

Providing a detailed description of how Jekyll works is beyond the scope of this documentation, but the Jekyll documentation does a good job of walking you through the process of getting a site up and running and explaining the details. There are already several great resources for understanding Jekyll and its inner workings already out on the web, for example [here](http://jekyllbootstrap.com/lessons/jekyll-introduction.html) with additional results from googling "how does Jekyll work?". However we'll provide a minimum example of creating the core components of Jekyll and show how they work together to build a page of the website.

# A minimal example

We're going to make an example

- A single page made with Markdown. This page will use a layout we specify and it will include an external HTML snippet. 
- A single layout that will use parts of the page's YAML front matter and data from `_config.yaml` to customize what appears on the rendered page
- A single HTML snippet that generates a list dynamically using external data
- Data specfied in YAML that is used to generate the previouse list 

First, here is the page we'd like to create:

```markdown
{%- raw -%}
<!-- # file: _pages/home.md -->
<!-- The is the YAML Front Matter, a set of YAML lists and dictionaries that specify the particular settings and data that can be used in this page. Within a layout, these data can be accessed with page.key-name. All front Matter is encapsulated between two "---" -->
---
<!-- This says use the layout contained in _layouts/default.html to generate this page -->
layout: default
<!-- This is data that can be accessed within the specified layout as page.title -->
title: Home Page
<!-- This is data that can be accessed within the specified layout as page.tagline -->
tagline: Jekyll builds nice websites
---
<!-- Everything that comes after the YAML front matter is called the page content -->
# This is the syntax for a Markdown heading which will render out to have h1 tags

<p> Raw html can also be included in Markdown </p>

<!-- Raw text separated by new-lines gets rendered out into paragraphs with <p> tags -->
I'm going to include a dynamically generated list here from `_includes/list.html`:

<!-- This Liquid tag pulls the content from _includes/list.html and renders it out within this page. -->
{% include list.html %}

{% endraw %}
```

We can see that this page includes a file called `list.html` which will be pulled from `_includes/list.html`. The example we'll use is
```html
{%- raw -%}
<!-- file: _includes/list.html -->
<h3>
  <!-- Access the data structure in _data/list-items.yaml, getting the value corresponding to the key 'name' -->
  <!-- two curly braces with text inside means treat the text inside as a variable and evaluate that variable out to text -->
  {{ site.data.list-items.name }}
</h3>
<ul>
  <!-- Access the data structure in _data/list-items.yaml, getting the value corresponding to the key 'fruits', which is a list and can be iterated over with a for-loop -->
  {% for fruit in site.data.list-items.fruits %}
  <li>
    <!-- evaluate the fruit item from the above list into text -->
    {{ fruit }}
  </li>
  {% endfor %}
</ul>
{% endraw %}
```

This HTML snippet is dynamically generated by Jekyll using data stored in `_data/list-items.yaml`. This data structure is specified as follows
```yaml
# file: _data/list-items.yaml
# our data structure can be accessed with site.data.list-items
# this data structure is a dictionary at the root level with keys: name, fruits, and recipes
# indexing the dictionary with those keys will give back the following data structures
# site.data.list-items.name --> String (equal to "Assorted foods and things")
# site.data.list-items.fruits --> List (of strings, each item is a fruit)
# site.data.list-items.recipes --> List (of dictionaries)

# a string
name: "Assorted foods and things"

# a list of fruits
fruits:
- banana
- orange

# a list of dictionaries
recipes:
- fruits:
  - mango
  vegetables:
  - zucchini
```

Using the above data, we can render out by hand what the HTML snippet from `_includes/list.html` would be:
```html
{%- raw -%}
<h3>
  {{ site.data.list-items.name }} --> Assorted foods and things
</h3>
<ul>
  {% for fruit in site.data.list-items.fruits %} --> Loop through the list [banana, orange]
  <li>
    {{ fruit }} --> banana on the first pass, orange on the second pass
  </li>
  {% endfor %}
</ul>
{% endraw %}
```
which evaluates to
```html
<h3>
  Assorted foods and things
</h3>
<ul>
  <li>
    banana
  </li>
  <li>
    orange
  </li>
</ul>
```

Returning to our page, we have
```markdown
{%- raw -%}
---
layout: default
title: Home Page
tagline: Jekyll builds nice websites
---
# This is the syntax for a Markdown heading which will render out to have h1 tags

<p> Raw html can also be included in Markdown </p>

I'm going to include a dynamically generated list here from `_includes/list.html`:

<h3>
  Assorted foods and things
</h3>
<ul>
  <li>
    banana
  </li>
  <li>
    orange
  </li>
</ul>
{% endraw %}
```

Rendering the Markdown syntax out to HTML we get:
```markdown
{%- raw -%}
---
layout: default
title: Home Page
tagline: Jekyll builds nice websites
---

<h1>
  This is the syntax for a Markdown heading which will render out to have h1 tags
</h1>

<p> Raw html can also be included in Markdown </p>

<p>
  I'm going to include a dynamically generated list here from <code>_includes/list.html</code>:
</p>

<h3>
  Assorted foods and things
</h3>
<ul>
  <li>
    banana
  </li>
  <li>
    orange
  </li>
</ul>
{% endraw %}
```

Finally, this can be pushed through the specified layout `default`, which would be at `_layouts/default.html`. We'll use the following as an example
```html
{%- raw -%}
<!-- file: _layouts/default.html -->
<body>
  <h1>
    {{ site.title }}
  </h1>
  <h2>
    {{ page.title }}
  </h2>
  {% if page.tagline %}
  <h2>
    {{ page.tagline }}
  </h2>
  {% endif %}
  {{ content }}
</body>
{% endraw %}
```

We can see that it uses the Liquid tag `{%- raw -%}{{ site.title }}{% endraw %}` which will pull data from the file `_config.yaml`:
```yaml
# file: _config.yaml
# accessible with site.title
title: My Website
```

Finally, we can see that when the page is pushed through the `default` layout, we get
```html
{%- raw -%}
<body>
  <h1>
    {{ site.title }} --> My Website
  </h1>
  <h2>
    {{ page.title }} --> Home Page
  </h2>
  {% if page.tagline %} --> Check if the page includes tagline in its YAML front matter, and only include the following if it does
  <h2>
    {{ page.tagline }} --> Jekyll builds nice websites
  </h2>
  {% endif %}
  {{ content }} --> The rest of the page
</body>
{% endraw %}
```
which gives us a complete HTML page that can be rendered in a browser:
```html
<body>
  <h1>
    My Website
  </h1>
  <h2>
    Home Page
  </h2>
  <h2>
    Jekyll builds nice websites
  </h2>
  <h1>
    This is the syntax for a Markdown heading which will render out to have h1 tags
  </h1>

  <p> Raw html can also be included in Markdown </p>

  <p>
    I'm going to include a dynamically generated list here from <code>_includes/list.html</code>:
  </p>

  <h3>
    Assorted foods and things
  </h3>
  <ul>
    <li>
      banana
    </li>
    <li>
      orange
    </li>
  </ul>
</body>
```
which looks like:
<h1>
  My Website
</h1>
<h2>
  Home Page
</h2>
<h2>
  Jekyll builds nice websites
</h2>
<h1>
  This is the syntax for a Markdown heading which will render out to have h1 tags
</h1>

<p> Raw html can also be included in Markdown </p>

<p>
  I'm going to include a dynamically generated list here from <code>_includes/list.html</code>:
</p>

<h3>
  Assorted foods and things
</h3>
<ul>
  <li>
    banana
  </li>
  <li>
    orange
  </li>
</ul>