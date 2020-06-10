import curses
import config
import time
import tui
import math
import discord

#resets the user input every time a command is run.
def usr_input(window, r, c, length, prompt):
    curses.echo()
    window.addstr(r, c, prompt)
    choice = window.getstr(r, c + 2, length)
    dec = choice.decode("utf-8")
    return dec

#Get the user's channels and guilds
def update_chans(list):
    outcount = 1
    for item in list:
        tui.chat_window.addstr(outcount,2,str(item)+" "+list[outcount])
        tui.chat_window.refresh()
        outcount+=1
        if outcount > int(tui.num_rows - 3):
            return

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
def clear_out(window):
    window.erase()
    window.border(0)
    window.refresh()
