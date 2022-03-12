import pyray
class Keyboard:

    """
    Keyboard class is a child class of the Keys class.
    It will get the inputs of player one and calculate the position of its character by using the keys: WASD
    to move up (W), down (S), left (A) and right (D)

    Attributes:

    Author: Karrass
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D
        self._direction = ""
        """ self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L """

    def get_input(self):
        """Gets the selected direction based on the currently pressed keys.

            return: int
        """
        if pyray.get_key_pressed() > 0:
            if pyray.is_key_down(self._keys['a']):
                self._direction = "-x"

            if pyray.is_key_down(self._keys['d']):
                self._direction = "x"

            if pyray.is_key_down(self._keys['w']):
                self._direction = "-y"

            if pyray.is_key_down(self._keys['s']):
                self._direction = "y"

        return self._direction
