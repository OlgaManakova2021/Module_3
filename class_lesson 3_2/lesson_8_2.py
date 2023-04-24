# Создать класс «Student», который содержит 
# имя студента - «full_name», номер группы 
# «group_number» и список полученных оценок - «progress». 
# В программе вводится список студентов. Далее список 
# сортируется по имени, потом выводятся студенты, 
# имеющие неудовлетворительные оценки.

class Student:
    def __init__(self, full_name="", group_number=0, progress=[]):      # конструктор
        self.full_name = full_name                                      # имя
        self.group_number = group_number                                # номер группы
        self.progress = progress                                        # оценки
    
    def __str__(self):               # печатаемое представление экземпляра класса
        txt = 'Студент:  ' + self.full_name + ' Группа:  ' + self.group_number
        txt  += '   Оценки:'
        for x in self.progress:
            txt += ' ' + str(x)      # добавляем список оценок
        return txt
    
#------------------------------------------------------------------
def SortPram(st): #
    return st.full_name
#------------------------------------------------------------------

st_size = 5                                 # количество студетов 

students = []                               # создание пустого списка
for i in range(st_size):                    # цикл для ввода студентов
    print("Введите полное имя студента:  ")
    full_name = input()                     
    print("Введите номер группы:  ")
    group_number = input()              
    n=5
    print('Введите  ' ,n, '  оценок в столбик')
    progress = []
    for i in range(n):
        score = int(input())                # ввод оценок
        progress.append(score)              # добавление оценок
    
    # создание экземпляра класса Student
    st = Student(full_name, group_number, progress)
    students.append(st)                     # добавление экземпляра в список

print("Students list: ")
for st in students:                         # вывод полного спика студентов
    print(st)

# сортировка по фамилии, ключ сортировки определяется функцией SortPram
students = sorted(students, key=SortPram)

print("Отсортированный список студентов")
for st in students:                         # выод отсортированного списка
    print(st)