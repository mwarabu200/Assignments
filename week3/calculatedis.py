#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage 
# (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount (price, discount_percent):
    if discount_percent >=20:
     discount_amount = (discount_percent/100)* price 
     return round(price -discount_amount, 2)

    else: return price

                                                   
price= float(input("enter the original price of the item:"))
discount_percent = float(input("enter the discount percentage:"))

if (price < 0 or discount_percent < 0) :
        print("price and discount percentage must be non-negative values.")
else:
        final_price =calculate_discount(price, discount_percent)
print(f"the final price after applying the discount(if applicable) is: {final_price}")


