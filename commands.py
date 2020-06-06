import curses
import config
import time

#resets the user input every time a command is run.
def usr_input(window, r, c, length, prompt):
    curses.echo()
    window.addstr(r, c, prompt)
    choice = window.getstr(r, c + 2, length)
    dec = choice.decode("utf-8")
    return dec

#writes the ouput array in config.py to the main window and then reloads it all, useful for diaplying messages.
def list_out(msg_window, num_rows, input_window):
    outcount = 0
    for items in config.output:
        msg_window.addstr(outcount,2,config.output[outcount])
        while len(config.output) > num_rows -6:
            config.output.pop(1)
        msg_window.refresh()
        input_window.border(0)
        input_window.refresh()
        outcount+=1

#Clears the output, dumbass
def clear_out(msg_window,num_rows, input_window):
    config.output = ["",]
    list_out(msg_window,num_rows, input_window)

#Guess what this function does.
def check_command(command, msg_window, num_rows, input_window):
    #empty input does nothing
    if command == "":
        return

    #Help command to list options, find them in the config.py
    elif command == "help" or command == "h":
        count = 0
        config.output.append("["+time.ctime()+"] Help Menu:")
        for items in config.commandlist:
            config.output.append(config.commandlist[count])
            count+=1

    #Enters send mode, or in vim terms: input mode
    elif command == "send" or command == "s":
        config.sendmode = True
        while True:
            out = usr_input(input_window, 1, 2, 200, "$")
            input_window.clear()
            input_window.border(0)
            input_window.refresh()
            if out == "exit" or out == "e":
                config.output.append("["+time.ctime()+"] Command Mode")
                list_out(msg_window,num_rows,input_window)
                break
            elif out =="":
                1+1

    #Catches command exceptions, don't remove!
    else:
        config.output.append("["+time.ctime()+"] Command '"+command+"' not recognised, please try another.")
    list_out(msg_window, num_rows, input_window)
