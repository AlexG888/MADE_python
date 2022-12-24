import sys
import asyncio
import aiohttp


async def fetcher(filename, threads=10):
    queue_urls = asyncio.Queue()
    async with aiohttp.ClientSession() as session:
        try:
            task = asyncio.create_task(_make_queue(filename, queue_urls))
            tasks = [
                asyncio.create_task(_fetch_url(f"w_{t}", session, queue_urls))
                for t in range(threads)
            ]
            await task
            await queue_urls.join()
        except StopAsyncIteration:
            return
        except ...:
            pass

    for task in tasks:
        task.cancel()
    task.cancel()


async def _fetch_url(name, session, queue_urls):
    while True:
        url = await queue_urls.get()
        try:
            async with session.get(url, timeout=4) as resp:
                data = await resp.read()
                print(name, len(data))
        except asyncio.TimeoutError:
            print("Timeout")
        finally:
            queue_urls.task_done()


async def _make_queue(filename, queue_urls):
    try:
        file = open(filename, "r", encoding="utf8")
        for url in file:
            await queue_urls.put(url.rstrip("\n"))
        file.close()
    except FileNotFoundError:
        pass

async def main():
    await fetcher(file_name, N)


if __name__ == "__main__":
    i = 0
    if "-c" in sys.argv:
        i = sys.argv.index("-c")
    N = int(sys.argv[i + 1])
    file_name = sys.argv[i + 2]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
