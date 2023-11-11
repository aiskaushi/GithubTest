num1=int(input("Enter number one: "))
num2=int(input("Enter number two: "))
opt= input("Choose any opt +, -, *, /")
if(opt=="+"):
    print(num1+num2)
elif(opt=="-"):
    print(num1-num2)    
elif(opt=="*"):
    print(num1*num2)  
elif(opt=="/"):
    print(num1/num2)    
elif(opt=="**"):
    print(num1%num2)    
else:
    print("invalid operation")    