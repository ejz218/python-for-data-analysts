# Lehigh University Student Dataset - Documentation

## Overview
This is a synthetic dataset created for educational purposes in BUAN 446 (Python for Data Analysts). It contains fictional student records with realistic patterns based on typical university distributions.

**This dataset is entirely synthetic. No real student information is included.**

---

## Three-Dataset Progression

This course uses **three distinct datasets** that progressively introduce complexity:

| Dataset | Variables | Records | Quality | Used In | Purpose |
|---------|-----------|---------|---------|---------|---------|
| **lehigh_students_clean.csv** | 7 | 600 | Perfect | Chapters 1-5 | Learn Python fundamentals |
| **lehigh_students_messy.csv** | 8 | 605 | 20+ issues | Chapter 5 (Midterm) | Learn data cleaning |
| **lehigh_students_extended.csv** | 15 | 600 | Clean | Chapters 6-9 | Perform rich analysis |

### Why Three Datasets?

1. **Start clean** (Chapters 1-5) - Build confidence and Python skills without data quality distractions
2. **Introduce mess** (Chapter 5) - Experience what real corporate data looks like; learn to clean it systematically
3. **Reward with depth** (Chapters 6-9) - After proving you can handle messy data, get a clean, expanded dataset with interesting new variables to explore

### Which Dataset Should I Use?

- **Chapters 1-4:** `lehigh_students_clean.csv`
- **Chapter 5 / Midterm project:** `lehigh_students_messy.csv`
- **Chapters 6-9 / Final project:** `lehigh_students_extended.csv`

---

## Dataset 1: Clean (`lehigh_students_clean.csv`)

**Records:** 600 students
**Variables:** 7 columns
**Quality:** No issues - ready for immediate analysis

### Data Dictionary

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| Student_ID | String | Unique anonymous identifier | LU100001, LU100002 |
| College | String | Lehigh college affiliation | "College of Business", "P.C. Rossin College of Engineering" |
| Major | String | Student's declared major | "Computer Science", "Finance", "Biology" |
| Class_Year | String | Current academic standing | "First Year", "Sophomore", "Junior", "Senior", "Graduate" |
| GPA | Float | Grade Point Average (0.0-4.0 scale) | 3.41, 2.87, 4.00 |
| Credits_Attempted | Integer | Total credit hours attempted | 105, 52, 89 |
| Credits_Earned | Integer | Total credit hours successfully earned | 99, 44, 81 |

### Loading

```python
# Pure Python (Chapters 1-5)
import csv
with open('data/lehigh_students_clean.csv', 'r') as file:
    reader = csv.DictReader(file)
    students = list(reader)

# Pandas (Chapter 7+)
import pandas as pd
df = pd.read_csv('data/lehigh_students_clean.csv')
```

---

## Dataset 2: Messy (`lehigh_students_messy.csv`)

**Records:** 605 students (includes 5 duplicates)
**Variables:** 8 columns (adds Enrollment_Date)
**Quality:** Intentionally degraded with 20+ types of data issues

This dataset mirrors what real corporate data looks like. See `messy_dataset_guide.md` for a complete catalog of every data quality issue and cleaning strategies.

### Key Issues

- Inconsistent college names (28 variations)
- Inconsistent class year labels (23 variations)
- Missing values (~6% of records)
- Extra whitespace (151 records)
- Mixed date formats (3+ formats)
- Typos in major names
- Numeric data stored as text
- Impossible values (GPA > 4.0, negative credits)
- 5 duplicate records

### Loading

```python
import pandas as pd
df_messy = pd.read_csv('data/lehigh_students_messy.csv')
print(df_messy.info())           # Notice object dtypes where you expect numbers
print(df_messy['College'].value_counts())  # Notice 28 variations instead of 5
```

---

## Dataset 3: Extended (`lehigh_students_extended.csv`)

**Records:** 600 students
**Variables:** 15 columns (7 original + 8 new)
**Quality:** Clean, consistent formatting

This is the same 600 students from the clean dataset, enriched with 8 additional variables that enable deeper analysis.

### Data Dictionary

