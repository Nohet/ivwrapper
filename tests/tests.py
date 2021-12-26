import asyncio
import ivwrapper

iv = ivwrapper.Api()


async def main():
    joke = await iv.get_joke()
    print(joke)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

