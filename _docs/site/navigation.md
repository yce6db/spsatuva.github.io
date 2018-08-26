---
layout: docs
title: Navigation
---

# Site header creation

Navigation of the main site is handled by the file `_data/navigation.yml`, which has the structure:

```yaml
header:
    - name: Item 1
      link: /path/to/item1
    - name: Item 2
      link: /path/to/item2
    - name: Dropdown 1
      sublinks:
        - name: Dropdown Item 1
          link: /path/to/dropdownitem1
        - name: Dropdown Item 2
          link: /path/to/dropdownitem2
```

The main navigation structure can be accessed with the liquid variable `site.data.navigation.header`, which is a list containing each of the links to be displayed in the header of each page of this site. This data is used in the file `_includes/header.html`, where a list like the one shown above is iterated over to generate the header on the top of the site. If you take a look at this file you will see something like:

```liquid
{% raw %}{% for item in site.data.nagivation.header %}
    <!-- Code to create header item -->
    {% if item.sublinks %}
        {% for subitem in item.sublinks %}
        <!-- Code to create a header item that has a dropdown menu -->
        {% endfor %}
    {% else %}
        <!-- Code to create a header item without a dropdown menu -->
    {% endif %}
{% endfor %}{% endraw %}
```

### Adding a header item

To add a new item to the header, you simply edit `_data/navigation.yml` to add an item to the `header` list that has a `name` and `link` attribute. To add an item that is a dropdown menu, you simply add an item with a `name` and a `sublinks` attribute, where `sublinks` is another list with header items that both have a `name` and `link` attribute. Header items with a dropdown menu will be generated with an arrow next to them that indicates that this item is a dropdown menu.