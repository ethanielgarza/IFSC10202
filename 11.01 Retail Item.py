class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0.0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price

    def inventory_value(self):
        return self.units_on_hand * self.price
# Define the Actions (Methods) of the Object
    def InventoryValue(self):
        InventoryValue = self.UnitsOnHand * self.Price
        return InventoryValue
def print_inventory(inventory_list):
    print(f"{'Description':<15}{'Units On Hand':<15}{'Price':<10}{'Inventory Value':<15}")
    for item in inventory_list:
        print(f"{item.description:<15}{item.units_on_hand:<15}{item.price:<10.2f}{item.inventory_value():<15.2f}")

def find_inventory(inventory_list, item_name):
    for i, item in enumerate(inventory_list):
        if item.description == item_name:
            return i
    return -1
def main():
    # Read initial inventory
    inventory_list = []
    with open("11.01 Inventory.txt", "r") as f:
        for line in f:
            parts = line.strip().split(', ')
            description = parts[0]
            units = int(parts[1])
            price = float(parts[2])
            inventory_list.append(RetailItem(description, units, price))

    print("Initial Inventory:")
    print_inventory(inventory_list)
    print("\n" + "="*55 + "\n")

    # Read updates and apply them
    with open("11.01 InventoryUpdate.txt", "r") as f:
        for line in f:
            parts = line.strip().split(', ')
            description = parts[0]
            new_price = float(parts[1])
            index = find_inventory(inventory_list, description)
            if index != -1:
                inventory_list[index].price = new_price

    print("Updated Inventory:")
    print_inventory(inventory_list)

if __name__ == "__main__":
    main()