#even_odd
num1=int(input("Enter lower limit: "))
num2=int(input("Enter upper  limit: "))
pick=input("pick even or odd:  ")
if pick=="even":
    for i in range(num1,num2):
        if i%2==0:
            print(i)
if pick=="odd":
    for i in range(num1,num2):
        if i%2==1:         
            print(i)