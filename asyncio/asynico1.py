import asyncio

async def user_inout(name):
    responce = await asyncio.to_thread(input, f"{name} typing something")
    print(f"{name} you typed {responce}")

async def download(name,delay):
    print(f"{name} start downloading")
    await asyncio.sleep(delay)
    print(f"{name} finished downloading")

async def other_process(name, delay):
    print(f"{name} start opening")
    await asyncio.sleep(delay)
    print(f"{name} opened")


async def main():
    tasks = [
        user_inout('shery'),
        user_inout('Raza'),
        user_inout('hamid'),
        download('Fifa 16', 10),mlk
        download('Gta 6', 15),
        other_process('Gta 6', 15),
        other_process('Fifa 16', 5)
        ]

    await asyncio.gather(*tasks)

asyncio.run(main())