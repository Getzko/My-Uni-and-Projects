'''class Dog:
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age
    def bark(self):
        print(f"{self.name} says Woof!")
    def getall(self):
        for dog in dogs:
            print(f"Name: {dog.name}, Breed: {dog.breed}, Age: {dog.age}")
     
            
d1=Dog("buddy","Labrador","3")
d1.bark()

dogs=[]
for i in range(3):
    name=input("Enter dog's name: ")
    breed=input("Enter dog's breed: ")
    age=int(input("Enter dog's age: "))
    dog=Dog(name,breed,age)
    dogs.append(dog)
d1.getall()
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self,amount):
        self.speed= self.speed + amount
        print(f"{self.make} current speed: {self.speed} km/h")
    def brake(self,amount):
        self.speed= self.speed - amount
        if self.speed < 0:
            self.speed = 0
            print(f"{self.make} has stopped.")
        print(f"{self.make} current speed: {self.speed} km/h")
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Current speed: {self.speed} km/h")
cars=[]
for i in range(3):
    make=input("Enter car's make: ")
    model=input("Enter car's model: ")
    year=int(input("Enter car's year: "))
    car=Car(make,model,year)
    cars.append(car)
cars[0].accelerate(50)
cars[0].brake(20)
cars[2].accelerate(88)
cars[2].brake(100)
for a in range(len(cars)):
    cars[a].display_info()
