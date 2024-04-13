# Multiprocessing in Python allows you to create and manage multiple processes, enabling parallelism and taking advantage of multiple CPU cores. It's especially useful for CPU-bound tasks that require heavy computation or processing.

import multiprocessing
import multiprocessing.pool
def square(num):
    return num*num
if __name__ == "__main__":
    numbers = [1,2,3,4,5,6]

    with multiprocessing.Pool(processes=2) as pool:
        result = pool.map(square,numbers)
    print("Result: ", result)



import multiprocessing
def cube(num):
    print("Cube: {}".format(num*num*num))
def square(num):
    print("Square: {}".format(num*num))
if __name__ == "__main__":
    pro1 = multiprocessing.Process(target=square,args=(11,))
    pro2 = multiprocessing.Process(target=cube,args=(11,))
    pro1.start()
    pro2.start()
    pro1.join()
    pro2.join()
    print("Complete")


