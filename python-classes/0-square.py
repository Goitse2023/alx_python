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
    my_square = Square(5)
    print(f"Size of the square: {my_square._Square__size}")