import asyncio
import time

async def async_hello_world():
    now = time.time()
    await asyncio.sleep(1)
    print(time.time() - now)
    print("Hello, world1!")
    await asyncio.sleep(1)
    print("Hello, world2!")
    print(time.time() - now)

async def main():
    await asyncio.gather(async_hello_world(), async_hello_world(), async_hello_world())

now = time.time()
# run 3 async_hello_world() coroutine concurrently
asyncio.run(main())