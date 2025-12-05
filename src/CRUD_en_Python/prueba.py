
# ========================================
# CONSTANTS
# ========================================
EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5

# ========================================
# DATA STRUCTURE
# ========================================
"""
Estructura de datos elegida: DICCIONARIO
- Clave: item_id (string)
- Valor: Diccionario con campos: name, price, quantity

Razón: Acceso O(1) por ID, más eficiente para operaciones CRUD
que requieren búsqueda frecuente por identificador único.
"""
inventory = {}  # Main data structure: dict of dicts

# ========================================
# CRUD FUNCTIONS
# ========================================
def create_item(data_store, item_id, name, price, quantity):
    """
    Create a new item in the data store.
    
    Args:
        data_store (dict): The main inventory dictionary
        item_id (str): Unique identifier for the item
        name (str): Item name
        price (float): Item price (>= 0)
        quantity (int): Item quantity (>= 0)
    
    Returns:
        bool: True if creation successful, False otherwise
    """
    if item_id in data_store:
        print("Error: Item ID already exists")
        return False
    
    data_store[item_id] = {
        'name': name,
        'price': float(price),
        'quantity': int(quantity)
    }
    return True

def read_item(data_store, item_id):
    """
    Retrieve an item from the data store by its ID.
    
    Args:
        data_store (dict): The main inventory dictionary
        item_id (str): Item identifier to search for
    
    Returns:
        dict or None: Item data if found, None otherwise
    """
    return data_store.get(item_id)

def update_item(data_store, item_id, new_name, new_price, new_quantity):
    """
    Update an existing item's data.
    
    Args:
        data_store (dict): The main inventory dictionary
        item_id (str): Item identifier to update
        new_name (str): New item name
        new_price (float): New item price
        new_quantity (int): New item quantity
    
    Returns:
        bool: True if update successful, False otherwise
    """
    if item_id not in data_store:
        return False
    
    data_store[item_id] = {
        'name': new_name,
        'price': float(new_price),
        'quantity': int(new_quantity)
    }
    return True

def delete_item(data_store, item_id):
    """
    Remove an item from the data store.
    
    Args:
        data_store (dict): The main inventory dictionary
        item_id (str): Item identifier to delete
    
    Returns:
        bool: True if deletion successful, False otherwise
    """
    if item_id not in data_store:
        return False
    
    del data_store[item_id]
    return True

def list_items(data_store):
    """
    Display all items in the data store.
    
    Args:
        data_store (dict): The main inventory dictionary
    
    Returns:
        list: All items as a list of tuples (id, data)
    """
    if not data_store:
        print("No items in inventory")
        return []
    
    items_list = []
    for item_id, item_data in data_store.items():
        items_list.append((item_id, item_data))
        print(f"ID: {item_id}")
        print(f"  Name: {item_data['name']}")
        print(f"  Price: ${item_data['price']:.2f}")
        print(f"  Quantity: {item_data['quantity']}")
        print("-" * 30)
    
    return items_list

# ========================================
# HELPER FUNCTIONS
# ========================================
def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("INVENTORY CRUD SYSTEM")
    print("=" * 40)
    print(f"{CREATE_OPTION}) Create item")
    print(f"{READ_OPTION}) Read item by ID")
    print(f"{UPDATE_OPTION}) Update item")
    print(f"{DELETE_OPTION}) Delete item")
    print(f"{LIST_OPTION}) List all items")
    print(f"{EXIT_OPTION}) Exit")
    print("=" * 40)

def get_valid_input(prompt, input_type=str, min_value=None):
    """
    Get and validate user input.
    
    Args:
        prompt (str): Message to display to user
        input_type (type): Expected data type (str, float, int)
        min_value: Minimum acceptable value for numeric types
    
    Returns:
        Validated input or None if invalid
    """
    try:
        user_input = input(prompt).strip()
        
        if input_type == str:
            if not user_input:
                print("Error: Input cannot be empty")
                return None
            return user_input
        
        elif input_type == float:
            value = float(user_input)
            if min_value is not None and value < min_value:
                print(f"Error: Value must be >= {min_value}")
                return None
            return value
        
        elif input_type == int:
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Error: Value must be >= {min_value}")
                return None
            return value
    
    except ValueError:
        print(f"Error: Invalid {input_type.__name__} format")
        return None
    
    return None

