class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(): Calculates and returns the area of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

# Example usage:
if __name__ == "__main__":
    my_square_1 = Square(3)
    print(f"{type(my_square_1)}")
    print(f" {my_square_1.__dict__}")

    
