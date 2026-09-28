'''class Vehicle:
    def __init__(self,speed):
        self.speed=speed
        print(f"This vehicel is going {self.speed} km/h")
class Car(Vehicle):
    def __init__(self, speed,num_doors):
        super().__init__(speed)
        self.num_doors=num_doors
    def describe(self):
        super().describe()
        print(f"This car has {self.num_doors} doors and is going {self.speed} km/h")
class SportsCar(Car):
    def __init__(self, speed, num_doors, top_speed):
        super().__init__(speed, num_doors)
        self.top_speed = top_speed
        def describe(self):
            super().describe()
            print(f"This sports car has a top speed of {self.top_speed} km/h")
sc=SportsCar(200, 2, 300)
sc.describe()
''' 


