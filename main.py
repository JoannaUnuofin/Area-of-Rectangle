class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(1245, 1090)
print("Dimension of Rectangle - Length : %d Width : %d" % (newRectangle.length, newRectangle.width))
print("Area of Rectangle :", newRectangle.rectangle_area())

