# def average(a=3,b=1):
#     print("The Average is: ", (a+b)/2)
#
# average(a=50)

# def Myname(fname, mname, lname):
#     print("my full name is: ",fname+" "+ mname+" "+lname)
#
# Myname(fname="Ahmed" , mname="Muhammad", lname="Asif")

def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c=average(5,6,7,8,9,10,11,22)
print(c)


# def name(**name):
#     print("Hello,",name["fname"], name["mname"], name["lname"])
#
# name(mname="Muhammad", lname="Asif", fname="Ahmed" )