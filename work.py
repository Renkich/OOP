class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_mark = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_mark}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.average_mark < other.average_mark

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_mark = 0    
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_mark}"

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
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def average_student(students_list, course):
    total_sum = 0
    total_count = 0
    for student in students_list:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    if total_count == 0:
        return 0
    return total_sum / total_count

def average_lecturer(lecturers_list, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    if total_count == 0:
        return 0
    return total_sum / total_count

# Создание и настройка объектов
student_1 = Student('Иван', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']

student_2 = Student('Ной', 'Ноев', 'M')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Excel']
student_2.courses_in_progress += ['Java']

students_list = [student_1, student_2]

reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']

# Выставление оценок
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Excel', 6)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Java', 6)
reviewer_1.rate_hw(student_2, 'Excel', 1)

# Расчет средних оценок студентов
for student in students_list:
    total = 0
    count = 0
    for course in student.grades:
        total += sum(student.grades[course])
        count += len(student.grades[course])
    student.average_mark = total / count if count > 0 else 0

lecturer_1 = Lecturer('Сидор', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

lecturer_2 = Lecturer('Авель', 'Авелев')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['Excel']

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 8)
student_1.rate_lecturer(lecturer_1, 'Excel', 2)

student_2.rate_lecturer(lecturer_2, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Java', 1)
student_2.rate_lecturer(lecturer_2, 'Excel', 10)

lecturer_list = [lecturer_1, lecturer_2]

# Расчет средних оценок лекторов
for lecturer in lecturer_list:
    total = 0
    count = 0
    for course in lecturer.grades:
        total += sum(lecturer.grades[course])
        count += len(lecturer.grades[course])
    lecturer.average_mark = total / count if count > 0 else 0

# Вывод результатов
print(f"Средняя оценка студентов по предмету Python: {average_student(students_list, 'Python')}")
print(f"Средняя оценка студентов по предмету Java: {average_student(students_list, 'Java')}")
print(f"Средняя оценка лекторов по предмету Python: {average_lecturer(lecturer_list, 'Python')}")
print(f"Средняя оценка лекторов по предмету Java: {average_lecturer(lecturer_list, 'Java')}")

print("\nИнформация о студентах:")
print(student_1)
print()
print(student_2)

print("\nИнформация о проверяющих:")
print(reviewer_1)

print("\nИнформация о лекторах:")
print(lecturer_1)
print()
print(lecturer_2)

'''
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_mark = 0

        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    
    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_mark}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.average_mark() < other.average_mark()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_mark = 0    
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}") 
 
class Lecturer(Mentor):
    grades = {}

  

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
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_mark}'
        return res

def average_student(students_list, course):
    grades_count = 0
    grades_sum = 0
    for student in students_list:
        if course in student.grades:
           for course in student.grades:
                grades_count = len(student.grades[course])
                grades_sum += student.grades[course]
           return grades_sum/grades_count
        else:
            print('Такого предмета нет')

def average_lecturer(lecturer_list, course):
     grades_count = 0
     grades_sum = 0
     for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
           
            for course in lecturer.grades:
                grades_count = len(lecturer.grades[course])
                grades_sum += sum(lecturer.grades[course])
            return grades_sum/grades_count
        else:
            print('Такого предмета нет')



        





student_1 = Student('Иван', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']

student_2 = Student('Ной', 'Ноев', 'M')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Excel']
student_2.courses_in_progress += ['Java']

students_list = [student_1, student_2]


print(f'Средняя оценка студентов по предмету Python {average_student(students_list, 'Python')}')

print(f'Средняя оценка студентов по предмету Java {average_student(students_list, 'Java')}')


reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Excel', 6)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print("-----------------\n")

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Java', 6)
reviewer_1.rate_hw(student_2, 'Excel', 1)
print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}')
print("-----------------\n")

lecturer_1 = Lecturer('Сидор', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 8)
student_1.rate_lecturer(lecturer_1, 'Excel', 2)
print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print("-----------------\n")

lecturer_2 = Lecturer('Авель', 'Авелев')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['Excel']

student_2.rate_lecturer(lecturer_2, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Java', 1)
student_2.rate_lecturer(lecturer_2, 'Excel', 10)
print(f'Оценки лектору: {lecturer_2.name} {lecturer_2.surname}\n{lecturer_2.grades}')
print("-----------------\n")

lecturer_list = [lecturer_1, lecturer_2]

print(f'Средняя оценка лекторов по предмету Python {average_lecturer(lecturer_list, 'Python')}')

print(f'Средняя оценка лекторов по предмету Java {average_lecturer(lecturer_list, 'Java')}')

print(student_1)

print(student_2)

print(reviewer_1)

print(lecturer_1)

print(lecturer_2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_mark = 0

        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
        def __average_mark(self):
            grades_count = 0
            grades_sum = 0
            for grade in self.grades:
                grades_count += len(self.grades[grade])
                grades_sum += sum(self.grades[grade])
            if grades_count > 0:
                return grades_sum / grades_count
            else:
                return 0
    
    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_mark}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.average_mark() < other.average_mark()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_mark = 0    
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}") 
 
class Lecturer(Mentor):
    grades = {}

    def __average_hw_grade(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0       

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
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_mark}'
        return res

student_1 = Student('Иван', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']

reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Excel', 6)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print("-----------------\n")

lecturer_1 = Lecturer('Сидор', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 8)
student_1.rate_lecturer(lecturer_1, 'Excel', 2)
print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print("-----------------\n")

print(student_1)

print(reviewer_1)

print(lecturer_1)
'''