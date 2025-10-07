class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, nex_r):
        self.radius = nex_r

    def get_area(self):
        return self.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
