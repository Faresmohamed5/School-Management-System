import json
from datetime import datetime
class Person: 
  
  def __init__(self,name,age):
    self.__name=name
    self.__age=age

  @property
  def name(self):
        return self.__name
   
  @name.setter 
  def name(self,value):
     if value:
        self.__name=value
     else:
        print("you shoud enter a correct name ")
  @property

  def age(self):
   return self.__age
  
  @age.setter
  def age(self,value):
     if value>0:
        self.__age=value
     else :
        print("you should enter a valid age ") 

  def display_info(self) :
     print(f"the name is {self.name} and the age is {self.age}")

class Course:
    def __init__(self, title):
        self.title = title

class Student(Person):
   def __init__(self, name, age,student_id):
      super().__init__(name, age)
      self.student_id=student_id
      self.grades={}
      self.attendance=[]
      self.courses=[]

   def add_grade(self,subject,grade):
    self.grades[subject] = grade 

   def avarage_grades(self):
      if self.grades:
         return sum(self.grades.values())/len(self.grades)
      return 0
   
   def add_course(self,course):
      if isinstance(course,Course) :
          if course  not in self.courses: 
             self.courses.append(course)
             print(f"Course '{course.title}' enrolled successfully.")
          else:
              print(f"Course '{course.title}' is already enrolled.")
      else:
        print("Invalid course object.")

   def show_courses(self):
      if self.courses:
        print(f"{self.name} courses is ")
        for course in self.courses:
          print(f"-{course.title}")

   def add_attendance(self,data):
      
      self.attendance.append(data)
             
   def  show_attendance(self): 
      if self.attendance:
         print(f"the attendace of {self.name} is :")
         for i,date in enumerate(self.attendance,start=1):
            print(f"{i}-{date}")
      else:
         print(f"{self.name} has no attendance ") 
   def data_in_dic(self):
        return { 
        "name": self.name,
        "age": self.age,
        "student_id": self.student_id,
        "grades": self.grades,
        "attendance": self.attendance,
        "courses": [course.title for course in self.courses]
        
    }       


class Teacher(Person):
   def __init__(self, name, age,tacher_id,subject):
      super().__init__(name, age)
      self.teacher_id=tacher_id
      self.subject=  subject 
      self.courses=[]
   def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has been assigned to course '{course.title}'")
        else:
            print(f"{self.name} is already assigned to course '{course.title}'")

   def display_info(self):
        super().display_info()
        print(f"The teacher ID is {self.teacher_id} and the subject is {self.subject}")
        if self.courses:
            print("Courses:")
            for course in self.courses:
                print(f"- {course.title}")

class School():
   def __init__(self,name):
      self.name =name 
      self.students=[]
      self.teachers=[]
      self.courses=[]
   def add_student(self,student):
     if isinstance(student,Student):
        self.students.append(student)
     else:
        print("he is not a student")

   def add_teacher (self,teacher):
      if isinstance(teacher,Teacher):
         self.teachers.append(teacher)
      else:
         print("he is not a teacher")

   def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)  
        else:
           print("it is not a course ") 

   def find_course_by_title(self, title):
        for course in self.courses:
            if course.title == title:
                return course
        return None     
   def show_all_students(self):
      print("all students : ")
      for student in self.students:
        student.display_info()
      print("................................................")

   def show_all_teachers(self):
      print("all teachers : ")
      for teacher in self.teachers:
         teacher.display_info()
      print("................................................")  
      
   def save_data_to_json(self, data_file):
    data=[student.data_in_dic() for student in self.students]
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
        print("The data of student added successfully.") 
        
   def take_data_from_file (self, data_file): 
     with open(data_file, "r") as file:
         data=json.load(file)
     for item in data:
        student = Student(item["name"], item["age"], item["student_id"])
        student.grades = item["grades"]
        for title in item["courses"]:
                    course = self.find_course_by_title(title)
                    if course:
                        student.add_course(course)
        self.add_student(student)
        print("Student records loaded.")

school = School("Smart Future School")

s1 = Student("Ali Mohamed", 16, "s001")
s1.add_grade("Math", 90)
s1.add_grade("Science", 85)
s1.add_grade("English", 80)

s2 = Student("Sara Mohamed", 15, "s002")
s2.add_grade("Math", 95)
s2.add_grade("Science", 88)
s2.add_grade("English", 80)

t1 = Teacher("Mr. Ahmed", 35, "T001", "Math")
t2 = Teacher("Ms. Mona", 30, "T002", "English")

c1 = Course("Math")
c2 = Course("Science")
c3 = Course("English")

school.add_course(c1)
school.add_course(c2)
school.add_course(c3)

s1.add_course(c1)
s1.add_course(c2)
s2.add_course(c1)
s2.add_course(c3)

t1.assign_course(c1)
t2.assign_course(c3)

school.add_student(s1)
school.add_student(s2)
school.add_teacher(t1)
school.add_teacher(t2)

school.show_all_students()
school.show_all_teachers()
