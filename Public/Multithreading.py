# This code demonstrates how to use Python's threading
# module to calculate the square and cube of a number
# concurrently. Two threads, t1 and t2 , are created to
# perform these calculations. They are started, and their
# results are printed in parallel before the program prints
# "Done!" when both threads have finished. Threading is
# used to achieve parallelism and improve program
# performance when dealing with computationally intensive
# tasks.


import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")