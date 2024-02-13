class Square:
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
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
    print("Area:", my_square_1.area())

    try:
        print(my_square_1.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square_1._Square__size)
    except AttributeError as e:
        print(e)

    my_square_2 = Square(5)
    print("Area:", my_square_2.area())