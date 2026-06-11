def main():
    parent_counter = 0

    while parent_counter < 3:
        child_counter = 0

        print(f"This is iteration #{parent_counter}")

        while child_counter < 2:
            if child_counter == 1:
                # Break statement will only break
                # the loop it is currently inside
                break

            print(f"\tThis is sub-iteration #{child_counter}")
            child_counter += 1

        parent_counter += 1
        print()


if __name__ == "__main__":
    main()