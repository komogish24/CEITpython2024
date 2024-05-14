"""This program should
accept input from user
and calculate the person's AGE"""

#Step 1 --> create class
class AgeCalculator:
    #Step 2 --> constructor
    def __init__(self) -> None:
        pass

    #Function
    def calcMyAge(self):
        YOB = int(input("Enter Year of Birth\n"))
        if (YOB > 2024):
            print("Invalid Year")
            
        else:
            Ans = 2024 - YOB
            print("You are ",Ans, "years (old) wiser...")

#object initialization
#object name can be any name
AgeObj = AgeCalculator()

#Use the object
print("Welcome")  #This is optional
AgeObj.calcMyAge()



