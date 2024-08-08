class Restaurant:
    def __init__(self):
        self.menu = {
            'Burger': 5.00,
            'Pizza': 8.00,
            'Pasta': 7.00,
            'Salad': 4.00
        }
        self.orders = []
        self.total_sales = 0.0

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        self.display_menu()
        while True:
            order = input("Enter the name of the item you want to order (or type 'done' to finish): ").capitalize()
            if order == "Done":
                break
            if order in self.menu:
                self.orders.append(order)
                self.total_sales += self.menu[order]
                print(f"{order} added to your order.")
            else:
                print("Sorry, we don't have that item.")
            print()
        
    def view_orders(self):
        if self.orders:
            print("Your Orders:")
            for order in self.orders:
                print(order)
        else:
            print("No orders yet.")
    
    def view_total_sales(self):
        print(f"Total Sales: ${self.total_sales:.2f}")

def main():
    restaurant = Restaurant()
    while True:
        print("\nRestaurant Management System")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. View Orders")
        print("4. View Total Sales")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            restaurant.display_menu()
        elif choice == "2":
            restaurant.take_order()
        elif choice == "3":
            restaurant.view_orders()
        elif choice == "4":
            restaurant.view_total_sales()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        print()

if __name__ == "__main__":
    main()

    
            
            
            
                    
                    
                  
                    
          
          
        