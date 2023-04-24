class Parrot:

    # атрибуты класса
    species = "птица"

    # атрибуты экземпляра
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #  методы экземпяра
    def sing(self, song):
        return "{} поет {}".format(self.name, song)
    
    def dance(self):
        return "{} танцует".format(self.name)
    

# создаем экземпляр класса
kesha = Parrot("Кеша", 10)

# вызвваем методы экземпляра
print(kesha.sing("песенки"))
print(kesha.dance())
