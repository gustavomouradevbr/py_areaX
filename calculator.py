print("==================\nArea Calculator 📐\n==================")

print("1) Square\n2) Rectangle\n3) Triangle\n4) Circle\n5) Exit")

calculator = int(input("Above are the geometric areas. Choose a number from 1 to 4 for the area you want to calculate or choose 5 to exit: "))

while calculator < 1 or calculator > 5:
    calculator = int(input("Above are the geometric areas. Choose a number from 1 to 4 for the area you want to calculate or choose 5 to exit: "))

if calculator == 1:
    print("Great, you chose Square.")
    side = int(input("Please enter the side length of the Square: "))
    square_area = side ** 2
    print(f"The area of your Square is {square_area}")
elif calculator == 2:
    print("Rectangle is a great choice!")
    length = int(input("Please enter the length of the Rectangle: "))
    width = int(input("Please enter the width of the Rectangle: "))
    rectangle_area = length * width
    print(f"The area of your Rectangle is {rectangle_area}")
elif calculator == 3:
    print("Triangle selected! Let's calculate.")
    base = int(input("Please enter the base of your Triangle: "))
    height = int(input("Please enter the height of your Triangle: "))
    triangle_area = (base * height) / 2
    print(f"The area of your Triangle is {triangle_area}")
elif calculator == 4:
    print("Let's calculate the area of a Circle.")
    pi = 3.14
    radius = int(input("Please enter the radius of your Circle: "))
    circle_area = pi * radius ** 2
    print(f"The area of your Circle is {circle_area}")