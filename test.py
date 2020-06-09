import discord
from multiprocessing import Process
import time
import curses

#Yes, this is an abominable use of discord.py. Do I care? No.
class MyClient(discord.Client):
    async def on_connect(self):

        for i in client.guilds.channels:
            print(i)

client = MyClient()
client.run("Mzg3MzIxNTQ1NzI4NDU4NzU4.Xtq5ig.M2jhvjpNPEvTiXxxb8uAzVE3G-I")
