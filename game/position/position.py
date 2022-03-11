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

    if characterA.get_X_position() == characterB.get_X_position() and characterA.get_Y_position() == characterB.get_Y_Position():
      return True

  
  def scale_X_position(self, x_direction):
    """
    Scales the position according directions
    """

    if x_direction > 0:
      return self._scale
    elif x_direction < 0:
      return - self._scale