import asyncio
import time

async def func1():
    print(f"Task func 1 start")
    await asyncio.sleep(1)
    print(f"Task func 1 end")

async def func2():
    print(f"Task func 2 start")
    await asyncio.sleep(1)
    print(f"Task func 2 end")

async def main():
    print(f"Creating func 1 task")
    # task1 = asyncio.create_task(func1())
    await func1()
    await asyncio.sleep(1)
    print(f"Creating func 2 task")
    task2 = asyncio.create_task(func2())
    await task2

if __name__ == "__main__":
    asyncio.run(main())
    