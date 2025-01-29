# OS MODULE


#create a directory and inside create 100 folders
# import os
#
# if(not os.path.exists("data")):
#     os.mkdir("data")
#
# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")


#Rename all 100 folders
# import os
#
# for i in range(0, 100):
#     os.rename(f"data/Day{i + 1}", f"data/Tut {i + 1}")

#list each folder and data inside
# import os
# folders = os.listdir("data")
#
# print(os.getcwd()) to show in which directory you are
# os.chdir("/Users") change the directory
# print(os.getcwd())
#
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# import os
#
# # Check if "data" directory exists
# if not os.path.exists("data"):
#     print("Error: 'data' directory does not exist.")
#     exit()
#
# # List folders in the "data" directory
# folders = os.listdir("data")
#
# # Print the current working directory
# print("Current Working Directory:", os.getcwd())
#
# try:
#     os.chdir("/Users")  # Change directory (only works on macOS/Linux)
#     print("Changed Directory To:", os.getcwd())
# except FileNotFoundError:
#     print("Error: '/Users' directory not found. Skipping directory change.")
#
# # Iterate over folders inside "data"
# for folder in folders:
#     folder_path = os.path.join("data", folder)  # Get full folder path
#     if os.path.isdir(folder_path):  # Ensure it's a directory
#         print(f"Contents of '{folder}':")
#         print(os.listdir(folder_path))
#     else:
#         print(f"'{folder}' is not a directory, skipping.")
