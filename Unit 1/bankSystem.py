class IanFirstBank:
    def __init__(self, name, password, address, balance):
        self.name = name
        self.password = password
        self.address = address 
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount 
        print('thanks '+ self.name +'your new balance is' + str(self.balance))

    def withdraw(self, amount):
        self.balance += amount
        print('')

    def accessAcount(self):
        return

    def accessAcount(self):
        print('')
    "123ABC"
    def transfer(self):
        print('')

acount_1 = IanFirstBank('John', '123ABC', 'NA', 100)
acount_2 = IanFirstBank('Ashley', '123ABC', 'NA', 200)


def createdAcount(self):
    print('welcome to Ians First bank.')
    print('Please complete the following instructions to create your acount')
    name = input("name: ")
    password = input("password")
    address = input("How much would you like to add tp the new acount")

    return