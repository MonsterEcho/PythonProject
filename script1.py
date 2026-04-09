
class Item:

    def __init__(self, name, quantity, expiry):

        self.name = name

        self.quantity = int(quantity)

        self.expiry = expiry  # format: YYYY-MM-DD



    def is_expired(self):

        today = datetime.today().date()

        expiry_date = datetime.strptime(self.expiry, "%Y-%m-%d").date()

        return expiry_date <= today



    def __str__(self):

        return f"{self.name} | Qty: {self.quantity} | Expiry: {self.expiry}"





    # -------------------- Inventory Class --------------------



class Inventory:

    def __init__(self, file_name="inventory.csv"):

        self.file_name = file_name

        self.items = {}

        self.load_data()



        # Load data from CSV

    def load_data(self):

        try:

            with open(self.file_name, mode='r') as file:

                reader = csv.reader(file)

                for row in reader:

                    name, qty, expiry = row

                    self.items[name] = Item(name, qty, expiry)

        except FileNotFoundError:

            pass



            # Save data to CSV

    def save_data(self):

        with open(self.file_name, mode='w', newline='') as file:

            writer = csv.writer(file)

            for item in self.items.values():

                writer.writerow([item.name, item.quantity, item.expiry])



                # Add Item

    def add_item(self, name, quantity, expiry):

        self.items[name] = Item(name, quantity, expiry)

        print("Item added successfully!")



        # Update Item

    def update_item(self, name, quantity):

        if name in self.items:

            self.items[name].quantity = int(quantity)

            print("Item updated successfully!")
*
        else:

            print("Item not found!")



            # Delete Item

    def delete_item(self, name):

        if name in self.items:

            del self.items[name]

            print("Item deleted successfully!")

        else:

            print("Item not found!")



            # Display Inventory

    def display_items(self):

        if not self.items:

            print("Inventory is empty.")

        for item in self.items.values():

            print(item)



            # Low Stock Alert

    def low_stock_alert(self, threshold=2):

        print("\nLow Stock Items:")

        for item in self.items.values():

            if item.quantity <= threshold:

                print(item.name)



                # Expiry Alert

    def expiry_alert(self):

        print("\nExpired / Expiring Items:")

        for item in self.items.values():

            if item.is_expired():

                print(item.name)



                # Consumption Analytics (Simple Example)

    def total_items(self):

        total = sum(item.quantity for item in self.items.values())

        print(f"\nTotal Quantity of All Items: {total}")





    # -------------------- Main Program --------------------



def main():

    inventory = Inventory()



    while True:

        print("\n==== HI-CAS MENU ====")

        print("1. Add Item")

        print("2. Update Item")

        print("3. Delete Item")

        print("4. View Inventory")

        print("5. Low Stock Alert")

        print("6. Expiry Alert")

        print("7. Total Quantity Report")

        print("8. Exit")



        choice = input("Enter choice: ")



        if choice == "1":

            name = input("Enter item name: ")

            qty = input("Enter quantity: ")

            expiry = input("Enter expiry date (YYYY-MM-DD): ")

            inventory.add_item(name, qty, expiry)



        elif choice == "2":

            name = input("Enter item name to update: ")

            qty = input("Enter new quantity: ")

            inventory.update_item(name, qty)



        elif choice == "3":

            name = input("Enter item name to delete: ")

            inventory.delete_item(name)



        elif choice == "4":

            inventory.display_items()



        elif choice == "5":

            inventory.low_stock_alert()



        elif choice == "6":

            inventory.expiry_alert()



        elif choice == "7":

            inventory.total_items()



        elif choice == "8":

            inventory.save_data()

            print("Data saved. Exiting program.")

            break



        else:

            print("Invalid choice! Try again.")





if __name__ == "__main__":

    main()