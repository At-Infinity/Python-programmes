def areas():
    square = lambda a: a * a
    rectangle = lambda l, b: l * b
    triangle = lambda b, h: 0.5 * b * h

    s = float(input("Enter side of square: "))
    print("Area of square:", square(s))

    l = float(input("Enter length of rectangle: "))
    b = float(input("Enter breadth of rectangle: "))
    print("Area of rectangle:", rectangle(l, b))

    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print("Area of triangle:", triangle(base, height))

areas()
