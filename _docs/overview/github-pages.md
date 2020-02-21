---
layout: docs
title: Hosting on GitHub Pages
doc-title: GitHub Pages
---

This website is hosted and built on GitHub's servers using their free [GitHub Pages](https://pages.github.com/) service. This website is hosted under the GitHub organization [spsatuva](https://github.com/). GitHub publishes our website at [https://spsatuva.github.io](https://spsatuva.github.io). To learn more about the service, see their [service information](https://pages.github.com/) and [help pages](https://help.github.com/en/github/working-with-github-pages). To see and manage the GitHub Pages settings for our website navigate to this [website's repository settings](https://github.com/spsatuva/spsatuva.github.io/settings) and scroll to the "GitHub Pages" section.

# Why GitHub pages?

GitHub pages makes it free to generate our website, host our website, provides us with a reasonable URL, and additionally provides a space to work collaboratively on the website. There's a lot of value there for the price. It also makes our website more accessible and easily maintained than locking it away on the physics department / UVA servers or by using the limited Wordpress options provided by the university.

# How does GitHub pages work?

On the backend, GitHub uses the [Jekyll](https://jekyllrb.com/) software to generate a set of HTML, CSS, and JavaScript files using what is contained in the repository [https://github.com/spsatuva/spsatuva.github.io](https://github.com/spsatuva/spsatuva.github.io) that are then served up by GitHub's web servers when someone accesses the URL [https://spsatuva.github.io](https://spsatuva.github.io).

At minimum, we can place raw HTML, CSS, and JavaScript files into the repository. For example, if the repository contents were simply the following three files
```
index.html
style.css
code.js
```
then the HTML contained in `index.html` would be published and available at `https://spsatuva.github.io/index.html` (or equivalently at `https://spsatuva.github.io/`). Additionally, the CSS and JavaScript would be available at `https://spsatuva.github.io/style.css` and `https://spsatuva.github.io/code.js`. Finally, the `index.html` file can load and use these CSS and JavaScript resources using just the structure of the repository. For example
```html
# file index.html
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <script src="code.js"></script>
</body>
```
would be enough for these resources to be loaded when the page `https://spsatuva.github.io/index.html` is accessed.

In our case, we take full advantage of the Jekyll software to go beyond simply serving up HTML, CSS, and JavaScript for our website. See the next section for details on how Jekyll works.