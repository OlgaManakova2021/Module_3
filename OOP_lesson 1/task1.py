# ****** АТРИБУТЫ КЛАССОВ И ОБЪЕКТОВ *************

class Point:

    "Класс для представления координат точек на плоскости"
    
    color = 'red'
    circle = 2

# после объявления класса он образовал пространство 
# имен Point, в котором есть две переменные color и circle

# print(Point.color)
# print(Point.circle)
# print(Point.__dict__)

# *****************
# создание экземпляров класса

pointOne = Point()
# print(pointOne.circle)
# print(pointOne.__dict__) # словарь будет пустым, т.к. внутри pointOne 
                         # указанных свойств не существует. pointOne ссылается на свойства (атрибуты) объекта Point

pointTwo = Point()
# print(pointTwo.color)
# print(pointTwo.__dict__)

# ********************
# измение значений свойств класса Point

# Point.circle = 3
# print(Point.circle)
# print(pointOne.circle)

# ********************
# измение значений свойств класса pointOne
# pointOne.color = "green" # теперь у класса pointOne есть свое собственное значение атрибута color
# print(pointOne.color)
# print(pointTwo.color) # свойство color у класса pointTwo не изменилось, 
                      # т.к. по-прежнему ссылается на пространство имен класса Point


# ********************
# добавление новых свойств класса Point
Point.hiddens = False
Point.inher = True
#print(Point.__dict__)
#print(pointOne.hiddens) # оба экземпляра приобрели новые свойства
#print(pointTwo.inher)

# ********************
# удаление атрибута из класса
del Point.hiddens
# print(Point.__dict__)

# функция getattr - позволяет проверить наличие атрибута у класса
# print(getattr(pointTwo, 'hiddens', False)) # в обоих экземплярах hiddens тоже удален
# print(getattr(pointTwo, 'inher', False))

# перед удалением атрибута необходимо проверить его наличие/отсутствие
# print(hasattr(Point, 'circle'))


# Упражнение 1
# Удалить атрибут inher класса Point, предварительно проверив его наличие.
# результат показать в консоль

# if hasattr(Point, 'inher'):
#     del Point.inher
# print(getattr(Point, 'inher', False))

#*************************
# Еще раз о пространстве имен
#*************************
# проверим пространста имен у экземпляров
# print(pointOne.__dict__)
# print(pointTwo.__dict__)
# они пустые
# добавим в класс pointOne собственный атрибут like
#pointOne.like = True
#print(pointOne.__dict__) # в пространстве имен класса pointOne появилось локальное свойство like

# изменим свойство circle
#pointOne.circle = 5
#print(pointOne.circle)

# теперь удалим  свойство circle из класса pointOne
#del pointOne.circle # свойство удаляется из собственного пространства имен класса pointOne
#print(pointOne.circle) # и замещается свойством из класса Point

#print(Point.__doc__)

