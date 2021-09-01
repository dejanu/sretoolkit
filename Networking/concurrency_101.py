#!.usr/bin/python3

import aiohttp
import asyncio

# Everything runs on a central event loop - that lets you run several coroutines at once
# Coroutines run in sync until they hit await and pass the function control to the event loop 

import asyncio

async def count():
    print("one")
    # await passes function control back to the event loop
    await asyncio.sleep(1)
    print("two")

# async def is a coroutine -> it may use await/return/yield
async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
