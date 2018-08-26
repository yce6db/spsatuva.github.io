---
layout: docs
title: Website Documentation
doc-title: Home
permalink: /docs/index
---

Here you can find documentation for how to modify and maintain this website. See the navigation bar on the left for links to the documentation.

## How to contribute to the documentation

To create new documentation, simply make a new `.md` file in the `_docs/` folder of this site with the following YAML Front Matter:
```yaml
---
layout: docs
# The title that appears at the top of the documentation page
title: Title of Page
# The page title that appears in the documentation sidebar
doc-title: Title in Sidebar
---
```
To create documentation under a category different from what's listed to the left, simply make a new folder in `_docs/` that is has the same name as the new category name. For example, if you have a documentation file in `_docs/new-category/my-docs.md` which has `doc-title: my-docs-title` in its YAML Front Matter, then the sidebar on the left will automatically be updated to include a categroy `NEW CATEGORY` with a single link below it called `my-docs-title`, styled as shown below:
{% include sidebar.html nav=site.data.docs.sidebar-example.new-category in-line=true %}
