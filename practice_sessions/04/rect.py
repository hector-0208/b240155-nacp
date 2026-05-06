def convert_to_si(value_string):
    value_string = value_string.strip()
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000
    }
    import re
    match = re.match(r'^([\d.]+)\s*([a-zA-Z]+)$', value_string)
    
    if not match:
        raise ValueError(f"Invalid format: '{value_string}'. Use format like '5 cm' or '10 mm'")
    
    value = float(match.group(1))
    unit = match.group(2).lower()
    
    if unit not in units:
        raise ValueError(f"Unknown unit: '{unit}'. Supported units: {', '.join(units.keys())}")
    
    return value * units[unit]

def perimeter(length, width):
    perimeter = 2 * (length + width)
    print(f"The perimeter of the rectangle is {perimeter} m")

def area(length, width):
    area = length * width
    print(f"The area of the rectangle is {area} m²")

try:
    length_input = input("Enter the length of the rectangle (e.g., 5 cm, 10 mm, 2 m): ")
    width_input = input("Enter the width of the rectangle (e.g., 5 cm, 10 mm, 2 m): ")
    
    length = convert_to_si(length_input)
    width = convert_to_si(width_input)
    
    print("\nConverted values in SI units:")
    print(f"Length: {length} m")
    print(f"Width: {width} m\n")
    
    perimeter(length, width)
    area(length, width)
except ValueError as e:
    print(f"Error: {e}")