#### Original Core Variables (1-7)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| Student_ID | String | Unique anonymous identifier | LU100001, LU100002 |
| College | String | Lehigh college affiliation | "College of Business" |
| Major | String | Student's declared major | "Accounting", "Computer Science" |
| Class_Year | String | Current academic standing | "First Year", "Senior", "Graduate" |
| GPA | Float | Grade Point Average (0.0-4.0) | 3.41, 2.87, 4.00 |
| Credits_Attempted | Integer | Total credit hours attempted | 105, 52, 89 |
| Credits_Earned | Integer | Total credit hours successfully earned | 99, 44, 81 |

#### New Variables (8-15)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| Enrollment_Date | String | First enrollment date (ISO format) | "2021-01-24", "2023-08-15" |
| Study_Hours_Per_Week | Float | Self-reported weekly study hours | 14.2, 8.5, 32.0 (range: 2.0-45.0) |
| Campus_Housing | String | Living situation | "On-campus", "Off-campus", "Commuter" |
| Financial_Aid | String | Financial aid status | "Yes", "No", "Partial" |
| Extracurriculars | Integer | Number of extracurricular activities | 0, 3, 5 (range: 0-5) |
| Part_Time_Job | String | Part-time employment status | "No", "Yes (18h)", "Yes (10h)" |
| First_Generation | String | First-generation college student | "Yes", "No", or blank (~10% prefer not to answer) |
| Distance_From_Home | Integer | Miles from home address | 19, 450, 2300 |

### New Analysis Possibilities

**Correlations:**
- Does study time correlate with GPA?
- Do students who live on-campus study more?
- Does distance from home affect outcomes?

**Comparisons:**
- Do first-generation students have different success patterns?
- Does financial aid status correlate with GPA?
- Do students with part-time jobs perform differently?

**Multi-dimensional:**
- GPA by college AND housing type
- Study hours by class year AND extracurriculars
- Financial aid patterns across colleges

**Visualizations:**
- Scatter: Study hours vs GPA
- Box plot: GPA distribution by housing type
- Stacked bar: Financial aid across colleges
- Heatmap: Correlation matrix of numeric variables

### Loading

```python
import pandas as pd
df = pd.read_csv('data/lehigh_students_extended.csv')
print(f"{len(df)} students, {len(df.columns)} variables")
print(df.describe())
```

---

## Colleges and Majors

### College of Business (109 students)
- Accounting
- Finance
- Marketing
- Supply Chain Management
- Business Analytics
- Management
- Economics

### P.C. Rossin College of Engineering (114 students)
- Computer Science
- Mechanical Engineering
- Civil Engineering
- Electrical Engineering
- Chemical Engineering
- Industrial Engineering
- Computer Engineering
- Bioengineering

### College of Arts and Sciences (121 students)
- Biology
- Chemistry
- Psychology
- English
- Mathematics
- Physics
- Political Science
- Sociology
- History
- Philosophy

### College of Health (135 students)
- Health Science
- Public Health
- Nursing
- Community Health

### College of Education (121 students)
- Elementary Education
- Secondary Education
- Special Education

---

## Dataset Characteristics

### Class Year Distribution
- First Year: 135 students (22.5%)
- Sophomore: 121 students (20.2%)
- Junior: 133 students (22.2%)
- Senior: 137 students (22.8%)
- Graduate: 74 students (12.3%)

### GPA Statistics
- Average: 3.27
- Minimum: 1.69
- Maximum: 4.00
- Pattern: Graduate students and upper-class students tend to have higher GPAs

### Credits Statistics
- Average Credits Attempted: 62.2
- Average Credits Earned: 56.9
- Overall Completion Rate: 91.4%
- Pattern: Credits increase with class year; graduate students have fewer credits (different scale)

### Realistic Patterns Built Into the Data

1. **GPA Progression:** Older students tend to have slightly higher GPAs than first-years
2. **Credit Accumulation:** Credits attempted and earned increase with class year
3. **Completion Rate:** Most students earn 85-100% of attempted credits
4. **Graduate Students:** Have fewer credits (9-36) as they're on a different scale
5. **Study Hours:** Correlate positively with GPA (in extended dataset)
6. **Housing:** On-campus students tend to be earlier in their academic careers

---

## Quick Reference Card: Extended Dataset (15 Variables)

*Print this page and keep it next to your notebook during Chapters 6-9.*

**File:** `data/lehigh_students_extended.csv` | **Records:** 600 | **Quality:** Clean

