class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return result

    def average_rate(self):
        result = 0
        for list in self.grades.values():
            result = result + sum(list) / len(list)
        result = result / len(self.grades.values())
        return "{:.2f}".format(result)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average_rate() < other.average_rate()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        result = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        if isinstance(self, Lecturer):
            result = result + f'Средняя оценка за лекции: {self.average_rate()}\n'
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.average_rate() < other.average_rate()

    def average_rate(self):
        result = 0
        for list in self.grades.values():
            result = result + sum(list) / len(list)
        result = result / len(self.grades.values())
        return "{:.2f}".format(result)


class Reviewer(Mentor):

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_rate_students(list_students, course):
    result = 0
    for student in list_students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            result = result + sum(student.grades[course]) / len(student.grades[course])
    result = result / len(list_students)
    return "{:.2f}".format(result)


def average_rate_lecturers(list_lecturers, course):
    result = 0
    for lecturer in list_lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            result = result + sum(lecturer.grades[course]) / len(lecturer.grades[course])
    result = result / len(list_lecturers)
    return "{:.2f}".format(result)


petrov_ivan = Student('Иван', 'Петров', 'male')
petrov_ivan.courses_in_progress += ['Python', 'Git']
petrov_ivan.finished_courses += ['Java']

sherbakova_zoya = Student('Зоя', 'Щербакова', 'female')
sherbakova_zoya.courses_in_progress += ['Web_Design', 'Python', 'Git']
sherbakova_zoya.finished_courses += ['PHP']

ilinskiy_gennadiy = Lecturer('Геннадий', 'Ильинский')
ilinskiy_gennadiy.courses_attached += ['Python', 'Git']

slesarenko_yuliya = Lecturer('Юлия', 'Слесаренко')
slesarenko_yuliya.courses_attached += ['Web_Design', 'Python']

plotnikova_angelina = Reviewer('Ангелина', 'Плотникова')
plotnikova_angelina.courses_attached += ['Git']

mirovaya_sofiya = Reviewer('София', 'Мировая')
mirovaya_sofiya.courses_attached += ['Python', 'Git', 'Web_Design']

# ocenka lectorov
petrov_ivan.rate_lecturer(slesarenko_yuliya, 'Python', 9)
petrov_ivan.rate_lecturer(ilinskiy_gennadiy, 'Python', 8)
petrov_ivan.rate_lecturer(ilinskiy_gennadiy, 'Git', 7)

sherbakova_zoya.rate_lecturer(slesarenko_yuliya, 'Web_Design', 9)
sherbakova_zoya.rate_lecturer(slesarenko_yuliya, 'Python', 6)
sherbakova_zoya.rate_lecturer(ilinskiy_gennadiy, 'Python', 7)

# ocenka studentov
mirovaya_sofiya.rate(petrov_ivan, 'Python', 5)
plotnikova_angelina.rate(petrov_ivan, 'Git', 2)
mirovaya_sofiya.rate(sherbakova_zoya, 'Python', 5)
plotnikova_angelina.rate(sherbakova_zoya, 'Git', 4)

mirovaya_sofiya.rate(petrov_ivan, 'Python', 3)
mirovaya_sofiya.rate(sherbakova_zoya, 'Python', 4)
mirovaya_sofiya.rate(sherbakova_zoya, 'Git', 3)
mirovaya_sofiya.rate(sherbakova_zoya, 'Web_Design', 4)
mirovaya_sofiya.rate(petrov_ivan, 'Git', 3)

print(sherbakova_zoya)
print(petrov_ivan)

print(slesarenko_yuliya)
print(ilinskiy_gennadiy)

print(mirovaya_sofiya)
print(plotnikova_angelina)

print(f'{sherbakova_zoya > petrov_ivan}')
print(f'{slesarenko_yuliya > ilinskiy_gennadiy}')

list_students = [petrov_ivan, sherbakova_zoya]
course = 'Git'
print(
    f'Средняя оценка за домашние задания по студентам из списка по курсу {course}: {average_rate_students(list_students, course)}')

list_lecturers = [slesarenko_yuliya, ilinskiy_gennadiy]
course = 'Python'
print(f'Средняя оценка лекторов за лекции по курсу {course}: {average_rate_lecturers(list_lecturers, course)}')
