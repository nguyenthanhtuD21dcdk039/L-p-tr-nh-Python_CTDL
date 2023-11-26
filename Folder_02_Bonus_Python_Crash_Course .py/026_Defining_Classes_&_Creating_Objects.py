'''
class Student:
    """Nguyễn Thanh Tú: 28/10/2003"""

    def __init__(self):
        self.name = "Tú"
        self.roll = 28
        self.marks = 2810.2003

    def __str__(self):
        return "This is Student Class"

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)


S1 = Student()
S2 = Student()
S3 = Student()
S1.display()
S2.display()
S3.display()
'''


class Student:
    """Nguyễn Thanh Tú: 28/10/2003"""

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return "This is Student Class"

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)


S = [
    Student("Tú", 28, 2810.2003),
    Student("Tú", 28, 2810.2003),
    Student("Tú", 28, 2810.2003),
]

for i in S:
    i.display()
