import math

a = float(input("Enter side A: "))
b = float(input("Enter side B" ))
c = math.sqrt(a ** 2 + b ** 2)

print(f"The side C is: {round(c, 2)}")