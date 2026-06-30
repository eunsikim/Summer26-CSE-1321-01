import os

def main():
    print(os.getcwd())

    print(os.listdir(os.getcwd()))

    os.mkdir(os.getcwd() + "/Week 4/Module 4/os_module_test_1")

    os.mkdir("os_module_test_2")
    
if __name__ == "__main__":
    main()