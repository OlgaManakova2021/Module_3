class Parrot:

    def fly(self):
        print("Попугай умеет летать")

    def swim(self):
        print("Попугай не умеет плавать")


class Penguin:

    def fly(self):
        print("Пингвин не умеет летать")

    def swim(self):
        print("Пингвин умеет плавать")

# общий интерфейс
def flying_test(bird):
    bird.fly()

# создаем экземпляр класса
kesha = Parrot()
peggy = Penguin()

# передача объектов в качестве аргумента
flying_test(kesha)
flying_test(peggy)

