class Person():
    """The basic functionality of a person"""

    def __init__(self, name, age, race):
        """Initializes name, age and race attributes."""
        self.name = name
        self.age = age
        self.race = race

    def run(self):
        """Run method"""
        print(self.name.title() + " 800m WR champion.")

    def get_old(self):
        """Aging like fine wine"""
        self.age += 1
        print(self.name.title() + " retired at the age of {}.".format(self.age))

    def get_name(self):
        """Prints name of person"""
        print(f"Hello, {self.name.title()} welcome to 2024 Paris Summer Olympics.")

p1 = Person('barry', 74, "black")

print(Person.__dict__)

