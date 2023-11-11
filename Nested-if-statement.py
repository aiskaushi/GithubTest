# Nested if statements:
x_str=input("enter value of x = ")
y_str=input("enter value of y = ")
x=int(x_str)
y=int(y_str)

if x > 5:
    if y > 2:
        print("Both x and y are greater than their respective thresholds value.")
    else:
        print("x > 5, but y < 2.")
else:
    print("x > peak value and y < peak value")
