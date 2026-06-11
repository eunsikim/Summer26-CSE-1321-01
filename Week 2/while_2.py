# Re-do in_class_ex_1.py.
# Implement a menu selection:
# 1. Burger
# 2. Soda
# 3. Pay
# 
# Keep adding the total amount for the purchase
# and keep asking the user for items to buy
# until the user decides to pay.

# Show the user the total amount to pay

# One Burgers costs $5.99 and One Soda costs $2.50

def main():
    total = 0

    while True:
        print("Choose an option:")
        print("1. Add a burger $5.99")
        print("2. Add a soda $2.50")
        print("3. Pay and Exit")
        choice = input("> ")

        match choice:
            case "1":
                total += 5.99
            case "2":
                total += 2.50
            case "3":
                print(f"Total Amount: ${total}")
                # The break statement will forcebly STOP the loop
                break
    
    print("[Program Terminated]")
    
    

if __name__ == "__main__":
    main()