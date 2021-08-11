# File manipulation

# %%

# file handling

# create a txt file
file_path = "./example.txt"

# open a file called example.txt in write mode
file_handler = open(file_path, "w")
file_handler.write("hello world!")
# you have to remember to close the file
file_handler.close()

# %%
# Here is a short-hand method same as the method above, but it's safer since you don't have to remember to close the file.
# Since the file exists, so it will be overwritten.
with open(file_path, "w") as file_handler: 
    file_handler.write("hello world again!\n") # \n is used for line separator

# %%
# append mode
with open(file_path, "a") as file_handler:
    file_handler.write("hello world!")
    file_handler.write(123)
    file_handler.write([1, 2, 3])

# %%
# read mode (read the whole file)
with open(file_path, "r") as file_handler:
    file_content = file_handler.read()
print(file_content)

# %%
# read mode (read line by line)
with open(file_path, "r") as file_handler:
    file_content = file_handler.readlines()
    print(file_content)
    for line in file_content:
        print(line)

# %%
import os

file_path_2 = "./example_2.txt"
# delete file
os.remove(file_path_2)

# %%

# check if file exists
print(os.path.exists(file_path_2))
if os.path.exists(file_path_2):
    os.remove(file_path_2)

if os.path.exists(file_path):
    os.remove(file_path)

# %%

# make a directory
os.makedirs("tmp", exist_ok=True) # It will not return error if the directory already exists if we turn exist_ok=True 

# remove a directory
os.rmdir("tmp")


# %%

# Manipulating paths

# Combine components into one path
a = "nas"
b = "MotionMetrics"
c = "python_club.py"
example_path = os.path.join(a,b,c)
print(example_path)

# Get filename from path
filename = os.path.basename(example_path)
print(filename)

# Split head and tail from a path
split_path = os.path.split(example_path) # This will return a tuple (head, tail)
print(split_path)

# Exclude extension from filename
split_filename = os.path.splitext(filename) # This will return a list [<filename>, <extension>]
print(split_filename)
real_filename = split_filename[0] # Get the first element in the list
print(real_filename)


# %%

# What if we want to find the files following certain pattern??

# Let's find some AGM photos

import glob

root_path = "N:\MotionMetrics\Photos"
file_pattern = "*AGM*/*.jpg"
path = os.path.join(root_path, file_pattern)
print(path)

photo_paths = glob.glob(path) # find all the path matching the pattern
print(photo_paths)

#%%

# Now let's copy these photos to our folder and see what's inside!

import shutil

# copy photos to destination folders
dst_path = "./tmp"
os.makedirs(dst_path, exist_ok=True)

for photo_path in photo_paths:
    filename = os.path.basename(photo_path)
    export_path = os.path.join(dst_path, filename)
    shutil.copy(photo_path, export_path)

# %%
