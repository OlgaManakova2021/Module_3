class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Цена продажи: {}".format(self.__maxprice))

    def setMaxPrice(self, prise):
        self.__maxprice = prise


c = Computer()
c.sell()

# изменение цены
c.__maxprice = 1000
c.sell()

# используем функцию изменения цены
c.setMaxPrice(1000)
c.sell()



# Ранее был объявлен класс «Computer». 
# Затем был использован метод «__init__()» 
# для хранения максимальной цены компьютера. 
# Затем была изменена цена - безуспешно, 
# так как Python воспринимает «__maxprice» как приватный атрибут. 
# Как можно заметить, для изменения цены нужно 
# использовать специальную функцию - «setMaxPrice()»,
# которая принимает цену в качестве параметра.
