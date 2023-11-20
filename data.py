
#9xwXZcpC4TJtUdG7yowvuQ



import sqlite3

con = sqlite3.connect("students.db")
db = con.cursor()

def main():
    create_student('George', 'Knightly', 10)
    students = fetch_students()
    print(students)

def create_student(first_name, last_name, grade_level):
    grade_level = int(grade_level)
    db.execute("INSERT INTO students (first_name, last_name, grade_level) VALUES(?, ?, ?)", (first_name, last_name, grade_level))
    con.commit();

def fetch_students():
    students = db.execute("SELECT * FROM students")
    return students.fetchall()


if __name__ == "__main__":
    main()