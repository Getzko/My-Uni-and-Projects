class Engine:
    def __init__(self, power):
        self.power=power
    def start(self):
        print("engine start")
    
class Car:
    def __init__(self,brand,power):
        self.brand=brand
        self.engine=Engine(power)
    def start_car(self):
        self.engine.start()
e1 = Engine(222)
car1=Car("toyota",e1)
print(car1.brand)
print(car1.engine.power)
car1.start_car

class Teacher:
    def __init__(self,name):
        self.name=name

class Department:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def show_teachers(self):
        print(self.teachers)

t1 = Teacher('tung')
t2 = Teacher('sahur')
d1=Department('ddeez nuts')
d1.add_teacher(t1)
d1.add_teacher(t2)