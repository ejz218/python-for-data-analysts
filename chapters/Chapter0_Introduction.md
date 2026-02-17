  ----------------------- ----------------------- -----------------------

  ----------------------- ----------------------- -----------------------

**BUAN 446**

PYTHON FOR

**DATA ANALYSTS**

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

*Intensive 6-Week Graduate Course*

# Chapter 0: Course Introduction & Setup

  -----------------------------------------------------------------------
  **WHAT YOU\'LL LEARN IN THIS COURSE**
  -----------------------------------------------------------------------
  **✓** Master Python fundamentals and data structures

  **✓** Clean and analyze real-world messy datasets

  **✓** Use NumPy, pandas, and data visualization tools

  **✓** Leverage AI effectively through the CRAWL → WALK → RUN framework
  -----------------------------------------------------------------------

  -------------------------------------------------------------------------
  **1**   **WELCOME TO BUAN 446**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

Welcome to BUAN 446, an intensive six-week graduate course that will
transform you from someone who may have never written a line of code
into a data analyst who can wrangle messy datasets, automate repetitive
tasks, and extract meaningful insights using Python.

**What This Course Is (and Isn\'t)**

This course is designed to give you practical, job-ready skills for data
analysis. You will learn Python fundamentals, data manipulation with
pandas and NumPy, data visualization with matplotlib and seaborn, and
most importantly, how to clean and prepare real-world messy data.

This course is NOT a computer science degree compressed into six weeks.
We will not cover advanced algorithms, software engineering principles,
or theoretical computer science. Instead, we focus relentlessly on the
skills you need as a data analyst: reading data from files, cleaning it,
analyzing it, visualizing it, and communicating your findings.

**Why Python Matters for Data Analysts**

Python has become the lingua franca of data analysis for good reasons:

> • It has powerful libraries (pandas, NumPy, matplotlib) that make data
> manipulation intuitive
>
> • It is open source and free, unlike proprietary tools like SAS or
> SPSS
>
> • It is versatile enough to handle everything from simple data
> cleaning to complex machine learning
>
> • It has a massive community, meaning you can find help and resources
> easily
>
> • Employers increasingly expect data analysts to know Python

**The Reality Check: Data Cleaning**

  -----------------------------------------------------------------------
  ★ **THE 60-80% RULE**
  -----------------------------------------------------------------------
  You will spend 60-80% of your time as a data analyst cleaning and
  preparing data, not analyzing it. Real-world data is messy. This course
  embraces that reality.

  -----------------------------------------------------------------------

Real-world data has missing values, inconsistent formatting, duplicates,
typos, invalid entries, and structural problems. We will work
extensively with intentionally messy datasets so that when you encounter
similar problems in your career, you will know exactly how to handle
them. This is not busy work. This is the actual job.

**Course Structure Overview**

BUAN 446 meets four days per week (Monday through Thursday) for 1 hour
and 45 minutes per session over six weeks. This is an intensive pace.
You should expect to spend 8-12 hours per week outside of class on
readings, DataCamp modules, assignments, and projects.

- Weeks 1-2: Python fundamentals (variables, control flow, functions)

- Week 3: Data structures, file I/O, midterm exam

- Weeks 4-5: Data analysis libraries (NumPy, pandas)

- Week 6: Data visualization and final project

  -------------------------------------------------------------------------
  **2**   **THE CRAWL → WALK → RUN FRAMEWORK**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

This course takes a unique approach to artificial intelligence (AI) in
education. Rather than banning AI tools like ChatGPT, Gemini, and
Claude, or allowing unrestricted use, we use a structured three-phase
framework that teaches you when and how to use AI effectively.

**How AI Fits into Your Learning**

AI is a tool, not a replacement for learning. A power saw in the hands of a master carpenter speeds up the work, but the tool itself cannot design a stable structure or select the right wood for the job. Those insights come from foundational knowledge, not the tool. The same principle applies here. You need to build foundational skills and mental models before AI becomes useful rather than a crutch that prevents learning.

**CRAWL Phase: Building Your Foundation**

  -----------------------------------------------------------------------
  ⚠ **NO AI ASSISTANCE ALLOWED**
  -----------------------------------------------------------------------
  In the CRAWL phase, you work independently without any AI help. This
  applies to chapter readings, DataCamp modules, basic practice problems,
  and all quizzes and exams.

  -----------------------------------------------------------------------

Why? Because you need to develop muscle memory. You need to struggle
with syntax errors. You need to learn to read error messages. You need
to build the mental models that make you an effective programmer. If AI
writes the code for you at this stage, you learn nothing. Think of CRAWL
work as going to the gym. You cannot hire someone to lift weights for
you and expect to get stronger.

**WALK Phase: AI as Your Tutor**

Once you have completed the CRAWL work and built basic competency, you
can use AI to deepen your understanding. In WALK phase, you may use AI
to explain concepts you find confusing, help debug code you have already
written, provide alternative explanations, and answer specific questions
about syntax or behavior.

You may NOT use AI to write assignment code for you, generate solutions
you then submit, or complete exercises on your behalf. The distinction
is critical. AI should help you understand, not do the work for you.

**RUN Phase: Full AI Collaboration**

In the RUN phase, you work on substantial projects where full AI
collaboration is not only allowed but encouraged. This mirrors
real-world data analysis where professionals routinely use AI to
generate boilerplate code faster, explore alternative approaches, debug
complex issues, and optimize code.

However, even in RUN phase projects, you must understand every line of
code you submit, document your AI usage, be able to explain your
approach, and make strategic decisions about data cleaning and analysis.

**QUICK REFERENCE: When Can I Use AI?**

| **CRAWL** | **WALK** | **RUN** |
| :--- | :--- | :--- |
| Quizzes, Exams, DataCamp<br>**NO AI** | Understanding concepts, Debugging your code<br>**AI FOR EXPLANATION** | Projects<br>**FULL AI COLLABORATION** with documentation |

**Why We Restrict AI on Exams**

All quizzes and exams in this course prohibit AI assistance. This is not
arbitrary. There are two critical reasons:

First, you need independent competency. Not every workplace allows AI
tools. Not every problem has internet access. You will face situations
where you must solve problems with your own knowledge. If you cannot
write basic Python without AI, you are not job-ready.

Second, assessment integrity matters. Employers hiring Crestview graduates
trust that your transcript reflects your actual capabilities. If you use
AI to inflate your performance, you devalue your degree and hurt future
Crestview students.

  -----------------------------------------------------------------------
  ⚠ **STRICT ENFORCEMENT**
  -----------------------------------------------------------------------
  The no-AI policy on exams is strictly enforced. Violations will result
  in a zero on the assignment and potential referral to the Office of
  Student Conduct.

  -----------------------------------------------------------------------

  -------------------------------------------------------------------------
  **3**   **THE CRESTVIEW STUDENT DATASET CASE STUDY**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

Rather than jumping between disconnected datasets, this course uses a
single comprehensive case study throughout all chapters: synthetic
Crestview University student enrollment data.

**What is Synthetic Data?**

Synthetic data is artificially generated information that mirrors the statistical properties of real-world data without containing any actual personal information. By using synthetic data, we can work with a realistic, complex dataset of "students" while maintaining complete privacy. It also allows us to intentionally design specific data messiness—like typos, inconsistent formats, and missing values—that you must learn to fix, ensuring you encounter every type of cleaning challenge you'll face in your career.

**What You Will Be Analyzing**

The Crestview student dataset contains realistic enrollment and academic
performance data for over 600 students. Each record includes:

> • Student_ID: Unique identifier for each student
>
> • College: Academic college (Business, Engineering, Arts & Sciences)
>
> • Major: Declared major within their college
>
> • Class_Year: Freshman, Sophomore, Junior, Senior, or Graduate
>
> • GPA: Grade point average on a 4.0 scale
>
> • Credits_Attempted: Total number of credits attempted
>
> • Credits_Earned: Total number of credits successfully earned

**Clean Data vs. Messy Data vs. Extended Data**

You will work with *three* versions of the Crestview student dataset as your skills evolve:

**1. Clean Dataset (crestview_students_clean.csv)**

This version contains 600 properly formatted records with no missing
values, no duplicates, and consistent formatting. You will use this
dataset early in the course (Weeks 1-2) when learning Python fundamentals.

**2. Messy Dataset (crestview_students_messy.csv)**

This version contains 605 records with 28+ intentional data quality
problems including missing values, inconsistent text formatting,
duplicate records, invalid data (GPAs above 4.0, negative credits), type
inconsistencies, structural issues, and logical inconsistencies. You will
tackle this in Week 3.

**3. Extended Dataset (crestview_students_extended.csv)**

This is the "Reward Dataset" for Weeks 4-6. It is clean like the first
dataset but twice as wide (15 variables instead of 7). It includes rich
dimensions like financial aid, study hours, extracurriculars, and
demo graphics, allowing for sophisticated multi-dimensional analysis
using NumPy and Pandas.

This version contains 605 records with 28+ intentional data quality
problems including missing values, inconsistent text formatting,
duplicate records, invalid data (GPAs above 4.0, negative credits), type
inconsistencies, structural issues, and logical inconsistencies.

**Why Messy Data Matters**

Corporate and institutional data is almost never clean. According to
industry surveys, data scientists and analysts spend 60-80% of their
time on data preparation and cleaning. The messy dataset problems you
will encounter in this course directly mirror issues you will face in
practice: data exported from legacy systems, manual data entry errors,
merged datasets with conflicting standards, and invalid entries from
users bypassing validation rules.

Learning to identify, diagnose, and systematically resolve these issues
is the most valuable skill you will develop in this course. Textbook
examples using clean data teach you Python syntax. Working with messy
data teaches you to be a data analyst.

  -------------------------------------------------------------------------
  **4**   **TECHNICAL SETUP**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

Before our first-class session, you must have Python and Jupyter
Notebook installed and working on your computer. Follow these steps
carefully.

**Installing Python via Anaconda**

We will use the Anaconda distribution of Python, which includes Python
itself plus all the scientific computing libraries we need (NumPy,
pandas, matplotlib, etc.) in a single installer.

**Step 1: Download Anaconda**

> • Visit https://www.anaconda.com/download
>
> • Download the installer for your operating system (Windows, macOS, or
> Linux)
>
> • Choose the version with Python 3.11 or higher

**Step 2: Run the Installer**

> • Run the downloaded installer and accept the license agreement
>
> • Install for \"Just Me\" (recommended)
>
> • Use the default installation location
>
> • IMPORTANT: Check the box to \"Add Anaconda to my PATH environment
> variable\" (Windows only)

**Step 3: Verify Installation**

Open a terminal (Mac) or command prompt (Windows) and type: python \--version

You should see output like \"Python 3.11.5\" or similar. If you get an
error, the installation may have failed or PATH was not configured
correctly.

**Installing and Launching Jupyter Notebook**

Jupyter Notebook is included with Anaconda, so you should already have
it installed. You can launch it via Anaconda Navigator or by typing
\"jupyter notebook\" in your terminal.

**Installing GitHub Desktop**

We use GitHub to distribute course materials. Visit
https://desktop.github.com to download GitHub Desktop. After
installation, you will clone the course repository to get all course
materials.

**Getting Course Files**

**Getting Course Files (The Easy Way)**

**1. Download Files**
*   Open **GitHub Desktop**.
*   Go to **File > Clone Repository**.
*   Select the **URL** tab.
*   Paste this URL: `https://github.com/ejz218/python-for-data-analysts.git`
*   **Local Path:** Click "Choose..." and select your `Desktop` folder.
*   Click **Clone**.

**2. Verify**
You should now see a `python-for-data-analysts` folder on your Desktop.

  -----------------------------------------------------------------------
  ℹ **GETTING WEEKLY UPDATES**
  -----------------------------------------------------------------------
  This course follows an **Immutable Release** strategy. Once a week's content
  is released, the instructor will not modify those specific files again.

  To get new chapters and assignments:
  1. Open GitHub Desktop.
  2. Click **Fetch origin** (or **Pull origin**).
  3. The new files will appear in your folder automatically.

  **No need to make copies.** You can work directly in the assignment files.
  Since the instructor won't touch them again, your work remains safe.

  -----------------------------------------------------------------------

  -------------------------------------------------------------------------
  **5**   **DATACAMP ACCOUNT SETUP**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

DataCamp is an online learning platform with interactive Python courses.
Crestview provides free access to DataCamp for all students in this course.

**Creating Your Account**

You will receive an email invitation to join the BUAN 446 DataCamp
group. Follow the link in the email to create your account using your
Crestview email address.

**How DataCamp Fits Into CRAWL Phase Learning**

DataCamp exercises are considered CRAWL phase work. You must complete
them independently without AI assistance. The platform provides
immediate feedback, which helps you learn from mistakes, but you must
write the code yourself. DataCamp modules complement but do not replace
chapter readings and in-class work.

  -------------------------------------------------------------------------
  **6**   **COURSE POLICIES & EXPECTATIONS**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

**Attendance Requirements**

This is a six-week intensive course. Missing even one class session
means you fall significantly behind. Regular attendance is expected and
required. Excessive absences (more than two sessions) will negatively
impact your grade and may result in failure of the course.

**Assignment Submission**

All assignments must be submitted through Moodle by 11:59 PM on their
due date. Late submissions will be penalized 20% per day unless you have
made prior arrangements with the instructor. For Jupyter notebook
assignments, ensure your notebook runs completely from top to bottom
without errors before submission.

**Quiz and Exam Policies**

All quizzes and exams are closed-book and no-AI. You may not use
textbooks, notes, external resources, AI tools, or communicate with
other students during exams.

**Academic Integrity**

  -----------------------------------------------------------------------
  ⚠ **DO NOT POST SOLUTIONS TO PUBLIC GITHUB**
  -----------------------------------------------------------------------
  Posting your assignment solutions publicly violates academic integrity
  and enables future cheating. Build original projects for your portfolio
  instead.

  -----------------------------------------------------------------------

Academic integrity remains paramount even when AI tools are available.
Follow the CRAWL → WALK → RUN guidelines for each assignment, never use
AI on quizzes or exams, never submit work you do not understand, and
never share your code with other students.

**Grading Breakdown**

| **Assessment Component** | **Weight** |
| :--- | :--- |
| Weekly Quizzes (5 total) | **15%** |
| DataCamp Modules | **10%** |
| Assignments (Weekly) | **25%** |
| Midterm Exam | **20%** |
| Final Project | **20%** |
| Final Exam | **10%** |

Letter grades follow standard Crestview University scale: A (93-100), A-
(90-92), B+ (87-89), B (83-86), B- (80-82), C+ (77-79), C (73-76), C-
(70-72), D+ (67-69), D (60-66), F (below 60).

  -------------------------------------------------------------------------
  **7**   **WEEKLY SCHEDULE OVERVIEW**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

**Week 1: Python Fundamentals**

Topics: Variables, data types, operators, expressions, basic
input/output. Assessment: Quiz 1 (Friday). DataCamp: Introduction to
Python (Chapters 1-2).

**Week 2: Control Flow & Functions**

Topics: If statements, loops, function definition and calling, scope.
Assessment: Quiz 2 (Monday), Quiz 3 (Thursday). DataCamp: Python
Functions & Logic.

**Week 3: Data Structures & File I/O**

Topics: Lists, tuples, dictionaries, sets, file reading/writing,
exception handling. Assessment: Quiz 4 (Monday), Data Cleaning
Assignment (due Thursday), Midterm Exam (Friday). DataCamp: Python Data
Structures.

**Week 4: NumPy & Pandas Basics**

Topics: NumPy arrays, array operations, pandas DataFrames, reading CSV
files. Assessment: Quiz 5 (Thursday), Weekly Assignment. DataCamp: NumPy
& Pandas Fundamentals.

**Week 5: Advanced Pandas & Visualization**

Topics: GroupBy operations, merging datasets, pivot tables, matplotlib,
seaborn. Assessment: Weekly Assignment. DataCamp: Data Visualization
with Python.

**Week 6: Complete Workflow & Final Project**

Topics: End-to-end data analysis workflow, best practices, project work.
Assessment: Final Project (due Wednesday), Final Exam (Friday).
DataCamp: Optional enrichment modules.

  -------------------------------------------------------------------------
  **8**   **YOUR FIRST WEEK CHECKLIST**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **COMPLETE BEFORE END OF WEEK 1**
  -----------------------------------------------------------------------
  **✓** Install Anaconda and verify Python works

  **✓** Launch Jupyter Notebook successfully and run a test cell

  **✓** Install GitHub Desktop and clone the course repository

  **✓** Verify you have Chapter 1 notebook and clean dataset

  **✓** Activate your DataCamp account and complete the first assigned
  module

  **✓** Read Chapter 1 materials before Class 2

  **✓** Take Quiz 1 on Friday (covers Chapter 1 material)
  -----------------------------------------------------------------------

If you encounter any technical problems during setup, contact the
instructor immediately. Do not wait until class starts.

  -------------------------------------------------------------------------
  **9**   **GETTING HELP**
  ------- -----------------------------------------------------------------

  -------------------------------------------------------------------------

You will get stuck. Everyone does. Here is how to get unstuck.

**Office Hours**

Office hours are listed on the syllabus and Moodle. Come prepared with
specific questions. Bring your laptop and show me what is not working.
Do not just say \"I don\'t get it.\" Tell me what you tried and where
you got stuck.

**Course Communication**

All course announcements will be posted in Moodle. Check Moodle daily.
For questions that benefit the entire class, post in the Moodle
discussion forum. For private matters, email the instructor directly.

**When to Use AI vs. Ask the Instructor**

Follow the CRAWL → WALK → RUN framework. During CRAWL phase work, do not
use AI. During WALK phase, you may use AI to explain concepts, but if
you are still confused after getting an AI explanation, come to office
hours. For assignment clarifications, grading questions, or course
policy questions, always ask the instructor directly.

**Peer Collaboration Guidelines**

You are encouraged to discuss concepts and approaches with classmates.
You may help each other debug errors and explain topics to each other.
You may NOT share code, look at another student\'s solution, or divide
up assignment work. The line is simple: discussing strategy is fine,
sharing implementations is cheating.

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

**CLOSING THOUGHTS**

BUAN 446 is challenging. The pace is fast, and the workload is
significant. You will feel frustrated at times. Your code will not work
on the first try, or the second, or sometimes the tenth. This is normal
and expected.

Programming is a skill that improves with deliberate practice. The
students who succeed in this course are not necessarily the ones with
the most natural aptitude. They are the ones who show up consistently,
put in the effort, ask for help when stuck, and persist through
frustration.

By the end of this course, you will have a marketable skill that
employers value. You will be able to clean messy datasets, perform
sophisticated analyses, and communicate insights effectively. That is
worth the struggle.

**Welcome to BUAN 446. *Let\'s get started.***
