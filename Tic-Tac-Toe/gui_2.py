
memo = {1: 0, 2: 0, 3: 0, 
        4: 0, 5: 1, 6: 0, 
        7: 1, 8: 0, 9: 2}

x = ["  \    /  ", "    \/    ", "    /\    ", "  /    \  "]
o = ["  .----.  ", " /      \ ", " \      / ", "  '----'  "]

display = [x,o]

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
            display[pos] = " "*10+next
        elif pos in ver:
            display[pos] = "-"*10+next
        elif pos in plus:
            display[pos] = "+"
        else: display[pos] = "|"
        
    return display, memo_pos


def gui_for_terminal_1(memo, assembly,  time_com):

    # def changer(values): #TODO
    #     for ind, pos in enumerate(memo_pos[i]):
    #         next = ""
    #         if (pos+1) % 5 == 0:
    #             next = "\n"

    #         display[pos] = values+next

    display, memo_pos = assembly
    for i, v in memo.items():
        if v:
            x_or_o = x if v==1 else o
            for ind, pos in enumerate(memo_pos[i]):
                next = ""
                if (pos+1)%5 == 0: next = "\n"

                display[pos] = x_or_o[ind]+next
        else:
            for ind, pos in enumerate(memo_pos[i]):
                next = ""
                if (pos+1) % 5 == 0:
                    next = "\n"

                display[pos] = (" "*10)+next
    s = "\n-------- Tic-Tac-Toe! ---------\n\n"
    s += "".join(display)
    s +=f"\n{'_'*32}\n"
    
    return s



