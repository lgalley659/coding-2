
def discount():
    itemPrice = input("Please enter the item price. ")
    if itemPrice >= 50 or itemPrice <=75:
        discount = .15
        sum itemPrice * discount
        total = itemPrice - sum
        print("this is your final total "+ str(total))
    elif itemPrice >75:
        discount = .25
        total = itemPrice * discount
        total = itemPrice - sum
        print("This is your final total "+ str(total))
    else:
        print("Sorry, you do not get a discount")
        
discount()

def jobFairCheck(gpa , age):
    if gpa >= 90 and age >= 17:
        print("You meet the requirements for the fair")
    else: 
        print("You do not meet the requirements for the fair")

def GPA():
    gradeAverage = input('Enter your GPA')
    if gradeAverage >= 90
        print('You are qualified for the job fair')
    else:
        print("Not qualified")

def age():
    age = input("Enter your age")
    if age >= 17
        print("You are qualified for the job fair")
    else:
        ("You are too young for to attend the job fair")



def gpa():