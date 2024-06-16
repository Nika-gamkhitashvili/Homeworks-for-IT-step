import asyncio


async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")


async def task2():
    print("Task 2 start")
    await asyncio.sleep(5)
    print("Task 2 end")


async def main():
    await asyncio.gather(task1(), task2())


# Run the main function
asyncio.run(main())

# .................
import asyncio
import random


async def random_delay_task():
    for i in range(1, 11):
        delay = random.uniform(0.5, 1.5)  # Random delay between 0.5 to 1.5 seconds
        await asyncio.sleep(delay)
        print(i)


# Run the random delay task
asyncio.run(random_delay_task())
