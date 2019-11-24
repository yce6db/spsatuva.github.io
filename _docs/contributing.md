---
layout: docs
title: Contributing
---

Documentation is stored in the `_docs/` folder of [this site's source](https://github.com/spsatuva/spsatuva.github.io/). Adding new documentation requires two steps: 1) creating the new documentation page, and 2) adding it to the navigation bar present on any documentation page.

## Step 1

To create new documentation, simply make a new `.md` file in the `_docs/` folder of this site with the following YAML Front Matter:
```yaml
---
# file: my-new-page.md
# see _layouts/docs.html
layout: docs
# The title that appears at the top of the documentation page
title: Title of Page
---
```
To continue to step (2), you will need to note the URL that your new documentation will be located at. This URL will depend on where in the `_docs/` folder you've created the new page. For example, if this page is created in the folder `my-folder` at the location `_docs/my-folder/my-new-page.md` then this is will generate a URL on the site of `/docs/my-folder/my-new-page/index.html` or equivalently `/docs/my-folder/my-new-page/`. You will use this URL to create an entry in the nagivation bar that points to your new page in step (2).

## Step 2

Note the URL of the documentation you've created. Navigate to the file `_data/docs/docs-nav.yaml`. This file specifies the layout of the navigation bar present on the left of each documentation page. This file has the structure
```yaml
categories:
# a list of documentation categories, each of which has a header and a set of items that are navigable under that category
- header: "Header Name"
  nav-items:
  # each navigable item has a title and url to point to
  - title: "My New Page"
    # each url will have /docs prepended to it, so you don't need to worry about having it
    url: "/my-folder/my-new-page/"
```

If you are creating documentation under an existing category, e.g. "Pages", then you would add a new item to the `nav-items` list under the section with `header` equal to `Pages`. For example:
```yaml
categories:
...
- header: "Pages"
  nav-items:
  ...
  - title: "My New Page"
    url: "/my-folder/my-new-page/"
```
The navigation bar layout will respect the ordering of the `nav-items` list, so if you want your new page to appear first under the "PAGES" heading in the navigation bar, then place it first in the `nav-items` list.

If you are creating documentation under a new cateogry, e.g. "My New Category", then you would create a new item under the `sections` list that has a `header` field equal to "My New Category". For example:
```yaml
categories:
...
- header: "My New Category"
  nav-items:
  - title: "My New Page"
    url: "/my-folder/my-new-page/"
```
Similarly to the `nav-items` list, the navigation bar layout will respect the order of the `categories` list. If you'd like your new category and documentation to appear first in the list in the navigation bar, you would place it at the top of the `categories` list.