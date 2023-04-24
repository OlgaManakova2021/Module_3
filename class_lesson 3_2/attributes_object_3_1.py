class Person:

    def __init__(self, name):
        self.name = name    # имя человека
        self.age = 1        # возраст человека

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Tom")

# обращение к атрибутам
# получение значений
print(tom.name)             # Tom
print(tom.age)              # 1

# изменение значения
tom.age = 37
print(tom.age)              # 37

tom.company = "Microsoft"   # динамическое определение атрибута
print(tom.company)

tom.display_info()


bob = Person("Bob")
bob.age = 41
bob.display_info()