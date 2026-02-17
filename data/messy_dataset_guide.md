# Lehigh University Student Dataset - MESSY VERSION
## Data Cleaning Exercise for Week 3+

## Overview
This is the MESSY version of the student dataset, intentionally containing realistic data quality issues that students will encounter in professional data analysis work. This dataset should be used starting in Week 3 when students learn about data wrangling and cleaning.

**Dataset:** lehigh_students_messy.csv  
**Records:** 605 students (includes 5 duplicates)  
**Variables:** 8 columns (added Enrollment_Date)  
**Quality:** Intentionally degraded with 10+ types of data issues

---

## Data Quality Issues Present

### 1. Inconsistent College Names (28 variations)
**Problem:** Same college written multiple ways
```
Standard: "College of Business"
Variations found:
  - "COB" (abbreviation)
  - "Business" 
  - "college of business" (lowercase)
  - "College Of Business" (different capitalization)
  - "Buisness" (typo)
```

**Other examples:**
- Engineering: "RCOE", "engineering", "Rossin College of Engineering"
- Arts & Sciences: "CAS", "A&S", "Arts and Sciences"
- Education: "COE", "Ed"
- Health: "COH", "Health College"

**Cleaning Task:** Standardize all to official names
**AI Assistance (WALK):** Ask "How do I use pandas replace() to standardize college names?"

---

### 2. Inconsistent Class Year Labels (23 variations)
**Problem:** Multiple formats for same class standing
```
Standard: "First Year"
Variations found:
  - "Freshman"
  - "1st Year"
  - "Fr"
  - "first year" (lowercase)
```

**All variations:**
- First Year: "Freshman", "1st Year", "Fr", "first year"
- Sophomore: "Soph", "2nd Year", "sophomore"
- Junior: "Jr", "3rd Year", "junior"
- Senior: "Sr", "4th Year", "senior"
- Graduate: "Grad", "Masters", "Master's", "PhD", "graduate"

**Cleaning Task:** Standardize to consistent format
**AI Assistance (WALK):** Ask "What's the best way to map multiple variations to a standard value in pandas?"

---

### 3. Missing Values (~6% of records)
**Problem:** Empty cells where data should exist

**Missing data counts:**
- GPA: 35 records missing (5.8%)
- Credits_Earned: 36 records missing (6.0%)

**Examples:**
```csv
LU100004,Arts and Sciences,History,First Year,,22,21,2024-08-27
LU100011,College of Education,Elementary Education,PhD,,14,12,2023-08-28
```

**Cleaning Tasks:**
1. Identify which records have missing data
2. Decide how to handle (drop? impute? flag?)
3. Document your decision

**AI Assistance (WALK):** Ask "What are different strategies for handling missing GPA values in a dataset?"

---

### 4. Extra Whitespace (151 records affected)
**Problem:** Leading or trailing spaces in text fields

**Examples:**
```csv
"  P.C. Rossin College of Engineering  "  (spaces around entire string)
"  Civil Engineering  "  (spaces around major)
"  junior  "  (spaces around class year)
" 3.21"  (space before GPA)
```

