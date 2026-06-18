# n1...n4 are required parameters: You have to pass these values at fn. call
# n5 is a optional parameter.
# Optional parameters must be placed after the required parameters.
def average_of_five(n1, n2, n3, n4, n5=50):
    sum = n1 + n2 + n3 + n4 + n5
    average = sum/5
    return average

def main():
    print(average_of_five(100, 100, 100, 100, 100)) # n5 gets the value 100
    print(average_of_five(100, 100, 100, 100)) # n5 gets the default value 50

if __name__ == "__main__":
    main()