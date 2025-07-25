---
layout: syllabus
title: Syllabus
notitle: true
---

# Course Description

Data visualization is crucial to conveying information drawn from models,
observations or investigations. This course will provide an overview of
historical and modern techniques for visualizing data, drawing on
quantitative, statistical, and network-focused datasets. Topics will include
construction of communicative visualizations, the modern software ecosystem
of visualization, and techniques for aggregation and interpretation of data
through visualization. Particular attention will be paid to the Python
ecosystem and multi-dimensional quantitative datasets. 

# Land Acknowledgment

As a land-grant institution, the University of Illinois at Urbana-Champaign has
a responsibility to acknowledge the historical context in which it exists. In
order to remind ourselves and our community, we will begin this event with the
following statement. We are currently on the lands of the Peoria, Kaskaskia,
Peankashaw, Wea, Miami, Mascoutin, Odawa, Sauk, Mesquaki, Kickapoo, Potawatomi,
Ojibwe, and Chickasaw Nations. It is necessary for us to acknowledge these
Native Nations and for us to work with them as we move forward as an
institution. Over the next 150 years, we will be a vibrant community inclusive
of all our differences, with Native peoples at the core of our efforts.

[More information can be found on the Chancellor's
Website.](https://chancellor.illinois.edu/land_acknowledgement.html)

## Course Overview

This course is designed to give practical advice to students on
communicating data through visualization.  This will involve a considerable
amount of programming, and typically this programming will be done in Python, 
and some HTML (and possibly a tiny bit of JavaScript) later in the course.
For the most part, our data will be quantitative and multi-dimensional.  The
course will aim to provide both an understanding of what data visualizations
communicate and a set of tools for constructing them yourself.

The course will follow a common pattern within each single three-hour or two 1.5 hour instructional
session(s).  The first 60-90 minutes will be focused on lecture, where concepts
and tools will be introduced; typically, each class will focus on one type of
visualization or class of visualization.  The remaining time will include
exploration of a dataset, which may be independent or in groups, and then a
wrap-up session at the end.

Students are expected to have laptops with them, as well as access to Python
installations (we will go over how to setup the correct packages when necessary), and will be encouraged to participate in class.  Homework will
be assigned and collected through
other methods specified at time of submission like Moodle.

The central themes of the course are:

1. What are the components of an effective visualization of quantitative data?
2. What tools and ecosystems are available for visualizing data?
3. What systems can be put in place to generate visualizations rapidly and with
   high-fidelity representation?

## Course Context

This course meets a number of learning outcomes connected to program objectives for 
the BSIS/MSIM program, which in turn connect to larger iSchool and University of Illinois learning goals. 

#### BSIS
* Apply critical analytical skills to information issues
* Understand fundamental mathematical and programming tools for solving problems of
information modeling, expression, and transformation

#### MSIM
* Manage information using best practices in management and policy; knowledge representation;
human-centered design and systems; and data analytics.
* Accurately convey the implications of analytical results (in both oral and written modalities) to
diverse stakeholders


#### iSchool Goal
This course meets the following goal:
* Maintain global leadership in education for the information professions

#### University of Illinois Campus-Wide Learning Goals 
This course meets the following goals:
1. Intellectual Reasoning and Knowledge
2. Creative Inquiry and Discovery


## Pre- and Co-requisites

None, although intermediate Python programming experience is assumed.  
Generally the course assumes: an introductory knowledge of Python programming (equivalent to 1 grad course like IS430) + some experience with a Python-related project (and practice of debugging skills, googling errors).
A brief
introduction to several Python packages (e.g. Pandas) will be presented during the course. 

# Course Materials

There is no required textbook for this course.

<!-- 
A list of Python libraries week-by-week and tips on how to install them <a href="https://uiuc-ischool-dataviz.github.io/is445_spring2021/week01/installation_instructions">can be found by clicking this link</a>.
-->

**Optional** textbook [Visualization Analysis and Design by Tamara Munzner](https://www.amazon.com/gp/product/1466508914/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1).  You can find a lot of the concepts from this textbook on [the books webpage](https://www.cs.ubc.ca/~tmm/vadbook/) and the [associated lecture slides](https://www.cs.ubc.ca/~tmm/talks.html#vadallslides).

As the course progresses, a list of recommended readings will be generated for
each class.  These will be included in the course materials repository, and
students are encouraged to fork that repository and issue pull requests to add
suggested readings.

# Writing Resources
The iSchool Writing Resources is the in-house writing support team for graduate students at the iSchool.  They are here to help you with your writing and help you feel more comfortable and confident in your skills. The writing consultants are not professors or evaluators. They simply know the struggles of graduate and undergraduate-level writing and want to help you learn how to succeed and improve your writing skills. The iSchool writing consultants can help you with every step of the writing process. For detailed information on our services please visit our website:
https://publish.illinois.edu/ischoolwritingresources/


# Topic Calendar & Optional Reading

Below is an approximate outline of the course and **optional** reading for each week.  
Note that the reading is meant to be *complementary* to the course, i.e. we won't 
simply rehash what is in the reading during class.

This course is always under development and  the
course outline below is subject to some flexibility; students will be encouraged
to provide feedback on the topics covered, particularly toward the end.  Topics
that are of particular interest will be emphasized.

**Optional texts:**
 * <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/ref=sr_1_2?crid=1WC409BVX1489&keywords=visualization+analysis+and+design&qid=1580082878&sprefix=visualization%2Caps%2C158&sr=8-2">Visualization Analysis & Design, Tamara Munzner</a>. You can find a lot of the concepts from this textbook on [the books webpage](https://www.cs.ubc.ca/~tmm/vadbook/) and the [associated lecture slides](https://www.cs.ubc.ca/~tmm/talks.html#vadallslides).
 * Edward Tufte wrote a series of visualization books that are often thought of as foundational to the field.  These include <a href="https://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/ref=sr_1_1?keywords=edward+tufte+books&qid=1580082986&sr=8-1">The Visual Display of Quantitative Information</a>, <a href="https://www.amazon.com/Beautiful-Evidence-Edward-R-Tufte/dp/0961392177/ref=sr_1_2?keywords=edward+tufte+books&qid=1580082986&sr=8-2">Beautiful Evidence</a>, <a href="https://www.amazon.com/Envisioning-Information-Edward-R-Tufte/dp/0961392118/ref=sr_1_3?keywords=edward+tufte+books&qid=1580082986&sr=8-3">Envisioning Information</a>, and <a href="https://www.amazon.com/Visual-Explanations-Quantities-Evidence-Narrative/dp/0961392126/ref=sr_1_4?keywords=edward+tufte+books&qid=1580082986&sr=8-4">Visual Explanations: Images and Quantities, Evidence and Narrative<a>
 * There is a free online book, <a href="https://serialmentor.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a> that provies a lot of nice examples and serves as an intro to Tamara Munzner's book.  It has an <a href="https://serialmentor.com/dataviz/bibliography.html">annotated bibliography at the end</a> that gives a few references for books in data viz that include programming. It is built from the linked <a href="https://github.com/clauswilke/dataviz">GitHub repo</a>.  Note that this book is focused on static (not interactive) visualizations.
 * Additional references will be added as needed.

Acronyms for books:
 * VAD: Visualization Analysis & Design
 * FDV: Fundamentals of Data Visualization

**Course Outline and *Optional* Reading List**

<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 30%;
}
table th:nth-of-type(3) {
    width: 60%;
}
</style>
<!-- breaks: w2, w14 -->

| Week   | Topic  |  Reading 
-------|-------------------|---------
| <a name="week1">Week 1</a> | Introduction, syllabus, examples, and some basics | 1. VAD, Ch. 1: What's Viz, and Why Do It? <br> 2. <a href="https://serialmentor.com/dataviz/introduction.html">FDV, Ch. 1: Introduction</a> & <a href="https://serialmentor.com/dataviz/proportional-ink.html">FDV, Ch. 17: The principle of proportional ink</a> <br> 3. <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a> <br> 4. [Intro to Jupyter Notebook Video](https://www.youtube.com/watch?v=3C9E2yPBw7s)
| <a name="week2">Week 2</a> | Holiday! | No class, enjoy!
| <a name="week3">Week 3</a> | Data storage & Operations | 1. VAD, Ch. 2: What: Data Abstraction <br> 2. VAD, Ch. 13: Reduce Items and Attributes <br>  3. <a href="https://github.com/jnaiman/IS-452AO-Fall2019/blob/master/Lectures/Week-10-JSONandCSV.ipynb">IS452's intro to CSV files (bottom of page)</a> <br> 4. <a href="https://github.com/jnaiman/IS-452AO-Fall2019/blob/master/Lectures/Week-09-Dictionaries.ipynb">IS452's Intro to Dictionaries</a> <br> 5. <a href="https://pandas.pydata.org/pandas-docs/stable/">Pandas Docs</a> & <a href="https://docs.scipy.org/doc/numpy/reference/">NumPy Docs</a> 
| <a name="week4">Week 4</a> | Types of Viz and color, colormaps; Image data | 1. VAD, Ch. 10: Map Color and Other Channels <br> 2. <a href="https://serialmentor.com/dataviz/color-basics.html">FDV, Ch. 4: Color scales</a> <br> 3. VAD, Ch. 5: Marks and Channels <br> 4. <a href="https://www.csc2.ncsu.edu/faculty/healey/PP/">Perception in Visualization (pay extra attention to the parts about color)</a>  <br> 5. <a href="https://jiffyclub.github.io/palettable/#documentation">Palettable Docs</a> <br> 6. <a href="https://serialmentor.com/dataviz/image-file-formats.html">FDV, Ch. 27: Understanding the most commonly used image file formats</a> <br> 7. <a href="https://serialmentor.com/dataviz/aesthetic-mapping.html">FDV, Ch. 2: Visualizing data: Mapping data onto aesthetics</a>
| <a name="week5">Week 5</a> | Beginning Interactivity | 1. <a href="https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html">Intro to ipywidgets</a> <br> 2. <a href="https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Index.ipynb">Example Widgets Notebooks</a> <br> 3. VAD Ch. 7: Arrange Tables <br> 4. <a href="https://serialmentor.com/dataviz/histograms-density-plots.html">FDV, Ch. 7: Visualizing distributions: Histograms and density plots</a> 
| <a name="week6">Week 6</a> | Distributions, Engines |  1. <a href="https://www.youtube.com/watch?v=rraXF0EjRC8">Video about bqplot</a> <br> 2. <a href="https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149">An introduction to Grammar of Graphics</a> <br> 3. <a href="https://ipywidgets.readthedocs.io/en/latest/">ipywidgets Docs</a>; <a href="https://traitlets.readthedocs.io/en/stable/">Traitlets Docs</a>; <a href="https://bqplot.readthedocs.io/en/latest/">bqplot Docs</a>
| <a name="week7">Week 7</a> | Dashboards & Maps with bqplot | 1. VAD Ch. 8.1-8.3: Arrange Spatial Data <br> 2. VAD Ch. 11.1-11.5: Manipulate View <br> 3. <a href="https://serialmentor.com/dataviz/geospatial-data.html">FDV, Ch. 15: Visualizing geospatial data</a>
| <a name="week8">Week 8</a> | More with maps - bqplot, cartopy, ipyleaflet, geopandas | 1. VAD Ch. 8.1-8.3: Arrange Spatial Data <br> 2. <a href="https://serialmentor.com/dataviz/geospatial-data.html">FDV, Ch. 15: Visualizing geospatial data</a> <br> 3. VAD, Ch. 13.4.2: Reduce Items and Attributes <br> 4. <a href="https://scitools.org.uk/cartopy/docs/latest/">Cartopy docs</a>; <a href="https://ipyleaflet.readthedocs.io/en/latest/">ipyleaflet docs</a>; <a href="https://geopandas.org/">Geopandas Docs</a>
| <a name="week9">Week 9</a> | Designing for the web with vega-lite & Altair & Streamlit | 1. <a href="https://vega.github.io/vega-lite/docs/">vega-lite docs</a>  <br> 2. <a href="https://altair-viz.github.io/gallery/index.html">Altair docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types">Encoding Data Types</a>, <a href="https://altair-viz.github.io/user_guide/internals.html#converting-vega-lite-to-altair">Vegalite-Altair conversions</a>, <a href="https://altair-viz.github.io/user_guide/transform/bin.html#bin-transforms">Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html">Filter transforms</a> and <a href="https://altair-viz.github.io/gallery/interactive_cross_highlight.html#interactive-chart-with-cross-highlight">interactive examples</a> <br> 3. <a href="https://serialmentor.com/dataviz/directory-of-visualizations.html">FDV, Ch. 5: Directory of visualizations</a> 
| <a name="week10">Week 10</a> | More with Altair | 1. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions.html#bindings-selections-conditions-making-charts-interactive">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/09-Geographic-plots.html">Geographic plots</a>, and <a href="https://altair-viz.github.io/user_guide/transform/fold.html">Fold Transformations</a>
| <a name="week11">Week 11</a> | Web dev with Jekyll; Considering your audience | 1. <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a> <br> 2. <a href="https://serialmentor.com/dataviz/telling-a-story.html">FDV, Ch. 29: Telling a story and making a point</a> <br> 3. <a href="https://jekyllrb.com/tutorials/home/">Jekyll Tutorials (hit "Next" to see them at bottom)</a>
| <a name="week12">Week 12</a> | More with Jekyll; Streamlit | 1. <a href="https://streamlit.io/">Streamlit docs</a> - in particular the <a href="https://docs.streamlit.io/get-started/fundamentals/main-concepts">the Main Concepts </a> and  <a href="https://docs.streamlit.io/get-started/tutorials/create-an-app">Make an App</a> tutorials, and the docs for <a href="https://docs.streamlit.io/develop/api-reference/text">text</a>, <a href="https://docs.streamlit.io/develop/api-reference/layout">layout</a> and <a href="https://docs.streamlit.io/develop/api-reference/media/st.image">image</a> API elements<br> 2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a> 
| <a name="week13">Week 13</a> | Web dev with Streamlit + HuggingFace; Publishing Viz  | 1. <a href="https://streamlit.io/">Streamlit docs</a> - in particular <a href="https://docs.streamlit.io/develop/api-reference/charts/st.pyplot">matplotlib plots</a><br> 2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a> <br> 3. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions.html#bindings-selections-conditions-making-charts-interactive">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a> <br> 4. <a href="https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148">This blog post for a walkthrough of deploying a Streamlit space on HuggingFace</a>
| <a name="week14">Week 14</a> | Fall break! | No class, enjoy!
| <a name="week15">Week 15</a> | More web dev with Streamlit & Altair + Guest lecture about scientific & cinematic viz from <a href="https://avl.ncsa.illinois.edu/">NCSA's AVL</a> | 1. <a href="https://streamlit.io/">Streamlit docs</a><br> 2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a> with a focus on <a href="https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app">Multi-page apps</a> <br> 3. <a href="https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148">This blog post for a walkthrough of deploying a Streamlit space on HuggingFace</a> <br> 4. <a href="https://books.google.com/books?hl=en&lr=&id=jUw7DwAAQBAJ&oi=fnd&pg=PA91&dq=scientific+visualization+misinformation&ots=Cv0QmoCdM2&sig=7xycURu8Um_C9VtHqf-aWg4qaEo#v=onepage&q=scientific%20visualization%20misinformation&f=false">Chapter 5: Dimensions of Visual Misinformation in the Emerging Media Landscape in the book "Misinformation and Mass Audiences"</a>
| <a name="week16">Week 16</a> | SciViz, Network Viz & Word cloud Viz; Class summary | 1. VAD Ch. 8.4-8.6: Arrange Spatial Data <br> 2. VAD Ch. 11.6: Manipulate View <br> 3. <a href="https://yt-project.org/">yt docs</a> <br> 4. <a href="https://yt-project.org/doc/visualizing/volume_rendering.html">yt Volume Rendering Tutorial</a><br> 5. VAD Ch. 9: Arrange Networks and Trees <br> 6. VAD, Ch. 13.4.3.1: Reduce Items and Attributes <br> 7. VAD, Ch. 6: Rules of Thumb <br> 8. [FDV, Ch. 28: Choosing the right visualization software](https://serialmentor.com/dataviz/choosing-visualization-software.html) <br> 9. [FDV, Ch. 26: Don't go 3D](https://serialmentor.com/dataviz/no-3d.html) <br> 10. [FDV, Ch. 25: Avoid line drawings](https://serialmentor.com/dataviz/avoid-line-drawings.html)


# Assignments and Evaluation

## General Assignment Info
Assignments in this course will be a mixture of coding/visualization work and
written work.  These two may not be distinct assignments; students will be
asked to describe their code and justify choices for making decisions with
respect to visualizations.

Students are expected, unless otherwise instructed, to be the principal authors
of their code.  This does not mean they may not investigate resources such as
StackOverflow, package documentation, etc; however, they *must* cite when
resources (especially StackOverflow and other "recipe" sites) are utilized.

Each assignment will be based on "correctness" and the narrative description of
the process.  "Correctness" in this case indicates that the code runs without
issue, results are produced, and each component of the assignment is completed.
The narrative description of the process will be graded on grammar minimally and
more so on completeness and thoughtfulness.

The submission process for homeworks will be described by example during class
before any homeworks are to be submitted.


## Assignment Details

Students will be graded based on a combination of assignments including weekly prose/code homeworks, coding-based automatically-graded labs which are a practice of in-class coding concepts and/or preparatory setup work for future assignments, and automatically quizzes and a final project.
The final project will be a capstone to the course, and will
have greater flexibility in software packages and data sources.  This project
will be introduced around Week 8.

Assignments will either be graded by the [PrairieLearn](https://us.prairielearn.com/) autograder for instant feedback, or by the instructional team after the assignment has been submitted.

The breakdown of your grade will be:

| 40% | Homework: ~every-other week, prose or code, graded whole or partially by instructional team 
| 25% | Labs: ~every-other week, code, graded automatically (can be attempted as many times as you want before the due date)
| 5%  | Quizzes: ~weekly, short questions about lecture material, graded automatically (multiple attempts are allowed, however with decreasing scores)
| 30% | Final project: prose and code, graded by instructional team

### Other notes about assessments
 * Unless otherwise specified, all assignments will be completed on the [PrairieLearn platform](https://us.prairielearn.com/).
 * There will be opportunities for extra credit in the homework and final project portions.  
 * The suggested order to complete assignments for each module is Quiz, Lab, Homework/Final project part.
 * The *maximum* homework score is fixed at 40% (even with extra credit included).
 * Your lowest homework score will be dropped, however, we will not drop:
   * Homework \#1 (introduction, installations, etc)
   * Streamlit OR Jekyll Page Homework (Homework \#5 or \#6) -- i.e. you need to do AT LEAST one of these assignments (and maybe both, depending on what homework score you are aiming for)
   



<!--
There are several homework assignments which are **required** to pass the course:
 * Any installation/package test assignments (Part of Homework #1, Homework #5, and Homework #7) with a grade of 85% or better on *each* assignment portion
 * Final-project preparatory assignments: Homework #6, *either* Homework #9 *or* Homework #10 with a grade of 50% or better on *each* assignment portion

 
Failure to submit these assignments above these grading thresholds will automatically lead to a failing grade in the course.

**In summary, your grades consist of:**

| 50% | Standard assignments in prose or code form (50% is the MAX grade, even with extra credit)
| 20% | Weekly visualization labs
| 30% | Final project




Assignments in this course will be a mixture of coding/visualization work and
written work.  These two may not be distinct assignments; students will be
asked to describe their code and justify choices for making decisions with
respect to visualizations.

Students are expected, unless otherwise instructed, to be the principal authors
of their code.  This does not mean they may not investigate resources such as
StackOverflow, package documentation, etc; however, they *must* cite when
resources (especially StackOverflow and other "recipe" sites) are utilized.

Assignments will take two forms, and will be given at the end of each class.
Students will have until the following class to turn these in; assignments will
be collected electronically.

 * The first type of assignment will be a written document, constituting 
   either a brief literature review or an analysis of a visualization or
   set of visualizations.  The parameters for these assignments will be given
   during class, but will typically involve a critique of a visualization,
   including citing relevant works in the visualization literature.
 * The second type of assignment will be a hands-on, code-based assignment.
   Students will be provided either a dataset *or* a class of datasets from
   which they can choose, and construct one or multiple mechanisms of drawing
   information out of this visually.  These will be submitted in the form of
   Jupyter notebooks.  Each visualization must be accompanied by narrative
   description from the student describing why design decisions were made.

The submission process for homeworks will be described by example during class
before any homeworks are to be submitted.

Submissions will be in PDF and/or .ipynb (Jupyter notebook) format, and, when 
appropriate, a datafile needed to run the notebook file.  If coding is 
required for the assignment, you will *not* get full points if you do not 
submit the notebook file.  If the code requires a dataset and this is not 
included in your submission you will not get full credit.  Files should be 
uploaded individually, no *.zip files will be accepted.

Each assignment will be based on "correctness" and the narrative description of
the process.  "Correctness" in this case indicates that the code runs without
issue, results are produced, and each component of the assignment is completed.
The narrative description of the process will be graded on grammar minimally and
more so on completeness and thoughtfulness.

-->

### Grading Policy

All assignments are required for all students, aside from one homework (lowest HW grade will be dropped). 
<!-- Note that the Syllabus Quiz is in the homework grading category, but will *not* be droppable. -->
Completing all assignments is
not a guarantee of a passing grade.  You must do homework, visualization labs, quizzes, and final project to 
receive a passing grade. Late or incomplete assignments will not be given full credit
unless the student has contacted the instructor prior to the due date of the
assignment (or in the case of emergencies, as soon as practicable).


**Grading Scale:**

| above 94        | A
| 90-93.99        | A-
| 87-89.99        | B+
| 83-86.99        | B
| 80-82.99        | B-
| 77-79.99        | C+
| 73-76.99        | C
| 70-72.99        | C-
| 67-69.99        | D+
| 63-66.99        | D
| 60-62.99        | D-
| 59.99 and below | F


#### Assignment Late Policies

We allow students to turn in *all* Homeworks up to a week late without penalty.  If you need to “use” one of these late homeworks use the "Extension Request" tool for each assignment in that week's module and specify that you would like to use an extension.  The extension request needs to be submitted *before the assignment is due* and can not be requested retroactively.  You do not need to provide any explanation for why you’d like to use an extension.  You will then have one extra week to submit this assignment. **Please note:** Once you submit your extension request wait until you receive a confirmation email from the instructional team (generally *after* the assignment due date) before submitting your assignment.  If you submit your assignment before receiving this email, it will be marked late even if you have requested an extension.  All homeworks not on extension will be given a zero if turned in after 3 days past the due date. 

No extensions can be applied to Labs, Quizzes, or any parts of the Final Project.

Late policies for homeworks not on extension include: 10% off for up to 1 day late, 20% off for 2 days late, 30% off for 3 days late.  All homeworks not on extension will be given a zero if turned in after 3 days past the due date.

Late policies for labs will be: 5% off for up to 1 day late, 10% for up to 3 days late, 20% for up to 4 days late, 30% for up to 5 days late. There are no extensions for Labs.

Quiz late policies follow homework late policies: 10% off for up to 1 day late, 20% off for 2 days late, 30% off for 3 days late.

Extra Credit assignments, and all parts of Final Project Part 3 (Part 3.1, 3.2, 3.3, 3.4, 3.5) cannot be turned in late (these are due toward the end of class so there is no "wiggle" room for late assignments).  Extra credit assignments and *all* parts of the Final Project do not have extensions.

**Notes if adding the course late:**
* There will be NO late adds after 10th day
* Students add the course after the start of class are responsible for submitting all assignments on time (even if assigned before they have added the class) -- this includes requesting a homework extension using the Extension Tool, if applicable  



# About Your Instructor

Jill Naiman's background is in theoretical and computational astrophysics with a current research emphasis on scientific data visualization and the digitization of historical scientific images and text.  In addition to her position as Teaching Faculty at the iSchool, she is also currently a Visiting Scholar at the Advanced Visualization Lab at the National Center for Supercomputing Applications.  She is currently involved in projects related to increasing access to industry-standard special effects software for scientists - more info can be found <a href="http://ytini.com">here</a> and <a href="http://astroblend.com">here</a>.  Information about her astrophysical research and outreach efforts can be found <a href="http://astronaiman.com">here</a>.

# Library Resources

| http://www.library.illinois.edu/lis/ |
| lislib@library.illinois.edu          |
| Phone: (217) 300-8439                |
| https://www.library.illinois.edu/infosci/ |

# Writing and Bibliographic Style Resources
The campus-wide Writers Workshop provides free consultations. For more
information see <http://www.cws.illinois.edu/workshop/> The iSchool
has a Writing Resources Moodle site
<https://courses.ischool.illinois.edu/course/view.php?id=1705> and
iSchool writing coaches also offer free consultations.

# Disruptive behavior
Behavior that persistently or grossly interferes with classroom activities is considered disruptive behavior and may be subject to disciplinary action. Such behavior inhibits other students’ ability to learn and an instructor’s ability to teach. A student responsible for disruptive behavior may be required to leave class pending discussion and resolution of the problem and may be reported to the Office for Student Conflict Resolution (https://conflictresolution.illinois.edu; conflictresolution@illinois.edu; 333-3680) for disciplinary action.

Do not record voices or take photos of individuals in class without prior consent.  This is inline with the campus' [IRB/human subject research protocols](https://oprs.research.illinois.edu/) regarding data collection for human subjects. 

# Academic Integrity

Please review and reflect on the academic integrity policy of the University of Illinois, http://studentcode.illinois.edu/article1_part4_1-401.html, to which we subscribe. By turning in materials for review, you certify that all work presented is your own and has been done by you independently, or as a member of a designated group for group assignments. 

If, in the course of your writing, you use the words or ideas of another writer, proper acknowledgement must be given (using APA, Chicago, or MLA style). Not to do so is to commit plagiarism, a form of academic dishonesty. If you are not absolutely clear on what constitutes plagiarism and how to cite sources appropriately, now is the time to learn. Please ask me!

Please be aware that the consequences for plagiarism or other forms of academic dishonesty will be severe. Students who violate university standards of academic integrity are subject to disciplinary action, including a reduced grade, failure in the course, and suspension or dismissal from the University.

Criteria for grading homework assignments include (but are not limited to) creativity and the amount of original work demonstrated in the assignment. However, students are permitted to use and adapt the work of others, provided that the following guidelines are followed:
 * Use of other people’s material must not infringe the copyright of the original author, nor violate the terms of any licensing agreement. Know and respect the principles of fair use with respect to copyrighted material.
 * Students must scrupulously attribute the original source and author of whatever material has been adapted for the assignment. Summarize the changes or adaptations that have been made. Make plain how much of the assignment represents original work.
 
*This applies to code as well* -- you are welcome to use online sources (e.g. StackOverflow) but be sure to include the URL in your code comments.

Additionally, unless explicitly stated **do not** publish homework solutions online.


## Policy on ChatGPT and other Large Language Models (LLMs)
	
The purpose of written and programming assignments is for students to apply what they have learned in class and learn how to validate statements and code or software.  The purpose is not to produce a “perfect” bit of text or code/software – there is no such thing!  Instead, we want to see how you problem-solve and what you think about a particular topic.

LLMs can be useful for getting ideas about how to phrase text or to get started on a coding/software problem, however they are not meant to be used in place of your critical thinking skills.  Remember – it is more important that we hear your thoughts on topics than it is to generate 100% perfect English, and if you make use of LLMS, we expect significant extra work to be submitted with your submissions.  

We will be implementing several policies related to the use of LLMS as listed below:

 * **Acceptable Use:** Students are allowed to utilize ChatGPT or similar AI language models for course assignments or tests but in specific situations. Such usage should be restricted to brainstorming, seeking inspiration, expanding ideas, and improving writing, and must not constitute the primary source of content or answers. *You cannot copy full-text of assignment questions and input directly into an LLM -- this is plagiarism.*
 * **No Direct Answers:** Students must not directly copy or paraphrase AI-generated text without proper attribution. Usage of ChatGPT or similar AI language models to directly answer specific questions or complete entire assignments is strictly prohibited. Students should rely on their knowledge and understanding, supplemented by AI tools for assistance.
 * **Fact-Checking and Verification:** Students must critically assess and verify any information obtained through ChatGPT or similar AI language models before incorporating it into their work. Misleading or inaccurate information from the AI model should not be used in their submissions. Cross-reference the AI-generated information with reputable sources to verify its accuracy and reliability.  In particular, if you use an LLM you must:
    * Include the LLM name and date of usage
    * Include the prompt used
    * Include your “validation plan” for each statement that you use from the LLM.  
        * Writing: For example, if one wants to use the statement “The Sky is blue due to Rayleigh scattering.” as output by an LLM, links to research supporting this claim need to be included (and if those links have also been generated by the LLM, each will need to be verified).  
        * Code/Software: you will need to create your own validation tests to run the code.  Include this in your submission along with a few sentences describing how your validation tests relate to the prompt.
 * **Transparent Use and Academic Integrity:** Clearly indicate any sections or contents that are AI-generated.
 * **Assignment-Specific Guidelines:** Each assignment or test may have specific instructions regarding the use of AI tools. Students must carefully review and comply with any guidelines provided.
 * **Consequences of Misuse:** Violation of the class policy on the use of ChatGPT will be treated as an academic integrity breach and subject to disciplinary action as per the institution's guidelines.
	
The above class policy on the use of AI for course assignments were generated by ChatGPT, and selected, modified, and adapted by Dr. Koh on 8/3/23, and further modified by Dr. Naiman on 8/20/2023. The used prompts include: Give me class policy on the use of ChatGPT for course assignments and tasks; Come up with more specific class policy; and Give me examples of class policy on the use of ChatGPT for course assignments and tests.



# Statement of Inclusion

[Review statement](https://diversity.illinois.edu/about/senate-diversity-resolution/)

As the state’s premier public university, the University of Illinois at Urbana-Champaign’s core mission is to serve the interests of the diverse people of the state of Illinois and beyond. The institution thus values inclusion and a pluralistic learning and research environment, one which we respect the varied perspectives and lived experiences of a diverse community and global workforce. We support diversity of worldviews, histories, and cultural knowledge across a range of social groups including race, ethnicity, gender identity, sexual orientation, abilities, economic class, religion, and their intersections. 



# Religious Observances
In keeping with our Statement of Inclusion and Illinois law, the University is required to reasonably accommodate its students' religious beliefs, observances, and practices in regard to admissions, class attendance, and the scheduling of examinations and work requirements. 

Religious Observance Accommodation Request form: https://cm.maxient.com/reportingform.php?UnivofIllinois&layout_id=19
Other accommodations may be available.

# Accessibility Statement
To obtain accessibility-related academic adjustments and/or auxiliary aids, students with disabilities must contact the course instructor and the Disability Resources and Educational Services (DRES) as soon as possible. To contact DRES you may visit 1207 S. Oak St., Champaign, call 333-1970 (V/TTY), or e-mail a message to disability@illinois.edu.  

To insure disability-related concerns are properly addressed from the beginning of the semester, I request that students with disabilities who require assistance to participate in this class contact me as soon as possible to discuss your needs and any concerns you may have. The University of Illinois may be able to provide additional resources to assist you in your studies through the office of Disability Resources and Educational Services (DRES). This office can assist you with disability-related academic adjustments and/or auxiliary aids. Please contact them as soon as possible by visiting the office in person: 1207 S. Oak St., Champaign; visiting the website: http://disability.illinois.edu; calling (217) 333-4603 (V/TTY); or via e-mail disability@illinois.edu. NOTE: I do not require a letter from DRES in order to discuss your requested accommodations. 

DRES (Disability Resources and Educational Services) workshop on accommodations with Tina Cowsert (MS/LIS '19), Access Specialist/Interpreter Coordinator; Mandi Carey, Access Specialist/ Student Services; Lena Bohman (MS/LIS '20): 
Event date 02-13-21   https://mediaspace.illinois.edu/media/t/1_kfxfvga4





### Incompletes

Students must request an incomplete grade from the instructor. The instructor
and student will agree on a due date for completion of coursework and the
student must file an Incomplete Form signed by the student, the instructor, and
the student’s academic advisor with the School’s records representative. More
information on incompletes is available here:
<http://webdocs.ischool.illinois.edu/registration/incomplete_grade_form.pdf>

### Attendance Policy

Students are required to attend each class, and if they are unable to do so
must notify the instructor and TA in advance and request an excused absence.
Participation in class -- in the form of comments, questions, and discussion --
is expected.

### Email/Slack Policies and Turn-around times

We aim to respond to Slack messages in the main channel within 24 business hours and email within 3 business days.  Please note that personal Slack messages are treated as emails and turn around times will be within 3 days (though we will make every effort to respond sooner than that).  Please do not use Slack for any questions about grades, or other personal queries -- email is the appropriate venue for these questions.  Do not post working code or solutions of any kind on Slack publically.


## Emergency Response: Run, Hide, Fight

Emergencies can happen anywhere and at any time. It is important that
we take a minute to prepare for a situation in which our safety or
even our lives could depend on our ability to react quickly. When
we’re faced with any kind of emergency – like fire, severe weather or
if someone is trying to hurt you – we have three options: Run, hide or
fight.


### Run

Leaving the area quickly is the best option if it is safe to do so.

- Take time now to learn the different ways to leave your building.
- Leave personal items behind.
- Assist those who need help, but consider whether doing so puts
  yourself at risk.
- Alert authorities of the emergency when it is safe to do so.

### Hide

When you can’t or don’t want to run, take shelter indoors.

- Take time now to learn different ways to seek shelter in your building.
- If severe weather is imminent, go to the nearest indoor storm refuge area.
- If someone is trying to hurt you and you can’t evacuate, get to a place
  where you can’t be seen, lock or barricade your area, silence your
  phone, don’t make any noise and don’t come out until you receive an
  Illini-Alert indicating it is safe to do so.

### Fight

As a last resort, you may need to fight to increase your chances of
survival.

- Think about what kind of common items are in your area which you
  can use to defend yourself.
- Team up with others to fight if the situation allows.
- Mentally prepare yourself – you may be in a fight for your life.

Please be aware of persons with disabilities who may need additional
assistance in emergency situations.


### Other resources

- [police.illinois.edu/safe](http://police.illinois.edu/safe) for more
  information on how to prepare for emergencies, including how to run,
  hide or fight and building floor plans that can show you safe areas.
- [emergency.illinois.edu](http://emergency.illinois.edu) to sign up for
  Illini-Alert text messages.
- Follow the University of Illinois Police Department on Twitter and
  Facebook to get regular updates about campus safety.



# Resources to help you succeed:
As members of the Illinois community, we each have a responsibility to express care and concern for one another. If you come across a classmate whose behavior concerns you, whether in regards to their well-being or yours, we encourage you to refer this behavior to the Student Assistance Center (217-333-0050 or http://odos.illinois.edu/community-of-care/referral/). Based
on your report, the staff in the Student Assistance Center reaches out to students to make sure they have the support they need to be healthy and safe.
 
Further, as a Community of Care, we want to support you in your overall wellness. We know that students sometimes face challenges that can impact academic performance (examples include mental health concerns, food insecurity, homelessness, personal emergencies). Should you find that you are managing such a challenge and that it is interfering with your coursework, you are encouraged to contact the Student Assistance Center (SAC) in the Office of the Dean of Students for support and referrals to campus and/or community resources.

## Mental Health Resources
Significant stress, mood changes, excessive worry, substance/alcohol misuse or interferences in eating or sleep can have an impact on academic performance, social development, and emotional wellbeing. The University of Illinois offers a variety of confidential services including individual and group counseling, crisis intervention, psychiatric services, and specialized screenings which are covered through the Student Health Fee. If you or someone you know experiences any of the above mental health concerns, it is strongly encouraged to contact or visit any of the University’s resources provided below. Getting help is a smart and courageous thing to do for yourself and for those who care about you.
 • Counseling Center (217) 333-3704
 • McKinley Health Center (217) 333-2700
 • National Suicide Prevention Lifeline (800) 273-8255
 • Rosecrance Crisis Line (217) 359-4141 (available 24/7, 365 days a year)
 If you are in immediate danger, call 911.

## Emergency Response Recommendations
Emergency response recommendations and campus building floor plans can be found at the following website: https://police.illinois.edu/em/run-hide-fight/. I encourage you to review this website within the first 10 days of class.

## Other Resources
Students experiencing economic hardships resulting in food insecurity, housing insecurity, homelessness, or other issues that may affect the quality of their work, are encouraged to reach out to iSchool Assistant Dean for Student Affairs, April Carter at acart22@illinois.edu or call 217–333-0532.

# Sexual Misconduct Reporting Obligation
The University of Illinois is committed to combating sexual misconduct. Faculty and staff members are required to report any instances of sexual misconduct to the University’s Title IX Office. In turn, an individual with the Title IX Office will provide information about rights and options, including accommodations, support services, the campus disciplinary process, and law enforcement options.
A list of the designated University employees who, as counselors, confidential advisors, and medical professionals, do not have this reporting responsibility and can maintain confidentiality, can be found here: wecare.illinois.edu/resources/students/#confidential.
Other information about resources and reporting is available here: wecare.illinois.edu.


# The iSchool Academic Support Center
The iSchool Academic Support Center offers academic success workshops; coordinates with faculty and instructors to provide support for specific courses or exams; and curates and shares academic support resources. Appointments are available online and in person in room 4020 (Academic Support Center) in the 614 E. Daniel iSchool building. For more information including hours of operation, please visit https://ischool.illinois.edu/student-life/academic-support-center.

# The Writers Workshop 
The Writers Workshop (https://writersworkshop.illinois.edu/) provides writing support to students, including individual consultations, workshops, and resources. In response to the ongoing COVID-19 pandemic, all Writers Workshop consultations are currently offered online (https://writersworkshop.illinois.edu/services/consultations/online/). 
To request disability-related accommodations for our services, please contact Dr. Carolyn Wisniewski at wow@illinois.edu or call 217-333-8796.

# Emergencies

### Covid-19
In keeping with University and iSchool policy, all students are required to engage in appropriate behavior to protect the health and safety of our community.  

If you feel ill or are unable to come to class or complete class assignments due to issues related to COVID-19, including but not limited to: testing positive yourself, feeling ill, caring for a family member with COVID-19, or having unexpected child-care obligations, should contact their instructor immediately and cc their advisor.

It is likely we can give you more time on assignments, however you need to reach out to your academic advisor and the course instructor *as soon as possible* so we have as much "runway" as possible in order to support you. If significant extra time is required to complete assignments, it is likely you will need to get a "Absence Letter" from the University -- please [see this link here](https://odos.illinois.edu/resources/students/absence-letters) for more information about retaining a letter.

Additionally, please be aware that there are mental health resources available to students:
 * https://www.counselingcenter.illinois.edu/
 * https://mckinley.illinois.edu/medical-services/mental-health
 * https://www.disability.illinois.edu/health/mental-health-resources

### Other Emergencies 

If students need to miss class or assignments for significant periods of time due to illness or other emergencies, it is imperative they acquire a letter from the University in order for the instructor to be able to give them extended time in order to avoid any [Capricious Grading](https://studentcode.illinois.edu/article3/part1/3-107) concerns.

Instructions for how to get a letter can be found at [this link here](https://odos.illinois.edu/resources/students/absence-letters).
