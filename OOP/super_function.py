# super () = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used

class Shape:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Square(Shape):

    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        print(f'Area: {self.length*self.breadth}')

class Cube(Shape):

    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        print(f'Cube: {self.length*self.breadth*self.height}')


square = Square(5, 5)
cube = Cube(5, 5, 5)

square.area()
cube.volume()


        
        