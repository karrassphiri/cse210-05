class Position:
  """
  This class will set the position of a character 


  Atributes:
    _X (int) : Position in x
    _y (int) : Position in y
    _scale (int) : Scale of position


  Author: Yami
  """

  def __init__(self, x, y, scale=0):

    self._x = x
    self._y = y
    self._scale = scale
    self._direction = ""

  def set_x_position(self, x):
    self._x = x

  def get_x_position(self):
    return self._x

  def set_y_position(self, y):
    self._y = y

  def get_y_position(self):
    return self._y  
  

  def get_position(self):
    """
    This will get the final position
    """

    return Position(self._x, self._y)



  def equals(self, characterA, characterB):
    """
    This will compare the positions between characterA adn characterB

    return: bool
    """

    """ if characterA.get_x_position()+15 == characterB.get_x_position() and characterA.get_y_position()+15 == characterB.get_y_position():
      return True """

    aCharX = characterA.get_x_position()
    aCharY = characterA.get_y_position()
    
    if self._direction == "x":
      aCharX = aCharX + self._scale
    elif self._direction == "-x":
      aCharX = aCharX - self._scale

    if self._direction == "y":
      aCharY = aCharY + self._scale
    elif self._direction == "-y":
      aCharY = aCharY - self._scale
        
    if aCharX == characterB.get_x_position() and aCharY == characterB.get_y_position():
      return True  

  
  def scale_X_position(self, x_direction):
    """
    Scales the position according directions
    """

    if x_direction > 0:
      return self._scale
    elif x_direction < 0:
      return - self._scale
    
  def get_direction(self):
    return self._direction

  def set_direction(self,direction):
    self._direction = direction