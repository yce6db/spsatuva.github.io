---
layout: docs
title: Events Page
doc-title: Events
source-files:
- "_pages/events.md"
- "_includes/card.html"
- "_posts/"
---

The events page is constructed from the file `_pages/events.md`. This file contains the following HTML:

```html
{%- raw -%}
<section class="blog">
<div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
    {% for post in site.posts %}
        {% include card.html %}
    {% endfor %}
    </div>
</div>
</section>
{% endraw %}
```

We can see this uses Liquid code (a for-loop and include statemment) to generate the full events page from the bare-bones HTML above. For each item in the collection `site.posts`, we will include an HTML snipped from `_includes/card.html`. The collection `site.posts` is generated from the contents of the `_posts/` directory in this site's source code. See [here](/docs/site/new-event/) for more information about making new posts / events.

Each post in `_posts/` will be rendered into a "card" on this events page. To change the behavior or look of these cards, edit the source at `_includes/card.html`. Within that HTML snippet, you will see references to the Liquid object `post`, such as `post.categories` or `post.featured-img`. These grab information from the YAML front matter of the individual post being included. You can access other values from each post's front matter by using `post.your_variable_name` and including `your_variable_name: you_variable_value` in a new post front matter. If you make such a change, ensure that you have a check for if this variable is not-defined in `_includes/card.html`, as there are dozens of posts already made that won't have your new variable.