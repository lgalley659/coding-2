
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
