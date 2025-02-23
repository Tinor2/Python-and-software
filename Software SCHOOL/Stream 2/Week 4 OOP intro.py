# Classes
    #Creates different objects that can be compared to each other
"""class Book:
    def __init__(self, title:str, author:str, pages:int):
        self.title = title
        self.author = author
        self.pages = pages
    def formatCover(self):
        return f"{self.title} by {self.author}"
    def bookLength(self):
        return f"{self.title} is {self.pages} pages long"


HarryPotter = Book("Harry Potter", "JK Rowling", 500)
MortalEngines = Book("Mortal Engines", "Philip Reeve", 300)
PercyJackson = Book("Percy Jackson", "Rick Riordan", 400)
"""
class BankAccount:
    def __init__(self, accountID, balance) -> None:
        self.accountID = accountID
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def checkBalance(self):
        print(f"Account ID: {self.accountID}. Balance: {self.balance}")
class Job:
    def __init__(self, jobName:str, experianceReq:float,experiancePerMonth:float, salaryPerMonth:float, educationReq = None) -> None:
        if educationReq == None:
            self.educationReq = 0
        self.jobName = jobName
        self.experianceReq = experianceReq
        self.experiancePerMonth = experiancePerMonth
        self.salaryPerMonth = salaryPerMonth
class Education: 
    def __init__(self, educationReq:float, educationGen:float) -> None:
        self.educationReq = educationReq
        self.educationGen = educationGen
class Stats:
    def __init__(self, money, education, experiance, age) -> None:
        pass
class Person:
    def __init__(self, name, stats:Stats, job:Job, bankAccount:BankAccount, education:Education) -> None:
        self.name = name
        self.Stats = Stats
        self.job = job
        self.bankAccount = bankAccount

HSstudent= Education(0,1000)
UNIstudent = Education(1000,10000)

Unemployed = Job("Unemployed",0,0,0)
Maccas = Job("Maccas", 0, 0, 100)
Kfc = Job("KFC", 0, 0, 100)
Retail = Job("Retail", 100, 450, 300)
Teacher = Job("Teacher", 1000, 1000, 1000)

SoftwareIntern = Job("Software Intern", 0, 500, 2500)
SoftwareEngineer =Job("Software Engineer", 1000, 10000, 10000)
userMoney = 0
userAge = 15
userEXP = 0
userEdu = 0
# # Do stuff

# jim = BankAccount(1, 1000)
# mike = BankAccount(2, 500)
# Gatsby = BankAccount(3, 5000)
turn = 0
while True:
    user = Person("Player",  Stats(userMoney,userEdu,userEXP,userAge), Maccas, BankAccount(0, userMoney), HSstudent)
    if userAge == 15:
        pass
    if userAge == 18:
        input("Tertiary education, Job, or gap year? ")
