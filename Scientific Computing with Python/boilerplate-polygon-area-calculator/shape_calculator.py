import math

class Rectangle():
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self): 
    return self.height*self.width

  def get_perimeter(self): 
    return (2 * self.width + 2 * self.height)
    
  def get_diagonal(self): 
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    line = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        line = line + '*'*self.width + '\n'
      return line  
        
  def get_amount_inside(self, shape):
    cantH = math.floor(self.height/shape.height)
    cantW = math.floor(self.width/shape.width)

    return cantH * cantW
  
  def __str__(self): 
    line = "Rectangle"
    line = line + f"(width={self.width}, height={self.height})"
    return line


class Square(Rectangle):
  def __init__(self, lado):
    super().__init__(lado, lado)   # hereda init del padre

  def set_side(self, side):
    self.width = side
    self.height = side
  
  def set_width(self, width):
    self.width = width
    self.height = width
    
  def set_height(self, height):
    self.width = height
    self.height = height
    
  def __str__(self): 
    line = "Square"
    line = line + f"(side={self.height})"
    return line