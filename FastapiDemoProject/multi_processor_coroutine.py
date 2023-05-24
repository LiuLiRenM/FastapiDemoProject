import asyncio
import multiprocessing


async def coroutine():
    # 这里是具体的协程任务逻辑
    # 在这个示例中，协程只是简单地打印一条消息
    print(f'Coroutine in process {multiprocessing.current_process().pid}')


def worker():
    # 创建一个事件循环
    loop = asyncio.new_event_loop()
    # 将事件循环设置为当前进程的默认事件循环
    asyncio.set_event_loop(loop)

    # 运行协程
    loop.run_until_complete(coroutine())


if __name__ == '__main__':
    # 创建多个进程
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()
