import random
import csv
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

# Define Crestview University colleges and their majors (with variations for messiness)
colleges_majors = {
    "College of Business": [
        "Accounting", "Finance", "Marketing", "Supply Chain Management",
        "Business Analytics", "Management", "Economics"
    ],
    "College of Engineering": [
        "Computer Science", "Mechanical Engineering", "Civil Engineering",
        "Electrical Engineering", "Chemical Engineering", "Industrial Engineering",
        "Computer Engineering", "Bioengineering"
    ],
    "College of Arts and Sciences": [
        "Biology", "Chemistry", "Psychology", "English", "Mathematics",
        "Physics", "Political Science", "Sociology", "History", "Philosophy"
    ],
    "College of Health": [
        "Health Science", "Public Health", "Nursing", "Community Health"
    ],
    "College of Education": [
        "Elementary Education", "Secondary Education", "Special Education"
    ]
}

# College name variations for messiness
college_variations = {
    "College of Business": [
        "College of Business", "COB", "Business", "college of business", 
        "College Of Business", "Buisness"  # intentional typo
    ],
    "College of Engineering": [
        "College of Engineering", "Engineering", "COE",
        "School of Engineering", "engineering", "Eng"
    ],
    "College of Arts and Sciences": [
        "College of Arts and Sciences", "CAS", "Arts and Sciences", 
        "Arts & Sciences", "college of arts and sciences", "A&S"
    ],
    "College of Health": [
        "College of Health", "COH", "Health", "college of health", "Health College"
    ],
    "College of Education": [
        "College of Education", "COE", "Education", "college of education", "Ed"
    ]
}

# Class year variations
class_year_variations = {
    "First Year": ["First Year", "Freshman", "1st Year", "Fr", "first year"],
    "Sophomore": ["Sophomore", "Soph", "2nd Year", "sophomore"],
    "Junior": ["Junior", "Jr", "3rd Year", "junior"],
    "Senior": ["Senior", "Sr", "4th Year", "senior"],
    "Graduate": ["Graduate", "Grad", "Masters", "PhD", "graduate", "Master's"]
}

class_years = ["First Year", "Sophomore", "Junior", "Senior", "Graduate"]
class_year_weights = [0.22, 0.20, 0.20, 0.23, 0.15]

def generate_gpa(class_year):
    """Generate realistic GPA based on class year"""
    if class_year == "First Year":
        gpa = random.gauss(3.1, 0.6)
    elif class_year == "Sophomore":
        gpa = random.gauss(3.2, 0.5)
    elif class_year == "Junior":
        gpa = random.gauss(3.3, 0.45)
    elif class_year == "Senior":
        gpa = random.gauss(3.4, 0.4)
    else:  # Graduate
        gpa = random.gauss(3.6, 0.3)
    
    return round(max(0.0, min(4.0, gpa)), 2)

def generate_credits(class_year):
    """Generate credits attempted and earned"""
    base_credits = {
        "First Year": (12, 30),
        "Sophomore": (42, 60),
        "Junior": (72, 90),
        "Senior": (102, 130),
        "Graduate": (9, 36)
    }
    
    min_credits, max_credits = base_credits[class_year]
    attempted = random.randint(min_credits, max_credits)
    completion_rate = random.uniform(0.85, 1.0)
    earned = int(attempted * completion_rate)
    
    return attempted, earned

def generate_enrollment_date(class_year):
    """Generate enrollment date based on class year"""
    current_year = 2024
    
    # Map class year to typical enrollment year
    years_ago = {
        "First Year": 0,
        "Sophomore": 1,
        "Junior": 2,
        "Senior": 3,
        "Graduate": random.choice([0, 1])  # Grads can start any time
    }
    
    year = current_year - years_ago.get(class_year, 0)
    
    # Random month between August and January (typical enrollment periods)
    month = random.choice([8, 8, 8, 9, 1])  # More likely to be fall
    day = random.randint(1, 28)
    
    return datetime(year, month, day)

