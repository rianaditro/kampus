import asyncio
import time
def count(name):
    print(f'{name}_1')
    time.sleep(1)
    print(f'{name}_2')
    time.sleep(1)
    print(f'{name}_3')

def all_count():
    count("first")
    count("second")
    count("third")

async def acount(name):
    print(f'{name}_1')
    await asyncio.sleep(1)
    print(f'{name}_2')
    await asyncio.sleep(1)
    print(f'{name}_3')

async def amain():
    await asyncio.gather(acount("first"), acount("second"), acount("third"))

if __name__ == "__main__":
    # all_count()
    asyncio.run(amain())