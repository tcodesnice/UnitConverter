# Function to perform length conversions
def convert_length(value, from_unit, to_unit):
    units = {
        'meters': 1.0,
        'feet': 3.28084,
        'inches': 39.3701
    }

    if from_unit in units and to_unit in units:
        return value * units[to_unit] / units[from_unit]
    else:
        return "Invalid units"

# Function to perform weight conversions
def convert_weight(value, from_unit, to_unit):
    units = {
        'kilograms': 1.0,
        'pounds': 2.20462,
        'grams': 1000.0
    }

    if from_unit in units and to_unit in units:
        return value * units[to_unit] / units[from_unit]
    else:
        return "Invalid units"

# Function to perform temperature conversions (Celsius to Fahrenheit and vice versa)
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    else:
        return "Invalid units"

# Function to get user input for a numeric value
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

# Function to get user input for category
def get_category():
    while True:
        category = input("Enter the category (length, weight, temperature): ").lower()
        if category in ["length", "weight", "temperature"]:
            return category
        else:
            print("Invalid category. Please enter 'length', 'weight', or 'temperature'.")

# Input
try:
    category = get_category()

    if category == "length":
        value = get_numeric_input("Enter the value to convert: ")
        from_unit = input("Enter the source unit (e.g., meters, feet, inches): ").lower()
        to_unit = input("Enter the target unit (e.g., meters, feet, inches): ").lower()
        result = convert_length(value, from_unit, to_unit)
    elif category == "weight":
        value = get_numeric_input("Enter the value to convert: ")
        from_unit = input("Enter the source unit (e.g., kilograms, pounds, grams): ").lower()
        to_unit = input("Enter the target unit (e.g., kilograms, pounds, grams): ").lower()
        result = convert_weight(value, from_unit, to_unit)
    elif category == "temperature":
        value = get_numeric_input("Enter the value to convert: ")
        from_unit = input("Enter the source unit (celsius, fahrenheit): ").lower()
        to_unit = input("Enter the target unit (celsius, fahrenheit): ").lower()
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = "Invalid category"

    if result != "Invalid units" and result != "Invalid category":
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    else:
        print("Invalid units or category entered.")

except ValueError:
    print("Invalid input. Please enter a valid numeric value for conversion.")
