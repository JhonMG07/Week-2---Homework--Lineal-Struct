# 1.create a dictionary of units for convert
units = {"m": 1, "cm": 0.01, "mm": 0.001, "in": 0.0254, "ft": 0.3048, "km": 1000}


# 2.put the number to convert

number = float(input("Enter a number: "))

# 3.put the origen unit

origin = input("Enter the origin unit: ")

# 4.put the destination unit

destination = input("Enter the destination unit: ")

# 5.convert the number

result = number * units[origin] / units[destination]

# 6.print the result

print(result)
