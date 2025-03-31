def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after applying discount or original price if discount is less than 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
