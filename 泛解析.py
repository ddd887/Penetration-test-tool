import asyncio
import aiodns
import random

loop = asyncio.get_event_loop()
resolver = aiodns.DNSResolver(loop=loop)


async def query(name, query_type):
    return await resolver.query(name, query_type)


def random_to_A(main_domain):
    total = []
    # 随机循环五次
    for i in range(5):
        sub_domain = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(8, 12)))
        res = query(sub_domain + "." + main_domain, 'A')
        result = loop.run_until_complete(res)
        total.append(result)
    return total


if __name__ == '__main__':
    main_domain = input("Please input the main_doamin: ")
    print(str(random_to_A(main_domain)).replace("],", "],\n"))
