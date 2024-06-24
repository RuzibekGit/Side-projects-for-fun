
import time
import os



memo = {1: 0, 2: 0, 3: 0, 
        4: 0, 5: 0, 6: 0, 
        7: 0, 8: 0, 9: 0}

x = ["  \    /  ", "    \/    ", "    /\    ", "  /    \  "]
o = ["  .----.  ", " /      \ ", " \      / ", "  '----'  "]

display = [x,o]

def gui_for_terminal(memo, position, X_or_O, time_com):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n-------- Tic-Tac-Toe! ---------\n")
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
                print(ver, end="")
            else:
                print(display[memo[10-(row+col)]-1][count][count_col] if memo[10-(row+col)] and i % space != 0 else hor, end = "")
                pass
            count_col += 1
        count += 1 
        print()

    print("\n"+"_"*32+"\n")
    if X_or_O:
        print(f"Previous:  position({position})  player({'X' if X_or_O!=2 else 'O'})")
    else:
        print(f"Previous:  position({position})  --------")

    print("Player(X)'s turn "if X_or_O==2 else "Player(O)'s turn ")
    t = int(time_com//3.3)
    print(f"Test is {time_com}% completed")
    print(f"+-{'-'*30}-+")
    print(f"| {'#'*t}{' '*(30-t)} |")
    print(f"+-{'-'*30}-+")

    return memo


