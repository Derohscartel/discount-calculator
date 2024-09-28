# Define the function that calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price using the function
final_price = calculate_discount(price, discount_percent)

# Display the results
if discount_percent >= 20:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
