# %%


class Polygon:

    def __init__(self, number_sides):
        self.number_sides = number_sides

    def __str__(self):
        return f"Polygone(number_sides={self.number_sides})"

    def __len__(self):
        return self.number_sides

    def __add__(self, other):
        print("Calling add:", self.number_sides, other.number_sides)
        return Polygon(self.number_sides + other.number_sides)
    
    def __mul__(self, other):
        print("Calling multiply:", self.number_sides, other.number_sides)
        return Polygon(self.number_sides * other.number_sides)





# %%
class Square(Polygon):
    def __init__(self):
        super().__init__(number_sides=4)


class Triangle(Polygon):
    def __init__(self):
        super().__init__(number_sides=3)


# %%

def polygone_factory(number_sides):
    if number_sides == 4:
        return Square()
    elif number_sides == 3:
        return Triangle()
    else:
        return Polygon(number_sides=number_sides)

def get_polygon_class(number_sides):
    if number_sides == 4:
        return Square
    elif number_sides == 3:
        return Triangle

def polygone_factory(number_sides):
    cls = get_polygon_class(number_sides)
    return cls()


def polygone_factory(number_sides):
    num_sides_to_class = {
        4: Square,
        3: Triangle,
    }
    cls = num_sides_to_class[number_sides]
    print("Creating instance using", cls)
    instance = cls()
    print("instance", instance)
    return instance
    
polygon = polygone_factory(4)



# %%

square = Polygon(4)

# %%
# print(square) -> str(square) -> square.__str__()
print(square)

triangle = Triangle()
print(triangle)

print("len(triangle)", len(triangle))
# %%

print(square + triangle)  # square + triangle -> square.__add__(triangle)
print(square + triangle + triangle)  # (square + triangle) + triangle -> (square.__add__(triangle)).__add__(triangle)

print(square * triangle)


# %%

class Employee(object):

    def __new__(cls, name, salary):
        print("__new__")
        if 0 < salary < 10000:
            return object.__new__(cls)
        else:
            return None
  
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
     

  
    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)
