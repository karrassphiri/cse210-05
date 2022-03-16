from game.position.position import Position

class Banner(Position):

  """
  Banner class is going to be another child class from Characters class. 
  It will create the character that the player two will be using (red)

  Attributes:

  Author:Samuel
  """
  def __init__(self, x, y,message,fontSize,color):
    super().__init__(x, y)
    self._message = message
    self._font_size = fontSize
    self._color = color
    self._extra_text = ""

  def set_message(self,message):
    self._message = message
  
  def get_message(self):
    return self._message + self._extra_text
  
  def get_font_size(self):
    return self._font_size

  def get_color(self):
    return self._color

  def add_to_message(self,text):
    self._extra_text = text
