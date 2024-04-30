print("1 - Add")
print("2 - Sbtraction")
print("3 - Multiplication")
print("4 - Division")
option=int(input("choose the operation:"))
if(option in[1,2,3,4]):
    num1=int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
if(option==1):
    result=num1 + num2
if(option==2):
    result=num1 - num2
if (option==3):
    result=num1 * num2
if(option==4):
    result=num1 // num2
else:
    print("invalid operation ,try again!")
print("the result of the operation is {}".format(result))