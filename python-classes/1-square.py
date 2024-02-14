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

my_square_1 = Square(3)
print(f"Type of my_square_1: {type(my_square_1)}")
print(f"Attributes of my_square_1: {my_square_1.__dict__}")

my_square_2 = Square()
print(f"Type of my_square_2: {type(my_square_2)}")
print(f"Attributes of my_square_2: {my_square_2.__dict__}")

try:
    print(my_square_1.size)
except AttributeError as e:
    print(e)

try:
    print(my_square_1._Square__size)
except AttributeError as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(f"Type of my_square_3: {type(my_square_3)}")
    print(f"Attributes of my_square_3: {my_square_3.__dict__}")
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(f"Type of my_square_4: {type(my_square_4)}")
    print(f"Attributes of my_square_4: {my_square_4.__dict__}")
except Exception as e:
    print(e)