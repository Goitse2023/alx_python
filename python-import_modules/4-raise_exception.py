def raise_exception():
    x = "hello"
    y = 5
    try:
        z = x + y
    except TypeError:
        print("A type error occurred.")
        raise