import time

def main():
    epoch = time.time()

    print(time.ctime(epoch))

    for x in range(10):
        print(x)
        time.sleep(0.1)

if __name__ == "__main__":
    main()