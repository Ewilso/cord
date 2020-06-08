import curses
import config

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()

#colours
curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

#windows
def main_window():
    global chat_window
    global msg_window
    global ticker_window
    global input_window
    global status_window
    chat_window = curses.newwin(num_rows-1, int(num_cols/5), 1, 0)
    chat_window.border(0)
    msg_window = curses.newwin(int(num_rows-4), int(num_cols/5*4-1), 1, int(num_cols-num_cols/5*4))
    msg_window.border(0)
    input_window = curses.newwin(3, int(num_cols/5*4-1), num_rows-3, int(num_cols-num_cols/5*4))
    input_window.border(0)
    status_window = curses.newwin(1, num_cols+2, 0, 0)
    status_window.attron(curses.color_pair(3))
    statusbarstr  = " | {} | Status: {} | Type '/help' to list commands |".format(config.aswho, config.loggedin)
    status_window.addstr(0, 0, statusbarstr)
    status_window.addstr(0, len(statusbarstr), " " * (num_cols - len(statusbarstr) - 1))
    status_window.attroff(curses.color_pair(3))

#main sequence
def mainseq():
    try:
        main_window()
        status_window.refresh()
        msg_window.refresh()
        chat_window.refresh()

    except:
        print("Your window is too small, try again with a larger window")
        curses.endwin()
