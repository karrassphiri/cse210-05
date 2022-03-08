class CharacterStorage:

  """ 
  CharacterStorage class will store the characters of both players, one red and one green.

  Attributes: 

  Author:
  """
  def __init__(self):
      self._characters = {}

  def add_new_character(self,group,character):
      """ Adds a new group or a new character in an existing group """
      if not group in self._characters.keys():
          self._characters[group] = []

      if not character in self._characters[group]:
          self._characters[group].append(character)

  def get_all_characters(self):
      """ Gets all the groups
          return: Dictionary
      """
      return self._characters

  def get_character(self,group):
      """ Gets a character 
          returns: Character
      """
      if group in self._characters.keys():
          return self._characters[group]
          