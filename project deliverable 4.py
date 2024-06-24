import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(self, password):
        return self.password == password

    def __str__(self):
        return f"Username: {self.username}"

class InventoryItem:
    def __init__(self, item_type):
        self.item_type = item_type

    def __str__(self):
        return f"Item Type: {self.item_type}"

class DataManager:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("File not found. Creating new file.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON. File may be corrupt. Creating new file.")
            return {}

    def save_data(self, data):
        try:
            with open(self.filename, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")

def validate_item_type(item_type):
    return bool(item_type.strip())  # Check if item type is not empty after stripping whitespace

def validate_item_id(item_id):
    return bool(item_id.strip())  # Check if item ID is not empty after stripping whitespace

class Manager(User):
    def __init__(self, username, password, inventory, data_manager):
        super().__init__(username, password)
        self.inventory = inventory
        self.data_manager = data_manager

    def manage_supplies(self, item_id):
        if item_id in self.inventory:
            return self.inventory[item_id]
        else:
            return None

    def add_to_inventory(self, item_id, item_type):
        if item_id not in self.inventory and validate_item_type(item_type) and validate_item_id(item_id):
            self.inventory[item_id] = InventoryItem(item_type)
            self.data_manager.save_data(self.inventory)
        else:
            print("Item already exists in inventory or invalid data.")

class Fan(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def access_merchandise(self):
        return "Merchandise"

    def __str__(self):
        return f"Fan: {self.username}"

class Player(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def select_supplies(self, selection):
        return "Selected Supplies"

    def __str__(self):
        return f"Player: {self.username}"

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username:
            if user.verify_password(password):
                return user
            else:
                print("Incorrect password.")
                return None
    print("User not found.")
    return None

def menu():
    print("1. Manager")
    print("2. Fan")
    print("3. Player")
    print("Type 'exit' to exit the application.")

def manage_supplies_menu():
    print("1. Manage Medical Supplies")
    print("2. Manage Transportation")
    print("3. Add Item to Inventory")

def select_supplies_menu():
    print("1. Select Player Supplies")
    print("2. Select Team Gear")

def logout(user):
    print(f"Logging out {user}.")

def menu_output():
    menu()
    choice = input("Select user type: ")
    return choice

def test_functions():
    # Unit Tests
    assert User("test_user", "test_pass").verify_password("test_pass") == True
    assert Manager("manager1", "password1", {}, None).inventory == {}
    assert Fan("fan1", "password2").__str__() == "Fan: fan1"
    assert Player("player1", "password3").__str__() == "Player: player1"
    assert InventoryItem("test_item").__str__() == "Item Type: test_item"
    
    # Additional Unit Tests
    assert validate_item_type("") == False
    assert validate_item_id("") == False
    assert validate_item_type("ValidType") == True
    assert validate_item_id("ValidID") == True

    print("Unit tests passed.")

def main():
    data_manager = DataManager("inventory_data.json")
    inventory = data_manager.load_data()
    users = [Manager("manager1", "password1", inventory, data_manager), Fan("fan1", "password2"), Player("player1", "password3")]

    while True:
        choice = menu_output()

        if choice == "1":
            manager = login(users)
            if manager:
                manage_supplies_menu()
                selection = input("Select option: ")
                if selection in ["1", "2"]:
                    item_id = input("Enter item ID: ")
                    item = manager.manage_supplies(item_id)
                    if item:
                        print(item)
                    else:
                        print("Item not found.")
                elif selection == "3":
                    item_id = input("Enter item ID: ")
                    item_type = input("Enter item type: ")
                    if validate_item_type(item_type) and validate_item_id(item_id):
                        manager.add_to_inventory(item_id, item_type)
                    else:
                        print("Invalid item type or item ID.")
                else:
                    print("Invalid selection.")
        elif choice == "2":
            fan = login(users)
            if fan:
                print(fan.access_merchandise())
        elif choice == "3":
            player = login(users)
            if player:
                select_supplies_menu()
                selection = input("Select option: ")
                if selection in ["1", "2"]:
                    item = player.select_supplies(selection)
                    if item:
                        print(item)
                    else:
                        print("Item not found.")
                else:
                    print("Invalid selection.")
        elif choice.lower() == "exit":
            print("Exiting application.")
            data_manager.save_data(inventory)  # Save data before exiting
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    test_functions()
