class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.item = {}

    def add_new_item(self, id, name, price, qunatity):
        if id in self.item:
            print("Item Already exists")
        else:
            new = Item(id, name, price, qunatity)
            self.item[id] = new
            print(f" {name} added to an Inventory")

    def update_item(self, id, quantity):
        if id in self.item:
            self.item[id].quantity += quantity
            print(f" {self.item[id].name} has been updated to {self.item[id].quantity}")
        else:
            print("Item not found in inventory")

    def remove_item(self, id):
        if id in self.item:
            del self.item[id]
            print(f" {id} has been deleted from inventory")
        else:
            print("Item not found in inventory")

    def display(self):
        if not self.item:
            print("Nothing to diplay")
        else:
            for i in self.item.values():
                print(i)

    def check_stock(self, id, name, quantity):
        if id in self.item:
            item = self.item[id]
            print(f" {name} is in stock and its quantity is : {quantity}")
        else:
            print("Item not found in inventory")

    def track_sales(self, id, quantity):
        if id in self.item:
            if self.item[id].quantity > quantity:
                self.item[id].quantity -= quantity
                print(f"{quantity} of {self.item[id].name}  "
                      f"New quantity :{self.item[id].quantity}")
            else:
                print("No quantity")
        else:
            print("Item not found in inventory")

    def report(self, price, quantity):
        total = 0
        for i in self.item.values():
            total += price * quantity
        print(f" Total value : {total}")


inventory = Inventory()
inventory.add_new_item(1, "Milk", 300, 50)
inventory.add_new_item(2, "Bread", 100, 70)
inventory.add_new_item(3,"Eggs",90,80)
inventory.update_item(3, -9)
inventory.remove_item(1)
inventory.display()
inventory.check_stock(1,"Milk",50)
inventory.check_stock(3,"Eggs",80)
inventory.track_sales(1,50)
inventory.track_sales(2,70)
inventory.track_sales(3,70)
inventory.report(300,50)
inventory.display()



