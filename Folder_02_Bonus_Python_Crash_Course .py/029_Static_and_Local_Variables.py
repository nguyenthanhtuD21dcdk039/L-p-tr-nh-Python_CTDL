class Student:
    college = "Vietnamese"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Student Name: ", self.name)
        print("Student Roll No: ", self.roll)
        print("Student Marks: ", self.marks)
        print("College Name: ", Student.college)
        print()


S1 = Student("Tú", 28, 2810.2003)
S2 = Student("Thanh", 10, 20.03)
S1.display()
S2.display()
