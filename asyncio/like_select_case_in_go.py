import asyncio
import time


async def task1():
    print("task 1 sleep")
    await asyncio.sleep(2)
    print("task 1 wakeup")
    return "Task 1 completed"

async def task2():
    print("task 2 sleep")
    await asyncio.sleep(1)
    print("task 2 wakeup")
    return "Task 2 completed"

async def main():
    done1 = asyncio.create_task(task1(), name="task1")
    done2 = asyncio.create_task(task2(), name="task2")

    done, pending = await asyncio.wait(
        [done1, done2], return_when=asyncio.FIRST_COMPLETED
    )

    for task in done:
        print(f"{task.get_name()}: {task.result()}")

    for task in pending:
        task.cancel()
        pass

    await asyncio.sleep(3)
    print("main done")

# イベントループを実行する
asyncio.run(main())
