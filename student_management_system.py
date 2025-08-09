#!/usr/bin/env python3
"""
Student Management System
A comprehensive CLI-based system for managing student records with persistent storage.

Features:
- Add, view, search, update, and delete student records
- Persistent storage using CSV format
- Input validation and error handling
- User-friendly menu-driven interface
- Sorted display options
"""

import csv
import os
from typing import List, Dict, Optional


class StudentManagementSystem:
    """Main class for managing student records."""
    
    def __init__(self, filename: str = "students.csv"):
        """Initialize the system with a data file."""
        self.filename = filename
        self.students: List[Dict[str, str]] = []
        self.load_data()
    
    def load_data(self) -> None:
        """Load student data from CSV file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.students = list(reader)
                print(f"✅ Loaded {len(self.students)} student records from {self.filename}")
            else:
                print(f"📁 No existing data file found. Starting with empty database.")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.students = []
    
    def save_data(self) -> None:
        """Save student data to CSV file."""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                if self.students:
                    fieldnames = ['roll_number', 'name', 'age', 'marks']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.students)
                print(f"💾 Data saved successfully to {self.filename}")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    def validate_roll_number(self, roll_number: str) -> bool:
        """Check if roll number is unique."""
        return not any(student['roll_number'] == roll_number for student in self.students)
    
    def validate_age(self, age_str: str) -> Optional[int]:
        """Validate and return age as integer."""
        try:
            age = int(age_str)
            if age < 1 or age > 150:
                raise ValueError("Age must be between 1 and 150")
            return age
        except ValueError:
            return None
    
    def validate_marks(self, marks_str: str) -> Optional[float]:
        """Validate and return marks as float."""
        try:
            marks = float(marks_str)
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100")
            return marks
        except ValueError:
            return None
    
    def validate_name(self, name: str) -> bool:
        """Validate student name."""
        return bool(name.strip()) and len(name.strip()) >= 2
    
    def add_student(self) -> None:
        """Add a new student record."""
        print("\n" + "="*50)
        print("📝 ADD NEW STUDENT")
        print("="*50)
        
        # Get and validate roll number
        while True:
            roll_number = input("Enter Roll Number: ").strip()
            if not roll_number:
                print("❌ Roll number cannot be empty!")
                continue
            if not self.validate_roll_number(roll_number):
                print("❌ Roll number already exists! Please enter a unique roll number.")
                continue
            break
        
        # Get and validate name
        while True:
            name = input("Enter Student Name: ").strip()
            if not self.validate_name(name):
                print("❌ Name must be at least 2 characters long!")
                continue
            break
        
        # Get and validate age
        while True:
            age_str = input("Enter Age: ").strip()
            age = self.validate_age(age_str)
            if age is None:
                print("❌ Please enter a valid age (1-150)!")
                continue
            break
        
        # Get and validate marks
        while True:
            marks_str = input("Enter Marks (0-100): ").strip()
            marks = self.validate_marks(marks_str)
            if marks is None:
                print("❌ Please enter valid marks (0-100)!")
                continue
            break
        
        # Add the student
        student = {
            'roll_number': roll_number,
            'name': name.title(),
            'age': str(age),
            'marks': str(marks)
        }
        
        self.students.append(student)
        self.save_data()
        print(f"\n✅ Student '{name}' added successfully!")
    
    def view_all_students(self) -> None:
        """Display all student records in a formatted table."""
        print("\n" + "="*80)
        print("👥 ALL STUDENT RECORDS")
        print("="*80)
        
        if not self.students:
            print("📭 No student records found!")
            return
        
        # Sort options
        print("\nSort options:")
        print("1. By Roll Number")
        print("2. By Name")
        print("3. By Marks (Highest first)")
        print("4. No sorting")
        
        while True:
            choice = input("\nChoose sorting option (1-4): ").strip()
            if choice == '1':
                sorted_students = sorted(self.students, key=lambda x: x['roll_number'])
                break
            elif choice == '2':
                sorted_students = sorted(self.students, key=lambda x: x['name'].lower())
                break
            elif choice == '3':
                sorted_students = sorted(self.students, key=lambda x: float(x['marks']), reverse=True)
                break
            elif choice == '4':
                sorted_students = self.students
                break
            else:
                print("❌ Please enter a valid option (1-4)!")
                continue
        
        # Display table
        print(f"\n{'Roll No':<10} {'Name':<20} {'Age':<5} {'Marks':<8} {'Grade':<5}")
        print("-" * 50)
        
        for student in sorted_students:
            marks = float(student['marks'])
            grade = self.calculate_grade(marks)
            print(f"{student['roll_number']:<10} {student['name']:<20} {student['age']:<5} {student['marks']:<8} {grade:<5}")
        
        print(f"\nTotal Students: {len(self.students)}")
    
    def calculate_grade(self, marks: float) -> str:
        """Calculate grade based on marks."""
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B+'
        elif marks >= 60:
            return 'B'
        elif marks >= 50:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'
    
    def search_student(self) -> None:
        """Search for a student by roll number or name."""
        print("\n" + "="*50)
        print("🔍 SEARCH STUDENT")
        print("="*50)
        
        if not self.students:
            print("📭 No student records found!")
            return
        
        print("Search by:")
        print("1. Roll Number")
        print("2. Name")
        
        while True:
            choice = input("\nChoose search option (1-2): ").strip()
            if choice in ['1', '2']:
                break
            print("❌ Please enter 1 or 2!")
        
        search_term = input("Enter search term: ").strip()
        if not search_term:
            print("❌ Search term cannot be empty!")
            return
        
        found_students = []
        
        if choice == '1':
            # Search by roll number
            for student in self.students:
                if student['roll_number'].lower() == search_term.lower():
                    found_students.append(student)
        else:
            # Search by name (partial match)
            for student in self.students:
                if search_term.lower() in student['name'].lower():
                    found_students.append(student)
        
        if found_students:
            print(f"\n🎯 Found {len(found_students)} student(s):")
            print(f"{'Roll No':<10} {'Name':<20} {'Age':<5} {'Marks':<8} {'Grade':<5}")
            print("-" * 50)
            
            for student in found_students:
                marks = float(student['marks'])
                grade = self.calculate_grade(marks)
                print(f"{student['roll_number']:<10} {student['name']:<20} {student['age']:<5} {student['marks']:<8} {grade:<5}")
        else:
            print(f"❌ No student found with the given {'roll number' if choice == '1' else 'name'}!")
    
    def update_student(self) -> None:
        """Update an existing student record."""
        print("\n" + "="*50)
        print("✏️ UPDATE STUDENT RECORD")
        print("="*50)
        
        if not self.students:
            print("📭 No student records found!")
            return
        
        roll_number = input("Enter Roll Number of student to update: ").strip()
        if not roll_number:
            print("❌ Roll number cannot be empty!")
            return
        
        # Find the student
        student_index = None
        for i, student in enumerate(self.students):
            if student['roll_number'] == roll_number:
                student_index = i
                break
        
        if student_index is None:
            print(f"❌ No student found with roll number '{roll_number}'!")
            return
        
        current_student = self.students[student_index]
        print(f"\n📋 Current details for Roll Number {roll_number}:")
        print(f"Name: {current_student['name']}")
        print(f"Age: {current_student['age']}")
        print(f"Marks: {current_student['marks']}")
        
        print("\n🔧 What would you like to update?")
        print("1. Name")
        print("2. Age")
        print("3. Marks")
        print("4. All details")
        
        while True:
            choice = input("\nChoose option (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                break
            print("❌ Please enter a valid option (1-4)!")
        
        updated = False
        
        if choice in ['1', '4']:  # Update name
            while True:
                new_name = input(f"Enter new name (current: {current_student['name']}): ").strip()
                if not new_name:
                    print("❌ Name cannot be empty!")
                    continue
                if not self.validate_name(new_name):
                    print("❌ Name must be at least 2 characters long!")
                    continue
                current_student['name'] = new_name.title()
                updated = True
                break
        
        if choice in ['2', '4']:  # Update age
            while True:
                age_str = input(f"Enter new age (current: {current_student['age']}): ").strip()
                if not age_str:
                    break
                age = self.validate_age(age_str)
                if age is None:
                    print("❌ Please enter a valid age (1-150)!")
                    continue
                current_student['age'] = str(age)
                updated = True
                break
        
        if choice in ['3', '4']:  # Update marks
            while True:
                marks_str = input(f"Enter new marks (current: {current_student['marks']}): ").strip()
                if not marks_str:
                    break
                marks = self.validate_marks(marks_str)
                if marks is None:
                    print("❌ Please enter valid marks (0-100)!")
                    continue
                current_student['marks'] = str(marks)
                updated = True
                break
        
        if updated:
            self.save_data()
            print(f"\n✅ Student record updated successfully!")
        else:
            print("ℹ️ No changes were made.")
    
    def delete_student(self) -> None:
        """Delete a student record."""
        print("\n" + "="*50)
        print("🗑️ DELETE STUDENT RECORD")
        print("="*50)
        
        if not self.students:
            print("📭 No student records found!")
            return
        
        roll_number = input("Enter Roll Number of student to delete: ").strip()
        if not roll_number:
            print("❌ Roll number cannot be empty!")
            return
        
        # Find the student
        student_to_delete = None
        student_index = None
        for i, student in enumerate(self.students):
            if student['roll_number'] == roll_number:
                student_to_delete = student
                student_index = i
                break
        
        if student_to_delete is None:
            print(f"❌ No student found with roll number '{roll_number}'!")
            return
        
        # Confirm deletion
        print(f"\n⚠️ Are you sure you want to delete this student?")
        print(f"Roll Number: {student_to_delete['roll_number']}")
        print(f"Name: {student_to_delete['name']}")
        print(f"Age: {student_to_delete['age']}")
        print(f"Marks: {student_to_delete['marks']}")
        
        while True:
            confirm = input("\nConfirm deletion (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                del self.students[student_index]
                self.save_data()
                print(f"\n✅ Student '{student_to_delete['name']}' deleted successfully!")
                break
            elif confirm in ['n', 'no']:
                print("ℹ️ Deletion cancelled.")
                break
            else:
                print("❌ Please enter 'y' for yes or 'n' for no!")
    
    def display_statistics(self) -> None:
        """Display system statistics."""
        print("\n" + "="*50)
        print("📊 SYSTEM STATISTICS")
        print("="*50)
        
        if not self.students:
            print("📭 No student records found!")
            return
        
        total_students = len(self.students)
        marks_list = [float(student['marks']) for student in self.students]
        
        avg_marks = sum(marks_list) / total_students
        highest_marks = max(marks_list)
        lowest_marks = min(marks_list)
        
        # Grade distribution
        grades = {'A+': 0, 'A': 0, 'B+': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for marks in marks_list:
            grade = self.calculate_grade(marks)
            grades[grade] += 1
        
        print(f"Total Students: {total_students}")
        print(f"Average Marks: {avg_marks:.2f}")
        print(f"Highest Marks: {highest_marks}")
        print(f"Lowest Marks: {lowest_marks}")
        
        print(f"\n📈 Grade Distribution:")
        for grade, count in grades.items():
            if count > 0:
                percentage = (count / total_students) * 100
                print(f"{grade}: {count} students ({percentage:.1f}%)")
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*60)
        print("🎓 STUDENT MANAGEMENT SYSTEM")
        print("="*60)
        print("1. 📝 Add Student Record")
        print("2. 👥 View All Records")
        print("3. 🔍 Search Student Record")
        print("4. ✏️ Update Student Record")
        print("5. 🗑️ Delete Student Record")
        print("6. 📊 System Statistics")
        print("7. 💾 Save & Exit")
        print("="*60)
    
    def run(self) -> None:
        """Main program loop."""
        print("🎓 Welcome to Student Management System!")
        print("="*50)
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\n👉 Enter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.view_all_students()
                elif choice == '3':
                    self.search_student()
                elif choice == '4':
                    self.update_student()
                elif choice == '5':
                    self.delete_student()
                elif choice == '6':
                    self.display_statistics()
                elif choice == '7':
                    self.save_data()
                    print("\n👋 Thank you for using Student Management System!")
                    print("💾 All data has been saved successfully.")
                    break
                else:
                    print("❌ Invalid choice! Please enter a number between 1-7.")
                
                # Wait for user to continue
                if choice in ['1', '2', '3', '4', '5', '6']:
                    input("\n🔄 Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Saving data before exit...")
                self.save_data()
                break
            except Exception as e:
                print(f"\n❌ An unexpected error occurred: {e}")
                print("Please try again.")


def main():
    """Main function to run the Student Management System."""
    try:
        sms = StudentManagementSystem()
        sms.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        print("Please check your system and try again.")


if __name__ == "__main__":
    main()
