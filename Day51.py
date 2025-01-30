# File Handling
# Seek() and Tell()

# Seek() method
# with open('D49.txt', 'r') as f:
#     print(type(f))
# # Move to the 10th byte in the file
#     f.seek(10)
#
#     # Read the next 5 bytes
#     data = f.read(13)
#     print (data)

# Tell() Method
# with open('D49.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#
#   # Save the current position
#   current_position = f.tell()
#
#   # Seek to the saved position
#   f.seek(current_position)

# Truncate() Method
with open('D51.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('D51.txt', 'r') as f:
  print(f.read())