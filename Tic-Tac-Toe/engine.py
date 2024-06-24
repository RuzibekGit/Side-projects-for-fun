from gui_2 import  gui_for_terminal_1, assembly
from time import sleep
from random import  choice
import os

import time



def check_win_or_draw(memo, assembl, time_com, wining_con=True) -> int:

    win_pos = {
        2: [[1, 2, 3]],
        4: [[1, 4, 7]],
        6: [[3, 6, 9]],
        5: [[4, 5, 6], [2, 5, 8], [1, 5, 9], [3, 5, 7]],
        8: [[7, 8, 9]]
    }

    for best in [pos for pos in win_pos if memo[pos]]:
        for position in win_pos[best]:
            maybe = [memo[pos] for pos in position]
            if len(set(maybe)) == 1:
                # congratulation, blinking figure part
                if wining_con:
                    for i in range(11):
                        x = maybe[0] if i % 2 == 0 else 0
                        for pos in position:
                            memo[pos] = x
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(gui_for_terminal_1(memo, assembl, time_com))
                        print(f"Winner is {'X' if maybe[0] == 1 else 'O'}")

                        sleep(0.1)

                return maybe[0]
                # ------------------------------------
    # draw , blinking figure part
    if 0 not in memo.values():
        if wining_con:
            s = memo.copy()
            for i in range(11):
                for pos in range(1,10):
                    memo[pos] = s[pos] if i % 2 == 0 else 0
                os.system('cls' if os.name == 'nt' else 'clear')
                print(gui_for_terminal_1(memo, assembl, time_com))
                print("Draw!...")

                sleep(0.1)

        return 3
    # -------------------------------------
    return 0

# @speedometer
def starter(time_com, who_start, gui=True, player_mode=False):
    clear_win = 'cls' if os.name == 'nt' else 'clear'
    
    memo = {1: 0, 2: 0, 3: 0, 
            4: 0, 5: 0, 6: 0, 
            7: 0, 8: 0, 9: 0}
    
    assembl = assembly()
    pos = {1,2,3,4,5,6,7,8,9}
    player = who_start

    while True:
        if player_mode and player == player_mode:
            
            r = int(input(f"You have {pos}: "))
        else:
            r = choice(list(pos))
        pos.remove(r)

        memo[r] = player
        player = 1 if player==2 else 2


        if gui:
            os.system(clear_win)

            print(gui_for_terminal_1(memo, assembl, time_com))
            print(f"Previous:  position({r})  player({'X' if player!=2 else 'O'})")
            
            sleep(0.2)

        if (winner := check_win_or_draw(memo,assembl, time_com, wining_con=gui)):
            return winner




def test_bench(times, gui_on, player=False):
    win = [0]*times
    t = times/100
    who_start = 1
    start_time = time.time()
    for i in range(times):
        if who_start == 3: who_start = 1
        time_com = round((i+1)/t, 3)
        s = starter(time_com,who_start, gui=gui_on, player_mode=player)
        win[i] = s
        who_start += 1


        if i%(times/100)==0: 
            print(f"Test is {time_com}% completed", end='\r')

    end_time = time.time()
    elapsed_time = end_time - start_time
    average = elapsed_time/times

        

    X = round(win.count(1)/t,3)
    O = round(win.count(2)/t,3)
    draw = round(win.count(3)/t,3)
    print(f"\nWin rate : \nX = {X}%,  \nO = {O}%, \nDraw = {draw}%")
    print(f"Average time is {round(average*1000,3)} milliseconds")


# starter()
gui_on = int(input("Gui 1 or 0: "))
times = int(input())
if gui_on:
    player = int(input())

test_bench(times, gui_on, player=0)

