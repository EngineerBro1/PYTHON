# Multithreading in Python allows you to execute multiple threads (units of execution) concurrently within the same process. It's particularly useful for I/O-bound tasks where the program spends most of its time waiting for input/output operations to complete, such as network communication, file I/O, or database access. However, due to Python's Global Interpreter Lock (GIL), multithreading does not provide true parallelism for CPU-bound tasks, where the program spends most of its time performing computations.


# Using the threading Module:
# Python's threading module provides a high-level interface for working with threads. You can create and manage threads using the Thread class and its methods.


import threading
def numbers():
    for x in range(10):
        print(x)

#creating thread and start
thread = threading.Thread(target=numbers)
thread.start()
thread.join()
print("Thread Execution is Complete")



# Passing Arguments to Threads:
# You can pass arguments to the target function of a thread using the args parameter.


import threading
def Greet(Name):
    print(f"Hello,{Name}")

# creating thread and start
thread = threading.Thread(target=Greet,args=("Hari",))
thread.start()



# Synchronization with Locks:
# To prevent race conditions and ensure thread safety when accessing shared resources, you can use locks (also known as mutexes) from the threading module.


import threading

counter = 0
def increment():
    global counter
    for _ in range(5000000):
        with lock:
            counter +=1

lock = threading.Lock()

# creating threading and start
thread = [threading.Thread(target=increment) for _ in range(20)]
for threads in thread:
    threads.start()
for threads in thread:
    threads.join()

print("Counter Value",counter)


# Thread Pooling:
# Using a thread pool can be more efficient than creating and managing individual threads, especially for applications with a large number of short-lived tasks. Python's concurrent.futures.ThreadPoolExecutor provides a high-level interface for thread pooling.


import concurrent.futures

def Task(Name):
    return  f"Task{Name} Completed"
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    result = [executor.submit(Task,i) for i in range(10)]
    for future in concurrent.futures.as_completed(result):
        print(future.result())

