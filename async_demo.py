import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} started at : {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at : {timer()}')

async def main():
    start = timer()
    await asyncio.gather(
        run_task('task 1', 2),
        run_task('task 2', 1),
        run_task('task 3', 3)
    )

    print(f"\ntotal time taken {timer() - start: .2f} seconds")

asyncio.run(main())