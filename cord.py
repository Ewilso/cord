import discord
from multiprocessing import Process
import commands
import config
import tui
import curses

#Yes, this is an abominable use of discord.py. Do I care? No.
class MyClient(discord.Client):
    async def on_connect(self):
        config.aswho = str(self.user)
        config.loggedin = "Connected"
        tui.mainseq()
        commands.update_messages(tui.msg_window, tui.num_rows, tui.input_window)
        guild = discord.utils.get(client.guilds, name=config.currentguild)
        channel = discord.utils.get(guild.text_channels, name=config.currentchan)
        messages = await channel.history(limit=100).flatten()
        for item in messages:
            config.output.append(str(item.author)+" "+str(item.content))
        commands.update_messages(tui.msg_window, tui.num_rows, tui.input_window)

        def messagein():
            while True:
                tui.main_window()
                msginput = commands.usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "#")
                tui.input_window.refresh()
                comm = commands.check_command(msginput, tui.msg_window, tui.num_rows, tui.input_window)
                tui.input_window.erase()
                if msginput == "quit" or msginput == "q":
                    curses.endwin()
                    break

        recieving = Process(target = messagein)
        recieving.start()

    async def on_message(e, message):
        guild = discord.utils.get(client.guilds, name=config.currentguild)
        channel = discord.utils.get(guild.text_channels, name=config.currentchan)
        messages = await channel.history(limit=100).flatten()
        #if message.channel == config.currentchan:
        commands.clear_out(tui.msg_window)
        for item in messages:
            config.output.append(str(item.author)+" "+str(item.content))
        commands.update_messages(tui.msg_window, tui.num_rows, tui.input_window)

client = MyClient()
client.run("Mzg3MzIxNTQ1NzI4NDU4NzU4.Xtq5ig.M2jhvjpNPEvTiXxxb8uAzVE3G-I")
