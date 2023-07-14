import math
#user main menu#
print("Choose a NUMBER: ")
print ("1. Sqaure Root")
print ("2. Addition")
print ("3. Subtraction")
print ("4. Multiplication")
print ("5. Division")

NUMBER = input()

if NUMBER == "1": #Square root#
    num = int(input("Enter number: "))
    print ("the total = %f "  %(math.sqrt(num)))
elif NUMBER == "2": #Addition#
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) + int(num2)))
elif NUMBER == "3" : #Subtraction#
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) - int(num2)))   
elif NUMBER == "4":  #Multiplication#
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) * int(num2))) 
elif NUMBER == "5": #Division#
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) / int(num2))) 
else: #Invalid#
    print ("Invalid entry")
    