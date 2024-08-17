class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f"Length={self.length} and breadth={self.breadth}"

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def is_square(self) -> bool:
        if self.length == self.breadth:
            return True
        return False


x = Rectangle(5, 10)  # <---- init
print(x.area())
print(x.perimeter())
print(x.is_square())
print(x)
