# import os 
# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

import os 

# Check if "data" directory exists
if not os.path.exists("data"):
    print("Error: 'data' directory does not exist.")
    exit()

# List folders in the "data" directory
folders = os.listdir("data")

# Print the current working directory
print("Current Working Directory:", os.getcwd())

try:
    os.chdir("/Users")  # Change directory (only works on macOS/Linux)
    print("Changed Directory To:", os.getcwd())
except FileNotFoundError:
    print("Error: '/Users' directory not found. Skipping directory change.")

# Iterate over folders inside "data"
for folder in folders:
    folder_path = os.path.join("data", folder)  # Get full folder path
    if os.path.isdir(folder_path):  # Ensure it's a directory
        print(f"Contents of '{folder}':")
        print(os.listdir(folder_path))
    else:
        print(f"'{folder}' is not a directory, skipping.")
