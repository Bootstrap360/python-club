from pympler import asizeof

class WithSlots:

    __slots__ = ("a", "b", "c")

    def __init__(self) -> None:
        self.a = "a"
        self.b = "b"
        self.c = "c"


class WithoutSlots:
    def __init__(self) -> None:
        self.a = "a"
        self.b = "b"
        self.c = "c"


without_slots = [WithoutSlots() for i in range(1_000)]
with_slots = [WithSlots() for i in range(1_000)]

sizer = asizeof.Asizer()
print("Witht slots:", sizer.asized(with_slots, detail=0).format())
print("Without slots:", sizer.asized(without_slots, detail=0).format())