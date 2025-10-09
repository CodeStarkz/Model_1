# Ascynchronous


""""
┌────────────────────────────────┐
│        asyncio module          │
├────────────────────────────────┤
│ Basic run methods              │
│ ├─ run()                       │
│ ├─ create_task()               │
│ └─ gather(), wait()            │
│                                │
│ Event loop control             │
│ ├─ get_event_loop()            │
│ ├─ run_until_complete()        │
│ └─ stop(), close()             │
│                                │
│ Task handling                  │
│ ├─ current_task(), all_tasks() │
│ ├─ cancel(), done(), result()  │
│ └─ ensure_future(), shield()   │
│                                │
│ Synchronization primitives     │
│ ├─ Event(), Lock(), Semaphore()│
│ └─ Queue()                     │
└────────────────────────────────┘


"""


import asyncio

async def count(n):
    for i in range(n,10):
        print(i)
        await asyncio.sleep(1)

    for j in range(n,10):
        print(j*200)
        await asyncio.sleep(1)


async def square(m):
    for i in range(m,10):
        print(i**2)




asyncio.run(count(2))
asyncio.run(square(3))



