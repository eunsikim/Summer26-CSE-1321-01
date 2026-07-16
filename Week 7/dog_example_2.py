import math

class Dog:
    def __init__(self, name, weight):
        self.rabbid = False
        self.name = name
        self.weight = weight
    
    def growl(self):
        print(f"{self.name} says grr")
    
    def eat(self, food):
        self.weight += food

        print(f"{self.name} now weights {self.weight}lbs.")

    # Setter
    def set_name(self, name):
        if name == "Alice":
            print("That name is not valid")
        else:  
            self.name = name
    
    def set_weight(self, weight):
        # Subtract weight
        if weight < 0:
            if self.weight - math.fabs(weight) <= 0:
                print("Invalid weight")
            else:
                self.weight -= math.fabs(weight)
        # Add weight
        else:
            self.weight += weight
    
    def set_rabbid(self, rabbid):
        self.rabbid = rabbid

    # Getter
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_rabbid(self):
        return self.rabbid

def main():
    d1 = Dog("Bob", 10)

    print(d1.get_name())
    
    d1.set_name("Dave")

    print(d1.get_name())

    print(d1.get_weight())

    d1.set_weight(-9.9)

    print(d1.get_weight())

if __name__ == "__main__":
    main()