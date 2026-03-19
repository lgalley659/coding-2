# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 

answer = "A class is ablueprint for creating objects. A Object is a specific thing in the class."

# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.

Answer = "An object property is a variable that stores data about a object." \
"A method is a function that belongs to the object."

# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 

class VideoGameCharacter:
    def __init__(self, name, health, level, strength):
        self.name = name
        self.health = health
        self.level = level
        self.strength = strength

    def damage(self, amount):
        self.health

    def Plus_level(self, bonus level):
        self.level += 1
        print(self.level) 

    def check_level(self):
        if self.health <= 0:
            self.is_alive = False
            print(self.name) + "Has not leveled up"
        else:
            print(self.name) + "Has gained 1 level"