import asyncio
import random

async def download_file(name):
    total_chunks = random.randint(3, 6)  # each file has 3–6 chunks
    for i in range(1, total_chunks + 1):
        await asyncio.sleep(random.uniform(0.5, 1.5))  # simulate variable network speed
        print(f"{name}: downloaded chunk {i}/{total_chunks}")
    return f"{name} finished downloading!\n"

async def main():
    tasks = [asyncio.create_task(download_file(f"File {i}")) for i in range(1,10)]
    print("Processing results as they complete...\n")
    for completed_task in asyncio.as_completed(tasks):
        done = await completed_task
        print("->", done)
    
asyncio.run(main())
