# IF ELSE CONDITIONAL STATEMENTS
# Conditional operators
# >,<,>=,<=,==,!=

# a = int(input("Enter a age: "))
# print("Your Age is: ", a)
# print(a>18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if a < 18:
#     print("You are not eligible to drive")
# else:
#     print("You are eligible to drive")


# appleprice = 10
# budget= 20
# if (budget - appleprice) >= 50:
#     print("You can buy the apple")
# elif (budget - appleprice) >= 70:
#     print("You can still buy the apple")
# else:
#     print("You can't buy the apple")

#
# num1 = int(input("Enter first number: "))
# if num1 < 0:
#     print("Number is negative")
# elif num1 == 0:
#     print("Number is zero")
# else:
#     print("Number is positive")#
num1 = int(input("Enter first number: "))
if num1 < 0:
    print("Number is negative")
elif num1 > 0:
    if num1 <= 10:
        print("Number is between 1 and 10")
    elif num1 > 10 and num1 <= 20:
        print("Number is between 11 and 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

