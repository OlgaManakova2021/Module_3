# концепция множественного наследования
# позволяет создать класс, имеющий несколько родителей. 
# В данном случае список наследуемых 
# классов перечисляется при объявлении класса.

class Student:
    def pass_exam(self):
        print("Я сдал экзамен!")

class Worker:
    def work(self):
        print("Работаю...")

class FoorballPlayer:
    def score(self):
        print("Забил гол!!!")

class StudentWorkerAndFoorballPlayer(Student, Worker, FoorballPlayer):
    pass


if __name__ == "__main__":
    s = StudentWorkerAndFoorballPlayer()
    s.pass_exam()
    s.work()
    s.score()