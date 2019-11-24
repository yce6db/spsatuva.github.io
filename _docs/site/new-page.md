---
layout: docs
title: How to Make a New Page
doc-title: New Page
---

All pages on this site are contained in the folder `_pages/`. To make a new page, you simply create a new Markdown (`.md`) file in the `_pages/` directory with the following YAML Front Matter:

```yaml
layout: page
title: Page Title
# Optional. Only include to mark it as 'false' in which case the page content will not be wrapped in container and page-content divs. For an example, see the events page
continer: false
# Optional. The following will produce (shown here in Markdown) a list of "quick links" at the top of the page below the banner. It will be formatted as:
# **Quick Links**: [My Title 1](/my/url/1), [My Title 2](/my/url/2)
quick-links:
- title: My Title 1
  url: /my/url/1
- title: My Title 2
  url: /my/url/2
```

All pages are pushed through the page template, which can be found in `_layouts/page.html`. You can modify the page layout to modify how all pages appear on this site. You can add new YAML Front Matter variables to pages and access them in the page layout using `page.variable-name` (as is done using the `container` variable).

The directory structure of `_pages/` determines the URLs that each pages has. This is set in `_config.yml` where under `collections`, `pages` the `permalink` variable is set to `/:path/`. For example, if you have a file `_pages/my-dir/my-dir-2/my-page.md`, it will have the URL `{{ site.url }}{{ site.baseurl }}/my-dir/my-dir-2/my-page/` associated with it. This behavior can be referenced in [these Jekyll docs](https://jekyllrb.com/docs/collections/#step3).