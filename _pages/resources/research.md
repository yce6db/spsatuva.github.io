---
layout: page
title: Research
featured-img: bubble_chamber.jpg
---

Performing original independent research in physics is an integral part of being a physicist, and it's often an enjoyable, enlightening experience. Plus, you can likely get paid to do physics research! Performing research is often a soft requirement when applying to a graduate program in physics. You will likely find yourself woefully behind your peers if applying to graudate school with little to no research experience. And if you're not in physics for the long haul (graduate school), performing original research can still be beneficial to you, as it acts as meaningful job experience in an *independent* and highly technical environment. AKA it makes you look smart and helps your resume stand out.

___

# What is physics research?

Physicists are trying to uncover the truth about our reality by probing it slowly and carefuly. This slow and careful probing is what we call "physics research". If you become a researcher as an undergraduate, you will often work together with a professor in our department to answer a specific question within the professor's field of study. You might find yourself in a lab, building novel devices to get an experiment off the ground (sometimes literally). You might find yourself at a computer, working with experimental data to extract valuable information from it about an experiment's ability to find the answer you seek. You might find yourself with pen and paper, working on a nasty integral that holds the key to a particular system's behavior. Research is different for each question being asked and for each person asking it, but often the process of asking questions and looking for answers is a rewarding, gratifying experience that each of our physics professors engage with on the day to day. The good news is that as a physics major, you too can perform physics research.

___

# Your first research experience

Getting your first research experience can be difficult, especially as a first year student. However, SPS has set up several resources to help you land your first research gig.

### PHYS 1910

PHYS 1910 is a student run, 1 credit seminar course held during the Fall which is intended to help students get a grasp on what research is currently being performed in the physics departent. The course is essentially a series of speakers, usually a professor in the physics department, who will speak to you about their research and the opportunities they have for **you** to join them. Enrolling in PHYS 1910 will help you meet all of the undergraduate employing physics professors in the department and will help break the ice in introducing yourself.

### ASTR 1610

ASTR 1610 is a mirror course for PHYS 1910 in the astronomy department. It is taught every Spring, whereas PHYS 1910 is taught in the Fall. So take both if you are interested in both physics and astronomy research, or are interested in where they overlap at all!

### PHYS 3993 / PHYS 3995 / ASTR 4993 / ASTR 4998

There are also several higher level courses that afford you the opporuntity to perform research for *credit* instead of pay or as a volunteer. These courses generally require a written report of your work at the end of the semester and are usually taken for a grade, and are often taken more seriously than research done for pay or as a volunteer. PHYS 3993 is an independent study course, which allows you to pursue an area of study of your own design with a professor. This is a good course to take if you're interested in studying a specific field of physics to learn something new, while not necessarily performing original research in that field. PHYS 3995 is the formalized physics research course, and is generally taken by 3rd and 4th years; however, there is no restriction on 1st or 2nd years taking this course. ASTR 4998 is a the astronomy senior thesis course, and can be seen as a more serious version of PHYS 3995. While both courses result in a written report on the work at the end of each semester, the end result of this course is an actual senior thesis which is given to the UVA library for [publication](https://www.library.virginia.edu/libra/etds/). ASTR 4998 is also usually taken for an entire academic year instead of a single year. Finally, ASTR 4993, entitled "Tutorial", is a course meant to introduce research to astronomy majors. This course is usually taken by all astrophysics majors.

___

# Who to ask?

