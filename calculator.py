print("calculator")
num1 = float(input("enter first number here: "))
num2 = float(input("enter second number here: "))
 
print ("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division \n ")
choice = int(input("enter your choice from 1-4: "))
if choice == 1:
    print("Adition of your given numbers is",num1 + num2)
elif choice == 2:    
    print("Substraction of your given numbers is",num1 - num2)
elif choice ==  3:
    print("Multiplication of your given numbers is ",num1*num2)
elif choice ==  4:
    print("Division of your given numbers is ",num1/num2)
else:   
    print("invalid_input")   