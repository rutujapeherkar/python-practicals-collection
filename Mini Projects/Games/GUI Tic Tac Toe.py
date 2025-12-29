from tkinter import *


def check_1():
    player1=b1.cget("text")
    if player1=="X":
        player1=b2.cget("text")
        if player1=="X":
            player1=b3.cget("text")
            if player1=="X":
                return 1
    player1=b4.cget("text")
    if player1=="X":
        player1 = b5.cget("text")
        if player1=="X":
            player1 = b6.cget("text")
            if player1=="X":
                return 1
    player1 = b7.cget("text")
    if player1=="X":
        player1 = b8.cget("text")
        if player1=="X":
            player1 = b9.cget("text")
            if player1=="X":
                return 1
    player1 = b1.cget("text")
    if player1=="X":
        player1 = b5.cget("text")
        if player1=="X":
            player1 = b9.cget("text")
            if player1=="X":
                return 1
    player1 = b3.cget("text")
    if player1=="X":
        player1 = b5.cget("text")
        if player1=="X":
            player1 = b7.cget("text")
            if player1=="X":
                return 1
    player1 = b1.cget("text")
    if player1=="X":
        player1 = b4.cget("text")
        if player1=="X":
            player1 = b7.cget("text")
            if player1=="X":
                return 1
    player1 = b2.cget("text")
    if player1=="X":
        player1 = b5.cget("text")
        if player1=="X":
            player1 = b8.cget("text")
            if player1=="X":
                return 1
    player1 = b3.cget("text")
    if player1=="X":
        player1 = b6.cget("text")
        if player1=="X":
            player1 = b9.cget("text")
            if player1=="X":
                return 1


def check_2():
    player2=b1.cget("text")
    if player2=="O":
        player2=b2.cget("text")
        if player2=="O":
            player2=b3.cget("text")
            if player2=="O":
                return 1
    player2=b4.cget("text")
    if player2=="O":
        player2= b5.cget("text")
        if player2=="O":
            player2= b6.cget("text")
            if player2=="O":
                return 1
    player2= b7.cget("text")
    if player2=="O":
        player2 = b8.cget("text")
        if player2=="O":
            player2 = b9.cget("text")
            if player2=="O":
                return 1
    player2 = b1.cget("text")
    if player2=="O":
        player2 = b5.cget("text")
        if player2=="O":
            player2 = b9.cget("text")
            if player2=="O":
                return 1
    player2 = b3.cget("text")
    if player2=="O":
        player2 = b5.cget("text")
        if player2=="O":
            player2 = b7.cget("text")
            if player2=="O":
                return 1
    player2 = b1.cget("text")
    if player2 == "O":
        player2 = b4.cget("text")
        if player2 == "O":
            player2 = b7.cget("text")
            if player2 == "O":
                return 1
    player2 = b2.cget("text")
    if player2 == "O":
        player2 = b5.cget("text")
        if player2 == "O":
            player2 = b8.cget("text")
            if player2 == "O":
                return 1
    player2 = b3.cget("text")
    if player2 == "O":
        player2 = b6.cget("text")
        if player2 == "O":
            player2 = b9.cget("text")
            if player2 == "O":
                return 1


def b_1():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b1.configure(text="X")
        w=check_1()
        if w==1:
            temp.configure(text="player-1 won.....")
            a=turn1_en.get()
            b=eval(a+"+"+str(1))
            turn1_en.insert(0,b)
        flag=1
    else:
        b1.configure(text="O")
        w=check_2()
        if w==1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")



    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_2():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b2.configure(text="X")
        w=check_1()
        if w==1:
            temp.configure(text="player-1 won.....")
            a =turn1_en.get()
            b = eval(a+"+"+str(1))
            turn1_en.insert(0,b)
        flag=1
    else:
        b2.configure(text="O")
        w=check_2()
        if w==1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b =eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_3():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b3.configure(text="X")
        w=check_1()
        if w==1:
            temp.configure(text="player-1 won.....")
            a = turn1_en.get()
            b = eval(a+"+"+str(1))
            turn1_en.insert(0,b)
        flag=1
    else:
        b3.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))


            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_4():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b4.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a =turn1_en.get()
            b =eval(a+"+"+str(1))
            turn1_en.insert(0, b)
        flag=1
    else:
        b4.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_5():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b5.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a = turn1_en.get()
            b =eval(a+"+"+str(1))
            turn1_en.insert(0,b)
        flag=1
    else:
        b5.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a =turn2_en.get()
            b =eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")

    if flag==1:
        p1.configure(text="PLAYER-2 turn")
