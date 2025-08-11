def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply (0-100)
    
    Returns:
    float: Final price after discount (if applicable), otherwise original price
    """
    # Only apply discount if it's 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate final price after discount
        final_price = price - discount_amount
        # Return the discounted price rounded to 2 decimal places
        return round(final_price, 2)
    else:
        # Return original price if discount is less than 20%
        return price


def get_valid_input(prompt, input_type=float, min_value=0):
    """
    Helper function to get valid user input with error handling.
    
    Parameters:
    prompt (str): Message to display to user
    input_type (type): Expected data type (float or int)
    min_value (float): Minimum acceptable value
    
    Returns:
    input_type: Validated user input
    """
    while True:
        try:
            user_input = input_type(input(prompt))
            if user_input >= min_value:
                return user_input
            else:
                print(f"Value must be {min_value} or greater. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_result(original_price, discount_percent, final_price):
    """
    Display the result in a user-friendly format with details.
    
    Parameters:
    original_price (float): Original price before discount
    discount_percent (float): Discount percentage attempted
    final_price (float): Price after discount (if applied)
    """
    print("\n" + "=" * 40)
    print("PRICE CALCULATION RESULTS".center(40))
    print("=" * 40)
    print(f"Original Price: ${original_price:.2f}")
    print(f"Discount Percentage: {discount_percent}%")
    
    # Check if discount was applied
    if discount_percent >= 20:
        discount_amount = original_price - final_price
        print(f"Discount Applied: -${discount_amount:.2f}")
        print(f"Final Price: ${final_price:.2f}")
    else:
        print("No discount applied (less than 20%)")
        print(f"Final Price: ${final_price:.2f}")
    print("=" * 40 + "\n")


def main():
    """
    Main function to run the discount calculator program.
    """
    print("WELCOME TO THE DISCOUNT CALCULATOR")
    print("This program calculates your final price after applying any eligible discounts.\n")
    
    # Get user input with validation
    price = get_valid_input("Enter the original price of the item: $", min_value=0.01)
    discount = get_valid_input("Enter the discount percentage (0-100): ", min_value=0)
    
    # Calculate final price
    final_price = calculate_discount(price, discount)
    
    # Display detailed results
    display_result(price, discount, final_price)
    
    # Additional helpful information
    if discount < 20:
        needed_for_discount = 20 - discount
        print(f"Note: You needed {needed_for_discount}% more to qualify for the discount.")


# Run the program
if __name__ == "__main__":
    main()