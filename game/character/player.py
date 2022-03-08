from game.character.character import Character


from game.character.character import Character
class Player(Character):

  """
  Player class is going to be a child class from Character class. 
  It will create the character that the player one will be using (green)


  Attributes:

  Author:
  """

  def __init__(self,appearance,groupName,x,y,fontSize,scale,color= ""):
      self._groupName = groupName
      Character.__init__(self,appearance,x,y,fontSize,scale,color)

  def get_group_name(self):
      """ Gets the name of the group of characters
          return: Str
      """
      return self._groupName