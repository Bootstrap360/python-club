# Debugging

# %%

# Create a function to calculate the multiplication result from a file
def read_float(path):
    l = []
    with open(path, "r") as fh:
        file_content = fh.readlines()
        for line in file_content:
            # Convert the number from each line to float type and multiply with res
            l.append(float(line.rstrip("\n")))
    return l

def multiply_list(l):
    res = 1
    for i in l:
        res *= i
    return res

def file_multiplication(path):
    num_list = read_float(path)
    multi_res = multiply_list(num_list)
    return multi_res

res = file_multiplication("0001_debugging.txt")
print(res)

# %%

# We got result=0.0! Something is wrong. But it's hard to tell which part cause the issue.

# Let's using debug to find out where is the problem

def read_float(path):
    l = []
    with open(path, "r") as fh:
        file_content = fh.readlines()
        for line in file_content:
            # Convert the number from each line to float type and multiply with res
            l.append(float(line.rstrip("\n")))
    return l

def multiply_list(l):
    res = 1
    for i in l:                              
        res *= i                             # put one checkpoint here to track res value
        if res == 0:                        
            print(l.index(i))                # put one checkpoint here to find out the index       
    return res

def file_multiplication(path):
    num_list = read_float(path)              # put one checkpoint here and check if num_list looks correct
    multi_res = multiply_list(num_list)      # put one checkpoint here and step in the function
    return multi_res

res = file_multiplication("0001_debugging.txt")   
print(res)