| # | Variable | Type | Description | Example Values | Range/Categories |
|---|----------|------|-------------|----------------|------------------|
| 1 | Student_ID | str | Unique identifier | LU100001 | LU100001-LU100600 |
| 2 | College | str | Lehigh college | College of Business | 5 colleges |
| 3 | Major | str | Declared major | Computer Science | ~30 majors |
| 4 | Class_Year | str | Academic standing | Junior | First Year, Sophomore, Junior, Senior, Graduate |
| 5 | GPA | float | Grade point average | 3.41 | 0.0 - 4.0 |
| 6 | Credits_Attempted | int | Credits attempted | 105 | 9 - 135 |
| 7 | Credits_Earned | int | Credits earned | 99 | 6 - 132 |
| 8 | Enrollment_Date | str | First enrollment (ISO) | 2021-01-24 | 2019 - 2025 |
| 9 | Study_Hours_Per_Week | float | Weekly study hours | 14.2 | 2.0 - 45.0 |
| 10 | Campus_Housing | str | Living situation | On-campus | On-campus, Off-campus, Commuter |
| 11 | Financial_Aid | str | Aid status | Partial | Yes, No, Partial |
| 12 | Extracurriculars | int | Activity count | 3 | 0 - 5 |
| 13 | Part_Time_Job | str | Employment status | No | No, Yes (10h), Yes (18h), etc. |
| 14 | First_Generation | str | First-gen student | Yes | Yes, No, or blank (~10% missing) |
| 15 | Distance_From_Home | float | Miles from home | 450 | ~5 - 3000 |

### Numeric Columns (for correlations, statistics, arrays)
`GPA`, `Credits_Attempted`, `Credits_Earned`, `Study_Hours_Per_Week`, `Extracurriculars`, `Distance_From_Home`

### Categorical Columns (for groupby, value_counts, bar/box plots)
`College`, `Major`, `Class_Year`, `Campus_Housing`, `Financial_Aid`, `Part_Time_Job`, `First_Generation`

### Common Derived Variables
| Variable | Formula | Purpose |
|----------|---------|---------|
| Completion_Rate | Credits_Earned / Credits_Attempted | Academic efficiency |
| Study_Efficiency | GPA / Study_Hours_Per_Week | GPA per study hour |
| Has_Job | Part_Time_Job != "No" | Boolean employment flag |
| Academic_Standing | GPA >= 3.5 → Dean's List; >= 2.0 → Good Standing; < 2.0 → Probation | Performance tier |
| At_Risk | GPA < 2.0 OR Completion_Rate < 0.85 OR Study_Hours < 5 | Early warning flag |

---

## Ethical Considerations

When discussing this dataset, remember:
- **This is entirely synthetic data.** No real student information is included.
- Real student data is protected by FERPA
- Analysis of student data can reveal sensitive patterns
- Predictions about student success must be used carefully to avoid bias
- Privacy and consent are critical in educational data

---

## Technical Notes

- **Encoding:** UTF-8
- **Delimiter:** Comma
- **Decimal Separator:** Period
- **Header Row:** Yes (row 1)
- **Data Starts:** Row 2

---

## Files in This Directory

**Datasets:**
1. `lehigh_students_clean.csv` - 600 students, 7 variables
2. `lehigh_students_messy.csv` - 605 students, 8 variables
3. `lehigh_students_extended.csv` - 600 students, 15 variables

**Generation Scripts:**
4. `generate_student_data.py` - Recreate clean dataset
5. `generate_messy_data.py` - Recreate messy dataset

**Documentation:**
6. `dataset_documentation.md` - This document (comprehensive reference)
7. `messy_dataset_guide.md` - Detailed guide to messy dataset issues and cleaning strategies
8. `dataset_comparison.md` - Side-by-side clean vs messy comparison
9. `three_dataset_guide.md` - Instructor-facing pedagogical design notes

---

## Version History

- **v1.0 (Clean):** 600 students, 7 core variables, no data quality issues
- **v1.0 (Messy):** 605 students, 8 variables, 20+ intentional data quality issues
- **v1.0 (Extended):** 600 students, 15 variables, clean formatting, rich analysis potential

---

## Questions or Issues?

This dataset was created specifically for BUAN 446. For questions about the data structure, realistic patterns, or suggestions for additional variables, contact the course instructor.
