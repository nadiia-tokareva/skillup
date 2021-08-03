import asyncio
from random import randint
from time import sleep



class My_stack:
    def __init__(self):
        self._stack_list = []
    
    def __str__(self) -> str:
        return str(self._stack_list)

    def sleeping(self, value: int):
        try:
            if value < 50:
                sleep(1)
                print('Sleep 1 second')
            if value > 50:
                sleep(1)
                print('Sleep 2 second')
        except ValueError:
            print(f'The {value} is not integer')
   

    
    def push(self, value: int):
        self.sleeping(value)
        self._stack_list.append(value)
            


class As_stack(My_stack):
    async def sleeping(self, value: int):
        try:
            if value < 50:
                await asyncio.sleep(1)
                print('Sleep 1')
            if value > 50:
                await asyncio.sleep(2)
                print('Sleep 2')
            return self._stack_list.append(value)
        except ValueError:
            print(f'The {value} is not integer')
   

    async def push(self, value: int):
        await self.sleeping(value)
        self._stack_list.append(value)
            

stack_1 = My_stack()

numbers = (randint(1, 100) for _ in range(10))
for number in numbers:
    stack_1.push(number)


stack_2 = As_stack()

numbers = (randint(1, 100) for _ in range(10))
loop = asyncio.get_event_loop()
task = [stack_2.push(number) for number in numbers]
loop.run_until_complete(asyncio.gather(*task))
loop.close


print(stack_2)
