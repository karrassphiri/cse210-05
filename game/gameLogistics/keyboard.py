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

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def __init__(self, cell_size=2):
        """Constructs a new KeyboardService using the specified cell size.
        """
        self._size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

            return: int
        """

        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        return dx

    def get_key_board(self):
        """ It checks the key that was pressed

            return: boolean
        """
        return pyray.is_key_down(pyray.KEY_A)