def introduce_messiness(student, messiness_probability=0.25):
    """Introduce various data quality issues"""
    messy_student = student.copy()
    
    # 1. Inconsistent college names (30% chance)
    if random.random() < 0.30:
        original_college = student["College"]
        messy_student["College"] = random.choice(college_variations[original_college])
    
    # 2. Inconsistent class year format (25% chance)
    if random.random() < 0.25:
        original_year = student["Class_Year"]
        messy_student["Class_Year"] = random.choice(class_year_variations[original_year])
    
    # 3. Missing GPA (8% chance - realistic for incomplete records)
    if random.random() < 0.08:
        messy_student["GPA"] = ""
    
    # 4. GPA formatting issues (5% chance)
    elif random.random() < 0.05:
        gpa = student["GPA"]
        # Various formatting issues
        issues = [
            str(gpa),  # Already a string, but might have extra decimals
            f"{gpa:.3f}",  # Too many decimals
            f" {gpa}",  # Leading space
            f"{gpa} ",  # Trailing space
        ]
        messy_student["GPA"] = random.choice(issues)
    
    # 5. Missing credits (6% chance)
    if random.random() < 0.06:
        messy_student["Credits_Earned"] = ""
    
    # 6. Credits as text (3% chance - data entry error)
    elif random.random() < 0.03:
        messy_student["Credits_Attempted"] = f"{student['Credits_Attempted']} credits"
    
    # 7. Impossible/outlier values (2% chance)
    if random.random() < 0.02:
        issues = [
            ("GPA", "5.0"),  # Impossible GPA
            ("Credits_Attempted", "-10"),  # Negative credits
            ("Credits_Earned", str(student["Credits_Attempted"] + 10)),  # More earned than attempted
        ]
        field, value = random.choice(issues)
        messy_student[field] = value
    
    # 8. Major typos (5% chance)
    if random.random() < 0.05:
        major = messy_student["Major"]
        typos = {
            "Computer Science": "Computer Sceince",
            "Psychology": "Psycology",
            "Business Analytics": "Business Analystics",
            "Mechanical Engineering": "Mech Engineering",
            "Biology": "Bioligy",
            "Finance": "Finace",
            "Marketing": "Marketting"
        }
        messy_student["Major"] = typos.get(major, major)
    
    # 9. Inconsistent date formats (for enrollment date)
    if "Enrollment_Date" in messy_student:
        date = messy_student["Enrollment_Date"]
        if random.random() < 0.20:
            # Various date format issues
            formats = [
                date.strftime("%m/%d/%Y"),  # MM/DD/YYYY
                date.strftime("%d/%m/%Y"),  # DD/MM/YYYY (ambiguous)
                date.strftime("%Y-%m-%d"),  # ISO format
                date.strftime("%m-%d-%Y"),  # MM-DD-YYYY
                date.strftime("%B %d, %Y"),  # Month DD, YYYY
                date.strftime("%m/%d/%y"),  # Short year
            ]
            messy_student["Enrollment_Date"] = random.choice(formats)
        else:
            messy_student["Enrollment_Date"] = date.strftime("%Y-%m-%d")
    
    # 10. Extra whitespace (10% chance on any text field)
    for field in ["College", "Major", "Class_Year"]:
        if random.random() < 0.10:
            messy_student[field] = f"  {messy_student[field]}  "
    
    return messy_student

def generate_messy_dataset(num_students=600):
    """Generate messy student dataset with data quality issues"""
    students = []
    
    for i in range(1, num_students + 1):
        student_id = f"CU{100000 + i:06d}"
        
        # Select college and major
        college = random.choice(list(colleges_majors.keys()))
        major = random.choice(colleges_majors[college])
        
        # Select class year
        class_year = random.choices(class_years, weights=class_year_weights)[0]
        
        # Generate data
        gpa = generate_gpa(class_year)
        credits_attempted, credits_earned = generate_credits(class_year)
        enrollment_date = generate_enrollment_date(class_year)
        
        student = {
            "Student_ID": student_id,
            "College": college,
            "Major": major,
            "Class_Year": class_year,
            "GPA": gpa,
            "Credits_Attempted": credits_attempted,
            "Credits_Earned": credits_earned,
            "Enrollment_Date": enrollment_date
        }
        
        # Introduce messiness (but not to all records)
        student = introduce_messiness(student)
        
        students.append(student)
    
    # 11. Add some duplicate records (5 duplicates with slight variations)
    for _ in range(5):
        original = random.choice(students)
        duplicate = original.copy()
        # Slight variation in one field
        if random.random() < 0.5:
            duplicate["GPA"] = str(float(str(original["GPA"]).strip() or "3.0") + 0.01)
        else:
            duplicate["Credits_Earned"] = str(int(str(original["Credits_Earned"]).strip() or "30") + 1)
        students.append(duplicate)
    
    return students

def save_to_csv(students, filename):
    """Save student data to CSV file"""
    fieldnames = ["Student_ID", "College", "Major", "Class_Year", "GPA", 
                  "Credits_Attempted", "Credits_Earned", "Enrollment_Date"]
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    
    print(f"Messy dataset saved to {filename}")
    print(f"Total records: {len(students)}")

