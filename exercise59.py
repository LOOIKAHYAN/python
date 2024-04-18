
height = float(input("Height: "))
unit = input("feet(f) or inches(i): ")

def get_height_in_cm(height, unit):
    if unit.lower() == "f":
        feet_to_cm = height * 30.48
        print("Height in cm: ",feet_to_cm)
    elif unit.lower() == "i":
        inches_to_cm = height * 2.54
        print("Height in cm: ", inches_to_cm)
    else:
        print("Invalid unit, only (f) and (i) accepted.")

get_height_in_cm(height, unit)