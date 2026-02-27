# OOP = Object Oriented Programming

# An object is a blueprint for describing something.

# Computer Object Descriptions
# it can tell time
# it can access the internet
# theres a power button
# it has programs

class computerItem:
    def __init__(self, color, shape ):
        self.color = color
        self.shape = shape
        self.soundOutput = soundOutput
        self.brand = brand
        self.ram = ram
        self.price = price
        self.storage = storage


# Create a pet animal class function.
# The class should have 4 properties and 4 methods.
# Then create 3 pets objects. Each Pet should have unique
# properties and use at least 1 method.

 
 
class PetCreator():  
        def __init__(self, color, age, name):
            self.color = color
            self.age = age
            self.name = name
        
        def feedPet(self):
            print('time to feed your pet')
        
        def sleeping(self):
             print("our pet is resting")

        def playtime(self):
             print("Our pet wants to play")

        def bathroom(self):
             print("needs to relieve itself")

pet_1 = PetCreator("brown", 4, "Brutus", "Freindly", "Dog")
pet_2 = PetCreator("gray", 6, "sam", "Independent", "Cat" )
pet_3 = PetCreator("green", 2, "Iggy", "Timid", "Lizard")

