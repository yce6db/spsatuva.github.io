---
layout: docs
title: How Documentation is Built
source-files:
- "_docs/how-docs-are-built.md"
- "_data/docs/docs-nav.yaml"
- "_includes/docs-sidebar.html"
- "_layouts/docs.html"
---

# Documentation page

Each page in the documentation uses the layout `docs`. This means that the content that you write in a new `.md` file within `_docs` while using the YAML front matter
```yaml
---
layout: docs
---
```
will be pushed through the template page contained in `_layouts/docs.html`. There are three main parts of this layout:
1) The page content
```html
{%- raw -%}
<div class="doc-content">
    {% if page.title %}
    <div class="doc-content-heading">
        <h1>{{ page.title }}</h1>
    </div>
    {% endif %}
    {% if page.source-files %}
    <div class="doc-source-files">
        <strong>Source Files: </strong>{% for file in page.source-files %}<a class="doc-source-file-link" href="{{ site.source-url | append: '/' | append: file }}">{{ file }}</a>{% unless forloop.index == page.source-files.size %}, {% endunless %}{% endfor %}
    </div>
    {% endif %}
    {{ content }}
</div>
{% endraw %}
```
2) The navigation bar (see the next section)
```html
{% raw %}
<div class="doc-container">
    {% include docs-sidebar.html %}
    ...
</div>
{% endraw %}
```
3) A short piece of JavaScript code
```js
{%- raw -%}
window.onload = function() {
    var item = document.getElementById(
        {% if page.doc-title %}
        "{{ page.doc-title | remove: ' '}}"
        {% else %}
        "{{ page.title | remove: ' '}}"
        {% endif %}
    );
    var topPos = item.offsetTop;
    var sidenav = document.getElementById('sidenav');
    var divHeight = sidenav.clientHeight;
    /* 20 is the combined padding on the top and bottom of the sidenav div */
    var not_visible = topPos > divHeight - 20;
    if (not_visible) {
        document.getElementById('sidenav').scrollTop = topPos;
    }
};
{% endraw %}
```
The JavaScript code scrolls the documentation navigation bar to keep the currently viewed page in-sight. Note that this code is searching for the link within the page using
```js
{%- raw -%}
var item = document.getElementById(
    {% if page.doc-title %}
    "{{ page.doc-title | remove: ' '}}"
    {% else %}
    "{{ page.title | remove: ' '}}"
    {% endif %}
);
{% endraw %}
```
This looks for an element with HTML ID equal to either the documentation page's `title` or `doc-title` field from the page's YAML front matter. The `doc-title` field should always be included however and should match the corresponding `title` key provided for the page in `_data/docs/docs-nav.yaml`. If `doc-title` or `title` do not match what is found in `_data/docs/docs-nav.yaml`, then the scrolling behavior will be broken as the ID used in the JavaScript code to find the element will not match the element's actual assigned ID (see below for more details).

# Navigation Bar

Within the `docs` layout is the Liquid tag
```liquid
{%- raw -%}
{% include docs-sidebar.html %}
{% endraw %}
```
which copy and pastes the content of `_includes/docs-sidebar.html` into the page before rendering. This allows for the navigation bar on each documentation page to be included automatically. Reference this file and the code comments within to get an understanding of how the navigation sidebar is constructed. In short, it will loop over the data specified within `_data/docs/docs-nav.yaml` to build the navigation bar. Additionally, it is important to understand that each item in the navigation bar has an HTML ID assigned as
```html
{%- raw -%}
<ul class="nav-list">
    {% for doc in nav-items %}
    <li class="nav-item" id="{{ doc.title | remove: ' ' }}">
    ...
    {% endfor %}
</ul>
{% endraw %}
```
The ID assigned is the title specified by the `title` key used for each item in `_data/docs/docs-nav.yaml`.