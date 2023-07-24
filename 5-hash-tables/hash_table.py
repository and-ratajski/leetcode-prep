class HashTable:
    """Basic implementation of a Hash Table in vanilla python."""

    default_initial_size = 7  # should be a prime nuber

    def __init__(self, size=default_initial_size):
        self.data_map = [None] * size

    def _hash(self, key: str, hashing_const=23) -> int:
        """
        Custom hash method to hash the keys.

        Mind that `hashing_const` should be a prime number.
        """
        _hash = 0
        for char in key:
            _hash = (_hash + ord(char) * hashing_const) % len(self.data_map)
        return _hash

