# Three-Dataset Progression Guide

## Overview

This course uses **three distinct datasets** that progressively introduce complexity and analytical capability:

| Dataset | Variables | Records | Quality | Used In | Purpose |
|---------|-----------|---------|---------|---------|---------|
| **crestview_students_clean.csv** | 7 | 600 | Perfect | Weeks 1-2 | Learn Python fundamentals |
| **crestview_students_messy.csv** | 8 | 605 | 20+ issues | Week 3 | Learn data cleaning |
| **crestview_students_extended.csv** | 15 | 600 | Clean | Weeks 4+ | Perform rich analysis |

---

## The Learning Progression

### 📖 Phase 1: Weeks 1-2 (Foundation)
**Dataset:** `crestview_students_clean.csv` (7 variables)

**Learning Focus:** Python basics without data quality distractions
- Variables, data types, expressions
- Control flow (if/else, loops)
- Functions and modular programming
- Data structures (lists, dictionaries)
- Basic file I/O

**Why Clean Data?** Students need to master Python syntax and logic before dealing with messy reality. Clean data removes distraction and builds confidence.

---

### 🧹 Phase 2: Week 3 (Reality Check)
**Dataset:** `crestview_students_messy.csv` (8 variables)

**Learning Focus:** Real-world data is messy
- Identify 20+ types of data quality issues
- Text standardization and normalization
- Missing value handling
- Type conversion and validation
- Duplicate detection and removal

**The Message:** "This is what corporate data actually looks like. 60-80% of data analyst work is cleaning."

**Expected Output:** Students produce a cleaned version comparable to the original clean dataset.

---

### 📊 Phase 3: Weeks 4-6 (Reward & Depth)
**Dataset:** `crestview_students_extended.csv` (15 variables)

**Learning Focus:** Rich analytical capabilities
- NumPy: Correlations, statistical analysis
- Pandas: Multi-dimensional groupby, aggregations
- Matplotlib: Meaningful visualizations with real patterns
- Complete data analysis workflows

**The Reward:** "You proved you can clean messy data. Here's a clean, expanded dataset with interesting variables to explore."

**Key Insight:** After mastering data cleaning, students get clean data with MORE variables (15 vs 7). This shows the value of cleaning - you unlock richer analysis.

---

## Detailed Dataset Comparison

### Dataset 1: Clean (crestview_students_clean.csv)

**Structure:**
- 600 students
- 7 variables
- Zero data quality issues
- Perfect for learning

**Variables:**
1. Student_ID - Unique identifier (CU100001-CU100600)
2. College - Full official names
3. Major - Standardized major names
4. Class_Year - "First Year", "Sophomore", "Junior", "Senior", "Graduate"
5. GPA - 0.0 to 4.0, 2 decimal places
6. Credits_Attempted - Integer values
7. Credits_Earned - Integer values

**Use Cases:**
- Calculate average GPA by college
- Count students per major
- Find at-risk students (GPA < 2.0)
- Basic aggregations and filtering
- Practice loops and conditionals

---

### Dataset 2: Messy (crestview_students_messy.csv)

**Structure:**
- 605 students (includes 5 duplicates)
- 8 variables (7 original + Enrollment_Date)
- 20+ types of data quality issues
- Mirrors corporate reality

**Variables:**
1-7. (Same as clean, but with issues)
8. Enrollment_Date - NEW: Three different date formats

**Data Quality Issues:**
- ✗ Inconsistent college names ("COB", "Business", "college of business")
- ✗ Mixed case ("Senior", "senior", "SENIOR")
- ✗ Leading/trailing whitespace ("  Management  ")
- ✗ Missing values (GPA: 5%, Credits_Earned: 5%)
- ✗ Mixed text/numbers (Credits: "23 credits")
- ✗ Floating point errors (GPA: 3.8899999999999997)
- ✗ Date format chaos ("2021-08-15", "01-04-2021", "08/03/24")
- ✗ Impossible values (Credits_Earned > Credits_Attempted)
- ✗ Duplicate records (5 duplicates)
- ✗ Typos ("Computer Sceince")
- ✗ Class year variations ("Sr", "senior", "4th Year")

