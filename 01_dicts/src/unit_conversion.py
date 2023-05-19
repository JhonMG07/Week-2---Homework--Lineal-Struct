# create a dictionary
units = {"m": 1, "cm": 0.01, "mm": 0.001, "in": 0.0254, "ft": 0.3048, "km": 1000}

def read_number_and_convert_to_destiantion_unit(
    number: float, origin: str, destination: str
) -> float:
    if origin in units and destination in units:
        result = number * units[origin] / units[destination]
        return result
    else:
        return None


result = read_number_and_convert_to_destiantion_unit(8, "km", "m")
print(result)
