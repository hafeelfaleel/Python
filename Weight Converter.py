# PYTHON WEIGHT CONVERTER

weight = float(input("Enter weight: "))
unit = input("Enter unit Kilograms or Pounds (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight ,1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight ,1)} {unit}")
else:
    print(f"{unit} was not valid")