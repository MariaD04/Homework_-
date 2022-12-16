#-*-coding: utf-8 -*-
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else: 
                lecturer.rates[course] = [rate] 
        else:
            return 'Ошибка'
        
    def sr_grades(self):
        count = 0 
        sum_grade = 0 
        for marks in self.grades.values():
            for mark in marks:
                sum_grade += mark 
            course_middle = sum_grade / len(marks) 
            count += course_middle
        if count == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{round(count / len(self.grades.values()))}'
    
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.sr_grades()}\n'
        res += f'Курсы в процессе изучения: {(", ".join(self.courses_in_progress))}\n'
        res += f'Завершённые курсы: {(", ".join(self.finished_courses))}\n'
        return res
    
    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Такого студента нет')
            return
        return self.sr_grades() < student.sr_grades()
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
     
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.rates = {}
        
    def sr_grades(self):
        count = 0
        sum_grade = 0
        for marks in self.rates.values():
            for mark in marks:
                sum_grade += mark
            sr_grade = sum_grade / len(marks)
            count += sr_grade
        if count != 0:
            return round(sr_grade / len(self.rates.values()))
        return '0'
    
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.sr_grades()}\n'
        return res
    
    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Такого лектора нет')
            return
        return self.sr_grades() < lecturer.sr_grades()
   
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade): 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade] 
        else:
            return 'Ошибка' 
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        return res

def students_grade(students_list, course): 
    mid_sum_grades = 0 
    counter = 0 
    for person in students_list:
        if course in person.grades.keys(): 
            person_grades = 0 
            for grades in person.grades[course]:
                person_grades += grades
            mid_sum = person_grades / len(person.grades[course]) 
            mid_sum_grades += mid_sum 
            counter += 1 
    if mid_sum_grades == 0: 
        return f'Оценок по этому предмету нет' 
    else: 
        return f'{round(mid_sum_grades / counter)}' 

def lecturers_grade(lecturer_list, course):
    mid_sum_grade = 0
    count=0
    for person in lecturer_list:
        if course in person.rates.keys():
            person_grades = 0
            for grades in person.rates[course]:
                person_grades += grades
            mid_sum = person_grades / len(person.rates[course])
            mid_sum_grade += mid_sum
            count += 1
    if mid_sum_grade != 0:
        return f'{round(mid_sum_grade / count)}'
    return f'Оценок по этому предмету нет'
                
first_student = Student('Ruoy', 'Eman', 'm')
first_student.finished_courses = ['Git','JavaScript']
first_student.courses_in_progress = ['Python','Java']
 
second_student = Student('Peter', 'Parker', 'm')
second_student.finished_courses = ['Python','Java']
second_student.courses_in_progress = ['JavaScript','Git']

first_lecturer = Lecturer('Tony', 'Stark')
first_lecturer.courses_attached = ['Python','Java']

second_lecturer = Lecturer('Bruce', 'Banner')
second_lecturer.courses_attached = ['Git','JavaScript']

first_reviewer = Reviewer('Steve', 'Rogers')
first_reviewer.courses_attached = ['Python','Git']

second_reviewer = Reviewer('Miles', 'Morales')
second_reviewer.courses_attached = ['Java','JavaScript']

students_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Java', 9)
first_reviewer.rate_hw(first_student, 'Java', 10)
first_reviewer.rate_hw(first_student, 'Java', 7)
first_reviewer.rate_hw(first_student, 'Git', 5)
first_reviewer.rate_hw(first_student, 'Git', 8)
first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(first_student, 'JavaScript', 9)
first_reviewer.rate_hw(first_student, 'JavaScript', 5)
first_reviewer.rate_hw(first_student, 'JavaScript', 8)

second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Java', 9)
second_reviewer.rate_hw(second_student, 'Java', 7)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Git', 5)
second_reviewer.rate_hw(second_student, 'Git', 3)
second_reviewer.rate_hw(second_student, 'JavaScript', 7)
second_reviewer.rate_hw(second_student, 'JavaScript', 5)
second_reviewer.rate_hw(second_student, 'JavaScript', 9)

first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 7)
first_student.rate_lecturer(first_lecturer, 'Python', 5)
first_student.rate_lecturer(first_lecturer, 'Java', 10)
first_student.rate_lecturer(first_lecturer, 'Java', 10)
first_student.rate_lecturer(first_lecturer, 'Java', 8)

second_student.rate_lecturer(second_lecturer, 'Git', 8)
second_student.rate_lecturer(second_lecturer, 'Git', 5)
second_student.rate_lecturer(second_lecturer, 'Git', 1)
second_student.rate_lecturer(second_lecturer, 'JavaScript', 1)
second_student.rate_lecturer(second_lecturer, 'JavaScript', 5)
second_student.rate_lecturer(second_lecturer, 'JavaScript', 10)

print(first_student)
print(second_student)
if first_student < second_student:
    print('Средняя оценка за дз у первого студента ниже')
else:
    print('Средняя оценка за дз у первого студента выше')
print()

print(first_lecturer)
print(second_lecturer)
if first_lecturer < second_lecturer:
    print('Средняя оценка за лекции у первого лектора ниже')
else:
    print('Средняя оценка за лекции у первого лектора выше')
print()
   
print(first_reviewer)
print(second_reviewer)

print(f'Средняя оценка студентов по курсу "Python": {students_grade(students_list, "Python")}')
print(f'Средняя оценка студентов по курсу "JavaScript": {students_grade(students_list, "JavaScript")}')
print()
print(f'Средняя оценка лекторов по курсу "Python": {lecturers_grade(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов по курсу "Java": {lecturers_grade(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "JavaScript": {lecturers_grade(lecturer_list, "JavaScript")}')
print(f'Средняя оценка лекторов по курсу "Git": {lecturers_grade(lecturer_list, "Git")}')