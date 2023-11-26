class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Student Name: ", self.name)
        print("Student Roll No: ", self.roll)
        print("Student Marks: ", self.marks)
        print()


S = Student("Tú", 28, 2810.2003)
S.display()
