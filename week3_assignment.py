def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or higher.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
    
    Returns:
        float: The final price after applying the discount or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")