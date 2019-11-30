---
layout: docs
title: Managing the Research Page
doc-title: Research
source-files:
    - "_pages/research.md"
    - "_data/research-opportunities.yml"
---

The file defining the research information page is `_pages/research.md`. Here, you can find and edit any of the information appearing on the page. A critical component of this is the *research opportunities* section, defined with the code:

```html
{% raw %}
<div class="project_list" id="project_list">
    {% for project in site.data.research-opportunities.project-list %}
    <a href="#" class="project" data-toggle="collapse" data-target="#{{ project.short-name }}" aria-expanded="false" aria-controls="{{ project.short-name }}">
        {{ project.name }} - {{ project.title }}
    </a>
    <div class="project_container collapse" id="{{ project.short-name }}" aria-labelledby="{{ project.short-name }}">
        <iframe style="width:100%;height:500px" src="{{ project.url }}?embeded=true"></iframe>
    </div>
    {% endfor %}
</div>
{% endraw %}
```

This snippet looks for a list called `project-list` in the file `_data/research-opportunities.yml`, and for every entry in the list creates

1. A collapsible link (`<a>`) with the short name of the project which, when clicked, opens...
2. A linked document (`<iframe>`) containing the full description of the project

These full documents are created from a Google Form which should be sent out to all of the faculty semi-regularly by SPS. This form is located in the SPS Google Drive, at `Drive > Undergraduate Research > New Research Opportunities > Undergraduate Research Projects`.

{% include lazy-image.html image="formsSnip.png" base-path="docs" image-class="doc-image" %}


In the current way we handle this page, the site is *not* automatically updated as professors respond. As responses come in, they populate a Google Sheet, `Undergraduate Research Projects (Responses)`, located at the same place in the Drive. If you open up this sheet, you should be able to see the responses from the professors, one per row.

{% include lazy-image.html image="sheetSnip.png" base-path="docs" image-class="doc-image" %}

To turn this information into the nicely laid out documents you see on the site, we use an add-on to Google Sheets called [Autocrat](https://gsuite.google.com/marketplace/app/autocrat/539341275670) to automate the process. To use this, navigate `Add-ons > Autocrat > Open`, and you should see a window like below.

{% include lazy-image.html image="runAutocrat.png" base-path="docs" image-class="doc-image" %}

This "New Research Summary" job takes our pre-defined Google Docs template, `Undergraduate Research Projects Template`, and fills it out once per populated row in the Sheet. To see the details of what information gets stuffed where, you can either compare the template to a complete document or click on "Edit" to see what the job is doing in detail. To run the job, just click the play button! Documents will be automatically generated for each professor, and (hopefully) placed in `Drive > Undergraduate Research Projects`. The exact output directory is known to be a bit finicky. If you can't find your generated documents, then in the Sheet there should be a column with links to the document. If for some reason they get generated elsewhere, please move them to `Drive > Undergraduate Research Projects` to keep things tidy for yourself and future Webmasters.

If a document has already previously been published to the site, this generation process should not affect anything. If one of these documents is new, there are two final steps needed to get it to appear on the site. First, open up the new Google Doc you'd like to publish. Click `File > Publish to the Web`. Click the "Publish" button, which will generate a public link for the document.

{% include lazy-image.html image="publishSnip.png" base-path="docs" image-class="doc-image" %}

Copy this link, and open `_data/research-opportunities.yml`. Add a new entry to the `project-list` following the structure of the others:

```yaml
project-list:
  - name: <Professor's Name>
    short-name: <Short Name Used For Internals>
    title: <Project Title>
    url: <Link You Just Copied>
  ... other projects ...
```

Save, test the site locally, then commit, push, and *Voilà* a new project is on the site.