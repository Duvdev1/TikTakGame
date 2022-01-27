import tkinter as tk
import random as r

print("instructions for tic tac game: \n" 
      "if the computer is a player hit the button for the computer turn and please wait 1 sec "
      "before press the button between each turn if both players are computer, please noted after choosing players watch bellow on screen to see the file, it is usually minimized")
player1 = int(input('who is the first player? 1 for person, 2 for computer'))
player2 = int(input('who is the second player? 1 for person, 2 for computer'))

root = tk.Tk()
root.title("Welcome To Tic Tac Game")  # define game title
root.geometry("800x800")  # define size of the gui
turn = 0  # whos turn
x = 0
y = 0
row = 0  # rows
col = 0  # column
apn = 0  # index of column and lines
draw = 0  # tie define
btn = []
btn_text = []
Xgame = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Ygame = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
not_empty_cells = []

while apn <= 9:
    btn.append(' ')
    btn_text.append('')
    btn_text[apn] = tk.StringVar()
    apn = apn + 1


def play_random():
    while True:
        num = r.randint(0, 9)
        if num not in not_empty_cells:
            return num


def add_to_player_array(player_list, y):
    if 0 <= y <= 2:
        player_list[0][int(y / 1)] = 1
    elif 3 <= y <= 5:
        player_list[1][y - 3] = 1
    elif 6 <= y <= 8:
        player_list[2][y - 6] = 1


def make3DarrayX(y):  #
    add_to_player_array(Xgame, y)


def make3DarrayY(y):
    add_to_player_array(Ygame, y)


def checkifXwon():
    global draw
    draw = draw + 1
    y = 0
    x = 0
    while y < 3:
        while x < 3:
            if Xgame[y][0] == 1 and Xgame[y][1] == 1 and Xgame[y][2] == 1:
                label = tk.Label(root, text="X won")
                label.grid(row=9, column=0)
            if Xgame[0][y] == 1 and Xgame[1][y] == 1 and Xgame[2][y] == 1:
                label = tk.Label(root, text="X won")
                label.grid(row=9, column=0)
            if Xgame[0][0] == 1 and Xgame[1][1] == 1 and Xgame[2][2] == 1:
                label = tk.Label(root, text="X won")
                label.grid(row=9, column=0)
            if Xgame[0][2] == 1 and Xgame[1][1] == 1 and Xgame[2][0] == 1:
                label = tk.Label(root, text="X won")
                label.grid(row=9, column=0)
            x = x + 1
        if draw == 9:
            label = tk.Label(root, text="DRAW")
            label.grid(row=9, column=0)
            return 0
        x = 0
        y = y + 1


def checkifYwon():
    global draw
    draw = draw + 1
    y = 0
    x = 0
    while y < 3:
        while x < 3:
            if Ygame[y][0] == 1 and Ygame[y][1] == 1 and Ygame[y][2] == 1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9, column=0)
            if Ygame[0][y] == 1 and Ygame[1][y] == 1 and Ygame[2][y] == 1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9, column=0)
            if Ygame[0][0] == 1 and Ygame[1][1] == 1 and Ygame[2][2] == 1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9, column=0)
            if Ygame[0][2] == 1 and Ygame[1][1] == 1 and Ygame[2][0] == 1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9, column=0)
            x = x + 1
        if draw == 9:
            label = tk.Label(root, text="DRAW")
            label.grid(row=9, column=0)
        x = 0
        y = y + 1


def update_btn_text(y):
    print("y = ", y)
    global turn
    global Xgame
    global Ygame
    turn = turn + 1
    if turn % 2 == 1:
        if player1 == 2:
            y = play_random()
            btn_text[y].set("X")
            make3DarrayX(y)
            checkifXwon()
            not_empty_cells.append(y)
        else:
            not_empty_cells.append(y)
            btn_text[y].set("X")
            make3DarrayX(y)
            checkifXwon()

    if turn % 2 == 0:
        if player2 == 2:
            y = play_random()
            btn_text[y].set("O")
            make3DarrayY(y)
            checkifYwon()
            not_empty_cells.append(y)

        else:
            btn_text[y].set("O")
            make3DarrayY(y)
            checkifYwon()
            not_empty_cells.append(y)


item = 0
while y < 9:
    btn[y] = tk.Button(root, text=item, textvariable=btn_text[y], command=lambda s=item: update_btn_text(s), height=9,
                       width=18)
    btn_text[y].set('')
    item = item + 1
    y = y + 1
item += 1
btn[9] = tk.Button(root, text="Hit for computer turn", command=lambda s=item: update_btn_text(s), height=18,
                   width=30)
btn[9].grid(row=12, column=12, sticky='nesw')
# btn[x].grid(row=10, column=10, sticky='nesw')
while row < 3:
    while col < 3:
        btn[x].grid(row=row, column=col, sticky='nesw')
        col = col + 1
        x = x + 1
    col = 0
    row = row + 1
label = tk.Label(root, text="")
label.grid(row=9, column=0)
root.mainloop()
