# Decorators
import time


def print_header(*args):
    print("\n", "#" * 2, *args, "#" * 2)


# the first thing to know is that functions are treated like other variables in that they can be assigned and used later


def func1():
    print("func1")


def func2():
    print("func2")


# you can assign a variable func to be referencing the function func1
func = func1

print_header("Calling func:")
func()

# you can change the variable to point to func2
func = func2
print_header("Calling func again:")
func()

# functions can even be looped over
print_header("Looping over functions")
for func in (func1, func2):
    func()

# %%

# This means that functions can also return other functions


def generate_func():
    def inner():
        print("Inner")

    return inner


func = generate_func()
print_header("Calling generated function")
func()

# %%
# Understanding variable scope is also important.
# The inner remembers the variables `generated_func_arg` and `generated_func_variable`
# they can be used later


def generate_func(generated_func_arg):
    generated_func_variable = "var"

    def inner():
        print("Inner", generated_func_arg, generated_func_variable)

    return inner


func = generate_func("gen_argument")
print_header("Calling generated function with arguments and local variables")
func()

# %%

# lets pretend you have two functions as follows.
def fast_func():
    time.sleep(0.1)


def slow_func():

    time.sleep(0.5)


# these functions are taking a long time so you want to add time measurements to see how long they are taking


def fast_func():
    t0 = time.time()

    time.sleep(0.1)

    t_end = time.time()
    dt = t_end - t0
    print(f"fast_func took {dt:0.3} seconds")


def slow_func():
    t0 = time.time()

    time.sleep(0.5)

    t_end = time.time()
    dt = t_end - t0
    print(f"fast_func took {dt:0.3} seconds")


print_header("Calling fast and slow func:")
fast_func()
slow_func()

# %%
# The above code has redundant timing code which is really annoying...
# How can we refactor this so that we do not need to repeat the timing blocks?
# What if we passed in fast_func and slow_func as an argument into a timer function?

print_header("Using a function to call the timer:")


def fast_func():
    time.sleep(0.1)


def slow_func():
    time.sleep(0.5)


def timeit(func):
    t0 = time.time()
    func()
    t_end = time.time()
    dt = t_end - t0
    print(f"{func.__name__} took {dt:0.3} seconds")
    return dt


timeit(fast_func)
timeit(slow_func)

# %%

# what if we do not want to call timeit immediately, but want to use it later?
# What if we assign it to a new function to be called later, can we just set it to a variable?

timed_fast_func = timeit(fast_func)

# timed_fast_func()  # fails because the return value of timeit is not a function, it is dt

# how can we make func callable? We need timeit to return another function that can be called later


def timeit_wrapper(func):
    def wrapper():
        t0 = time.time()
        func()
        t_end = time.time()
        dt = t_end - t0
        print(f"{func.__name__} took {dt:0.3} seconds")
        return dt

    return wrapper  # return a function to be called later


timed_fast_func = timeit_wrapper(fast_func)
print_header("Calling using timeit_wrapper")
timed_fast_func()

# %%

# if we never need to use the original fast_func without the timer, we can overwrite the variable

fast_func = timeit_wrapper(fast_func)
print_header("Calling using timeit_wrapper")
fast_func()

# %%
# The above code is ugly, I wish there was a prettier way to write `fast_func = timeit_wrapper(fast_func)`
# Enter decorator. You use the @<decorator function name> cleanly wrap the function definition. This is
# easier to read later.


@timeit_wrapper
def fast_func():
    time.sleep(0.1)


print_header("Calling using decorator")
fast_func()

# %%

# What if we need to pass in arguments into fast_func?


def timeit_wrapper(func):

    # since we are returning wrapper, we need to add the arguments here
    def wrapper(arg):
        t0 = time.time()
        func(arg)  # func now needs to be called with this argument
        t_end = time.time()
        dt = t_end - t0
        print(f"{func.__name__} took {dt:0.3} seconds")
        return dt

    return wrapper  # return a function to be called later


@timeit_wrapper
def fast_func(arg):
    time.sleep(0.1)
    print("fast_func results:", arg * 2)


print_header("Calling using decorator with arguments")
fast_func(4)

# %%

# What if we do not know how many arguments func is going to take when we wrap it?
# Slurp and splat with *args and **kwargs


def timeit_wrapper(func):

    # since we are returning wrapper, we need to add the arguments here
    def wrapper(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)  # func now needs to be called with this argument
        t_end = time.time()
        dt = t_end - t0
        print(f"{func.__name__}(...) took {dt:0.3} seconds")
        return dt

    return wrapper  # return a function to be called later


@timeit_wrapper
def fast_func(arg1, arg2, var=None):
    time.sleep(0.1)
    print("fast_func results:", arg1 + arg2, var)


print_header("Calling using decorator with arbitrary args")
fast_func(5, 1, var="apple")

# %%

# if we want to get fancy, we can format the input arguments


def timeit_wrapper(func):

    # since we are returning wrapper, we need to add the arguments here
    def wrapper(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)  # func now needs to be called with this argument
        t_end = time.time()
        dt = t_end - t0
        args_str = (*(str(a) for a in args), *(f"{k}={v!r}" for k, v in kwargs.items()))
        arg_str = ", ".join(args_str)
        print(f"{func.__name__}({arg_str}) took {dt:0.3} seconds")
        return dt

    return wrapper  # return a function to be called later


@timeit_wrapper
def fast_func(arg1, arg2, var=None):
    time.sleep(0.1)
    print("fast_func results:", arg1 + arg2, var)


print_header("Calling using decorator with arbitrary args and fancy printing")
fast_func(5, 1, var="apple")


# %%

# What if we want to pass arguments into the timer to call it `count` times?

def timeit_wrapper(count):

    # the we need an additional layer to manager the arguments used to call
    def inner_wrapper(func):
        # since we are returning wrapper, we need to add the arguments here
        def wrapper(*args, **kwargs):
            t0 = time.time()
            for i in range(count):
                func(*args, **kwargs)  # func now needs to be called with this argument
            t_end = time.time()
            dt = t_end - t0
            args_str = (
                *(str(a) for a in args),
                *(f"{k}={v!r}" for k, v in kwargs.items()),
            )
            arg_str = ", ".join(args_str)
            print(
                f"{func.__name__}({arg_str}) called {count} times took {dt:0.3} seconds"
            )
            return dt

        return wrapper  # return a function to be called later

    return inner_wrapper


@timeit_wrapper(3)
def fast_func(arg1, arg2, var=None):
    time.sleep(0.1)
    print("fast_func results:", arg1 + arg2, var)


print_header("Calling using decorator that has arguments")
fast_func(5, 1, var="apple")

# the above is the equivalent


def fast_func(arg1, arg2, var=None):
    time.sleep(0.1)
    print("fast_func results:", arg1 + arg2, var)


fast_func = timeit_wrapper(3)(fast_func)
print_header(
    "Calling again using decorator that has arguments but without fancy @ symbol"
)
fast_func(5, 1, var="apple")
