class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                for x in range(self.width):
                    picture += "*"
                picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        container_area = self.get_area()
        shape_area = shape.get_area()
        amount_inside = 0
        while container_area > 0:
            container_area = container_area - shape_area
            if container_area >=0:
                amount_inside = amount_inside + 1
        return amount_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})" 


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.heigth = width
    
    def __str__(self):
        return f"Square(side={self.width})" 
