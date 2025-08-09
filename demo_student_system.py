#!/usr/bin/env python3
"""
Demo script for Student Management System
This script demonstrates all features with sample data.
"""

from student_management_system import StudentManagementSystem
import time

def demonstrate_system():
    """Demonstrate all features of the Student Management System."""
    print("🎓 STUDENT MANAGEMENT SYSTEM DEMO")
    print("=" * 50)
    
    # Create system instance
    sms = StudentManagementSystem("demo_students.csv")
    
    # Add some sample students
    sample_students = [
        {"roll_number": "CS001", "name": "Alice Johnson", "age": "20", "marks": "95"},
        {"roll_number": "CS002", "name": "Bob Smith", "age": "19", "marks": "87"},
        {"roll_number": "CS003", "name": "Charlie Brown", "age": "21", "marks": "78"},
        {"roll_number": "CS004", "name": "Diana Prince", "age": "20", "marks": "92"},
        {"roll_number": "CS005", "name": "Eve Wilson", "age": "19", "marks": "69"},
    ]
    
    print("\n📝 Adding sample students...")
    sms.students = sample_students
    sms.save_data()
    print(f"✅ Added {len(sample_students)} sample students!")
    
    time.sleep(2)
    
    # Demonstrate view all with sorting
    print("\n" + "="*60)
    print("👥 VIEWING ALL STUDENTS (Sorted by Marks)")
    print("="*60)
    
    sorted_students = sorted(sms.students, key=lambda x: float(x['marks']), reverse=True)
    print(f"{'Roll No':<10} {'Name':<20} {'Age':<5} {'Marks':<8} {'Grade':<5}")
    print("-" * 50)
    
    for student in sorted_students:
        marks = float(student['marks'])
        grade = sms.calculate_grade(marks)
        print(f"{student['roll_number']:<10} {student['name']:<20} {student['age']:<5} {student['marks']:<8} {grade:<5}")
    
    time.sleep(3)
    
    # Demonstrate search
    print("\n" + "="*50)
    print("🔍 SEARCH DEMONSTRATION")
    print("="*50)
    
    print("Searching for 'Alice':")
    found_students = []
    for student in sms.students:
        if "alice" in student['name'].lower():
            found_students.append(student)
    
    if found_students:
        for student in found_students:
            marks = float(student['marks'])
            grade = sms.calculate_grade(marks)
            print(f"Found: {student['roll_number']} - {student['name']} ({student['marks']}% - Grade {grade})")
    
    time.sleep(2)
    
    # Demonstrate statistics
    print("\n" + "="*50)
    print("📊 SYSTEM STATISTICS")
    print("="*50)
    
    total_students = len(sms.students)
    marks_list = [float(student['marks']) for student in sms.students]
    
    avg_marks = sum(marks_list) / total_students
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)
    
    # Grade distribution
    grades = {'A+': 0, 'A': 0, 'B+': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for marks in marks_list:
        grade = sms.calculate_grade(marks)
        grades[grade] += 1
    
    print(f"📈 Total Students: {total_students}")
    print(f"📈 Average Marks: {avg_marks:.2f}%")
    print(f"📈 Highest Marks: {highest_marks}%")
    print(f"📈 Lowest Marks: {lowest_marks}%")
    
    print(f"\n🎯 Grade Distribution:")
    for grade, count in grades.items():
        if count > 0:
            percentage = (count / total_students) * 100
            bar = "█" * (count * 2)  # Simple bar chart
            print(f"{grade}: {count} students ({percentage:.1f}%) {bar}")
    
    time.sleep(3)
    
    # Demonstrate update
    print("\n" + "="*50)
    print("✏️ UPDATE DEMONSTRATION")
    print("="*50)
    
    print("Original record for CS003:")
    for student in sms.students:
        if student['roll_number'] == 'CS003':
            print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
            # Update marks
            student['marks'] = '85'  # Improved marks
            print(f"Updated marks to: {student['marks']}")
            break
    
    time.sleep(2)
    
    # Final save
    sms.save_data()
    print("\n💾 Demo completed! All data saved to demo_students.csv")
    print("\n🎓 You can now run the main system to explore these features interactively!")


if __name__ == "__main__":
    demonstrate_system()
