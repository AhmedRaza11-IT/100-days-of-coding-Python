# Recursion in python
# calling a function in the same function.

# factorial(n) = n * factorial(n-1)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
# print(factorial(0))
# print(factorial(8))

#fabonacci sequence
def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
print (fab(6))