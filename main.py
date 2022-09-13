
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: 9.9 \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return result


        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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
        result = f'Имя: {self.name} \nФамилия: {self.surname}'
        if isinstance(self, Lecturer):
            result = result + 'Средняя оценка за лекции: 9.9'
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




petrov_ivan = Student('Иван','Петров','male')
petrov_ivan.courses_in_progress = 'Pythone, Git'
petrov_ivan.finished_courses = 'Java'
sherbakova_zoya = Student('Зоя','Щербакова','female')

ilinskiy_gennadiy = Lecturer('Геннадий','Ильинский')
slesarenko_yuliya = Lecturer('Юлия','Слесаренко')

plotnikova_angelina = Reviewer('Ангелина','Плотникова')
mirovaya_sofiya = Reviewer('София','Мировая')


print(petrov_ivan)
    
        
        
        
