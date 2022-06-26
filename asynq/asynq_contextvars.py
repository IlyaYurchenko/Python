import asyncio
from contextvars import ContextVar

myCounter = ContextVar('counter', default=-0)


async def increase():
    my_counter = myCounter.get()

    my_counter += 1
    myCounter.set(my_counter)


async def count():
    while True:
        await increase()
        my_counter = myCounter.get()
        print(f"Счетчик: {my_counter}")

        await asyncio.sleep(1/10)


asyncio.run(count())