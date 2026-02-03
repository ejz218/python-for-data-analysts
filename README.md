# BUAN 446: Python for Data Analysts

**Lehigh University Graduate Course**  
6-week intensive | 4 days/week | 1.75 hours per session

## Course Overview

This repository contains comprehensive course materials for BUAN 446, a graduate-level Python course designed for first-year data analytics students. The course covers the first nine chapters of "Intro to Python for Computer Science and Data Science" with a focus on practical data analysis skills.

## Pedagogical Framework: CRAWL → WALK → RUN

This course implements a structured three-tier approach to AI integration in learning:

### 🐛 CRAWL Phase: Independent Learning
- **No AI assistance permitted**
- Students build foundational skills through direct practice
- DataCamp courses and textbook readings provide guided support
- Ensures mastery of core concepts needed for assessments

### 🚶 WALK Phase: AI as Learning Partner
- **AI permitted for understanding concepts only**
- Students use AI to clarify concepts, debug syntax, and explore alternatives
- Students must write their own code and understand their solutions
- Builds critical thinking about when and how to use AI effectively

### 🏃 RUN Phase: Full AI Collaboration
- **Full AI assistance permitted on projects**
- Students collaborate with AI to solve complex, real-world problems
- Emphasis on strategic thinking, problem decomposition, and validation
- Prepares students for professional data analyst workflows

**Assessment Balance**: Projects encourage AI collaboration while midterm and final exams are administered without AI access, ensuring students can demonstrate core competencies independently.

## Repository Structure

```
buan446-python-for-data-analysts/
├── chapters/               # Interactive Jupyter notebooks for each chapter
├── assessments/           # Quizzes and exams (Moodle XML + Jupyter notebooks)
├── assignments/           # Weekly assignments and projects
├── data/                  # Course datasets (clean and messy versions)
└── README.md
```

## Course Content

### Completed Chapters (1-5)

**Chapter 1: Python Fundamentals**
- Variables, data types, and expressions
- Basic input/output operations
- Introduction to the Lehigh student dataset

**Chapter 2: Control Flow**
- Conditional statements (if/elif/else)
- Iteration with for and while loops
- Loop control mechanisms

**Chapter 3: Functions**
- Function definition and calling
- Parameters, arguments, and return values
- Scope and modular programming

**Chapter 4: Data Structures**
- Lists, tuples, sets, and dictionaries
- Data structure operations and methods
- Choosing appropriate structures for tasks

**Chapter 5: File I/O and Exception Handling**
- Reading and writing text files
- CSV file processing
- Error handling with try/except blocks

### Future Chapters (6-9)

- Chapter 6: NumPy for numerical computing
- Chapter 7: Pandas for data manipulation
- Chapter 8: Data visualization with Matplotlib/Seaborn
- Chapter 9: Complete data analysis workflows

## Case Study: Lehigh University Student Data

The course centers on a comprehensive synthetic dataset representing Lehigh University students:

**Clean Dataset** (`lehigh_students_clean.csv`)
- 600 student records
- 7 variables: Student_ID, College, Major, Class_Year, GPA, Credits_Attempted, Credits_Earned
- Used for learning Python fundamentals and analysis techniques

**Messy Dataset** (`lehigh_students_messy.csv`)
- 605 records with 28+ intentional data quality issues
- Realistic problems: inconsistent formatting, missing values, duplicates, invalid entries
- Mirrors real-world corporate data environments where 60-80% of analyst time involves data cleaning
- Used for Week 3 data cleaning assignment and real-world practice

### Data Quality Issues Include:
- Inconsistent college name formatting (abbreviations, capitalization)
- Mixed case in categorical variables
- Missing values in various columns
- Duplicate student records
- Invalid GPA values (>4.0, negative numbers)
- Credits_Attempted stored as strings with formatting issues
- Invalid enrollment dates
- Extra whitespace and formatting inconsistencies

## Assessment Structure

### Quizzes (CRAWL Phase - No AI)
- Week 1: Chapters 1-2 (10 multiple choice questions)
- Week 2: Chapter 3 (10 multiple choice questions)
- Week 3: Chapters 4-5 (10 multiple choice questions)

### Midterm Exam (No AI)
**Part 1: Proctored Component**
- Multiple choice and short answer questions
- Covers Chapters 1-5 comprehensively
- Tests fundamental Python skills and concepts

**Part 2: Take-Home Project**
- Jupyter notebook-based analysis
- Uses clean Lehigh student dataset
- Demonstrates ability to apply concepts independently

### Assignments (RUN Phase - Full AI Collaboration)
**Week 3: Data Cleaning Project** (100+ points)
- Six progressive parts guiding students through data quality challenges
- Inspect, clean, and validate the messy Lehigh student dataset
- Requires strategic decision-making and documentation of cleaning choices

## Learning Objectives

By the end of this course, students will be able to:

1. Write clean, efficient Python code for data analysis tasks
2. Apply appropriate data structures to solve real-world problems
3. Read, process, and validate data from various file formats
4. Identify and correct data quality issues systematically
5. Use AI tools strategically while maintaining independent problem-solving skills
6. Document and communicate data analysis processes effectively

## Technical Requirements

- **Python**: 3.8 or higher
- **Required Libraries**: pandas, numpy, matplotlib, seaborn
- **Development Environment**: Jupyter Notebook or JupyterLab
- **Recommended IDE**: VS Code with Python extension, or Anaconda Navigator

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/buan446-python-for-data-analysts.git
cd buan446-python-for-data-analysts

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install jupyter pandas numpy matplotlib seaborn
```

## Usage

### For Students

1. Start with Chapter 1 and progress sequentially
2. Follow the CRAWL → WALK → RUN framework for each topic
3. Complete DataCamp courses before attempting chapter exercises
4. Practice with the clean dataset before tackling messy data challenges
5. Document your learning process and AI interactions

### For Instructors

This repository can be adapted for your own Python for Data Analytics courses:

- Modify the case study dataset to fit your institution or domain
- Adjust the AI integration framework to match your pedagogical goals
- Customize assessment difficulty and point values
- Add or remove chapters based on semester length

## Data Privacy Note

All student data in this repository is **100% synthetic** and generated specifically for educational purposes. No real student information is included. The data is designed to be realistic enough for learning while maintaining complete privacy.

## Contributing

This is an educational repository. If you find errors or have suggestions for improvements:

1. Open an issue describing the problem or enhancement
2. For significant changes, please discuss in an issue before submitting a pull request
3. Follow existing code style and documentation patterns

## License

This course material is provided for educational purposes. Please contact the course instructor before using or adapting materials for other courses.

## Contact

**Course Instructor**: Eric Hollow  
**Institution**: Lehigh University  
**Course**: BUAN 446 - Python for Data Analysts

## Acknowledgments

- Course content based on "Intro to Python for Computer Science and Data Science"
- DataCamp integration for supplementary learning resources
- Lehigh University College of Business for supporting innovative AI-integrated pedagogy

---

*Last Updated: February 2026*
