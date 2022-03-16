class GameOver:

  """
  GameOver class will display a message when finishing the game, change the color of the characters
  and its logistic.

  Attributes:

  Author:
  """

  def __init__(self,banner):
    self._main_banner = banner

  def game_over(self):
    self._main_banner.set_message("Game Over!!")
    return True