**Impact:** These look the same to humans but are different to computers
- "Engineering" ≠ "  Engineering  " (won't match in groupby operations)

**Cleaning Task:** Strip whitespace from all text columns
**AI Assistance (WALK):** Ask "How do I remove leading and trailing whitespace from all string columns in pandas?"

---

### 5. Inconsistent Date Formats (3+ formats)
**Problem:** Enrollment_Date stored in multiple formats

**Formats found:**
```
2021-01-14         (ISO format: YYYY-MM-DD)
09-01-2021         (MM-DD-YYYY)
08/17/24           (MM/DD/YY - short year)
```

**Impact:** 
- Can't sort dates correctly
- Can't calculate time since enrollment
- Excel might interpret dates incorrectly

**Cleaning Task:** Convert all dates to consistent format (preferably ISO: YYYY-MM-DD)
**AI Assistance (WALK):** Ask "How do I parse dates in different formats using pandas to_datetime()?"

---

### 6. Data Entry Errors - Typos in Majors
**Problem:** Misspelled major names

**Examples:**
```
"Computer Sceince" should be "Computer Science"
"Psycology" should be "Psychology"
"Business Analystics" should be "Business Analytics"
"Mech Engineering" should be "Mechanical Engineering"
"Bioligy" should be "Biology"
"Finace" should be "Finance"
"Marketting" should be "Marketing"
```

**Cleaning Task:** Find and correct typos
**AI Assistance (WALK):** Ask "How can I find similar strings that might be typos in pandas?"

---

### 7. Numeric Data as Text
**Problem:** Numbers stored with extra text or formatting

**Examples:**
```
Credits_Attempted: "23 credits" (should be 23)
GPA: " 3.21" (extra space makes it text)
GPA: "3.410" (too many decimal places)
```

**Impact:**
- Can't calculate statistics (mean, sum, etc.)
- Comparison operations fail
- Type errors in code

**Cleaning Task:** Extract numeric values and convert to proper type
**AI Assistance (WALK):** Ask "How do I extract numbers from strings that contain text in pandas?"

---

### 8. Impossible/Outlier Values
**Problem:** Values outside valid ranges

**Issues found:**
- GPA > 4.0: 8 records (impossible on 4.0 scale)
- GPA = "5.0" (data entry error)
- Credits_Attempted = "-10" (negative number)
- Credits_Earned > Credits_Attempted (earned more than attempted)

**Examples:**
```csv
LU100XXX,College of Business,Finance,Senior,5.0,105,99,2021-08-01
LU100YYY,Engineering,Computer Science,Junior,3.2,-10,30,2022-08-01
```

**Cleaning Tasks:**
1. Identify outliers
2. Determine if they're errors or legitimate special cases
3. Decide how to handle (correct? remove? flag?)

**AI Assistance (WALK):** Ask "How do I identify values outside expected ranges in a pandas DataFrame?"

---

### 9. Duplicate Records (5 duplicates)
**Problem:** Same student appears twice with slight differences

**Example pattern:**
```csv
LU100123,College of Business,Finance,Senior,3.41,105,99,2021-08-01
LU100123,College of Business,Finance,Senior,3.42,105,100,2021-08-01
```
(Same ID, but slightly different GPA or credits)

**Impact:**
- Inflates counts
- Skews statistics
- Which record is correct?

**Cleaning Task:** Identify duplicates and decide how to handle
**AI Assistance (WALK):** Ask "How do I find duplicate records based on Student_ID in pandas?"

---

### 10. Inconsistent Null Representations
**Problem:** Missing data represented multiple ways

**Variations found:**
```
""           (empty string)
" "          (space)
"N/A"        (text)
None         (Python None)
NaN          (after pandas loads)
```

**Cleaning Task:** Standardize missing value representation
**AI Assistance (WALK):** Ask "How do I replace various null representations with pandas NaN?"

---

## Cleaning Strategy for Students

### Week 3: Basic Cleaning (WALK Mode)

**Exercise 1: Inspect the Data**
```python
# Load and examine
import pandas as pd
df = pd.read_csv('data/lehigh_students_messy.csv')

# What do you notice?
print(df.info())
print(df['College'].value_counts())
print(df['Class_Year'].value_counts())
```

**Exercise 2: Fix One Issue at a Time**

Start with easiest issues first:
1. Strip whitespace
2. Standardize college names
3. Standardize class year labels
4. Handle missing values
5. Fix date formats
6. Correct typos
7. Validate numeric ranges

**Exercise 3: Document Your Cleaning**
Keep a log of what you changed and why:
```python
# Example cleaning log
print("Original records:", len(df))
print("Records with missing GPA:", df['GPA'].isna().sum())

# After cleaning
print("After dropping missing GPA:", len(df_clean))
print("Records removed:", len(df) - len(df_clean))
```

---

## AI Collaboration Guidelines (WALK Mode)

### ✅ Good AI Usage:
- "How do I check for missing values in pandas?"
- "What's the difference between .replace() and .map() in pandas?"
- "Show me how to strip whitespace from a column"
- "Explain this error: ValueError: could not convert string to float"
- "What are best practices for handling duplicate records?"

### ❌ Poor AI Usage:
- "Clean this entire dataset for me" (too broad, you learn nothing)
- "Write code to fix all my data problems" (you need to understand each issue)
- "Here's my messy data, make it perfect" (skips learning process)

### 🎯 Best Approach:
1. Identify ONE specific data quality issue
2. Ask AI how to solve THAT specific issue
3. Write the code yourself based on AI's explanation
4. Test your solution
5. Move to next issue
6. Repeat

---

## Expected Outcomes After Cleaning

Your clean dataset should have:
- ✓ Exactly 600 unique student records (5 duplicates removed)
- ✓ All college names in standard format (5 official names only)
- ✓ All class years in standard format (5 categories only)
- ✓ No leading/trailing whitespace in text fields
- ✓ All dates in consistent format (YYYY-MM-DD recommended)
- ✓ GPA values between 0.0 and 4.0 (or missing)
- ✓ Credits_Earned ≤ Credits_Attempted
- ✓ All numeric columns have proper data types (float, int)
- ✓ Documented decision about missing values

---

## Week 4+ Advanced Cleaning

Once basic cleaning is complete, students can:
- Calculate completion rate: `Credits_Earned / Credits_Attempted`
- Add derived columns: `Years_Enrolled` from Enrollment_Date
- Flag at-risk students: `GPA < 2.0`
- Create groupings: `High_Achiever` for `GPA > 3.5`

---

## Assessment Rubric

When students submit cleaned data, check for:

**Basic Cleaning (70%):**
- [ ] Whitespace removed
- [ ] College names standardized (5 categories)
- [ ] Class years standardized (5 categories)  
- [ ] Dates in consistent format
- [ ] Duplicates handled
- [ ] Typos corrected

**Data Validation (20%):**
- [ ] GPA values validated (0.0-4.0)
- [ ] Credits relationship validated (earned ≤ attempted)
- [ ] Missing values identified and handled
- [ ] Numeric columns have correct data types

**Documentation (10%):**
- [ ] Cleaning steps documented
- [ ] Decisions about missing data explained
- [ ] Number of records affected by each change noted

---

## Comparison Files

Students should keep:
1. **Original:** lehigh_students_messy.csv (never modify)
2. **Cleaned:** lehigh_students_clean_[name].csv (their work)
3. **Cleaning Script:** cleaning_script.py or .ipynb (reproducible)
4. **Documentation:** cleaning_log.md (what they did and why)

This teaches professional data science workflow: always keep original data and document transformations.

---

## Common Mistakes to Avoid

1. **Overwriting original data** - Always work on a copy
2. **Cleaning without understanding** - Know why each step matters
3. **Not validating results** - Check that cleaning worked correctly
4. **Inconsistent standards** - Pick one format and stick to it
5. **Undocumented changes** - Future you won't remember what you did
6. **Dropping data without justification** - Explain why you removed records
7. **Using AI without understanding** - Don't copy code you can't explain

---

## Real-World Connection

This messy dataset simulates what students will encounter in actual data analyst jobs:

- **Corporate databases:** Multiple people entering data = inconsistent formats
- **Legacy systems:** Data accumulated over years with changing standards  
- **Manual entry:** Human error creates typos and formatting issues
- **System migrations:** Moving data between systems creates format problems
- **Multiple sources:** Combining data from different sources = inconsistencies

Learning to clean messy data is one of the most valuable skills for data analysts. Studies show data scientists spend 60-80% of their time on data cleaning and preparation.

---

## Questions for Discussion

1. How do you decide whether to drop records with missing values or keep them?
2. What's the trade-off between spending time cleaning vs. working with messy data?
3. How do you validate that your cleaning improved data quality?
4. When should cleaning be automated vs. manual review?
5. How do you balance "perfect" cleaning with "good enough" for analysis?

---

## Next Steps

After cleaning this dataset, students should be able to:
- Use pandas for Week 4-5 analysis with confidence
- Calculate statistics without type errors
- Group data without formatting issues
- Create visualizations without data quality problems
- Explain their data quality decisions

The cleaned version becomes the foundation for all subsequent analysis in Weeks 4-6.
