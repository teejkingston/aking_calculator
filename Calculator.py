print("Choose a NUMBER: ")
print ("3. Addition")
print ("4. Subtraction")
print ("5. Multiplication")
print ("5. Division")

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
    