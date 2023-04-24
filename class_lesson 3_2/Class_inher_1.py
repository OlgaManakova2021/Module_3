# родительский класс
class Bird:

    def __init__(self):
        print("Птица готова")

    def whoisThis(self):
        print("Птица")

    def swim(self):
        print("Плывет быстрее")


# дочерний класс
class Penguin(Bird):

    def __init__(self):
        # вызов функции super()
        super().__init__()
        print("Пингвин готов")

    def whoisThis(self):
        print("Пингвин")

    def run(self):
        print("Бежит быстрее")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()






