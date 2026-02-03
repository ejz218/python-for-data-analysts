# Lehigh University Student Dataset - Documentation

## Overview
This is a synthetic dataset created for educational purposes in BUAN 446 (Python for Data Analysts). It contains 600 fictional student records with realistic patterns based on typical university distributions.

**Dataset:** lehigh_students_clean.csv  
**Records:** 600 students  
**Variables:** 7 columns  
**Format:** CSV (comma-separated values)

---

## Data Dictionary

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| Student_ID | String | Unique anonymous identifier | LU100001, LU100002 |
| College | String | Lehigh college affiliation | "College of Business", "P.C. Rossin College of Engineering" |
| Major | String | Student's declared major | "Computer Science", "Finance", "Biology" |
| Class_Year | String | Current academic standing | "First Year", "Sophomore", "Junior", "Senior", "Graduate" |
| GPA | Float | Grade Point Average (0.0-4.0 scale) | 3.41, 2.87, 4.00 |
| Credits_Attempted | Integer | Total credit hours attempted | 105, 52, 89 |
| Credits_Earned | Integer | Total credit hours successfully earned | 99, 44, 81 |

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
- Pattern: Credits increase with class year, Graduate students have fewer credits (different scale)

---

## Realistic Patterns Built Into the Data

1. **GPA Progression:** Older students (juniors, seniors, graduates) tend to have slightly higher GPAs than first-years
2. **Credit Accumulation:** Credits attempted and earned increase with class year
3. **Completion Rate:** Most students earn 85-100% of attempted credits, reflecting typical success rates
4. **Graduate Students:** Have fewer credits (9-36) as they're on a different scale than undergraduates

---

## Data Quality Notes

This is the "clean" version suitable for Week 1-2 of the course:
- No missing values
- Consistent formatting
- All values are valid and within expected ranges
- No duplicate records
- Standard CSV format with headers

Future versions of this dataset will intentionally include:
- Missing values
- Inconsistent text formatting
- Data entry errors
- Outliers
- Additional variables

---

## Suggested Analysis Questions for Students

### Week 1 (Basic Python)
1. What is the average GPA across all students?
2. How many students are in each college?
3. What is the total number of credits attempted by all students?

### Week 2 (Control Structures)
4. How many students have a GPA above 3.5?
5. Which students are on academic probation (GPA < 2.0)?
6. What percentage of students earn 90% or more of their attempted credits?

### Week 3 (Data Structures & Files)
7. Create a list of all unique majors
8. Count how many students are in each major
9. Find the student with the highest GPA in each college

### Week 4 (NumPy)
10. Calculate mean and standard deviation of GPA by class year
11. Find students who are statistical outliers in credits attempted
12. Calculate correlation between credits attempted and GPA

### Week 5 (Pandas)
13. Group students by college and calculate average GPA for each
14. Identify which majors have the highest average completion rates
15. Analyze the relationship between class year and academic performance

### Week 6 (Visualization)
16. Create bar chart showing average GPA by college
17. Visualize the distribution of students across class years
18. Show the relationship between credits attempted and credits earned

---

## Usage in Course

This dataset is designed to grow with the course:
- **Weeks 1-2:** Use as-is for basic operations and simple analysis
- **Weeks 3-4:** Introduce "messy" versions with data quality issues
- **Weeks 5-6:** Add additional variables for more complex analysis

Students should be able to:
1. Load and explore the data
2. Calculate basic statistics
3. Filter and subset the data
4. Group and aggregate by categories
5. Visualize patterns and trends
6. Draw insights about student success factors

---

## Ethical Considerations

**This is entirely synthetic data.** No real student information is included.

When discussing this dataset, instructors should remind students:
- Real student data is protected by FERPA
- Analysis of student data can reveal sensitive patterns
- Predictions about student success must be used carefully to avoid bias
- Privacy and consent are critical in educational data

---

## Technical Notes

- **Encoding:** UTF-8
- **Line Endings:** CRLF (Windows-style, compatible with Excel)
- **Delimiter:** Comma
- **Decimal Separator:** Period
- **Header Row:** Yes (row 1)
- **Data Starts:** Row 2

**Python Loading:**
```python
import pandas as pd
df = pd.read_csv('lehigh_students_clean.csv')
```

**Excel:** Can be opened directly in Excel or Google Sheets

---

## Version History

- **v1.0 (Clean):** Initial dataset with 600 students, 7 core variables, no data quality issues
- Future versions will add complexity for later weeks of the course

---

## Questions or Issues?

This dataset was created specifically for BUAN 446. For questions about the data structure, realistic patterns, or suggestions for additional variables, contact the course instructor.
