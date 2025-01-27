#Enumerate function\\
from operator import index

# marks=[12,50,70,98,55,66,56,1]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("3rd index")
#     index += 1
marks=[12,50,70,98,55,66,56,1]
for index,mark in enumerate(marks,start=1):
    print(mark)
    if (index == 3):
        print("3rd index")
    index += 1