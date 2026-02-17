import random
import csv

# Set random seed for reproducibility
random.seed(42)

# Define Crestview University colleges and their majors
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

# Class year distribution (realistic for a university)
class_years = ["First Year", "Sophomore", "Junior", "Senior", "Graduate"]
class_year_weights = [0.22, 0.20, 0.20, 0.23, 0.15]  # More undergrads than grads

def generate_gpa(class_year):
    """Generate realistic GPA based on class year (older students tend higher)"""
    if class_year == "First Year":
        # First years have wider distribution, some struggling to adjust
        gpa = random.gauss(3.1, 0.6)
    elif class_year == "Sophomore":
        gpa = random.gauss(3.2, 0.5)
    elif class_year == "Junior":
        gpa = random.gauss(3.3, 0.45)
    elif class_year == "Senior":
        gpa = random.gauss(3.4, 0.4)
    else:  # Graduate
        gpa = random.gauss(3.6, 0.3)
    
    # Clamp between 0.0 and 4.0
    return round(max(0.0, min(4.0, gpa)), 2)

def generate_credits(class_year):
    """Generate credits attempted and earned based on class year"""
    base_credits = {
        "First Year": (12, 30),      # 12-30 credits attempted
        "Sophomore": (42, 60),       # 42-60 credits
        "Junior": (72, 90),          # 72-90 credits
        "Senior": (102, 130),        # 102-130 credits
        "Graduate": (9, 36)          # 9-36 credits (varies widely)
    }
    
    min_credits, max_credits = base_credits[class_year]
    attempted = random.randint(min_credits, max_credits)
    
    # Most students earn most credits, but some fail/withdraw
    # Higher GPA correlates with higher completion rate
    completion_rate = random.uniform(0.85, 1.0)
    earned = int(attempted * completion_rate)
    
    return attempted, earned

def generate_student_dataset(num_students=600):
    """Generate synthetic student dataset"""
    students = []
    
    for i in range(1, num_students + 1):
        # Generate Student ID (format: CU + 6 digits)
        student_id = f"CU{100000 + i:06d}"
        
        # Select college and major
        college = random.choice(list(colleges_majors.keys()))
        major = random.choice(colleges_majors[college])
        
        # Select class year
        class_year = random.choices(class_years, weights=class_year_weights)[0]
        
        # Generate GPA
        gpa = generate_gpa(class_year)
        
        # Generate credits
        credits_attempted, credits_earned = generate_credits(class_year)
        
        student = {
            "Student_ID": student_id,
            "College": college,
            "Major": major,
            "Class_Year": class_year,
            "GPA": gpa,
            "Credits_Attempted": credits_attempted,
            "Credits_Earned": credits_earned
        }
        
        students.append(student)
    
    return students

def save_to_csv(students, filename):
    """Save student data to CSV file"""
    fieldnames = ["Student_ID", "College", "Major", "Class_Year", "GPA", 
                  "Credits_Attempted", "Credits_Earned"]
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    
    print(f"Dataset saved to {filename}")
    print(f"Total students: {len(students)}")

def print_summary_statistics(students):
    """Print summary statistics of the generated dataset"""
    print("\n=== Dataset Summary Statistics ===\n")
    
    # Count by college
    print("Students by College:")
    college_counts = {}
    for student in students:
        college = student["College"]
        college_counts[college] = college_counts.get(college, 0) + 1
    for college, count in sorted(college_counts.items()):
        print(f"  {college}: {count}")
    
    # Count by class year
    print("\nStudents by Class Year:")
    year_counts = {}
    for student in students:
        year = student["Class_Year"]
        year_counts[year] = year_counts.get(year, 0) + 1
    for year, count in sorted(year_counts.items(), key=lambda x: class_years.index(x[0])):
        print(f"  {year}: {count}")
    
    # GPA statistics
    gpas = [student["GPA"] for student in students]
    avg_gpa = sum(gpas) / len(gpas)
    min_gpa = min(gpas)
    max_gpa = max(gpas)
    print(f"\nGPA Statistics:")
    print(f"  Average: {avg_gpa:.2f}")
    print(f"  Minimum: {min_gpa:.2f}")
    print(f"  Maximum: {max_gpa:.2f}")
    
    # Credits statistics
    credits_attempted = [student["Credits_Attempted"] for student in students]
    credits_earned = [student["Credits_Earned"] for student in students]
    avg_attempted = sum(credits_attempted) / len(credits_attempted)
    avg_earned = sum(credits_earned) / len(credits_earned)
    completion_rate = (sum(credits_earned) / sum(credits_attempted)) * 100
    print(f"\nCredits Statistics:")
    print(f"  Average Attempted: {avg_attempted:.1f}")
    print(f"  Average Earned: {avg_earned:.1f}")
    print(f"  Overall Completion Rate: {completion_rate:.1f}%")
    
    # Sample records
    print("\n=== Sample Records (first 5 students) ===\n")
    for student in students[:5]:
        print(f"ID: {student['Student_ID']}")
        print(f"  College: {student['College']}")
        print(f"  Major: {student['Major']}")
        print(f"  Class Year: {student['Class_Year']}")
        print(f"  GPA: {student['GPA']}")
        print(f"  Credits: {student['Credits_Earned']}/{student['Credits_Attempted']}")
        print()

if __name__ == "__main__":
    # Generate dataset
    print("Generating synthetic Crestview University student dataset...\n")
    students = generate_student_dataset(num_students=600)
    
    # Save to CSV
    output_file = "/mnt/user-data/outputs/crestview_students_clean.csv"
    save_to_csv(students, output_file)
    
    # Print summary statistics
    print_summary_statistics(students)
    
    print("\n=== Data Dictionary ===\n")
    print("Student_ID: Unique anonymous identifier (format: CUXXXXXX)")
    print("College: Crestview University college the student belongs to")
    print("Major: Student's declared major")
    print("Class_Year: Academic year (First Year, Sophomore, Junior, Senior, Graduate)")
    print("GPA: Grade Point Average on 4.0 scale")
    print("Credits_Attempted: Total credit hours attempted")
    print("Credits_Earned: Total credit hours successfully earned")
    print("\nNote: This is synthetic data for educational purposes.")
