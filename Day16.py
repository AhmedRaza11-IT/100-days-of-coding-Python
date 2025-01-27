# Match Case

x = int(input("Enter the value of x: "))

match x:
    case _ if x <= 50:
        print("Your Grade is FAIL and obtained mark is:", x)
    case _ if 60 <= x <= 69:
        print("Your Grade is D and obtained mark is:", x)
    case _ if 70 <= x <= 79:
        print("Your Grade is C and obtained mark is:", x)
    case _ if 80 <= x <= 89:
        print("Your Grade is B and obtained mark is:", x)
    case _ if 90 <= x <= 100:
        print("Your Grade is A and obtained mark is:", x)
    case _:
        print("Invalid Input")









# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")
#
#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)