**Learning Objectives:**
Students must systematically:
1. Identify all issues through exploration
2. Standardize text fields (college names, class years)
3. Handle missing values (decide strategy per column)
4. Convert types (dates, numbers)
5. Validate constraints (earned <= attempted)
6. Remove duplicates
7. Export clean dataset
8. Document changes made

---

### Dataset 3: Extended (crestview_students_extended.csv)

**Structure:**
- 600 students
- 15 variables (7 original + 8 new)
- Clean, consistent formatting
- Rich analytical potential

**All Variables:**

**Original Core (1-7):**
1. Student_ID
2. College
3. Major
4. Class_Year
5. GPA
6. Credits_Attempted
7. Credits_Earned

**New Variables (8-15):**
8. **Enrollment_Date** - Clean ISO format (YYYY-MM-DD)
9. **Study_Hours_Per_Week** - Float, 2.0-45.0 range
10. **Campus_Housing** - "On-campus", "Off-campus", "Commuter"
11. **Financial_Aid** - "Yes", "No", "Partial"
12. **Extracurriculars** - Integer, 0-5 activities
13. **Part_Time_Job** - "No" or "Yes (Xh)" format
14. **First_Generation** - "Yes", "No", or blank (10% prefer not to answer)
15. **Distance_From_Home** - Integer, miles from home

**New Analysis Possibilities:**

*Correlations:*
- Does study time correlate with GPA?
- Do students who live on-campus study more?
- Does distance from home affect outcomes?

*Comparisons:*
- Do first-generation students have different success patterns?
- Does financial aid status correlate with GPA?
- Do students with part-time jobs perform differently?

*Multi-dimensional:*
- GPA by college AND housing type
- Study hours by class year AND extracurriculars
- Financial aid patterns across colleges

*Rich Visualizations:*
- Scatter: Study hours vs GPA
- Box plot: GPA distribution by housing type
- Stacked bar: Financial aid across colleges
- Heatmap: Correlation matrix of numeric variables

---

## The Pedagogical Design

### Why Three Datasets?

**Problem with Single Dataset:**
- Clean only → Students unprepared for reality
- Messy only → Students overwhelmed, can't learn basics
- One transitioning dataset → Confusing, hard to isolate issues

**Our Solution:**
1. **Start clean** - Build confidence and Python skills
2. **Introduce mess** - Show reality, teach cleaning systematically
3. **Reward with depth** - Provide richer, clean data for advanced analysis

### The Psychological Journey

**Weeks 1-2:** "Python is fun! Look what I can do with data!"

**Week 3:** "Wait, real data is THIS messy? This is frustrating!"
- The struggle is intentional
- 60-80% of analyst time is cleaning
- You need to experience this frustration
- By the end, you feel accomplished

**Weeks 4+:** "I earned this. Now I have clean, rich data to explore!"
- The expanded dataset feels like a reward
- You're ready for complex analysis
- You understand why data quality matters
- You can handle both clean and messy data

### Assessment Alignment

**Midterm (End of Week 3):**
- Tests: Python fundamentals (no AI)
- Project: Data cleaning (with AI collaboration)
- Students demonstrate both independent coding and AI-assisted work

**Final (End of Week 6):**
- Tests: Python + NumPy + Pandas (no AI)
- Project: Complete analysis using extended dataset (with AI)
- Students perform sophisticated analysis on rich, clean data

---

## Technical Implementation

### Loading Each Dataset

```python
import pandas as pd

# Week 1-2: Clean dataset
df_clean = pd.read_csv('data/crestview_students_clean.csv')
print(f"Clean: {len(df_clean)} rows, {len(df_clean.columns)} columns")

# Week 3: Messy dataset
df_messy = pd.read_csv('data/crestview_students_messy.csv')
print(f"Messy: {len(df_messy)} rows, {len(df_messy.columns)} columns")

# Week 4+: Extended dataset
df_extended = pd.read_csv('data/crestview_students_extended.csv')
print(f"Extended: {len(df_extended)} rows, {len(df_extended.columns)} columns")
```

