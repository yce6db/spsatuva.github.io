---
layout: docs
title: Managing the Exec Page
doc-title: Exec Page
---

The [About (or Exec) Page](/about/) is managed almost entirely by editing the file `_data/exec-board.yml`, which has the following structure:

```yaml
# The current academic year with a hyphen in between
current-year: 2018 - 2019

# A list of ALL of the SPS exec members
members:
    # their name
    - name: Member 1
    # their email
      email: Member1@virginia.edu
    # An image of them found in /assets/img/exec/
    # If no extension is included, .jpg is assumed
      img: Member_1.png
    # their chosen description
      description:
        # paragraphs are separated into a list
        - Content of paragraph 1
        - Content of paragraph 2
    # Optional. Their homepage
      homepage: www.MemberOne.com
    # continue this format for each member
    - name:
    ...

# A list of all of the members on each of the executive boards for each academic year
exec-boards:
    # The academic year that this executive board was active
    - year: 2018 - 2019
      # A list of each of the members on the board
      board:
      # The member's name. This is matched to the list 'members' above
      - name: Member 1
      # The member's role in the club
        role: President
    # Continue this format for each year
    - year: 
    ...
```

When a new exec board is elected in, add all of their information to the `members` list and add a new `board` with their roles to `exec-boards`. All of their headshots should be stored in `_img/exec/`. Running `img-resize.py` will resize and move them to `assets/img/exec` which is the assumed location of their images (see the [adding images documentation](/docs/site/images/)).