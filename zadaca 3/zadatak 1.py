import asyncio
import os

async def afun1(list_param):
    await asyncio.sleep(0.2)
    return [{'naziv': x, 'velicina': (os.path.getsize(x))} for x in list_param]

def fun2(list_param):
    for x in list_param:
        fp = open(x,'w')
        for y in range(1,10000):
            fp.write(str(y)+ " ")
        fp.close()

async def main():
    imena_datoteka = ['datoteka1', 'datoteka2', 'datoteka3']
    for x in imena_datoteka:
        fp = open(x, 'w')
        fp.close()
    var1 = asyncio.create_task(afun1(imena_datoteka))
    fun2(imena_datoteka)
    await var1
    print(var1.result())


if __name__ == '__main__':
    asyncio.run(main())