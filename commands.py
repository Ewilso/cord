import curses
import config
import time
import tui
import math

#resets the user input every time a command is run.
def usr_input(window, r, c, length, prompt):
    curses.echo()
    window.addstr(r, c, prompt)
    choice = window.getstr(r, c + 2, length)
    dec = choice.decode("utf-8")
    return dec

#Get the user's channels and guilds
def update_chans():
    outcount = 0
    for items in config.chanput:
        tui.chat_window.addstr(outcount,2,config.chanput[outcount])
        tui.chat_window.refresh()
        outcount+=1

#funky little function to deal with multi line messages and outputting messages clearly
def update_messages():
    outcount = 0
    lineno = int(tui.num_rows - 5)
    limit = int(tui.num_cols/5*4-4)
    for item in config.output:
        if lineno < 1:
            break
        if len(item) > limit-6:
            msglines = math.ceil(len(item) / limit)
            lineno -= msglines - 1
            limitcounter = 1
            for i in range(msglines):
                lower = limitcounter -1
                upper = limitcounter * limit
                tui.msg_window.addstr(lineno,2,config.output[outcount][lower*limit:upper])
                limitcounter +=1
                lineno +=1
            lineno -= 3
            outcount += 1
        else:
            tui.msg_window.addstr(lineno,2,config.output[outcount])
            lineno-=1
            outcount+=1
        tui.msg_window.refresh()

#Clears the output, dumbass. Needs work
def clear_out(msg_window):
    config.output = [""]
    msg_window.erase()
    msg_window.border(0)
    msg_window.refresh()

#Guess what this function does.
def check_command(command):
    #empty input does nothing
    if command == "":
        return

    #command to load a guild
    elif command == "/load" or command == "/l":
        tui.main_window()
        tui.input_window.erase()
        tui.input_window.border(0)
        tui.input_window.refresh()
        out = usr_input(tui.input_window, 1, 2, int(tui.num_cols/5*4-7), "$")
        if out == "/exit" or out == "/e":
            config.output.append("["+time.ctime()+"] Command Mode")
            update_messages()
            return
        elif out =="":
            1+1

    #Help command to list options, find them in the config.py
    elif command == "/help" or command == "/h":
        count = 0
        config.output.append("["+time.ctime()+"] Help Menu:")
        for items in config.commandlist:
            config.output.append(config.commandlist[count])
            count+=1

    #Catches command exceptions, don't remove!
    else:
        config.output.append("["+time.ctime()+"] Command '"+command+"' not recognised, please try another.")
    update_messages()
