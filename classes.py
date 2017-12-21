students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, given_name, family_name, student_id=332):
        self.firstName = given_name
        self.lastName = family_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.firstName + " " + self.lastName

    def get_name_capitalized(self):
        return self.firstName.capitalize() + " " + self.lastName.capitalize()

    def get_school_name(self):
        """
        Returns the name of this student's school.
        :return: The string saved for the name of the student's school.
        """
        return self.school_name


class HS_Student(Student):

    school_name = "Springfield High"

    def get_school_name(self):
        return self.firstName + " " + self.lastName + " is a high school student"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + " -HS"