# ========================================
# MAIN PROGRAM
# ========================================
def main():
    """Main program loop."""
    print("Inventory CRUD System initialized")
    
    while True:
        display_menu()
        
        # Get menu option using input()
        option_input = input("Select option (0-5): ").strip()
        
        # Validate option
        if not option_input.isdigit():
            print("Error: Invalid option - enter a number between 0 and 5")
            continue
        
        option = int(option_input)
        
        # Check if option is valid
        if option not in [EXIT_OPTION, CREATE_OPTION, READ_OPTION, 
                         UPDATE_OPTION, DELETE_OPTION, LIST_OPTION]:
            print("Error: Invalid option - choose 0-5")
            continue
        
        # Process option
        if option == EXIT_OPTION:
            print("Exiting program. Goodbye!")
            break
        
        elif option == CREATE_OPTION:
            print("\n--- CREATE ITEM ---")
            
            # Get item ID using input()
            item_id = input("Enter item ID: ").strip()
            if not item_id:
                print("Error: Item ID cannot be empty")
                continue
            
            if item_id in inventory:
                print("Error: Item ID already exists")
                continue
            
            # Get item name using input()
            name = input("Enter item name: ").strip()
            if not name:
                print("Error: Item name cannot be empty")
                continue
            
            # Get price using input() with validation
            price_input = input("Enter price (must be >= 0): ").strip()
            try:
                price = float(price_input)
                if price < 0:
                    print("Error: Price must be >= 0")
                    continue
            except ValueError:
                print("Error: Price must be a valid number")
                continue
            
            # Get quantity using input() with validation
            quantity_input = input("Enter quantity (must be >= 0): ").strip()
            try:
                quantity = int(quantity_input)
                if quantity < 0:
                    print("Error: Quantity must be >= 0")
                    continue
            except ValueError:
                print("Error: Quantity must be a valid integer")
                continue
            
            if create_item(inventory, item_id, name, price, quantity):
                print("Item created successfully")
            else:
                print("Error: Failed to create item")
        
        elif option == READ_OPTION:
            print("\n--- READ ITEM ---")
            
            # Get item ID using input()
            item_id = input("Enter item ID to read: ").strip()
            if not item_id:
                print("Error: Item ID cannot be empty")
                continue
            
            item = read_item(inventory, item_id)
            if item:
                print(f"\nItem found:")
                print(f"  ID: {item_id}")
                print(f"  Name: {item['name']}")
                print(f"  Price: ${item['price']:.2f}")
                print(f"  Quantity: {item['quantity']}")
            else:
                print("Item not found")
        
        elif option == UPDATE_OPTION:
            print("\n--- UPDATE ITEM ---")
            
            # Get item ID using input()
            item_id = input("Enter item ID to update: ").strip()
            if not item_id:
                print("Error: Item ID cannot be empty")
                continue
            
            if item_id not in inventory:
                print("Item not found")
                continue
            
            print(f"\nCurrent data for item '{item_id}':")
            print(f"  Name: {inventory[item_id]['name']}")
            print(f"  Price: ${inventory[item_id]['price']:.2f}")
            print(f"  Quantity: {inventory[item_id]['quantity']}")
            print("\nEnter new data (press Enter to keep current value):")
            
            # Get new name using input()
            name_input = input(f"Enter new name [{inventory[item_id]['name']}]: ").strip()
            name = name_input if name_input else inventory[item_id]['name']
            
            # Get new price using input()
            while True:
                price_input = input(f"Enter new price [${inventory[item_id]['price']:.2f}]: ").strip()
                if not price_input:
                    price = inventory[item_id]['price']
                    break
                try:
                    price = float(price_input)
                    if price < 0:
                        print("Error: Price must be >= 0")
                        continue
                    break
                except ValueError:
                    print("Error: Price must be a valid number")
                    continue
            
            # Get new quantity using input()
            while True:
                quantity_input = input(f"Enter new quantity [{inventory[item_id]['quantity']}]: ").strip()
                if not quantity_input:
                    quantity = inventory[item_id]['quantity']
                    break
                try:
                    quantity = int(quantity_input)
                    if quantity < 0:
                        print("Error: Quantity must be >= 0")
                        continue
                    break
                except ValueError:
                    print("Error: Quantity must be a valid integer")
                    continue
            
            if update_item(inventory, item_id, name, price, quantity):
                print("Item updated successfully")
            else:
                print("Error: Failed to update item")
        
        elif option == DELETE_OPTION:
            print("\n--- DELETE ITEM ---")
            
            # Get item ID using input()
            item_id = input("Enter item ID to delete: ").strip()
            if not item_id:
                print("Error: Item ID cannot be empty")
                continue
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete item '{item_id}'? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("Deletion cancelled")
                continue
            
            if delete_item(inventory, item_id):
                print("Item deleted successfully")
            else:
                print("Item not found")
        
        elif option == LIST_OPTION:
            print("\n--- LIST ALL ITEMS ---")
            list_items(inventory)

