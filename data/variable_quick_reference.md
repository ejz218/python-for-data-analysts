# Crestview University Student Dataset - Quick Reference

*Print this page or keep it open while working through Chapters 6-9.*

**File:** `data/crestview_students_extended.csv`  
**Records:** 600 students | **Variables:** 15 | **Quality:** Clean

## The 15 Variables

| # | Variable | Type | Description | Example Values | Range/Categories |
|---|----------|------|-------------|----------------|------------------|
| 1 | `Student_ID` | String | Unique identifier | CU100001 | CU100001-CU100600 |
| 2 | `College` | String | Crestview college | College of Business | 5 colleges |
| 3 | `Major` | String | Declared major | Computer Science | ~30 majors |
| 4 | `Class_Year` | String | Academic standing | Junior | First Year, Sophomore, Junior, Senior, Graduate |
| 5 | `GPA` | Float | Grade point average | 3.41 | 0.0 - 4.0 |
| 6 | `Credits_Attempted` | Integer| Credits attempted | 105 | 9 - 135 |
| 7 | `Credits_Earned` | Integer| Credits earned | 99 | 6 - 132 |
| 8 | `Enrollment_Date` | String | First enrollment (ISO) | 2021-01-24 | 2019 - 2025 |
| 9 | `Study_Hours_Per_Week` | Float | Weekly study hours | 14.2 | 2.0 - 45.0 |
| 10 | `Campus_Housing` | String | Living situation | On-campus | On-campus, Off-campus, Commuter |
| 11 | `Financial_Aid` | String | Aid status | Partial | Yes, No, Partial |
| 12 | `Extracurriculars` | Integer| Activity count | 3 | 0 - 5 |
| 13 | `Part_Time_Job` | String | Employment status | No | No, Yes (10h), Yes (18h), etc. |
| 14 | `First_Generation` | String | First-gen student | Yes | Yes, No, or blank (~10% missing) |
| 15 | `Distance_From_Home` | Float | Miles from home | 450 | ~5 - 3000 |

## Variable Groupings for Analysis

### Numeric Columns 
*Use for correlations, statistical summaries, and scatter plots.*
- `GPA`, `Credits_Attempted`, `Credits_Earned`, `Study_Hours_Per_Week`, `Extracurriculars`, `Distance_From_Home`

### Categorical Columns
*Use for grouping, value counts, and segmenting data (box plots, bar charts).*
- `College`, `Major`, `Class_Year`, `Campus_Housing`, `Financial_Aid`, `Part_Time_Job`, `First_Generation`

## Common Derived Variables

When doing data analysis, you'll often calculate these helpful new variables:

| Variable | Formula / Logic | Purpose |
|----------|---------|---------|
| `Completion_Rate` | `Credits_Earned / Credits_Attempted` | Academic efficiency / success rate |
| `Study_Efficiency` | `GPA / Study_Hours_Per_Week` | Find students who get high grades with less studying |
| `Has_Job` | `Part_Time_Job != "No"` | Simple boolean employment flag |
| `Academic_Standing`| GPA >= 3.5 → Dean's List; >= 2.0 → Good Standing; < 2.0 → Probation | Performance benchmarking |
| `At_Risk` | GPA < 2.0 OR Completion_Rate < 0.85 OR Study_Hours < 5 | Early warning indicator for advisors |
