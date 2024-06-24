import gui
from gui import gui_for_terminal
from time import sleep
from random import randint
import os

import time


def speedometer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        return result
    return wrapper


def check_win_or_lost(memo, time_com) -> int:
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
                for i in range(5):
                    x = maybe[0] if i % 2 == 0 else 0
                    for pos in position:
                        memo[pos] = x
                    gui_for_terminal(memo, pos, x, time_com)

                    # sleep(0.1)
                # ------------------------------------
                return maybe[0]

    return 0

# @speedometer
def starter(time_com):
    
    memo = {1: 0, 2: 0, 3: 0, 
            4: 0, 5: 0, 6: 0, 
            7: 0, 8: 0, 9: 0}
    
    while True:
        # player = [int(input("Enter the position: ")), int(input("Enter the player: "))]
        # memo = gui_for_terminal(player[0], player[1])

        gui_for_terminal(memo, randint(1,9), randint(1,2), time_com)

        if (winner := check_win_or_lost(memo, time_com)):
            print(f"Winner is {'X' if winner == 1 else 'O'}")
           
            return winner
        # sleep(0.2)




def test_bench(times):
    win = [0]*times
    average = [0]*times
    t = times/100
    for i in range(times):
        time_com = round((i+1)/t, 2)
        start_time = time.time()
        s = starter(time_com)
        end_time = time.time()
        elapsed_time = end_time - start_time
        average[i] = elapsed_time
        win[i] = s

        

    X = round(win.count(1)/t,3)
    O = round(win.count(2)/t,3)
    print(f"\nWin rate : \nX = {X}%,  \nO = {O}% ")
    print(f"Average time is {round(sum(average)/times,3)} seconds")


# starter()
test_bench(57)