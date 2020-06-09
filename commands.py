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

#funky little function to deal with multi line messages and outputting messages clearly
def update_messages(msg_window, num_rows, input_window):
    outcount = 0
    lineno = int(num_rows - 5)
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
                msg_window.addstr(lineno,2,config.output[outcount][lower*limit:upper])
                limitcounter +=1
                lineno +=1
            lineno -= 3
            outcount += 1
        else:
            msg_window.addstr(lineno,2,config.output[outcount])
            lineno-=1
            outcount+=1
        msg_window.refresh()

#Clears the output, dumbass. Needs work
def clear_out(msg_window):
    config.output = [""]
    msg_window.erase()
    msg_window.border(0)
    msg_window.refresh()

#Guess what this function does.
def check_command(command, msg_window, num_rows, input_window):
    #empty input does nothing
    if command == "":
        return

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
    update_messages(msg_window, num_rows, input_window)
