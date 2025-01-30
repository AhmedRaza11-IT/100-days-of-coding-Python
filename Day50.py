# IO Methods

# Readline() Method
# f = open("D50.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# Writelines Method
f = open("D50-1.txt","w")
lines = ["line 1\n","line 2\n","line 3\n"]
f.writelines(lines)
f.close()