#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
from os import system
import curses
from doubam_token import *
import locale #中文输出
#---------------------------------------------------------------------------
locale.setlocale(locale.LC_ALL,"")
def get_param(prompt_string):
    screen.clear()
    screen.border(1)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""

douban = Doubanfm('', '')
douban.login()

screen = curses.initscr()
screen.clear()
screen.border(0)
screen.addstr(2, 2, douban.user_name)
x = screen.getch()


x = 0

while x != ord('5'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - 频道")
    screen.addstr(5, 4, "2 - 喜欢这首歌")
    screen.addstr(6, 4, "3 - 不再播放")
    screen.addstr(7, 4, "4 - 下一首")
    screen.addstr(8, 4, "5 - 退出")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        shell = get_param("Enter the shell, eg /bin/bash:")
        curses.endwin()
        execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
    if x == ord('2'):
        curses.endwin()
        execute_cmd("apachectl restart")
    if x == ord('3'):
        curses.endwin()
        execute_cmd("df -h")
    if x == ord('4'):
        curses.endwin()

curses.endwin()
