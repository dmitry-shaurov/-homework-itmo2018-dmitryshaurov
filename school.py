class Course(object):
    def __init__(self, name, teacher):
        teachers = []
        teachers.append(teacher)
        self.name = name
        self.teachers = teachers

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def get_teachers(self):
        return self.teachers
    def delete_teacher(self, teacher):
        self.teachers.remove(teacher)

class Teacher(object):
    def __init__(self, name, student_group):
        student_groups = []
        student_groups.append(student_group)
        self.name = name
        self.student_groups = student_groups

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def add_student_group(self, student_group):
        self.student_groups.append(student_group)
    def get_student_groups(self):
        return self.student_groups
    def delete_student_group(self, student_group):
        try:
            self.student_groups.remove(student_group)
        except ValueError:
            print("{} is not in the list of student_groups". format(student_group))

# Creating objects
teacher1 = Teacher("Kirill", "Winter 2018")
teacher2 = Teacher("Mr. Smith", "Summer 2017")
# Adding a new group
teacher1.add_student_group("Spring 2018")
# Creating a course
course1 = Course("python developer", teacher1)
course1.add_teacher(teacher2)
course1.delete_teacher(teacher3)