def analyze_data_quality(students):
    """Analyze and report data quality issues"""
    print("\n=== Data Quality Report ===\n")
    
    total = len(students)
    
    # Missing values
    missing_gpa = sum(1 for s in students if s["GPA"] == "")
    missing_credits = sum(1 for s in students if s["Credits_Earned"] == "")
    
    print(f"Missing Values:")
    print(f"  GPA: {missing_gpa} records ({missing_gpa/total*100:.1f}%)")
    print(f"  Credits Earned: {missing_credits} records ({missing_credits/total*100:.1f}%)")
    
    # Inconsistent formats
    college_variations_count = len(set(s["College"].strip() for s in students))
    year_variations_count = len(set(s["Class_Year"].strip() for s in students))
    
    print(f"\nInconsistent Formatting:")
    print(f"  College name variations: {college_variations_count} unique values")
    print(f"  Class year variations: {year_variations_count} unique values")
    
    # Records with whitespace
    whitespace_count = sum(1 for s in students 
                          if any(str(s[field]).startswith(' ') or str(s[field]).endswith(' ')
                                for field in ["College", "Major", "Class_Year"]))
    print(f"  Records with extra whitespace: {whitespace_count}")
    
    # Date format variations
    date_formats = set()
    for s in students:
        date_str = s["Enrollment_Date"]
        if '/' in date_str:
            date_formats.add("MM/DD/YYYY or similar")
        elif '-' in date_str:
            date_formats.add("YYYY-MM-DD or similar")
        elif ',' in date_str:
            date_formats.add("Month DD, YYYY")
    print(f"  Date format variations: {len(date_formats)} different formats")
    
    # Potential outliers
    try:
        gpas = [float(str(s["GPA"]).strip()) for s in students if s["GPA"] and str(s["GPA"]).strip()]
        outlier_gpas = sum(1 for g in gpas if g > 4.0 or g < 0.0)
        print(f"\nPotential Data Entry Errors:")
        print(f"  Impossible GPAs (>4.0 or <0.0): {outlier_gpas} records")
    except:
        print(f"\nPotential Data Entry Errors:")
        print(f"  Non-numeric GPA values detected")
    
    # Duplicate Student IDs
    ids = [s["Student_ID"] for s in students]
    duplicates = len(ids) - len(set(ids))
    print(f"  Duplicate Student IDs: {duplicates} duplicates")
    
    print(f"\n=== Sample Data Quality Issues ===\n")
    
    # Show examples of messy data
    issues_shown = 0
    for student in students[:50]:  # Check first 50
        if issues_shown >= 5:
            break
        
        issues = []
        if student["GPA"] == "":
            issues.append("Missing GPA")
        if student["College"].startswith(" ") or student["College"].endswith(" "):
            issues.append(f"Whitespace in college: '{student['College']}'")
        if student["College"] in ["COB", "COE", "CAS", "COH"]:
            issues.append(f"Abbreviated college: {student['College']}")
        if student["Class_Year"] in ["Fr", "Soph", "Jr", "Sr", "Grad"]:
            issues.append(f"Abbreviated year: {student['Class_Year']}")
        
        if issues:
            print(f"Student {student['Student_ID']}:")
            for issue in issues:
                print(f"  - {issue}")
            issues_shown += 1
            print()

if __name__ == "__main__":
    print("Generating messy Crestview University student dataset...\n")
    students = generate_messy_dataset(num_students=600)
    
    # Save to CSV
    output_file = "/mnt/user-data/outputs/crestview_students_messy.csv"
    save_to_csv(students, output_file)
    
    # Analyze data quality issues
    analyze_data_quality(students)
    
    print("\n=== Common Data Cleaning Tasks for Students ===\n")
    print("1. Standardize college names to consistent format")
    print("2. Standardize class year labels")
    print("3. Handle missing GPA and credits values")
    print("4. Remove extra whitespace from text fields")
    print("5. Standardize date formats")
    print("6. Identify and fix impossible values (GPA > 4.0)")
    print("7. Detect and handle duplicate records")
    print("8. Fix typos in major names")
    print("9. Convert text numbers to numeric (e.g., '45 credits' -> 45)")
    print("10. Validate that credits_earned <= credits_attempted")
    
    print("\n=== AI Assistance Strategy ===\n")
    print("WALK Mode: Students can use AI to:")
    print("  - Explain pandas methods for handling missing data")
    print("  - Suggest regex patterns for text cleaning")
    print("  - Debug error messages when parsing dates")
    print("  - Understand why certain cleaning approaches work")
    print("\nStudents should NOT ask AI to 'clean the entire dataset' but rather")
    print("learn specific techniques for each type of data quality issue.")
