def calculate_area(base, height):
    return base * height / 2


base = float(input("Base: "))
height = float(input("Height: "))

area = calculate_area(base, height)

print("Triangle area:", area)