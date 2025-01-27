# String Methods
name="!!Ahmed    !!!! Raza !!!"

# length of string
print(len(name))

# Strings are immutable (can not be changed)
# Conversion of string to uppercase and get new string
print(name.upper())

# Conversion of string to uppercase and get new string
print(name.lower())
# print (name)

price = 49.99959661
print(f"The price is: ${price:.6f}")

# Exclude specific character from name but only the last character
print(name.rstrip("!"))

# Replace all accurences
print(name.replace("Ahmed","Ahsan"))

print(name.split(" "))

blogHead= "introductION TO PYTHON"
print(blogHead.capitalize())

str1="w3resource"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))
print(name.count("!"))
print(name.endswith("!!!"))
print(name.startswith("!!"))
print(name.endswith("med !!",4,10))
print(name.find("a"))

str1="          "
print(str1.isspace())