
import asyncio

async def fx():
	print("This is ")
	await asyncio.sleep(1)
	print("asynchronous programming")
	await asyncio.sleep(1)
	print("and this is not multi-threading Single Thread")


asyncio.run(fx())

