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
    def print_inventory(inventory_list, heading):
         print(heading)
         print(f"{'Description':<15}{'Units on Hand':<15}{'Price':<10}{'Inventory Value':<15}")
         for item in inventory_list:
              print(f"{item.Description:<15}{item.UnitsOnHand:<15}{item.Price:<10.2f}{item.get_InventoryValue():15.2f}")
         print()
    def find_inventory(inventory_list, item_name):
         for i, item in enumerate(inventory_list):
              if item.Description == item_name:
                   return i 
              return -1
# Read File to get values and then print them out in Terminal
def main():
    # Read initial inventory
    inventory_list = []
    with open("11.01 Inventory.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            description = parts[0]
            units = int(parts[1])
            price = float(parts[2])
            inventory_list.append(RetailItem(description, units, price))

    print_inventory(inventory_list, "Initial Inventory")

    # Read updates and modify inventory
    with open("11.01 InventoryUpdate.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            description = parts[0]
            new_price = float(parts[1])
            index = find_inventory(inventory_list, description)
            if index != -1:
                inventory_list[index]._price = new_price

    print_inventory(inventory_list, "Updated Inventory")

if __name__ == "__main__":
    main()