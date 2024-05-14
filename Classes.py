#constructors
#objects
#encapsulation
#polymorphism
#inheritance 

#Rule 1: Create constructor
#aka init method (function)
#before creating objects

#Why? Package everything so 
#we can use it anywhere

#Creating first class that contains 
#functions we can use to calculate
# perimeter
import math

class PerimeterBox:
    #create constructor
    def __init__(self) -> None:
        pass

    #second function
    def PeriRectangle(self):
        l = int(input("Enter length:\n"))
        w = int(input("Enter width:\n"))
        p = l + w + l + w
        print("Perimeter is: ",p, " cm")

    #third function --> PeriSquare
    def PeriSquare(self):
        s = int(input("Enter side:\n"))
        p = s + s + s + s
        print("Perimeter of square is: ", p , " cm")
    #fourth function - Triangle
    def PeriTriangle(self):
        s = int(input("Enter side:\n"))
        p = s + s +s
        print("Perimeter of Triangle is: ",p, " cm") 

    #fifth function - Circle
    def CCircumference(self):
        r = int(input("Enter radius: \n"))
        c = 2 * math.pi * r
        print("Circumference of circle is: ",c," cm")

#initialize objects
periObj = PerimeterBox()
#User Choice
print("Welcome to the Perimeter Box\b")
print("Choose which object to Calculate its perimeter\b")
choice = int(input("1.Rectangle\n2.Square\n3.Triangle\n4.Circle\n"))
#periObj = PerimeterBox(choice)
#Calling/using object
#periObj.PeriRectangle()

#if statement
if choice==1:
    periObj.PeriRectangle()
elif choice==2:
    periObj.PeriSquare()
elif choice==3:
    periObj.PeriTriangle()
elif choice==4:
    periObj.CCircumference()
else:
    print("Invalid option")

