---
layout: docs
title: How to Edit CSS Styling
doc-title: CSS
---

To brush up on CSS syntax, see [here](https://www.w3schools.com/css/).

# How the site CSS works

Jekyll uses a special language called [SASS](https://sass-lang.com/) which builds upon standard CSS to build a single CSS style sheet that this whole site uses. SASS allows for users to define variables and include CSS from various files into one.

The main CSS file this site uses is generated from `assets/css/main.scss` which Jekyll then compiles to `/assets/css/main.css`. This file contains `@import` statements that pull SASS from the `_sass/` folder. For example, the `main.scss` file currently looks like

```scss
---
---

@import "vendor/bootstrap/bootstrap";

@import "jekyll-sleek";

@import "user-style";
```

which pulls in the SASS stored in `_sass/vendor/bootstrap/bootstrap.scss`, `_sass/jekyll-sleek.scss`, and `_sass/user-style.scss`. Each file contains more `@import` statements, but we can think of the first file as containing SASS and CSS that is crucial for [Bootstrap](http://getbootstrap.com/) elements to work, the second file as containing all of the SASS and CSS to make the [Sleek](https://github.com/janczizikow/sleek) theme to work, and the third file as containing everything needed to make what we built upon the sleek theme work. All of the CSS from these three separate places gets compiled into `main.scss` and rendered out into `/assets/css/main.css` which the site uses as the stylesheet for each page.

# Adding your own CSS

To add your own CSS, make a new file in `_sass/style`, for example `_sass/style/my-new-css.scss`. Then, update the file `_sass/user-style.scss` to `@import` this new CSS you made, by adding the line
```scss
@import "style/my-new-css"
```
to the file. This should add your CSS to the stylesheet!

Unfortunately, there's no way to check if the classes and IDs you've used conflict with anything else we've written or already exists in the Boostrap or Sleek CSS. This means that you should be careful to make your class names unique and hard to replicate elsewhere on the site.

# Writing responsive CSS

The CSS written for this site is *responsive*, meaning we use `@media` queries in the CSS to change how the site looks depending on what device is being used to look at it. In particular, we try to make the site look nice on mobile.

In order to make writing responsive CSS easier, when creating your own CSS you should copy the file `_sass/style/template.scss` before writing your own CSS. This template has predefined media queries that make it easy to make your new CSS responsive.

To see what the definitions of the breakpoints (`$sm`, `$md`, `$lg`, and `$xl`) used in this site, see `_sass/abstracts/_variables.scss`.

# Where the CSS is located in HTML

The CSS is loaded in the `head` of each page. Examine `_includes/head.html` to see how the CSS is loaded in.
