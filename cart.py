import keyboard
from product import Product
class Cart:
    def __init__(self, item, quantityBought):
        
        self.itemName = item.name
        self.quantityBought = quantityBought
        self.price = item.price

    def TotalCost(self):
        total_price = self.quantityBought * self.price
        return total_price
    
    # Call the UserManager class's method using obj

    def AddressAndConfirmation(self, street,city,country) :
        print(f"Here is your address {street} {city} {country}. Press Enter to Confirm")
        keyboard.wait('Enter')
        print("Order Confirmed")
        Product.UpdateCount(self.itemName,self.quantityBought)
        # go to main menu
    