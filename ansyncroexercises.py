import asyncio

#Exercise 1: Two Tasks
async def task1():
    await asyncio.sleep(3)
    print('task 1 done')

async def task2():
    await asyncio.sleep(1)
    print('task 2 done')

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())


#Exercise 2: Timer Countdown

async def timer1():
    for i in range(3):
        print(f"timer 1 is {3-i}")
        await asyncio.sleep(1)

async def timer2():
    for i in range(4):
        print(f"timer 2 is {4-i}")
        await asyncio.sleep(1)

async def timer3():
    for i in range(5):
        print(f"timer 3 is {5-i}")
        await asyncio.sleep(1)

async def timercounter():
    await asyncio.gather(timer1(), timer2(), timer3())

asyncio.run(timercounter())

#Exercise 3: File Download Simulation
import random
async def file1(name):
    total_chunks = random.randint(3,6)
    for i in range(1,total_chunks+1):
        await asyncio.sleep(random.uniform(0.5,1.5))
        print(f"{name} downloading chunk {i}/{total_chunks}......")
    print(f"{name} downloading chunk {i}/{total_chunks}......")


async def downloader():
    await asyncio.gather(
        file1("kabhi.mp3"),
        file1("myword1.pdf"),
        file1("assg1.zip"),
        file1("kabhi.mp3"),
        file1("myword4.pdf"),
        file1("assg2.zip"),
        file1("kabh22i.mp3"),
        file1("myword.pdf"),
        file1("assg3.zip"),
        file1("kabhi1131.mp3")
        )

asyncio.run(downloader())