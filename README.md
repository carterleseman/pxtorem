# pxtorem

This script is designed to convert pixel (px) values in a CSS file into rem units. It specifically looks for CSS properties related to sizing (e.g., `margin`, `padding`, `width`, `height`, `line-height`, etc.) and replaces pixel values with their equivalent in `rem`, based on a base font size of `16px` (1rem = 16px).

How it works:

1. **Reads a CSS file** – Takes an input CSS file and loads its content.
2. **Identifies px-based values** – Uses regular expressions to find CSS properties with pixel values, including both standard properties (e.g., `width: 20px;`) and shorthand properties (e.g., `margin: 10px 20px;`).
3. **Converts px to rem** – Divides the pixel value by 16 and replaces it with the corresponding `rem` value.
4. **Writes to a new file** – Saves the converted CSS into an output file.

Usage:

Run the script from the command line by specifying an input CSS file and an output file:

`python pxtorem.py input.css output.css`

This will process `input.css`, convert all `px` values to `rem`, and save the result in `output.css`.