You can find all of the professors in the physics and astronomy department on their respective websites. As a UVA student, you also have access to the nearby Charlottesvile portion of the National Radio Astronomy Observatory (NRAO), and you are able to work with several of the scientists who work there as well. Feel free to send any of them an email. They're all friendly people!
- [Physics Department](http://www.phys.virginia.edu/People/people-list.asp?CLASS=Faculty&SUBCLASS=Faculty)
- [Astronomy Department](http://astronomy.as.virginia.edu/people)
- [National Radio Astronomy Observatory](http://astronomy.as.virginia.edu/people/visitors)

Also feel free to seek collaboration outside of the physics / astronomy departments. Modern physics and astronomy, both experimental and theoretical has a lot of cross-over with the fields of [mathematics](http://math.virginia.edu) , [computer science](http://cs.virginia.edu), [chemistry](http://chemistry.as.virginia.edu/), and [electrical engineering](https://engineering.virginia.edu/departments/electrical-and-computer-engineering). Feel free to take classes and seek research opporuntities with professors in those departments as well.

### List of professors looking for students

Here you will find a list of professors who have specific research projects to advertise to undergraduate students. Simply click on any projects that sound interesting to you to find out more about the project and to find out information on how to contact them.

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
___

# Research funding

Generally, professors will have funding to pay undergraduates to work with them. However, grant money is often spread thin, so sometimes you have to hunt for your own funding to pay for yourself for either the semester or the summer. Below are links to several possible sources of funding for yourself while conducting research, which you should bring to your professor to discuss applying for.
- [Mitchell Summer Scholarship](http://www.phys.virginia.edu/Announcements/Mitchell/): This award is the most applicable to you. It is a $5,000 award to pay for you to undergo a summer research project with a professor in the physics department. If you are interested in this, approach a professor and let them know you would like to work with them and would like to apply for the Mitchell Scholarship with their assistance. The award is available to all rising 3rd and 4th years who are DECLARED physics majors (it is one of the benefits of declaring your major).
- [Medical Physics Scholarship](http://www.phys.virginia.edu/Announcements/MedicalPhysics/): This $5,000 award provides funding for you to work with a professor on a medical physics project. It is similar to the Mitchell, except that research topics are restricted to Medical Physics.
- [UVA Research Grants](https://undergraduateresearch.virginia.edu/our-opportunities/grants): A short-list of grants awarded to support research projects at UVA
- [UVA Research Opportunities](https://undergraduateresearch.virginia.edu/our-opportunities/research-opportunities): A complete list of research opportunities and grants funded by UVA. Notable mentions are: College Council Scholars Award, Double Hoo Research Grant, Harrison Undergraduate Research Awards, Minerva Award, and Small Research and Travel Grants; however, there are many more opportunities available to you.

___

# REUs

You can also perform physics research outside of UVA by pursuing admittance to a Reseach Experience for Undergraduates (REU). REUs are often funded by the National Science Foundation (NSF), however some institutions around the globe offer REU experiences without funding from the NSF. Getting an REU is an awesome way to gain meaningful research experience, and it's also is an incredible opportunity to travel somewhere new! There are REUs offered by universities across the nation and by institutions across the globe!

SPS has compiled a list of resources to help you apply for REUs. Below you will find information about several REUs that are available to you along with reflections from UVA students about their REU experiences.

Listing of REU opportunitites that UVA students have been succesful in applying to:
- [Complete list of current NSF REUs](https://www.nsf.gov/crssprgm/reu/reu_search.jsp)
- [MIT Summer Research Program](https://odge.mit.edu/undergraduate/msrp/)
- [Caltech Summer Undergraduate Research Fellowships](http://sfp.caltech.edu/programs/surf) (SURF)
    - [Caltech LIGO SURF](https://labcit.ligo.caltech.edu/LIGO_web/students/SURF/)
- [National Radio Astronomy Observatory](https://science.nrao.edu/opportunities/student-programs/summerstudents)
- [Space Telescope Science Institute](http://www.stsci.edu/institute/smo/students)
- [Department of Energy Science Undergraduate Laboratory Internships](https://science.energy.gov/wdts/suli/) (SULI)

### REU Reflections

Reflections about REU experiences that UVA students have had can be found below. Each reflection contains information about the REU they participated in, including tips for applying, stipend amount, and perks of the program.

<div class="project_list" id="project_list">
    {% for reflection in site.data.research-reflections.reflection-list %}
    <a href="#" class="project" data-toggle="collapse" data-target="#{{ reflection.short-name }}" aria-expanded="false" aria-controls="{{ reflection.short-name }}">
        {{ reflection.location }} - {{ reflection.name }} - {{ reflection.time }}
    </a>
    <div class="project_container collapse" id="{{ reflection.short-name }}" aria-labelledby="{{ project.short-name }}">
        <iframe style="width:100%;height:500px" src="{{ reflection.url }}?embeded=true"></iframe>
    </div>
    {% endfor %}
</div>

___

# Present and Publish

So you've finished a research project, or you are still working on it but have some interesting findings. Now what do you do? You share your results with the rest of the physics community! Physicists share their results in one of two ways: either publishing a paper or presenting their results at a scientific meeting. In either case, you should discuss with your advisor pursuing either of these options as often as possible.

Presenting your research at a scientific meeting allows you to travel to another location (usually nice places), meet others in the physics community (often famous people and nobel prize winners), and share your results with your peers. Presenting your research is also a **core** part of being a scientist. Many physicists spend a large portion of their time writing papers for their research group and presenting work on behalf of the collaborations they work with, so if you plan on sticking around, you should get used to presenting your work. It is also a great thing to have on your CV / resume when appling for graduate programs, as presenting your work is a sign that you've *produced results*, which is a sign of an effective researcher and physicist.

### Posters and Talks

If you are an undergraduate, and especially if you are coming out of your first research experience, you will likely be presenting a *poster* on your research, which is an informational document that you present to others at a poster session at a conference. Posters are relatively straightforward to make, and it's best to follow a few general guidelines (you can find plenty of information on this with Google. A simple search revealed these guides [here](https://guides.nyu.edu/posters), [here](https://www.youtube.com/watch?v=AwMFhyH7_5g), and [here](https://hsp.berkeley.edu/sites/default/files/ScientificPosters.pdf)). First, use a large font that will be visible from far away. Second, limit the amount of text you use. Replace it all with pretty pictures instead! Third, tailor you poster content and spoken explanations to be accessbile to a general audience. Likely no one other than you and your advisor will understand the details of your work so keep it simple. These are just general guidelines and what the poster looks like is up to you, but just make something pretty and accessible and people will enjoy reading it. 

The advice for making a good talk is generally similar to making a poster. Make your slides easily readable and dynamic. Use lots of pictures to get your point across and limit how much text you use. And keep your talk short, simple, and accessible. Finally, and most importantly: **DO NOT GO OVER YOUR ALLOTTED TIME**. Practice your talk to ensure that you can get through it in the presentation time you are given with room at the end for questions.

You can find examples of posters from past SPS members below to act as a guide when making your own poster or talk.

{% assign path = "/assets/pdf/research/" %}

#### Posters 
- [Poster presented at AAS]({{ path | append: "Poster_1.pdf" }})
- [Poster presented at APS]({{ path | append: "Poster_2.pdf" }})
- [Poster 3]({{ path | append: "Poster_3.pdf" }})

#### Talks
- [A collection of informal research talks given at SPS by students]({{ path | append: "SPS_Research_Talks.pdf" }})
- [Talk 2]({{ path | append: "talk_2.pdf" }})
- [Talk 3]({{ path | append: "talk_3.pdf" }})

### Meetings you should attend

What follows are several of the major meetings that you should try to attend, based on your research area. Of course, all meetings are open 
- [American Physical Society (APS) April Meeting](https://www.aps.org/meetings/april/): This meeting is generally for those interested in: high energy physics, nuclear physics, astrophysics, and gravitational physics.
- [American Physical Society (APS) March Meeting](https://www.aps.org/meetings/march/): This meeting is generally for those interested in: atomic, molecular, and optical physics, condensed matter physics, plasma physics, and biophysics
- [Southeast Section of the American Physical Society (SESAPS)](https://www.aps.org/units/sesaps/meetings/): This meeting is hosted in the South Eastern part of the United States, so it is likely to be close by. If it is hosted in 
Charlottesville, you should definitely plan to both attend and volunteer at the conference. It is not restricted
in the topics that it covers.
- [American Astronomical Society (AAS)](https://aas.org/): This meeting is for all branches of astronomy. There are two meetings, a larger one in the Winter and a smaller one in the Summer. All branches of astronomy are welcome to present at AAS meetings.

### Travel funding

It can often cost a lot to travel to a conference. Luckily, there are funding options available to you as a student through both SPS and through UVA. Many conferences also offer a wide array of travel awards that you can apply for (look for them on the meeting website). Of course, you should discuss with your professor whether they have travel funding first, as they often do. Every year, our SPS chapter will make an attempt to travel to one of the major APS or AAS meetings, and we petition as a group for funding through the following sources:
- [SPS Travel Awards](https://www.spsnational.org/awards/travel): These $200 individual awards are granted to national SPS members who are presenting at any conference. You are pretty much guaranteed to get one as long as you apply well in advance of the conference.
- [SPS Reporter Awards](https://www.spsnational.org/awards/reporter): These $200 - $600 awards are granted to national SPS members who are presenting at any conference, as long at the end of the conference an reflection on the conference is written by the SPS members who applied for the award. The award is for $200 per individual writing the reflection, up to a maximum of 3 people ($600 award maximum).
- [UVA Research and Travel Grants](http://college.as.virginia.edu/research_travel_grants): These awards are granted by UVA to students conducting research or traveling to present their research. The award cap is $1,500, and grant proposals are accepted on a seasonal basis with two annual deadlines: **November 1** and **March 15**.