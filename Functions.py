#Create a new function
#Call it grossnetCalculator
#It should take 1 parameter
#Parameter 1. gross

#Step 1: use the key word def
#Step 2: include function name
#Step 3: specify the parameters
#Step 4: main code 
#Step 5: return value

def grossnetCalculator(gross):
    net = (gross -(0.1*(gross)))
    print("Net salary is: ",net)

#gross = float(input("Enter annual gross salary\n"))

#calling/using the function
#grossnetCalculator(gross)

#Function 2 - Calculating Perimeter of a rectangle
def periRectangle():
    l = int(input("Enter length:\n"))
    w = int(input("Enter width:\n"))
    p = l + l + w + w
    print("Perimeter of rectangle is: ",p," cm")

#call the function
#periRectangle()

#Homework Question
#Question: Create a function without parameters
# call this AreaRectangle
#In the function, ask user to enter Length
#and Width
#Calculate the area and print out the result.
def AreaRectangle():
    l = int(input("Enter length:\n"))
    w = int(input("Enter width:\n"))
    area = l * w
    print("Area of rectangle is: ",area, "cm2")

#calling the function
AreaRectangle()