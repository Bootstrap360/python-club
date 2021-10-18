# %%

def flex_function(*args, **kwargs):
    print("args", type(args), args)
    print("kwargs", type(kwargs), kwargs)


flex_function(1,2,3, b=5, c= 10)

args = (4,5,6)
kwargs = dict(a=4, b= 5)
flex_function(*args, **kwargs)