# for i in range(201,250):
#     print(i)
# for i in range(20):
#     print(i)
# for i in range(0,101,5):
#     print(i)
# for i in range(23,231,23):
#       print(i)
# num=int(input("Enter a number to know its first 10 multiples"))
# for i in range(1,11):
#     print(num*i)
# num=int(input("Enter a number: "))
# if num%2 == 0:
#     print("even no")
# else:
#     print("odd no.")

# for i in range(0,51):
#     if(i%2==0):
#         print(i)
for i in range(0,51):
    if(i%2==1):
        print(i)

num1=int(input("enter lower range"))
num2=int(input("enter upper limit"))
choose=input("Even or odd")
if choose=="even":
    for i in range(num1,num2):
        if(i%2==0):
            print(i)
if choose=="odd":
    for i in range(num1,num2):
        if(i%2==1):
            print(i)