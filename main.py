class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students.append(Student(roll, name))
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent List")
        for s in students:
            print(s.roll_no, "-", s.name)

    elif choice == "3":
        break
