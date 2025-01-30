# File IO in Python

# Opening a file to only read
# f = open("D49.txt","r")
# # print (f)
# text = f.read()
# print (text)
# f.close()

# Opening a file to only read
# f = open("capture.PNG","rb")
# # print (f)
# text = f.read()
# print (text)
# f.close()

# Writing to a file
# f = open("D49.txt","w")
# f.write("Hello, World!")
# f.close()

#Append a file
# f = open("D49.txt","a")
# f.write("Hello, World!")
# f.close()

with open('D49.txt','a') as f:
    f.write("I am inside with")