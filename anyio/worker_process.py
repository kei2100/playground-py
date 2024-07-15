import functools
import pathlib
import time

import anyio
from anyio import run, to_process


def cpu_intensive_function(arg1, arg2):
    # time.sleep(10)
    pathlib.Path(arg2).touch()
    return arg1 + arg2


async def exec_cpu_intensive_function(arg1: str, arg2: str):
    async with anyio.create_task_group() as tg:
        for i in range(10):
            tg.start_soon(functools.partial(to_process.run_sync, cancellable=True), cpu_intensive_function, arg1, arg2 + str(i))
        # await anyio.sleep(2)
        # print("cancel")
        # tg.cancel_scope.cancel()


async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(functools.partial(exec_cpu_intensive_function, "hello", "world"))
        await anyio.sleep(3)
        tg.start_soon(functools.partial(exec_cpu_intensive_function, "hello", "sekai"))
        await anyio.sleep(3)

    print("done")
    await anyio.sleep(10)



# This check is important when the application uses run_sync_in_process()
if __name__ == '__main__':
    run(main, backend='asyncio')
