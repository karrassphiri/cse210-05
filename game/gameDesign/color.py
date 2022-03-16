class Color:

  """
  Color class will give colors to the characters of player one and two.

  Attributes:
    _red (int): Red color value
    _green (int): Green color value
    _blue (int): Blue color value
    _alpha (int): Color's opacity

  Author: Yami
  """

  def __init__(self, red, green, blue, alpha=255):
    """
    Constructs a new Color using the specified red, green, blue and alpha values.
    """

    self._red = red
    self._green = green
    self._blue = blue
    self._alpha = alpha


  def to_tuple(self):
    """
    Gets a color as a tuple of 4 values (red, green, blue, and alpha)

    Return the color as a tuple
    """

    return (self._red, self._green, self._blue, self._alpha)
