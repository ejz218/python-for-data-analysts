# Dataset Comparison: Clean vs. Messy Versions

## Quick Reference

| Feature | Clean Version | Messy Version |
|---------|--------------|---------------|
| **File** | lehigh_students_clean.csv | lehigh_students_messy.csv |
| **Records** | 600 | 605 (includes 5 duplicates) |
| **Columns** | 7 | 8 (added Enrollment_Date) |
| **Use In** | Week 1-2 | Week 3+ |
| **Quality** | Perfect | Intentionally degraded |
| **Purpose** | Learn Python basics | Learn data cleaning |

## What Changed?

### Added in Messy Version:
1. **Enrollment_Date column** - New variable with date formatting issues
2. **Data quality problems** - 10+ types of realistic issues
3. **5 duplicate records** - Same Student_ID with slight variations

### Data Quality Issues in Messy Version:

| Issue Type | Examples | Affected Records |
|------------|----------|------------------|
| Inconsistent college names | "COB", "college of business", "Business" | ~30% |
| Inconsistent class years | "Fr", "Freshman", "first year" | ~25% |
| Missing values | Empty GPA or Credits_Earned | ~6% |
| Extra whitespace | "  Engineering  " | ~25% |
| Date format variations | "2024-08-01", "08/01/24", "01-08-2024" | ~20% |
| Typos in majors | "Computer Sceince", "Finace" | ~5% |
| Numeric as text | "45 credits", " 3.2" | ~3% |
| Impossible values | GPA = 5.0, Credits = -10 | ~2% |
| Duplicate records | Same ID, different data | 5 records |

## Teaching Progression

### Week 1-2: Use CLEAN version
**Focus:** Python fundamentals
- Variables and types
- Basic operations
- Simple analysis
- Students shouldn't worry about data quality yet

**Example tasks:**
```python
# Calculate average GPA
total_gpa = 0
count = 0
for student in students:
    total_gpa += student['GPA']
    count += 1
average = total_gpa / count
```

### Week 3+: Switch to MESSY version
**Focus:** Real-world data challenges
- Data inspection
- Cleaning techniques
- Validation
- Documentation

**Example tasks:**
```python
# Now students deal with reality
df = pd.read_csv('data/lehigh_students_messy.csv')
print(df['GPA'].dtype)  # Oh no, it's 'object' not 'float'!
print(df['College'].value_counts())  # 28 variations?!
```

## Learning Objectives

### With Clean Data (Week 1-2):
Students learn to:
- ✓ Load and read data
- ✓ Access columns and rows
- ✓ Perform basic calculations
- ✓ Write loops and conditionals
- ✓ Focus on Python syntax

### With Messy Data (Week 3+):
Students learn to:
- ✓ Inspect data quality
- ✓ Identify patterns in errors
- ✓ Apply string methods
- ✓ Handle missing values
- ✓ Validate data transformations
- ✓ Document cleaning decisions
- ✓ Think critically about data

## AI Assistance Strategy

### Week 1-2 (Clean Data):
**CRAWL Mode:** No AI for basic Python
```python
# Students write this from memory
age = 21
name = "Sarah"
print(f"{name} is {age} years old")
```

### Week 3+ (Messy Data):
**WALK Mode:** AI helps understand cleaning techniques
```
Student prompt: "I have a column with college names in different formats 
like 'COB', 'College of Business', 'business'. How do I standardize them 
in pandas?"

AI helps explain .replace() or .map() methods, but student writes the code.
```

## File Organization

Recommended folder structure for students:
```
BUAN446_Project/
├── data/
│   ├── original/
│   │   ├── lehigh_students_clean.csv      (Week 1-2)
│   │   └── lehigh_students_messy.csv      (Week 3+, never modify)
│   └── cleaned/
│       └── lehigh_students_cleaned.csv    (Student's cleaned version)
├── notebooks/
│   ├── week1_basics.ipynb
│   ├── week2_control.ipynb
│   └── week3_cleaning.ipynb
└── scripts/
    └── data_cleaning.py
```

## Assessment Differences

### Week 1-2 Projects (Clean Data):
Assessed on:
- Python syntax correctness
- Logic and algorithm design
- Code readability
- Correct calculations

### Week 3+ Projects (Messy Data):
Assessed on:
- Data quality improvement
- Cleaning methodology
- Validation of results
- Documentation of decisions
- Understanding of trade-offs

## Common Student Questions

**Q: Why do we start with clean data?**
A: So you can focus on learning Python without being overwhelmed by data issues. You need to walk before you run.

**Q: Is real data always this messy?**
A: Often worse! This is actually a tame example. Real corporate databases can have decades of accumulated issues.

**Q: Can I just ask AI to clean it all?**
A: You could, but then you won't learn how to diagnose and fix data quality issues. On the job, you need to understand what AI did and verify it's correct.

**Q: Do I need to fix EVERY issue?**
A: Depends on your analysis goals. Document what you fixed and what you left, and explain why. Perfect is the enemy of good enough.

**Q: What if I make the data worse?**
A: That's why you always keep the original file untouched! Work on copies.

## Instructor Tips

1. **Don't show students the messy version too early** - Let them build confidence with clean data first

2. **The "Aha!" moment** - When students first load messy data after working with clean data, they experience real-world data shock. This is intentional and valuable.

3. **Progressive difficulty** - You can create even messier versions later (Week 4-5) with more complex issues

4. **Peer review** - Have students clean the data independently, then compare approaches. There's no single "right" way.

5. **Connect to jobs** - Emphasize that data cleaning is 60-80% of real data science work. This skill is highly valuable.

## Technical Notes

Both datasets:
- Same underlying patterns (GPA by class year, etc.)
- Same Student_IDs (for comparability)
- Same statistical properties (when cleaned properly)
- CSV format, UTF-8 encoding

Key difference:
- Clean: Ready for immediate analysis
- Messy: Requires 2-4 hours of cleaning work before analysis

## Next Steps

After students successfully clean the messy dataset, they should have:
1. A cleaned CSV file
2. A Python script that performs the cleaning (reproducible)
3. Documentation of what they changed and why
4. Validation that the cleaning worked correctly

This cleaned version then becomes their dataset for Weeks 4-6 when they learn NumPy, Pandas, and visualization.
