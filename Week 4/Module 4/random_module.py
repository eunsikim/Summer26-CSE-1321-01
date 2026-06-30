import random

def main():
    random.seed(123)

    for x in range(10):
        print(random.randint(1, 10)) #Start and Stop are inclusive
        print(random.randrange(1, 11, 2)) #Stop is exclusive

    print()
    
    for x in range(10):
        print(random.choice("Hello World"))

if __name__ == "__main__":
    main()