---
layout: docs
title: How to Edit Site JavaScript
doc-title: JavaScript
---

To brush up on JavaScript, see [here](https://www.w3schools.com/js/).

# How the site JavaScript works

Most of the JavaScript crucial to this site come pre-bundled with the Sleek theme and is stored in `assets/js/bundle.js`. JavaScript that we made on top of that is found in `assets/js/user.bundle.js`.

The JavaScript found in `user.bundle.js` is a bundled and [minified](https://en.wikipedia.org/wiki/Minification_(programming)) version of the individual scripts found in the `_js/` folder. The Python script found in the root directory, `js-min.py` takes these individual scripts, runs them through the Python package [slimit](https://github.com/rspivak/slimit) for minification and then spits it all out into `assets/js/user.bundle.js`.

# Adding your own JavaScript

To add your own JavaScript, create a new JavaScript file in the `_js/` folder. For example, you might create the file `_js/my-javascript.js`. You can add any JavaScript you'd like to this file, as long as the functions and global variables you declare do no conflict with any found in the other files in the `_js/` folder.

Once you are ready to test your new JavaScript, simply open a new command line shell, change directory to the website folder, and run the Python program using
```sh
$ python js-min.py
```

Your JavaScript should be succesfully bundled into `assets/js/user.bundle.js`.

# Where the JavaScript is located in HTML

The JavaScript is loaded in the `footer` of the site (see `_includes/footer.html`). This is because when your browser hits a line in the page HTML telling it to load a JavaScript file, it stops loading anything below it until the file loads. Putting the JavaScript load commands in the `footer` of the site allows the rest of the site to continue loadin while the JavaScript loads since the `footer` is at the bottom of the page.