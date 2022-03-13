class GameOver:

  """
  GameOver class will display a message when finishing the game, change the color of the characters
  and its logistic.

  Attributes:

  Author:
  """

  def __init__(self,mainBanner):
    self._main_banner = mainBanner

  def game_over(self):
    self._main_banner.set_message("Game Over!!")
    return True