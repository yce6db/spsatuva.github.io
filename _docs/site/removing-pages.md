---
layout: docs
title: Removing Pages
doc-title: Removing Pages
---

For any page on the site, you can set `published: false` in its YAML front matter to prevent the page from being rendered. This will exclude any post in `_posts/` and `_pages` from being included in `site.posts` and `site.pages`. This allows your to archive pages on this site without removing them. If you do remove a page, ensure that you remove links to it elsewhere on this website, for example in navigation bars.