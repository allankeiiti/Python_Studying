import asyncio
from time import sleep

async def ping_server(ip):
    pass


@asyncio.coroutine
def load_file(path):
    pass


async def printer():
    for i in range(0, 100):
        print(i)
        sleep(1)


async def printer2():
    for i in range(0, 10):
        print('printer2: ', i)
        sleep(1)
        await printer()

printer()
printer2()
print('TESTE')
