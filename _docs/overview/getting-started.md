---
layout: docs
title: Getting Started
doc-title: Getting Started
---

The standing webmaster should get each entering webmaster prepped and ready to manage the website by walking through the steps below.

# Editing files on GitHub

You can edit all of the files on this website from your web browser. Navigate to our site GitHub repository at [https://github.com/spsatuva/spsatuva.github.io](https://github.com/spsatuva/spsatuva.github.io) and click on a file, either at the top-level or within a sub-directory:

{% include lazy-image.html image="githubSnip.png" base-path="docs" image-class="doc-image" %}

Next for that file you will want to click on the pencil icon to edit that file in the browser:

{% include lazy-image.html image="githubConfigSnip.png" base-path="docs" image-class="doc-image" %}

You can edit the text freely, and then when you are sure you are finished and want to "save" your work, you will scroll to the bottom of the page and commit your changes. You should enter a descriptive commit message saying what changes you made and then hit the big green button to commit your work. 

{% include lazy-image.html image="githubCommitSnip.png" base-path="docs" image-class="doc-image" %}

Each commit you make in this way will trigger a build of the website on GitHub's end. If there are no errors, you will see your changes on the live site at [https://spsatuva.github.io](https://spsatuva.github.io). If you have an error (usually a problem with Liquid code), then the site won't build successfully and you won't see your changes. The admins of the page will get an email saying that the page build failed and you can review the page build by navigating to the commits page of our repository at [https://github.com/spsatuva/spsatuva.github.io/commits/master](https://github.com/spsatuva/spsatuva.github.io/commits/master). Commits that triggered a successful page build will have a green check icon next to them. Commits that triggered a failed page build will have a red cross next to them. You can click on the red cross (or green check) and click on "Details" to find further information on why the build failed and what caused it.

{% include lazy-image.html image="githubFailDetailsSnip.png" base-path="docs" image-class="doc-image" %}

# Editing Locally

Editting locally is much preferred to editing files individually on the browser. Editting locally allows you to edit multiple files at the same time without triggering a re-build of the live website and gives you immediate feedback on whether you have an error in your code (it happens a lot).

You will want to follow a guide on getting Jekyll up and running on your system. You can find instructions for any system you are running on (Windows, Mac OS X, Linux) here: [https://jekyllrb.com/docs/installation/](https://jekyllrb.com/docs/installation/).

Additionally you will want to install git, either the [desktop version](https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop) or the [command line version](https://gist.github.com/derhuerst/1b15ff4652a867391f03). If you are not familliar with Git or using the command line, then the desktop version is recommended.

You will want to clone our repository, make your changes locally, commit those changes, and finally push them back up to the master branch on GitHub. Each push to the master branch on GitHub will trigger a build of the website and republish our website if the build was successful.

You can preview your changes before pushing them by running Jekyll locally on your machine. For example, you might do the following in a bash shell
```bash
# clone our repository (only do this once)
git clone https://github.com/spsatuva/spsatuva.github.io.git
cd spsatuva.github.io
# run this once to install all of the required Ruby gems located in the files Gemfile and jekyll-sleek.gemspec
bundle install
# start Jekyll with an HTTP server at localhost:4000
bundle exec jekyll serve
```
Navigate to [localhost:4000](localhost:4000) in any web browser on your computer and you will see our website! By previewing the site as you make changes, you can ensure that the live version at [https://spsatuva.github.io](https://spsatuva.github.io) remains a stable and error-free version of the website while you make small or large changes to it locally. You can also see any page build warnings or errors by looking at the logs in the command line outputted from the command `bundle exec jekyll serve`.

Note: If you make changes to `_config.yml`, you will need to stop Jekyll and restart it. In the command line, you can interrupt it with `CTRL-C` on your keyboard and then start it again with the same command.

Once you've made all of your changes and you are ready for those changes to be pushed to the live site, you can use `git` to push your changes to GitHub:
```bash
# see a list of the files you changed
git status
# add each file who's changes you want to be permanent. If you want to add all of them, use git add -A
git add <filename>
# commit the changes you made with a descriptive commit message
git commit -m "Made a whole bunch of changes"
# push your changes to GitHub. This will trigger a page build with your changes
git push
```