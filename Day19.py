# Break and Continue Statement

# for i in range(12):
#     if i == 10:
#         break
#     print("5 X",i+1," = ",5*(i+1))


# for i in range(12):
#     if i == 10:
#         print("skip 10th iteration")
#         continue
#     print("5 X",i," = ",5*i)

# do while loop emulation

i=0
while True:
    print(i)
    i =i + 1
    if i % 100 == 0:
        break
