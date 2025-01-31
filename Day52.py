# Lambda Function


double = lambda x: x*2
print(double(5))
cube = lambda x: x*x*x
print(cube(5))

# passing a function inside a function
def application(fx,value):
    return 6 + fx(value)

print(application(lambda x: x * x ,2))