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
def main():
    Inventory_items = []
    with open("10.02 Inventory.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if len(data) == 3:
                Description = data[0]
                UnitsOnHand = int(data[1])
                Price = float(data[2])
                item = RetailItem(Description, UnitsOnHand, Price)
                Inventory_items.append(item)
    print(f"{"Description":<20}{"Units on Hand":<20}{"Price":<20}{"Inventory Value":<20}")
    print("-" * 70)
    for item in Inventory_items:
        InventoryValue = item.InventoryValue()
        print(f"{item.Description:<20}{item.UnitsOnHand:<20}{item.Price:<10.2f}{InventoryValue:>20.2f}")
if __name__ == "__main__":
     main()