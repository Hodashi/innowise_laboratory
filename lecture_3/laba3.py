def main():
    students = []  # Student data storage list

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                add_grades_for_a_student(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
        except Exception as e:
            print("Invalid choice. Please enter a number between 1-5.")


def add_new_student(students):
    name = input("Enter student name: ").strip()

    # Check if the student exists
    for student in students:
        if student["name"].lower() == name.lower():
            print(f'Student "{name}" already exists.')
            return

    # Create a new student
    new_student = {"name": name, "grades": []}

    students.append(new_student)


def add_grades_for_a_student(students):

    if not students:
        print("No students available. Please add a student first.")
        return

    name = input("Enter student name: ").strip()

    # Looking for a student
    student_found = None
    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break

    if not student_found:
        print(f"Student '{name}' not found.")
        return

    print(f"Adding grades for {student_found["name"]}. Enter 'done' to finish.")

    while True:

        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()

        if grade_input == "done":
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student_found["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print(
                "Invalid input. Please enter a number between 0-100 or 'done' to finish."
            )


def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


def show_report(students):
    if not students:
        print("No students available.")
        return

    print("\n--- Student Report ---")

    averages = []

    for student in students:
        try:
            avg = calculate_average(student["grades"])
            if avg is None:
                print(f"{student['name']}'s average grade is N/A.")
            else:
                formatted_avg = round(avg, 1)
                print(f"{student['name']}'s average grade is {formatted_avg}.")
                averages.append(formatted_avg)
        except Exception as e:
            print(f"Error calculating average for {student['name']}: {e}")

    # General statistics
    if averages:
        max_averages = max(averages)
        min_averages = min(averages)
        overall_averages = sum(averages) / len(averages)

        print("---")
        print(f"Max Average: {round(max_averages,1)}")
        print(f"Min Average: {round(min_averages,1)}")
        print(f"Overall Average: {round(overall_averages,1)}")
    else:
        print("---")
        print("No valid averages to display statistics.")


def find_top_performer(students):

    if not students:
        print("No students available.")
        return

    # Filter students with valid grades
    students_with_grades = [i for i in students if i["grades"]]

    if not students_with_grades:
        print("No students with grades available.")
        return

    try:
        # Using max() with a lambda function
        top_student = max(
            students_with_grades, key=lambda x: calculate_average(x["grades"])
        )
        top_avg = round(calculate_average(top_student["grades"]), 1)
        print(
            f"The student with the highest average is {top_student['name']} with a grade of {top_avg}."
        )
    except Exception as e:
        print(f"Error finding top performer: {e}")


if __name__ == "__main__":
    main()
