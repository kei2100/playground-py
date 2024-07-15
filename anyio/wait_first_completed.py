import functools

import anyio


async def task1():
    await anyio.sleep(2)
    print("task 1 wakeup")
    return "Task 1 completed"


async def task2():
    await anyio.sleep(1)
    print("task 2 wakeup")
    return "Task 2 completed"


async def task3():
    await anyio.sleep(3)
    print("task 3 wakeup")
    return "Task 3 completed"


async def main():
    async def run_and_capture(task_func, result_holder, task_group):
        result_holder.append(await task_func())
        task_group.cancel_scope.cancel()

    results = []
    async with anyio.create_task_group() as task_group:
        task_group.start_soon(functools.partial(run_and_capture, task1, results, task_group))
        task_group.start_soon(functools.partial(run_and_capture, task2, results, task_group))
        task_group.start_soon(functools.partial(run_and_capture, task3, results, task_group))

    print(results[0])  # 最初に完了したタスクの結果を表示
    await anyio.sleep(5)


anyio.run(main)
