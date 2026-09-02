from unit_converter import mm_to_inches, inches_to_mm

direction = input("Enter conversion (mm_to_in or in_to_mm): ")
value = float(input("Enter the measurement: "))

if direction == "mm_to_in":
    result = mm_to_inches(value)
    print("Converted value:", result, "inches")

elif direction == "in_to_mm":
    result = inches_to_mm(value)
    print("Converted value:", result, "mm")

else:
    print("Invalid conversion option.")

print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)

from unit_converter import (
    mm_to_inches,
    inches_to_mm,
    cm_to_inches,
    inches_to_cm
)

direction = input("Enter conversion (mm_to_in, in_to_mm, cm_to_in, or in_to_cm): ")
value = float(input("Enter the measurement: "))

if direction == "mm_to_in":
    print("Converted value:", mm_to_inches(value), "inches")
elif direction == "in_to_mm":
    print("Converted value:", inches_to_mm(value), "mm")
elif direction == "cm_to_in":
    print("Converted value:", cm_to_inches(value), "inches")
elif direction == "in_to_cm":
    print("Converted value:", inches_to_cm(value), "cm")
else:
    print("Invalid conversion option.")

print("\n--- Documentation ---")
print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)
print(cm_to_inches.__doc__)
print(inches_to_cm.__doc__)

def build_menu():
    """Build and return a list of available menu options.

    Returns:
        list: A list of strings representing the program options.
    """
    options = [
        "Calculate Resistance",
        "Convert mm to Inches",
        "Convert Inches to mm",
        "Convert cm to Inches",
        "Convert Inches to cm",
        "Exit"
    ]
    return options


def display_menu():
    """Display the menu options to the user using build_menu()."""
    options = build_menu()
    print("\n--- Engineering Calculator Menu ---")
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")