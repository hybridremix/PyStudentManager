students = []

class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalization(self):
        return self.get_name_capitalization()

    def get_school_name(self):
        return self.school_name


#mark = Student("Mark")
#print(mark)

print(Student.school_name)