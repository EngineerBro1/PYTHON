# AsyncIO, also known as asynchronous I/O, is a library in Python that provides a way to write concurrent code using the async and await syntax introduced in Python 3.5. It allows you to write asynchronous, non-blocking code, which is particularly useful for I/O-bound tasks such as network communication or disk I/O.

# Coroutine Functions:
# AsyncIO revolves around the concept of coroutine functions, which are defined using the async keyword. Inside coroutine functions, you can use the await keyword to suspend execution until an asynchronous operation completes.

# import asyncio
# async def Hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("Hello")
# asyncio.run(Hello())


# Event Loop:
# AsyncIO programs typically run inside an event loop, which is responsible for scheduling and executing coroutine functions. You can create an event loop using asyncio.get_event_loop() and run coroutine functions using loop.run_until_complete() or asyncio.run().

# import asyncio
# async def Hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("World")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(Hello())


# Asynchronous I/O Operations:
# AsyncIO provides various utility functions for performing asynchronous I/O operations, such as asyncio.sleep() for delaying execution, asyncio.open_connection() for opening network connections, and asyncio.open() for reading and writing files asynchronously


# Concurrency and Parallelism:
# AsyncIO enables concurrency by allowing multiple tasks to run concurrently within a single thread. However, it does not provide true parallelism by itself. To achieve parallelism, you can run multiple event loops in separate threads or processes using libraries like asyncio.run_in_executor() or concurrent.futures.


import asyncio
async def factorial(n):
    result = 1
    for x in range(1,n+1):
        result *= x
        await asyncio.sleep(2)
    return result
loop = asyncio.get_event_loop()
tasks = [factorial(5),factorial(7),factorial(10)]
results = loop.run_until_complete(asyncio.gather(*tasks))
print(results)