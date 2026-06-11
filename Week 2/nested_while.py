import time

def main():
    parent_counter = 0

    while parent_counter < 3:
        child_counter = 0

        print(f"This is iteration #{parent_counter}")

        while child_counter < 2:
            print(f"\tThis is sub-iteration #{child_counter}")
            child_counter += 1
            time.sleep(2)

        parent_counter += 1
        print()
        time.sleep(2)


if __name__ == "__main__":
    main()