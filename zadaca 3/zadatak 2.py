import asyncio
import numpy
import psutil


async def afunc1():
    data = []
    for x in range(1, 10):
        data_n = numpy.random.normal(loc=0.0, scale=1.0, size=1000000)
        data.append(data_n)
        await asyncio.sleep(0.9)

    return data


async def afunc2():
    return psutil.cpu_percent(10)


async def main():
    var1 = asyncio.create_task(afunc1())
    var2 = asyncio.create_task(afunc2())
    await var1
    await var2
    print(var2.result())


if __name__ == "__main__":
    asyncio.run(main())
