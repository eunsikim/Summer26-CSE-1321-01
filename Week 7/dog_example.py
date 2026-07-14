class Dog:
    rabid = False
    weight = 10
    name = "Scrappy"

    def growl(self):
        print(f"{self.name} says grr")
    
    def eat(self, food):
        self.weight += food

        print(f"{self.name} now weights {self.weight}lbs.")

def main():
    d1 = Dog()
    d1.name = "Alice"
    d1.weight = 5.0
    d1.rabid = False

    print(f"{d1.name} is a dog.")

    d2 = Dog()
    d2.name = "Bob"
    print(f"{d2.name} is a dog.")

    d3 = Dog()

    print(f"The Dog class weighs {Dog.weight}lbs")
    print(f"{d1.name} weighs {d1.weight}lbs")
    print(f"{d2.name} weighs {d2.weight}lbs")
    print(f"{d3.name} weighs {d3.weight}lbs")

    print("\nChanging Dog class weight attribute...\n")
    Dog.weight = 20

    print(f"The Dog class weighs {Dog.weight}lbs")
    print(f"{d1.name} weighs {d1.weight}lbs")
    print(f"{d2.name} weighs {d2.weight}lbs")
    print(f"{d3.name} weighs {d3.weight}lbs")

    print(f"d3 is called {d3.name}")
    print(f"The Dog class is called {Dog.name}")

if __name__ == "__main__":
    main()