### Week 3 Success Metric

After cleaning, students' output should match this structure:

```python
# Target: 600 rows, 8 clean columns
assert len(df_cleaned) == 600
assert df_cleaned['College'].nunique() == 5  # Five colleges
assert df_cleaned['GPA'].between(0, 4.0).all()
assert (df_cleaned['Credits_Earned'] <= df_cleaned['Credits_Attempted']).all()
```

### Week 4+ Analysis Examples

```python
# Correlation between study hours and GPA
correlation = df_extended['Study_Hours_Per_Week'].corr(df_extended['GPA'])

# Average GPA by housing type
df_extended.groupby('Campus_Housing')['GPA'].mean()

# First-gen outcomes
df_extended.groupby('First_Generation')['GPA'].describe()

# Financial aid distribution by college
pd.crosstab(df_extended['College'], df_extended['Financial_Aid'])
```

---

## Instructor Notes

### Dataset Reveal Strategy

**Week 1:** Introduce clean dataset. "This is your case study for the course."

**Week 2:** Continue with clean dataset. Students feel confident.

**Week 3 Start:** "By the way, real corporate data doesn't look like this. Here's a messy version. Your job is to make it look like the clean version."

**Week 3 End:** "Great work cleaning that data. Want to see something cool?"

**Week 4:** "Since you proved you can handle messy data, here's a reward: a clean dataset with WAY more interesting variables. Now let's do real analysis."

### Common Student Reactions

**After Week 3:** "That was so much work! Is this really what analysts do?"
- Yes, data cleaning is 60-80% of the job
- You now understand why data quality matters
- You have skills most business graduates don't

**After Week 4:** "Wait, this clean extended dataset is amazing! I can answer so many questions!"
- That's the reward for mastering cleaning
- Clean data with rich variables enables sophisticated analysis
- You now appreciate both the struggle and the payoff

### Files Provided

**Datasets:**
1. crestview_students_clean.csv - 600 students, 7 variables
2. crestview_students_messy.csv - 605 students, 8 variables
3. crestview_students_extended.csv - 600 students, 15 variables

**Generation Scripts:**
4. generate_student_data.py - Recreate clean dataset
5. generate_messy_data.py - Recreate messy dataset

**Documentation:**
7. dataset_documentation.md - Clean dataset guide
8. messy_dataset_guide.md - Messy dataset issues reference
9. three_dataset_guide.md - This document

---

## FAQ

**Q: Why not just use the messy dataset throughout?**
A: Students need to master Python basics before dealing with data quality issues. Trying to learn both simultaneously is overwhelming.

**Q: Why not add the extra variables to the messy dataset?**
A: Week 3 is already challenging with 8 variables and 20+ issues. Adding 15 variables with 30+ issues would be overwhelming. The progression is intentional.

**Q: Can students use the extended dataset in Week 3?**
A: No. They need to complete the cleaning challenge first. The extended dataset is their reward for mastering data cleaning.

**Q: What if students struggle with the messy dataset?**
A: That's expected and intentional. Provide support, but let them struggle a bit. The struggle builds resilience and appreciation for data quality.

**Q: Should we tell students about the extended dataset upfront?**
A: No. Surprise them with it after Week 3. The reveal is pedagogically powerful: "You earned this."

---

## Success Metrics

### By End of Week 2
- ✓ Students comfortable with Python basics
- ✓ Can analyze clean data confidently
- ✓ Ready for the complexity ahead

### By End of Week 3
- ✓ Students understand data quality challenges
- ✓ Can systematically clean messy data
- ✓ Appreciate why 60-80% of analyst work is cleaning
- ✓ Feel accomplished after producing clean output

### By End of Week 6
- ✓ Students perform sophisticated multi-dimensional analysis
- ✓ Create meaningful visualizations with real patterns
- ✓ Answer complex research questions
- ✓ Ready for corporate data analyst roles

---

**The Bottom Line:** Three datasets provide a structured progression from Python basics → data cleaning reality → sophisticated analysis. Each serves a specific pedagogical purpose, and the progression maximizes both learning and confidence-building.