def b_6():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b6.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a = turn1_en.get()
            b = eval(a+"+"+str(1))
            turn1_en.insert(0, b)
        flag=1
    else:
        b6.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_7():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b7.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a = turn1_en.get()
            b =eval(a+"+"+str(1))
            turn1_en.insert(0, b)
        flag=1
    else:
        b7.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b =eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_8():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b8.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a =turn1_en.get()
            b =eval(a+"+"+str(1))
            turn1_en.insert(0, b)
        flag=1
    else:
        b8.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")


    if flag==1:
        p1.configure(text="PLAYER-2 turn")

def b_9():
    flag=0
    p = p1.cget("text")
    if p=="PLAYER-1 turn":
        b9.configure(text="X")
        w = check_1()
        if w == 1:
            temp.configure(text="player-1 won.....")
            a = turn1_en.get()
            b = eval(a+"+"+str(1))
            turn1_en.insert(0, b)
        flag=1
    else:
        b9.configure(text="O")
        w = check_2()
        if w == 1:
            temp.configure(text="player-2 won.....")
            a = turn2_en.get()
            b = eval(a+"+"+str(1))
            turn2_en.insert(0, b)
        p1.configure(text="PLAYER-1 turn")

    if flag==1:
        p1.configure(text="PLAYER-2 turn")



def clear():
    b1.configure(text="1")
    b2.configure(text="2")
    b3.configure(text="3")
    b4.configure(text="4")
    b5.configure(text="5")
    b6.configure(text="6")
    b7.configure(text="7")
    b8.configure(text="8")
    b9.configure(text="9")


root=Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
p1=Label(root,text="PLAYER-1 turn")
temp=Label(root)

ft = ("Times New Roman", 15)

turn1=Label(root,text="Player-1")
turn1_en=Entry(root)
turn1_en.insert(0,"0")
turn2=Label(root,text="Player-2")
turn2_en=Entry(root)
turn2_en.insert(0,"0")
p=Entry(root,text="player-1",)

b1=Button(root,text="1",fg="black",command=b_1, font = ft)
b2=Button(root,text="2",fg="black",command=b_2, font = ft)
b3=Button(root,text="3",fg="black",command=b_3, font = ft)
b4=Button(root,text="4",fg="black",command=b_4, font = ft)
b5=Button(root,text="5",fg="black",command=b_5, font = ft)
b6=Button(root,text="6",fg="black",command=b_6, font = ft)
b7=Button(root,text="7",fg="black",command=b_7, font = ft)
b8=Button(root,text="8",fg="black",command=b_8, font = ft)
b9=Button(root,text="9",fg="black",command=b_9, font = ft)
clea=Button(root,text="Reset",command=clear)

b1.place(x=40,y=40)
b2.place(x=80,y=40)
b3.place(x=120,y=40)
b4.place(x=40,y=80)
b5.place(x=80,y=80)
b6.place(x=120,y=80)
b7.place(x=40,y=120)
b8.place(x=80,y=120)
b9.place(x=120,y=120)
temp.place(x=120,y=160)
turn1.place(x=200,y=80)
turn2.place(x=200,y=120)
turn1_en.place(x=200,y=100)
turn2_en.place(x=200,y=140)
clea.place(x=200,y=180)
root.mainloop()
