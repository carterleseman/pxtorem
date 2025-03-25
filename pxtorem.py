import re
import argparse

# Define base sizes for conversion
BASE_FONT_SIZE = 16  # 1rem = 16px, 1em = 16px

# Properties to convert to rem
PROPERTIES = {
    "margin", "padding", "width", "height", "min-width", "min-height",
    "padding-left", "padding-right", "padding-bottom", "padding-top",
    "margin-left", "margin-right", "margin-top", "margin-bottom", "line_height"
}

# Regex to match CSS properties followed by a px value (e.g., "margin: 20px;" or "margin: -20px;")
px_pattern = re.compile(r'(\b(?:' + '|'.join(PROPERTIES) + r')\b)\s*:\s*([-\d\.]+)px')

# Regex to match shorthand properties (e.g., margin: 10px 20px 30px 40px; or margin: -10px 20px -30px 40px;)
shorthand_pattern = re.compile(r'(\b(?:' + '|'.join(PROPERTIES) + r')\b)\s*:\s*([-\d\.px\s]+)')

def convert_px(match):
    px_value = float(match.group(1))

    converted_value = round(px_value / BASE_FONT_SIZE, 3)
    return f"{converted_value}rem"

def convert_shorthand(match):
    property_name = match.group(1)
    values = match.group(2)

    # Split shorthand values into individual components
    values = values.split()

    converted_values = []

    for value in values:
        # Check if it's a px value and convert, otherwise keep the original value
        if 'px' in value:
            # Match and convert px value
            px_match = re.match(r'([-\d\.]+)px', value)
            if px_match:
                converted_values.append(convert_px(px_match))
            else:
                converted_values.append(value)  # Append non-px values directly
        else:
            converted_values.append(value)  # Non-px values (auto, %, etc.)

    # Join the converted values and return the updated shorthand
    return f"{property_name}: {' '.join(converted_values)}"

def convert_css_units(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            css_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Apply conversion to shorthand properties (e.g., margin: 10px 20px)
    css_content = shorthand_pattern.sub(convert_shorthand, css_content)

    # Apply conversion to other px values
    converted_css = px_pattern.sub(convert_px, css_content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(converted_css)

    print(f'Conversion complete! Output saved to {output_file}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert px values in CSS to rem/em.")
    parser.add_argument("input_file", help="Path to the input CSS file")
    parser.add_argument("output_file", help="Path to save the converted CSS file")
    
    args = parser.parse_args()
    convert_css_units(args.input_file, args.output_file)