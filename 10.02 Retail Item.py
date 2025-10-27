# Define Class
class RetailItem():
# Define Initializer
    def __init__(self, Description ="" , UnitsOnHand = 0, Price = 0):
            
            # Define Attributes
            self.Description = Description
            self.UnitsOnHand = UnitsOnHand
            self.Price = Price
# Define the Actions (Methods) of the Object
    def InventoryValue(self):
        InventoryValue = self.UnitsOnHand * self.Price
        return InventoryValue
# Read File to get values and then print them out in Terminal
open("10.02 Inventory.txt", "r") 


