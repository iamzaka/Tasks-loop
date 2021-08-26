import discord
from discord.ext import commands, tasks

@tasks.loop(seconds = 40) #초단위
async def test():
    print("ㅁㄴㅇㄹ")

test.start()
