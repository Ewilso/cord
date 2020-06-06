import discord
import threading
import time
import commands
import config
import tui
import curses

#Yes, this is an abominable use of discord.py. Do I care? No. I'll take standard
#procedural progrmming anyday over weird ass async and await
class MyClient(discord.Client):
    async def on_connect(self):
        tui.mainseq()
        config.output.append("["+time.ctime()+"] Logged in as "+str(self.user))
        config.output.append("["+time.ctime()+"] Fetching Messages...")
        commands.list_out(tui.msg_window, tui.num_rows, tui.input_window)
        #for i in client.guilds:
        #    print(i)
        #nameguild = input("Jump to a guild: ")
        guild = discord.utils.get(client.guilds, name=config.currentguild)
        #for i in guild.channels:
        #    print(i)
        #namechan = input("Jump to a channel: ")
        channel = discord.utils.get(guild.text_channels, name=config.currentchan)
        time.sleep(1)
        while True:
            tui.main_window()
            messages = await channel.history(limit=100).flatten()
            for message in messages[::-1]:
                #str(message.created_at)+" "+str(message.author)+" "+
                config.output.append(str(message.content))
            commands.list_out(tui.msg_window, tui.num_rows, tui.input_window)
            time.sleep(1)

        def messageout():
            while True:
                tui.input_window.refresh()
                msginput = commands.usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "#")
                tui.input_window.refresh()
                tui.input_window.clear()
                comm = commands.check_command(msginput, tui.msg_window, tui.num_rows, tui.input_window)
                if msginput == "quit" or msginput == "q":
                    curses.endwin()
                    break

client = MyClient()
client.run("Mzg3MzIxNTQ1NzI4NDU4NzU4.Xtq5ig.M2jhvjpNPEvTiXxxb8uAzVE3G-I")
