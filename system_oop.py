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
        print(f"{self.name} courses is: ")
        for course in self.courses:
          print(f"-{course.title}")

    

   def add_attendance(self):
    today = datetime.now().strftime("%Y-%m-%d") 
    self.attendance.append(today)
    print(f"Attendance recorded for {self.name} on {today}")
             
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

   def display_info(self):
        super().display_info()
        print(f"The teacher ID is {self.teacher_id} and the subject is {self.subject}")

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

while True:
    print(" School Management Menu ")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Add Teacher")
    print("4. Show All Teachers")
    print("5. Save Students to File")
    print("6. Load Students from File")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")
        student = Student(name, age, student_id)

        while True:
            title = input("Enter course title to add. Type 'done' when finished: ")
            if title.lower().strip() == "done":
                break
            course = school.find_course_by_title(title)
            if not course:
                course = Course(title)
                school.add_course(course)
        student.add_course(course)

        school.add_student(student)

    elif choice == "2":
        school.show_all_students()

    elif choice == "3":
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        teacher_id = input("Enter teacher ID: ")
        subject = input("Enter subject: ")
        teacher = Teacher(name, age, teacher_id, subject)
        school.add_teacher(teacher)

    elif choice == "4":
        school.show_all_teachers()

    elif choice == "5":
        filename = input("Enter filename to save data (e.g. students.json): ")
        school.save_data_to_json(filename)

    elif choice == "6":
        filename = input("Enter filename to load data from: ")
        school.take_data_from_file(filename)

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
