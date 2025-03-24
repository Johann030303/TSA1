class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}
        self.next_id = 1
    
    def create_item(self, name: str, description: str, price: float):
        try:
            item = Item(self.next_id, name, description, price)
            self.items[self.next_id] = item
            self.next_id += 1
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self, item_id: int, name: str = None, description: str = None, price: float = None):
        if item_id not in self.items:
            print("Item not found.")
            return
        
        item = self.items[item_id]
        try:
            if name:
                if not name.strip():
                    raise ValueError("Name cannot be empty.")
                item.name = name
            if description:
                item.description = description
            if price is not None:
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                item.price = price
            print("Item updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_item(self, item_id: int):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully.")
        else:
            print("Item not found.")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Create Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            try:
                price = float(input("Enter item price: "))
                manager.create_item(name, description, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave blank to keep current): ") or None
                description = input("Enter new description (leave blank to keep current): ") or None
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
