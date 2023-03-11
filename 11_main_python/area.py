def calculate_area(base, height):
    print("__name__: ", __name__)
    return 1/2*(base*height)


if __name__ == "__main__":
    print("I am in main function of area.py")
    a = calculate_area(10,15)
    print("Area is: ", a)