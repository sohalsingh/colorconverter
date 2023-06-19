import webcolors

def color_to_code(color):
    try:
        # Attempt to convert the color name to its corresponding code
        code = webcolors.name_to_hex(color)
        return code
    except ValueError:
        try:
            # Attempt to convert the color code to its corresponding name
            name = webcolors.hex_to_name(color)
            return name
        except ValueError:
            # Invalid color value
            return None

# Example usage
color = "red"
code = color_to_code(color)
if code is not None:
    print(f"The code for the color '{color}' is '{code}'.")
else:
    print(f"Invalid color: '{color}'.")

