class Person:
    type = "Person"
    desctiption = "Описывает человека"

    def __init__(self, name):
        self.name = name    # имя человека
       

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")

print(Person.type)          # Person
print(Person.desctiption)   # Описывает человека

# Person.type = "Class Person"
# print(Person.type)          # Class Person

tom = Person("Tom")
bob = Person("Bob")
print(tom.type)             # Person
print(bob.type)             # Person