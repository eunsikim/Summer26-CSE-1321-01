# You are creating a program for a Point of Sales terminal
# at a fast food restaurant.

# The program should ask the user how many burgers and soda they
# would like to purchase. Then, the program should print a
# receipt showing the number of burgers and soda sold and the total.

# One Burgers costs $5.99 and One Soda costs $2.50

def main():
    burgers = int(input("How many burger(s): "))
    sodas = int(input("How many soda(s): "))

    total = burgers * 5.99 + sodas * 2.50

    print(f"{burgers} Burgers")
    print(f"{sodas} Soda")
    print(f"Total: ${total}")

if __name__ == "__main__":
    main()