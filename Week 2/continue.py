def main():
    counter = 1
    while counter < 50:
        # Check if the counter value is divisble by 2
        if counter % 2 == 0:
            counter += 1
            # `continue` will prematurely stop the current iteration and jump to the next
            continue
        elif counter == 33:
            break
        else:
            print(counter)

        counter += 1



if __name__ == "__main__":
    main()