# ========================================
# ENTRY POINT
# ========================================
if __name__ == "__main__":
    print("========================================")
    print("INVENTORY CRUD SYSTEM")
    print("========================================")
    print("This program allows you to manage an inventory")
    print("with Create, Read, Update, and Delete operations.")
    print("\nFeatures:")
    print("- Create new items with unique ID")
    print("- Read item details by ID")
    print("- Update existing items")
    print("- Delete items")
    print("- List all items")
    print("========================================")
    
    # Ask user if they want to run test cases
    test_choice = input("Do you want to run test cases first? (yes/no): ").strip().lower()
    
    if test_choice == 'yes':
        print("\n" + "=" * 50)
        print("RUNNING TEST CASES")
        print("=" * 50)
        
        # Test Case 1: Normal flow
        print("\nTest 1: Normal flow - Creating and managing an item")
        print("-" * 40)
        print("Creating item with ID 'P001', name 'Laptop', price 999.99, quantity 5")
        create_item(inventory, "P001", "Laptop", 999.99, 5)
        print("Item created successfully" if "P001" in inventory else "Failed to create")
        
        print("\nReading item 'P001':")
        item = read_item(inventory, "P001")
        if item:
            print(f"  Found: {item['name']} - ${item['price']} - Qty: {item['quantity']}")
        
        print("\nUpdating item 'P001' to new price 899.99")
        update_item(inventory, "P001", "Laptop", 899.99, 3)
        print("Item updated" if inventory["P001"]["price"] == 899.99 else "Update failed")
        
        print("\nListing all items:")
        list_items(inventory)
        
        print("\nDeleting item 'P001'")
        delete_item(inventory, "P001")
        print("Item deleted" if "P001" not in inventory else "Delete failed")
        
        # Test Case 2: Border cases
        print("\n\nTest 2: Border cases - Minimal valid data")
        print("-" * 40)
        print("Creating item with minimal valid data: ID 'X', name 'a', price 0.0, quantity 0")
        create_item(inventory, "X", "a", 0.0, 0)
        print("Item created successfully" if "X" in inventory else "Failed to create")
        
        print("\nListing all items after border case test:")
        list_items(inventory)
        
        # Clear inventory for main program
        inventory.clear()
        
        print("\n" + "=" * 50)
        print("TEST CASES COMPLETED")
        print("=" * 50)
        input("Press Enter to start the interactive program...")
    
    # Start the main program
    main()
