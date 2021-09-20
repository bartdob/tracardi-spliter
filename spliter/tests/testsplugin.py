import asyncio

from spliter.plugin import SpliterAction

init = dict(
    message='dev, sopp, dev',
    dot=',',
)

payload = {}


async def main():
    plugin = SpliterAction(**init)
    result = await plugin.run(payload)
    print(result)


asyncio.run(main())