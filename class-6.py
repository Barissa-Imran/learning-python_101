class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initializes attribute model."""
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"This car is the latest model of {self.model}."

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        name = str(self.year) + ' ' + self.make + ' ' + self.model
        return name.title()

c = Car('subaru WRX', 'sti', 2014)

print(str(c))
print(Car.__doc__)
print(str.__doc__)
print(c.get_descriptive_name())
