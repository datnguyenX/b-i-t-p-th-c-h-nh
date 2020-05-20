class Circle(object):
    def _init_(self, r):
        sef.radius = r
    def area(self):
        return self.radius**2*3.14
aCircle = Circle(2)
print(aCircle.area())
