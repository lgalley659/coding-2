#1. In your own words describe what a class property is. Write your response as a string.
# Variables that belong to a class and store data for eatch object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#2. Describe what a class method is, Write your response as a string.
#Methods are functions of a class.

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

#3. Create a student class function. This function should create unique student objects.

class student:
    def __init__(self, pencil, books, laptop):
      self.pencil = pencil
      self.books = books
      self.laptop = laptop

student_1 = student("jimmy", "pen", "iPad")
student_2 = student("josh", "pencil", "laptop")

#4.create a video game character class function

class gameCharacter:
  def __init__(self, armour, shield, weapon, health):
    self.armour = armour
    self.shield = shield
    self.weapon = weapon
    self.health = health

  def Heal(self):
    return

  