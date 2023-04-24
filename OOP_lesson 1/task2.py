# ****** МЕТОДЫ КЛАССОВ. АТРИБУТ self *************

class Point:

    "Класс для представления координат точек на плоскости"

    color = 'red'
    circle = 2

    #  создание методов
    #******************
    # метод назначения координат
    def set_coords(self, x=0, y=0):
        print("вызов метода set_coords для " + str(self))
        self.x = x
        self.y = y

    # метод получения координат
    def get_coords(self):
        print("вызов метода get_coords для " + str(self))
        return (self.x, self.y)

pointOne = Point()

# вызов метода
pointOne.set_coords(10, 20)
print(pointOne.__dict__)

# если при вызове не передаются значения, то подставятся начения по умолчанию
# pointOne.set_coords()
# print(pointOne.__dict__)

pointTwo = Point()
#pointTwo.set_coords(100, 200)
#print(pointTwo.__dict__)

print(pointOne.get_coords())


