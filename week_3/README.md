# Discount Price Calculator - README

## Overview

This Python program calculates the final price of an item after applying a discount, but only if the discount percentage is 20% or higher. The program demonstrates good coding practices including input validation, modular design, and user-friendly output formatting.

## Features

- **Intelligent Discount Calculation**: Automatically applies discounts only when they meet the 20% threshold
- **Robust Input Handling**: Validates all user input to prevent errors
- **Detailed Output**: Presents results in a clean, formatted display
- **Helpful Feedback**: Provides additional information when discounts aren't applied
- **Modular Design**: Organized into reusable functions for maintainability

## Requirements

- Python 3.x

## How to Use

1. Run the program in a Python environment
2. Enter the original price of the item when prompted
3. Enter the discount percentage you'd like to apply
4. View the results which will show:
   - Original price
   - Discount percentage attempted
   - Whether discount was applied
   - Final price
   - Additional helpful information if no discount was applied

## Code Structure

The program consists of four main functions:

1. `calculate_discount(price, discount_percent)`
   - Core logic that applies discount if percentage is ≥20%
2. `get_valid_input(prompt, input_type, min_value)`

   - Handles all user input with validation
   - Prevents errors from invalid entries

3. `display_result(original_price, discount_percent, final_price)`

   - Formats and displays the output professionally
   - Shows detailed calculation results

4. `main()`
   - Orchestrates the program flow
   - Combines all components into complete application

## Example Usage

```
WELCOME TO THE DISCOUNT CALCULATOR
This program calculates your final price after applying any eligible discounts.

Enter the original price of the item: $50
Enter the discount percentage (0-100): 25

========================================
      PRICE CALCULATION RESULTS
========================================
Original Price: $50.00
Discount Percentage: 25%
Discount Applied: -$12.50
Final Price: $37.50
========================================
```

## Extra Features

- Clear visual separation of output sections
- Rounding to proper currency decimals
- Helpful message showing how much more discount was needed if threshold not met
- Comprehensive error handling
- Professional code documentation

## Author

[Natasha Hinga]Sure! Here’s your README with those small tweaks applied and polished for markdown clarity:

````markdown
# Discount Price Calculator - README

## Overview

This Python program calculates the final price of an item after applying a discount, but only if the discount percentage is 20% or higher. The program demonstrates good coding practices including input validation, modular design, and user-friendly output formatting.

## Features

- **Intelligent Discount Calculation:** Automatically applies discounts only when they meet the 20% threshold.
- **Robust Input Handling:** Validates all user input to prevent errors.
- **Detailed Output:** Presents results in a clean, formatted display.
- **Helpful Feedback:** Provides additional information when discounts aren't applied.
- **Modular Design:** Organized into reusable functions for maintainability.

## Requirements

- Python 3.x

## How to Use

1. Run the program in a Python environment:
   ```bash
   python calculate_discount.py
   ```
````

2. Enter the original price of the item when prompted.
3. Enter the discount percentage you'd like to apply.
4. View the results, which will show:

   - Original price
   - Discount percentage attempted
   - Whether the discount was applied
   - Final price
   - Additional helpful information if no discount was applied.

## Code Structure

The program consists of four main functions:

1. `calculate_discount(price, discount_percent)`

   - Core logic that applies the discount if the percentage is ≥ 20%.

2. `get_valid_input(prompt, input_type, min_value)`

   - Handles all user input with validation.
   - Prevents errors from invalid entries.

3. `display_result(original_price, discount_percent, final_price)`

   - Formats and displays the output professionally.
   - Shows detailed calculation results.

4. `main()`

   - Orchestrates the program flow.
   - Combines all components into a complete application.

## Example Usage

```
WELCOME TO THE DISCOUNT CALCULATOR
This program calculates your final price after applying any eligible discounts.

Enter the original price of the item: $50
Enter the discount percentage (0-100): 25

========================================
      PRICE CALCULATION RESULTS
========================================
Original Price: $50.00
Discount Percentage: 25%
Discount Applied: -$12.50
Final Price: $37.50
========================================
```

## Extra Features

- Clear visual separation of output sections.
- Rounding to proper currency decimals.
- Helpful message showing how much more discount was needed if threshold not met.
- Comprehensive error handling.
- Professional code documentation.

## Author

Natasha Hinga
