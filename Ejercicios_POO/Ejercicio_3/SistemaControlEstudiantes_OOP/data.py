import csv
from student import Student


def export_students(students):

    fieldnames = [
        "full_name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_studies_grade",
        "science_grade"
    ]

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            writer.writerow(student.__dict__)


def import_students(students):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            imported_students = []

            for row in reader:
                student = Student(
                    row["full_name"],
                    row["section"],
                    int(row["spanish_grade"]),
                    int(row["english_grade"]),
                    int(row["social_studies_grade"]),
                    int(row["science_grade"])
                )

                imported_students.append(student)

            students.clear()
            students.extend(imported_students)

    except FileNotFoundError:
        print("El archivo students.csv no existe.")
        return False

    return True