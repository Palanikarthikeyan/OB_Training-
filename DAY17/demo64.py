import asyncio
async def task1():
    await asyncio.sleep(2)
    
async def task2():
    await asyncio.sleep(2)
'''
async def main():  # Sequential 
    await task1()
    await task2()
    
asyncio.run(main())
'''
async def main():  # Concurrent Fast 
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    
    await t1
    await t2
    
asyncio.run(main())