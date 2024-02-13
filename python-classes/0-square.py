class Square:
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square (no type or value verification).
        """
        self.__size = size

# Example usage:
if __name__ == "__main__":
    my_square = Square(3)
    print(f"Type of my_square: {type(my_square)}")
    print(f"Attributes of my_square: {my_square.__dict__}")

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square._Square__size)
    except AttributeError as e:
        print(e)