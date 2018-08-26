---
layout: docs
title: How to Make a New Event Post
doc-title: New Event
---

Events can be recorded in what Jekyll calls "posts". Each post generally has some text, one or more images that represent the event, and perhaps links to a few other posts/pages/external sites. Each post is written in Markdown and is contained in a `.md` file in the `_posts/` folder. Each post has the following YAML Front Matter:

```yaml
---
# Required
layout: post
# Required
title: "Post Title"
# Optional. Allows categorizing all of the posts on the site (see {{ site.url }}{{ site.baseurl }}/categories/).
categories: [Category One, Category Two, ...]
# Optional. Assumed path: /assets/img/posts/my-featured-img.jpg
featured-img: my-featured-img.jpg
---
```

Each post file must contain a timestamp in it's file name, leading to the file name format: `yyyy-mm-dd-title-with-hyphens.md` for all posts. This timestamp determines the URL of each post, in the format `/yyyy/mm/dd/title-with-hyphens/`. For example, [this]({{ "/2018/04/14/sps-holds-elections/" | absolute_url }}) post has the file name `2018-04-14-sps-holds-elections.md` and URL `{{ "/2018/04/14/sps-holds-elections/" | absolute_url }}`.

A banner image (what appears at the top of the post page) and card image can be specified with the `featured-img` variable in the front matter. Simply provide the file name of the image you would like to use and the site will automatically place it as the banner image for the post and use it for a card image on the [events page](/events/). See [the docs](/docs/site/images/) for how to integrate images into this site.

You can optionally provide a few categories for the event. For example, 'Speaker' or 'National SPS'. These categories will appear over the card image on the [events page](/events/) and will appear over the banner image on the post page. This allows the post to be [categorized](/categories/) easily on the site.