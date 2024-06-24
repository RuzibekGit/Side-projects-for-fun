
import time
import os



memo = {1: 0, 2: 0, 3: 0, 
        4: 0, 5: 1, 6: 0, 
        7: 1, 8: 0, 9: 2}

x = ["  \    /  ", "    \/    ", "    /\    ", "  /    \  "]
o = ["  .----.  ", " /      \ ", " \      / ", "  '----'  "]

display = [x,o]

def gui_for_terminal(memo, position, X_or_O, time_com):
    str_print = "\n-------- Tic-Tac-Toe! ---------\n\n"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    memo[position] = X_or_O

    space = 5
    betw = space * 2

    count = 0
    row = 0
    
    


    for i in range(1, space * 3):
        hor, ver = " ", "|"

        if i % space == 0:
            hor, ver = "-", "+"
            row += 3
            count = -1

        col = 3
        count_col = -1
        for j in range(1, (betw+1) * 3):
            if j % (betw+1) == 0:
                col -= 1
                count_col = -1
                str_print += ver
            else:
                str_print += display[memo[10-(row+col)]-1][count][count_col] if memo[10-(row+col)] and i % space != 0 else hor
                pass
            count_col += 1
        count += 1 
        str_print += '\n'
    str_print += "\n"+"_"*32+"\n\n"
    if X_or_O:
        str_print += f"Previous:  position({position})  player({'X' if X_or_O!=2 else 'O'})\n"
    else:
        str_print += f"Previous:  position({position})  --------\n"
    str_print += "Player(X)'s turn \n"if X_or_O==2 else "Player(O)'s turn \n"

    t = int(time_com//3.3)
    str_print += f"\nTest is {time_com}% completed\n+-{'-'*30}-+\n| {'#'*t}{' '*(30-t)} |\n+-{'-'*30}-+\n"
    print(str_print, end='\r')
   

    return memo



def assembly():
    display = [""]*70
    ver = [20,22,24,45,47,49]
    plus = [21,23,46,48]
    memo_pos = {key + 1: [val + 5 * i for i in range(4)] for key, val in enumerate([50, 52, 54, 25, 27, 29, 0, 2, 4])}
    memo = set()
    for i in memo_pos.values():
        for j in i:
            memo.add(j)

    for pos in range(70):
        next = ""
        if (pos+1)%5 == 0: next = "\n"
        if pos in memo:
            display[pos] = "          "+next
        elif pos in ver:
            display[pos] = "----------"+next
        elif pos in plus:
            display[pos] = "+"
        else: display[pos] = "|"
        
    return display, memo_pos


def gui_for_terminal_1(memo,assembly,  time_com):

    display, memo_pos = assembly
    for i, v in memo.items():
        if v:
            x_or_o = x if v==1 else o
            for ind, pos in enumerate(memo_pos[i]):
                next = ""
                if (pos+1)%5 == 0: next = "\n"

                display[pos] = x_or_o[ind]+next

    s = "".join(display)
    s += f"\n{'-'*32}\n"
    # os.system('cls' if os.name == 'nt' else 'clear')

    print(s)
    print("\r")
