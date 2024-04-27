def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 8, 5, 3, 6, 7, 9, 1, 4, 2))


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get["make"]
        self.model = kw.get["model"]
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(model="GT-R", make="Nissan", color="Red", seats="4")
print(my_car.make)