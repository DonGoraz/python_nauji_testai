import threading


def iterate_print(iter):
    # A function prints the elements of a list
    for item in iter:
        print(item)


if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=iterate_print, args=(range(5000),))  # writing out successive natural numbers
    t2 = threading.Thread(target=iterate_print, args=("Python",))  # writing the characters of the string

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    t1.join()
    t2.join()

    print("Done!")