'''# Local and Global variable in Python

x=4
# print(x)

def hello():
    x=5
    print(f"The Local x is {x}")
    # print("Hello Ahmed")
print(f"The Global x is {x}")
hello()
# print(f"The Global x is {x}")'''

x = 10 # global variable
y = 1
def my_function():
    global  x
    x = 4
    a = 5 # local variable
    print(y)

my_function()
print(x)
print(a) # this will cause an error because y is a local variable and is not accessible outside of the function