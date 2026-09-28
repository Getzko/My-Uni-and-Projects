class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def run(self):
        print(f"{self.name} is running")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
        
rabbit = Prey("bugs")
tiger = Predator("bonzo")
rabbit.flee()
tiger.hunt()