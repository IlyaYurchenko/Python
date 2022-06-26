import asyncio
from contextvars import ContextVar

myCounter = ContextVar('counter', default=0)


async def count(counter):
    print(f'Кол-во записей в списке: {len(counter)}')

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_one_second(counter):
    while True:
        await asyncio.sleep(1)
        print(f'---1секунда прошла'
              f'Кол-во записей в списке: {len(counter)}')


async def print_every_five_second():
    while True:
        await asyncio.sleep(1)
        print(f'-----5 секунд прошлo')


async def print_every_ten_second():
    while True:
        await asyncio.sleep(1)
        print(f'--------10секунд прошлo')


async def main():
    counter = list()

    tasks = [
        count(counter),
        print_every_one_second(counter),
        print_every_five_second(),
        print_every_ten_second()
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())