from ohms_law import calc_resistance

result = calc_resistance(24, 2)

print("Resistance =", result, "ohms")
print(calc_resistance.__doc__)
from ohms_law import calc_resistance, calc_power

# Existing resistance test
print("Resistance =", calc_resistance(9, 0.03), "ohms")

# Exercise 1: Power tests
print("Power Test 1 (12V, 4Ω) =", calc_power(12, 4), "watts")
print("Power Test 2 (24V, 6Ω) =", calc_power(24, 6), "watts")

# Display docstring
print("\n--- Function Documentation ---")
print(calc_power.__doc__)