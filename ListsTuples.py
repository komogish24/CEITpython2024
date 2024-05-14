my_list =  ['p','r','o','g','r','a','m','i','z']
#print(my_list[2:5])
#print(my_list[5:])
#print(my_list[:])

#create new list called CEIT with
#values CCIT,CCDBM, CCNS,CCAIT
ceit = ["CCIT","CCDBM","CCNS","CCAIT"]
ceit.append("CCLSA")

#changing an item in the list
ceit[2]="CCDCN"
print(ceit)

#removing/deleting items in a list
#del ceit[3]
#ceit.remove("CCAIT")
#print(ceit)

#using len function
print(len(ceit))

list2 = [1,3,4,6,4,7,8,2,3]
#print(sum(list2))
#print(min(list2))
#print(max(list2))
#print(list2[0])
#print(list2[-1])

#TUPLE
#Task: Create a new tuple
#Call this myinfo
#in this tuple >> Name, Age, Phone, ceit_list

myinfo = ("Shirley",16,3267424,ceit)
#print(myinfo)
#print(type(myinfo))
#myinfo[1]=21
#print(myinfo)

#QUESTIONS 1 - 3
#1
#a = (1,2,3,4,5)
#del a
#print(a)
#Q2

a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
print(a.count(1))
print(a.index(5))



#Create a new File called
#Functions.py

#Task--> Create a new function
#call this GrossNetCalculator
#this function should take 2 parameters. 