class Dog:
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
