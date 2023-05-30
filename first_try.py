class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def _not_genius_(self):
        averages = {}
        for key, values in self.grades.items():
            average = sum(values) / len(values)
            averages = average
        return averages
        
    def __str__(self) :
        return  f"""
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за домашние задания: {Student._not_genius_(self)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}
                """
    
    def __lt__(self, other):
        a = self._not_genius_()
        b = other._not_genius_()
        print(a < b)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def _not_genius_(self):
        averages = {}
        for key, values in self.grades.items():
            average = sum(values) / len(values)
            averages = average
        return averages
    
    def __str__(self) :
        return  f"""
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {(Lecturer._not_genius_(self))}
                """
    def __lt__(self, other):
        a = self._not_genius_()
        b = other._not_genius_()
        print(a < b)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"""
Имя: {self.name} 
Фамилия: {self.surname}
                """
        
def student_midle_rate(student_list, course):
    total_grades = []
    count = 0
    for student in student_list:
        if course in student.courses_in_progress and course in student.grades:
            grades = student.grades[course]
            total_grades.extend(grades)
            count += len(grades)
    if count > 0:
        average_grade = sum(total_grades) / count
        return round(average_grade, 1)
    else:
        return 'Нет оценок для данного курса'

eren = Student('Eren', 'Eger', 'male')
armin = Student('Armin', 'Alert', 'male')
mikasa = Student('Mikasa', 'Ackerman', 'female')

eren.courses_in_progress += ['Python',]
armin.courses_in_progress += ['Python', 'Java', 'SQL']
mikasa.courses_in_progress += ['C++', 'C#']
eren.finished_courses += ['Ведение в програмирование']
armin.finished_courses += ['Ведение в програмирование']
mikasa.finished_courses += ['Ведение в програмирование']
 
erwin = Lecturer('Erwin', 'Smith')
hanji = Lecturer('Hanji', 'Zoe')

erwin.courses_attached += ['Python', 'Java']
hanji.courses_attached += ['C++', 'C#', 'SQL']

grisha = Reviewer('Grisha', 'Eger')

eren.rate_hw(erwin, 'Python', 10)
armin.rate_hw(erwin, 'Java', 8)
armin.rate_hw(erwin, 'Python', 5)
mikasa.rate_hw(hanji, 'C++', 9)
armin.rate_hw(hanji, 'SQL', 10)
mikasa.rate_hw(hanji, 'C#', 3)

grisha.rate_hw(eren, 'Python', 6)
grisha.rate_hw(armin, 'Java', 10)
grisha.rate_hw(armin, 'Python', 9)
grisha.rate_hw(armin, 'SQL', 9)
grisha.rate_hw(mikasa, 'C++', 8) 
grisha.rate_hw(mikasa, 'C#', 6) 

# print(grisha)
# print(erwin)
# print(eren)
# eren > mikasa
# hanji > erwin

students_list = [eren, mikasa, armin]

middle = student_midle_rate(students_list, 'Python')
print(middle)


    