import discord
from multiprocessing import Process
import commands
import config
import tui
import curses
import sys
import time

#Yes, this is an abominable use of discord.py. Do I care? No.
class MyClient(discord.Client):
    async def on_connect(self):
        config.aswho = str(self.user)
        config.loggedin = "Connected"
        tui.mainseq()
        counter = 1
        for i in client.guilds:
            config.chanput[counter] = (str(i))
            counter+=1
        commands.update_chans(config.chanput)
        commands.update_messages()
        guild = discord.utils.get(client.guilds, name=config.currentguild)
        channel = discord.utils.get(guild.text_channels, name=config.currentchan)
        messages = await channel.history(limit=100).flatten()
        for item in messages:
            config.output.append(str(item.author)+" "+str(item.content))
        commands.update_messages()

        #Guess what this function does.
        def check_command(command):
            #empty input does nothing
            if command == "":
                return
            #command to load a guild adn channel
            elif command == "/load" or command == "/l":
                tui.main_window()
                commands.clear_out(tui.input_window)
                commands.update_chans(config.chanput)
                out = commands.usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "$")
                if out == "/exit" or out == "/e":
                    return
                elif out =="":
                    1+1
                else:
                    choice = config.chanput.get(int(out))
                    config.currentguild = choice
                    guild = discord.utils.get(client.guilds, name=choice)
                    config.chatput = {}
                    commands.clear_out(tui.chat_window)
                    counter = 1
                    for i in guild.text_channels:
                        config.chatput[counter] = (str(i))
                        counter+=1
                    commands.update_chans(config.chatput)
                    tui.main_window()
                    commands.clear_out(tui.input_window)
                    chan = commands.usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "$")
                    if chan == "/exit" or chan == "/e":
                        commands.clear_out(tui.input_window)
                        commands.update_chans(config.chanput)
                        return
                    chanchoice = config.chanput.get(int(chan))
                    config.currentchan = chanchoice
                    commands.update_chans(config.chanput)

            #Help command to list options, find them in the config.py
            elif command == "/help" or command == "/h":
                count = 0
                config.output.append("["+time.ctime()+"] Help Menu:")
                for items in config.commandlist:
                    config.output.append(config.commandlist[count])
                    count+=1
            #Catches command exceptions, don't remove!
            else:
                return
            commands.update_messages()

        def messagein():
            while True:
                tui.main_window()
                msginput = commands.usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "#")
                tui.input_window.refresh()
                comm = check_command(msginput)
                tui.input_window.erase()
                if msginput == "/quit" or msginput == "/q":
                    sys.exit(0)
                    break
        recieving = Process(target = messagein)
        recieving.start()

    async def on_message(e, message):
        guild = discord.utils.get(client.guilds, name=config.currentguild)
        channel = discord.utils.get(guild.text_channels, name=config.currentchan)
        messages = await channel.history(limit=100).flatten()
        if message.channel == config.currentchan:
            commands.clear_out(tui.msg_window)
            for item in messages:
                config.output.append(str(item.author)+" "+str(item.content))
            commands.update_messages()

client = MyClient()
client.run("Mzg3MzIxNTQ1NzI4NDU4NzU4.Xtq5ig.M2jhvjpNPEvTiXxxb8uAzVE3G-I")
