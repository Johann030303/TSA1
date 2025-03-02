import json
import os

def compute_grade(class_standing, exam_grade):
    return (class_standing * 0.6) + (exam_grade * 0.4)

def load_records(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def show_all_students(records):
    for student in records:
        print(student)

def order_by_last_name(records):
    return sorted(records, key=lambda x: x["name"][1])

def order_by_grade(records):
    return sorted(records, key=lambda x: compute_grade(x["class_standing"], x["major_exam"]), reverse=True)

def show_student(records, student_id):
    for student in records:
        if student["id"] == student_id:
            return student
    return "Student not found."

def add_record(records, student_id, first_name, last_name, class_standing, major_exam):
    records.append({
        "id": student_id,
        "name": (first_name, last_name),
        "class_standing": class_standing,
        "major_exam": major_exam
    })

def edit_record(records, student_id, first_name=None, last_name=None, class_standing=None, major_exam=None):
    for student in records:
        if student["id"] == student_id:
            if first_name:
                student["name"] = (first_name, student["name"][1])
            if last_name:
                student["name"] = (student["name"][0], last_name)
            if class_standing is not None:
                student["class_standing"] = class_standing
            if major_exam is not None:
                student["major_exam"] = major_exam
            return "Record updated successfully."
    return "Student not found."

def delete_record(records, student_id):
    for student in records:
        if student["id"] == student_id:
            records.remove(student)
            return "Record deleted successfully."
    return "Student not found."

def main():
    filename = "students.json"
    records = load_records(filename)
    
    while True:
        print("\nStudent Record Management System")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Save File")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            show_all_students(records)
        elif choice == "2":
            records = order_by_last_name(records)
            show_all_students(records)
        elif choice == "3":
            records = order_by_grade(records)
            show_all_students(records)
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            print(show_student(records, student_id))
        elif choice == "5":
            student_id = input("Enter Student ID (6-digit): ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            add_record(records, student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "6":
            student_id = input("Enter Student ID: ")
            first_name = input("Enter New First Name (Leave blank to skip): ") or None
            last_name = input("Enter New Last Name (Leave blank to skip): ") or None
            class_standing = input("Enter New Class Standing Grade (Leave blank to skip): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam = input("Enter New Major Exam Grade (Leave blank to skip): ")
            major_exam = float(major_exam) if major_exam else None
            print(edit_record(records, student_id, first_name, last_name, class_standing, major_exam))
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            print(delete_record(records, student_id))
        elif choice == "8":
            save_records(filename, records)
            print("Records saved successfully.")
        elif choice == "9":
            break
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()
