class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0.0

    def describe(self):
        print(f"I am a {self.name} with an area of {self.area():.2f}")


# ==========================
# CHILD CLASS 1 : Triangle
# ==========================

class Triangle(Shape):

    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ==========================
# CHILD CLASS 2 : Rectangle
# ==========================

class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# ==========================
# CHILD CLASS 3 : Circle
# ==========================

class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# ==========================
# MAIN PROGRAM
# ==========================

triangle = Triangle(10, 5)
rectangle = Rectangle(8, 4)
circle = Circle(7)

triangle.describe()
rectangle.describe()
circle.describe()

#===========================
# MOKSHADA MALI
#===========================