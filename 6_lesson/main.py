class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_db.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for grades_list in self.grades.values():
                count += sum(grades_list) / len(grades_list)
            return round(count / len(self.grades), 1)
        else:
            return 'У студента нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.__average_grade()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() < other.__average_grade()
        return 'У одного/обоих студентов нет оценок'

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() <= other.__average_grade()
        return 'У одного/обоих студентов нет оценок'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() == other.__average_grade()
        return 'У одного/обоих студентов нет оценок'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_db.append(self)

    def __average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for grades_list in self.grades.values():
                count += sum(grades_list) / len(grades_list)
            return round(count / len(self.grades), 1)
        else:
            return 'У лектора нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() < other.__average_grade()
        return 'У одного/обоих лекторов нет оценок'

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() <= other.__average_grade()
        return 'У одного/обоих лекторов нет оценок'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() == other.__average_grade()
        return 'У одного/обоих лекторов нет оценок'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


students_db = []
lecturer_db = []


student_1 = Student('Студент1', 'Один', 'М')
student_2 = Student('Студент2', 'Два', 'Ж')

lecturer_1 = Lecturer('Лектор1', 'Один')
lecturer_2 = Lecturer('Лектор2', 'Два')

reviewer_1 = Reviewer('Проверяющий1', 'Один')
reviewer_2 = Reviewer('Проверяющий2', 'Два')


student_1.finished_courses = ['Git']
student_2.finished_courses = ['English', 'Git']

student_1.courses_in_progress = ['Python', 'DevOps']
student_2.courses_in_progress = ['Python', 'DataBase']

lecturer_1.courses_attached = ['Git', 'Python', 'DevOps', 'English']
lecturer_2.courses_attached = ['Git', 'Python', 'DataBase']

reviewer_1.courses_attached = ['Git', 'Python', 'DataBase']
reviewer_2.courses_attached = ['Git', 'Python', 'DevOps', 'English']


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 9)

student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 7)

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 5)

reviewer_2.rate_hw(student_1, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Python', 3)


def view_grandes(human):
    if isinstance(human, Student) or isinstance(human, Lecturer):
        for itm, grn in human.grades.items():
            print(f'Оценки за предмет {itm}: {grn}\n')
    return


print(student_1)
view_grandes(student_1)

print(student_2)
view_grandes(student_2)

print(lecturer_1)
view_grandes(lecturer_1)

print(lecturer_2)
view_grandes(lecturer_2)

print(reviewer_1, '\n')

print(reviewer_2, '\n')


print(f'student1 > student2 - {student_1 > student_2}')
print(f'student1 < student2 - {student_1 < student_2}')
print(f'student1 >= student2 - {student_1 >= student_2}')
print(f'student1 <= student2 - {student_1 <= student_2}')
print(f'student1 == student2 - {student_1 == student_2}\n')


def average_grade_student(students, course_name):
    filter_students = [i for i in students if course_name in i.grades.keys()]
    count = 0
    for item in filter_students:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    return round(count / len(filter_students), 1)


print('Средняя оценка студентов на курсе Python -', average_grade_student(students_db, 'Python'), '\n')


def average_grade_lecturer(lecturers, course_name):
    filter_lecturers = [i for i in lecturers if course_name in i.grades.keys()]
    count = 0
    for item in filter_lecturers:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    return round(count / len(filter_lecturers), 1)


print('Средняя оценка лекторов на курсе Python -', average_grade_lecturer(lecturer_db, 'Python'))
