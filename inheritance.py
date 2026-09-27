class Person:
    def __init__(self,fname,lname,age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
    def print_info(self):
        print(self.first_name, self.last_name, self.age)
    

class Student(Person):
    def __init__(self, fname, lname, age, student_id, major, standard):
        super().__init__(fname, lname, age)
        
        self.student_id = student_id
        self.major = major
        self.standard = standard

    def print_student_info(self):
        print(self.student_id, self.major, self.standard)

class Teacher(Person):
    def __init__(self, fname, lname, age, teacher_id, designation, course):
        super().__init__(fname, lname, age)
        
        self.teacher_id = teacher_id
        self.designation = designation
        self.course = course
    
    def print_teacher_info(self):
        print(self.teacher_id, self.designation, self.course)

stu1 = Student("Syed", "Ahmed", 20, "STU123", "computer science", 12)
tea1 = Teacher("James", "Cooler", 30, "TEA123", "Professor", "python")

stu1.print_info()
stu1.print_student_info()

tea1.print_info()
tea1.print_teacher_info()

