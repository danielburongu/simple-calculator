#how to build a simple calculator
#Display menu for the user
# 1 ADD 
# 2 SUBTRACT
# 3 MULTIPLE
# 4 DIVIDE
# print("select an operation to perform")
# print("1. ADD")
# print("2. SUBTRACT")
# print("3. MULTIPLE")
# print("4. DIVIDE")

operation=input()

operation==1;
num1=input("Enter first number:")
num2=input("Enter second number:")
print("The sum is " + str(int(num1)+int(num2)))
if operation==2:
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The difference is" + str(int(num1)-int(num2)))

    if operation==3:
        num1=input("Enter first number")
        num2=input("Enter second number")
        print("The product is" + str(int(num1)*int(num2)))

        if operation==4:
            num1=input("Enter first number")
            num2=input("Enter second number")
            print("The result is" + str(int(num1)/int(num2)))

        else:
            print("invalid Entry")








