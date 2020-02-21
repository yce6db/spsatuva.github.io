---
layout: docs
title: Courses Page
doc-title: Courses
source-files:
- "_pages/resources/courses.md"
---

This page makes extensive use of our custom collabsible elements. It would be helpful to make yourself familiar with them [here](/docs/tutorials/collapsible-elements/).

To add a new course, follow the structure of the HTML on that page (copy and paste one of them). For example, this is one of them:
```html
<div class="collapse-list-wrapper4phys1710"
     id="wrapper-1710">
    <div class="collapse-list-heading collapsed"
        data-toggle="collapse" 
        data-target="#1710" 
        aria-controls="1710" 
        aria-expanded="false">
        <i class="arrow h2arrow"></i>
        <h2> Intro Physics 1: PHYS 1710 </h2>
        
  </div>
    <div class="collapse-list-target collapse"
        id="1710" 
        aria-labelledby="1710" 
        data-parent="#wrapper-1710">
        <p>     
        This is often the first physics class someone will take when they begin the physics major at UVA. It is a calculus based introduction that covers the following topics: kinematics, mechanics, fluid dynamics, thermodynamics, and simple harmonic motion. This class is 5 credit course (4 credit lecture) and includes a 1 credit discussion session. 
        <br>
        <br>
        The standard text is <a href="https://www.amazon.com/MasteringPhysics-Student-Physics-Scientists-Engineers/dp/0131992260"> Physics for Scientists and Engineers, Giancoli, 4th edtion</a>
        <br>
        <br>
        You can expect to cover chapters 1-21 
        <br>
        <br>
        Prerequisite: Calculus 1 (MATH 1310) 
        </p>
  </div>
</div>
```
The course title is captured in the `<h2>` tags, "Intro Phyics I: PHYS 1910", and the content relevant to that course is captured in the `<div>` with `id="1710"`. You could copy-paste the above, and change the course title and course content for the new course you'd like to include.