from game.gameDesign.color import Color
from game.position.position import Position


class Character (Position):
    """ This will create a character

    Attributes: 

        _appearance (str) : how the character will look like
        _position (Position): the position of the character
        _font_size (int) : the size of the character
        _color (rgb) : the color of the character

    Author: Yami 
    """

    def __init__(self, appearance, x, y, fontSize, scale, color=""):

        self._appearance = appearance
        self._position = Position.__init__(self, x, y, scale)
        self._fontSize = fontSize
        self._color = color

        if color == "":
            self._color = self._set_character_color()


    def get_appearance(self):
        return self._appearance


    def set_appearance(self, appearance):
        self._appearance = appearance

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._fontSize

    def _set_character_color(self):
        return Color().to_tuple()