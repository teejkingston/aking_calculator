print("Choose a NUMBER: ")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

NUMBER = input()

if NUMBER == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) + int(num2)))
elif NUMBER == "2" :
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) - int(num2)))   
elif NUMBER == "3": 
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) * int(num2))) 
elif NUMBER == "4": 
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print ("the total = " + str(int(num1) / int(num2))) 
else: 
    print ("Invalid entry")
    