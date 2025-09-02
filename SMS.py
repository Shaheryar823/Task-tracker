from abc import ABC, abstractmethod
from typing import List, Optional
import asyncio

class Person(ABC):
    @abstractmethod
    def get_role(self)->str:
        pass

    @abstractmethod
    def introduce(self)->str:
        pass

    @property
    @abstractmethod
    def id_number(self)->int:
        pass


class Student(Person):

    def __init__(self, name:str, id_number:int, grades:List[int]):
        self.name = name
        self._id_number = id_number   # use underscore to avoid clash
        self.__grades = grades

    async def study(self)->None:
        print(f"{self.name} start studing..")
        await asyncio.sleep(1)
        print(f"{self.name} finished studing")

    def get_grades(self)->List[int]:
        return self.__grades

    def set_grades(self,grades:int)->None:
        self.__grades.append(grades)

    def get_role(self)->str:
        return "Student"

    def introduce(self)->str:
        return f"Hi, my name is {self.name} and my ID is {self._id_number}, and I am a Student"


    def daily_task(self)->None:
        print("Attend classes")
        
    @property
    def id_number(self)->int:
        return self._id_number

class Teacher(Person):

    def __init__(self, name:str, id_number:int, salary:int)->None:
        self.name = name
        self._id_number = id_number   # use underscore to avoid clash
        self.__salary = salary

    async def Teaching(self)->None:
        print(f"{self.name} start Teaching..")
        await asyncio.sleep(2)
        print(f"{self.name} finished teaching")


    def get_salary(self)->int:
        return self.__salary

    def set_salary(self, salary:int)->None:
        self.__salary = salary

    def get_role(self)->str:
        return "Teacher"

    def introduce(self)->str:
        return f"Hi, my name is {self.name} and my ID is {self._id_number}, and I am a Teacher"

    def daily_task(self)->None:
        print("Take lectures")

    @property
    def id_number(self)->int:
        return self._id_number

class Principal(Person):

    def __init__(self, name:str, id_number:int, salary:int)->None:
        self.name = name
        self._id_number = id_number   # use underscore to avoid clash
        self.__salary = salary

    def get_salary(self)->int:
        return self.__salary

    def set_salary(self, salary:int)->None:
        self.__salary = salary

    def get_role(self)->str:
        return "Principal"

    def introduce(self)->str:
        return f"Hi, my name is {self.name} and my ID is {self._id_number}, and I am a Principal"

    def daily_task(self)->None:
        print("Manage school")

    async def Host_meeting(self)->None:
        print(f"{self.name} start meeting..")
        await asyncio.sleep(5)
        print(f"{self.name} finished meeting")

    @property
    def id_number(self)->int:
        return self._id_number

class School:
    def __init__(self,name:str)->None:
        self.name = name
        self._students:List[Student] = []
        self._teachers:List[Teacher] = []
        self._principal:Optional[Principal] = None

    def add_students(self, students:Student)->None:
        if not isinstance(students,Student):
            raise TypeError("only student objects can be added")
        if students in self._students:
            raise ValueError(f"{students.name} is already enrolled")
        self._students.append(students)

    def add_teachers(self,teachers:Teacher)->None:
        self._teachers.append(teachers)

    def add_principal(self,principal:Principal)->None:
        self._principal = principal

    def get_students(self)->List[Student]:
        return self._students

    def get_teachers(self)->List[Teacher]:
        return self._teachers
    
    def get_principal(self)->Optional[Principal]:
        return self._principal



import random

# Create a School
my_school = School("Green Valley High")

# Add 100 Students
Student_obj = []
for i in range(1, 101):  # IDs 1–100
    name = f"Student{i}"
    student_id = 1000 + i
    grades = [random.randint(50, 100) for _ in range(5)]  # 5 random grades
    s = Student(name, student_id, grades)
    Student_obj.append(s)
    my_school.add_students(s)



# Add 25 Teachers
Teacher_obj = []
salaries = 0
for i in range(1, 26):  # IDs 1–25
    name = f"Teacher{i}"
    teacher_id = 2000 + i
    salary = random.randint(40000, 70000)  # random salary
    t = Teacher(name, teacher_id, salary)
    Teacher_obj.append(t)
    salaries += t.get_salary()
    my_school.add_teachers(t)

# Add 1 Principal
p = Principal("Dr. Brown", 3001, 120000)
my_school.add_principal(p)
s = Student("Student1", 1001, [40,50,45,40,-1])
Student_obj.append(p)
my_school.add_students(p)

# Quick Summary
print(f"School: {my_school.name}")
print(f"Total Students: {len(my_school.get_students())}")
print(f"Total Teachers: {len(my_school.get_teachers())}")
principal = my_school.get_principal()
if principal is not None:
    print(f"Principal: {principal.introduce()}")
else:
    print("No principal assigned yet.")
print(f"Teachers total salary cost is {salaries}")


#Students Avearage Grades
for S_O in Student_obj:
    average = 0
    for j in S_O.get_grades():
        average += j
    print(f"Student name : {S_O.name}, average grade : {average/5}")


async def main():
    await asyncio.gather(
        *(i.study() for i in Student_obj[:5]),
        *(i.Teaching() for i in Teacher_obj),
        p. Host_meeting()
        )

asyncio.run(main())