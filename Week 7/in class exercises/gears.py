class item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.stock = 0
        # 0 Sporting Goods, 1 Camping Gear, or 2 Inflatables
        self.category = category
    
    def set_price(self, price):
        if price <= 0:
            print("Invalid price value")
        else:
            self.price = price
    
    def set_discount(self, percentage):
        if percentage <= 0 or percentage >= 100:
            print("Invalid discount")
        else:
            self.price = self.price - self.price * percentage / 100
    
    def set_stock(self, stock):
        if stock < 0:
            print("Invalid stock value")
        else:
            self.stock = stock
    
    def add_stock(self, stock):
        self.stock += stock
    
    def subtract_stock(self, stock):
        if stock > self.stock:
            print("Invalid stock value")
        else:
            self.stock -= stock
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return f"${self.price:.2f}"
    
    def get_stock(self):
        return self.stock

    def get_category(self):
        return self.category
    
def main():
    items = []

    while True:
        print("Select an option")
        print("1. Add a new item")
        print("2. Add/Subtract stock")
        print("3. Set discount")
        print("4. Set price")
        print("5. View items")
        print("6. Sell item(s)")
        print("7. Exit")

        option = int(input("> "))

        if option == 1:
            # Ask the user for name, price, and category
            items.append(item("name", 6.89, 2))
        elif option == 2:
            # Print all of the items with their index
            #   You need to make sure you print the name attribute of the object
            # ask the user to select an item in the list
            # how much they want to subtract the stock of the item
            index = int(input())
            stock = float(input())
            amount = int(input())
            if stock > 0:
                items[index].add_stock(amount)
            else:
                item[index].subtract_stock(amount)
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            # You need to make sure you print the name attribute of the object
            for item in items:
                print(item.name)

            # We can also print by the category by adding an if statement to
            # check the object's category attribute
            for item in items:
                if item.category == 0:
                    print(item.name)
        elif option == 6:
            pass
        elif option == 7:
            pass

if __name__ == "__main__":
    main()