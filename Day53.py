# Map, Filler and Reduce in python

# Map
# def cube(x):
#     return x*x*x

# print(cube(2))

l = [1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
#
# print(newl)
# by using map method
newl = list(map(lambda x: x*x*x,l))
print(newl)

# Filter method
def filter_function(a):
    return a>2

new_newl = list(filter(filter_function,l))
print(new_newl)