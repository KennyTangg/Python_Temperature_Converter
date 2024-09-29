# Simple Temperature Converter

## Overview

This is a Python program designed to convert temperatures between Celsius, Kelvin, and Fahrenheit. Created by Kenny Tang on September 23, 2024, this script provides a simple interface for users to input a temperature and select the units for conversion.

## Features

- Convert temperatures between:
  - Celsius (C)
  - Kelvin (K)
  - Fahrenheit (F)
- User-friendly prompts for input and output
- Handles invalid input gracefully

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/k3nnytang/Temperature_Converter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd repo-name
   ```

3. Ensure you have Python installed on your system.

## Usage

1. Run the program:

   ```bash
   python Temp_Conv.py
   ```

2. Follow the on-screen prompts:
   - Enter the temperature you wish to convert.
   - Choose the unit of the input temperature (C/K/F).
   - Select the unit you want to convert to (C/K/F).

3. The converted temperature will be displayed.

## Example

```
=========================================
 Welcome to Simple Temperature Converter 
=========================================
Please Input Your The Number: 100
Which Unit do you want to convert ?   
1. Celcius       (C)
2. Kelvin        (K)
3. Fahrenheit    (F)

Select An Option (C/K/F): C
Which unit do you want to convert into ?   
1. Celcius       (C)
2. Kelvin        (K)
3. Fahrenheit    (F)

Select An Option (C/K/F): F
Temperature Convert from 100.0 C to 212.0 F
```

## Error Handling

If an invalid choice is made at any prompt, the program will notify the user and request input again until a valid option is chosen.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements!

