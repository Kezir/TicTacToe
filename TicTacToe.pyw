from tkinter import *
import os
import random
import time
import random

root = Tk()
root.title("TicTacToe")
root.geometry("400x300")
positionRight = int(root.winfo_screenwidth() / 2 - 200)
positionDown = int(root.winfo_screenheight() / 2 - 220)

root.geometry("+{}+{}".format(positionRight, positionDown))

def wybor(przeciwnik):
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    labelwybor = Label(root, text="Wybierz kim chcesz zaczac", font=10)
    labelwybor.place(x = 80,y=60)
    buttonx = Button(root, text="X", font=15,padx = 10,pady = 10,bg = "white",command = lambda : gracz1("x",przeciwnik))
    buttonx.place(x = 80,y=150)
    buttono = Button(root, text="O", font=15,padx = 10,pady = 10,bg = "white",command = lambda : gracz1("o",przeciwnik))
    buttono.place(x = 280,y=150)
    buttonrandom = Button(root, text="Losowo", font=15, padx=10, pady=10,bg = "white", command=lambda: gracz1("los",przeciwnik))
    buttonrandom.place(x=151, y=150)

def change(widget,i,nr,player,przeciwnik):
    global count,tab,gracz
    gracz = player

    if gracz == "x":
        if przeciwnik == "Gracz":
            widget.config(text="O",command = donothing)
        else:
            widget.config(text="X", command=donothing)
    elif gracz == "o":
        if przeciwnik == "Gracz":
            widget.config(text="X",command = donothing)
        else:
            widget.config(text="O", command=donothing)
    tab = check(i, nr, tab, gracz, przeciwnik)

    if gracz == "x":
        widget.config(text="X",command = donothing)
    elif gracz == "o":
        widget.config(text="O",command = donothing)

    if not tab2:
        win("remis")
        sys.exit()

def donothing():
    return

def checkwin(player,tab):
    global scorex,scoreo
    if tab[0] == tab[1] == tab[2]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[3] == tab[4] == tab[5]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[6] == tab[7] == tab[8]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[0] == tab[3] == tab[6]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[1] == tab[4] == tab[7]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[2] == tab[5] == tab[8]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[0] == tab[4] == tab[8]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral " + player)
        sys.exit()
    elif tab[2] == tab[4] == tab[6]:
        if player == "x":
            scorex += 1
        else:
            scoreo += 1
        win("wygral "+player)
        sys.exit()

def check(i,number,tab,player,przeciwnik):
    global count,gracz,scoreo,scorex
    gracz = player

    if count == 1 and przeciwnik == "Gracz":
        tab[number-1]="x"
        tab2.remove(number-1)
        count += 1
        gracz = "o"
        if tab[0] == tab[1] == tab[2] or tab[3] == tab[4] == tab[5] or tab[6] == tab[7] == tab[8] or tab[0] == tab[3] == tab[6] or tab[1] == tab[4] == tab[7] or tab[2] == tab[5] == tab[8] or tab[0] == tab[4] == tab[8] or tab[2] == tab[4] == tab[6]:
            scoreo += 1
            win("wygral O")

    elif count == 2 and przeciwnik == "Gracz":
        tab[number-1]="o"
        tab2.remove(number-1)
        count -= 1
        gracz = "x"
        if tab[0] == tab[1] == tab[2] or tab[3] == tab[4] == tab[5] or tab[6] == tab[7] == tab[8] or tab[0] == tab[3] == tab[6] or tab[1] == tab[4] == tab[7]or tab[2] == tab[5] == tab[8] or tab[0] == tab[4] == tab[8] or tab[2] == tab[4] == tab[6]:
            scorex += 1
            win("wygral X")

    elif gracz == "x" and przeciwnik == "CPU1": # gracz = x   CPU = o

        tab[number-1] = "x"
        tab2.remove(number-1)
        checkwin("x",tab)

        if not tab2:
            win("remis")
            sys.exit()

        for i in range (len(tab2)):
            rand = random.sample(tab2, 1)
            if rand[0] != "x" and rand[0] != "o":
                break

        tab[rand[0]] = "o"
        tab2.remove(rand[0])

        if rand[0] == 0:
            button1.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 1:
            button2.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 2:
            button3.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 3:
            button4.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 4:
            button5.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 5:
            button6.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 6:
            button7.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 7:
            button8.config(text = "O",command = donothing)
            count -= 1

        elif rand[0] == 8:
            button9.config(text = "O",command = donothing)
            count -= 1

        checkwin("o", tab)

        if not tab2:
            win("remis")
            sys.exit()

    elif gracz == "o" and przeciwnik == "CPU1":

        tab[number - 1] = "o"
        tab2.remove(number - 1)
        checkwin("o", tab)

        for i in range(len(tab2)):
            rand = random.sample(tab2, 1)
            if rand[0] != "x" and rand[0] != "o":
                break
        tab[rand[0]] = "x"
        tab2.remove(rand[0])

        if rand[0] == 0:
            button1.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 1:
            button2.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 2:
            button3.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 3:
            button4.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 4:
            button5.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 5:
            button6.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 6:
            button7.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 7:
            button8.config(text="X", command=donothing)
            count -= 1

        elif rand[0] == 8:
            button9.config(text="X", command=donothing)
            count -= 1
        checkwin("x", tab)
        if not tab2:
            win("remis")
            sys.exit()
    elif gracz == "x" and przeciwnik == "CPU2": # gracz = x   CPU = o
        tab[number-1] = "x"
        tab2.remove(number-1)
        checkwin("x",tab)

        it = danger(tab, tab2)

        tab[it] = "o"
        tab2.remove(it)

        if it == 0:
            button1.config(text = "O",command = donothing)
            count -= 1

        elif it == 1:
            button2.config(text = "O",command = donothing)
            count -= 1

        elif it == 2:
            button3.config(text = "O",command = donothing)
            count -= 1

        elif it == 3:
            button4.config(text = "O",command = donothing)
            count -= 1

        elif it == 4:
            button5.config(text = "O",command = donothing)
            count -= 1

        elif it == 5:
            button6.config(text = "O",command = donothing)
            count -= 1

        elif it == 6:
            button7.config(text = "O",command = donothing)
            count -= 1

        elif it == 7:
            button8.config(text = "O",command = donothing)
            count -= 1

        elif it == 8:
            button9.config(text = "O",command = donothing)
            count -= 1

        checkwin("o", tab)
    elif gracz == "o" and przeciwnik == "CPU2":

        tab[number - 1] = "o"
        tab2.remove(number - 1)
        checkwin("o", tab)

        it = danger(tab,tab2)

        tab[it] = "x"
        tab2.remove(it)

        if it == 0:
            button1.config(text="X", command=donothing)
            count -= 1

        elif it == 1:
            button2.config(text="X", command=donothing)
            count -= 1

        elif it == 2:
            button3.config(text="X", command=donothing)
            count -= 1

        elif it == 3:
            button4.config(text="X", command=donothing)
            count -= 1

        elif it == 4:
            button5.config(text="X", command=donothing)
            count -= 1

        elif it == 5:
            button6.config(text="X", command=donothing)
            count -= 1

        elif it == 6:
            button7.config(text="X", command=donothing)
            count -= 1

        elif it == 7:
            button8.config(text="X", command=donothing)
            count -= 1

        elif it == 8:
            button9.config(text="X", command=donothing)
            count -= 1
        checkwin("x", tab)
        if not tab2:
            win("remis")
            sys.exit()
    elif gracz == "x" and przeciwnik == "CPU3": # gracz = x   CPU = o
        tab[number-1] = "x"
        tab2.remove(number-1)
        checkwin("x",tab)

        it = dangerwin(tab, tab2)

        tab[it] = "o"
        tab2.remove(it)

        if it == 0:
            button1.config(text = "O",command = donothing)
            count -= 1

        elif it == 1:
            button2.config(text = "O",command = donothing)
            count -= 1

        elif it == 2:
            button3.config(text = "O",command = donothing)
            count -= 1

        elif it == 3:
            button4.config(text = "O",command = donothing)
            count -= 1

        elif it == 4:
            button5.config(text = "O",command = donothing)
            count -= 1

        elif it == 5:
            button6.config(text = "O",command = donothing)
            count -= 1

        elif it == 6:
            button7.config(text = "O",command = donothing)
            count -= 1

        elif it == 7:
            button8.config(text = "O",command = donothing)
            count -= 1

        elif it == 8:
            button9.config(text = "O",command = donothing)
            count -= 1

        checkwin("o", tab)
    elif gracz == "o" and przeciwnik == "CPU3":

        tab[number - 1] = "o"
        tab2.remove(number - 1)
        checkwin("o", tab)

        it = dangerwin(tab,tab2)

        tab[it] = "x"
        tab2.remove(it)

        if it == 0:
            button1.config(text="X", command=donothing)
            count -= 1

        elif it == 1:
            button2.config(text="X", command=donothing)
            count -= 1

        elif it == 2:
            button3.config(text="X", command=donothing)
            count -= 1

        elif it == 3:
            button4.config(text="X", command=donothing)
            count -= 1

        elif it == 4:
            button5.config(text="X", command=donothing)
            count -= 1

        elif it == 5:
            button6.config(text="X", command=donothing)
            count -= 1

        elif it == 6:
            button7.config(text="X", command=donothing)
            count -= 1

        elif it == 7:
            button8.config(text="X", command=donothing)
            count -= 1

        elif it == 8:
            button9.config(text="X", command=donothing)
            count -= 1
        checkwin("x", tab)
        if not tab2:
            win("remis")
            sys.exit()
    return tab

def danger(tab,tab2):
    for i in range(len(tab2)):
        rand = random.sample(tab2, 1)
        if rand[0] != "x" and rand[0] != "o":
            break
    if not tab2:
        win("remis")
        sys.exit()
    number = rand[0]
    #poziom
    if tab[0] == tab[1] and tab2.count(2) == 1 :
        number = 2
    elif tab[0] == tab[2] and tab2.count(1) == 1 :
        number = 1
    elif tab[1] == tab[2] and tab2.count(0) == 1 :
        number = 0
    elif tab[3] == tab[4] and tab2.count(5) == 1 :
        number = 5
    elif tab[3] == tab[5] and tab2.count(4) == 1 :
        number = 4
    elif tab[4] == tab[5] and tab2.count(3) == 1 :
        number = 3
    elif tab[6] == tab[7] and tab2.count(8) == 1 :
        number = 8
    elif tab[6] == tab[8] and tab2.count(7) == 1 :
        number = 7
    elif tab[7] == tab[8] and tab2.count(6) == 1 :
        number = 6
    #pion
    elif tab[0] == tab[3] and tab2.count(6) == 1 :
        number = 6
    elif tab[0] == tab[6] and tab2.count(3) == 1 :
        number = 3
    elif tab[3] == tab[6] and tab2.count(0) == 1:
        number = 0
    elif tab[1] == tab[4] and tab2.count(7) == 1 :
        number = 7
    elif tab[1] == tab[7] and tab2.count(4) == 1 :
        number = 4
    elif tab[4] == tab[7] and tab2.count(1) == 1 :
        number = 1
    elif tab[2] == tab[5] and tab2.count(8) == 1 :
        number = 8
    elif tab[2] == tab[8] and tab2.count(5) == 1 :
        number = 5
    elif tab[5] == tab[8] and tab2.count(2) == 1 :
        number = 2
    #skos
    elif tab[0] == tab[4] and tab2.count(8) == 1 :
        number = 8
    elif tab[0] == tab[8] and tab2.count(4) == 1 :
        number = 4
    elif tab[4] == tab[8] and tab2.count(0) == 1:
        number = 0
    elif tab[2] == tab[4] and tab2.count(6) == 1 :
        number = 6
    elif tab[2] == tab[6] and tab2.count(4) == 1 :
        number = 4
    elif tab[4] == tab[6] and tab2.count(2) == 1 :
        number = 2

    return number

def dangerwin(tab,tab2):
    for i in range(len(tab2)):
        rand = random.sample(tab2, 1)
        if rand[0] != "x" and rand[0] != "o":
            break
    if not tab2:
        win("remis")
        sys.exit()
    number = rand[0]
    #bemyslne
    if tab[0] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 0:
                break
    if tab[1] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 1:
                break
    if tab[2] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 2:
                break
    if tab[3] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 3:
                break
    if tab[5] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 5:
                break
    if tab[6] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 6:
                break
    if tab[7] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 7:
                break
    if tab[8] == gracz :
        for i in range(len(tab2)):
            number = random.sample(tab2, 1)[0]
            if number != 8:
                break
    #kwadrat
    if tab[1] == tab[3] and tab2.count(0) == 1 :
        number = 0
    if tab[1] == tab[5] and tab2.count(2) == 1 :
        number = 2
    if tab[3] == tab[7] and tab2.count(6) == 1 :
        number = 6
    if tab[5] == tab[7] and tab2.count(8) == 1 :
        number = 8
    #poziom
    if tab[0] == tab[1] and tab2.count(2) == 1 :
        if tab[0] != gracz:
            number = 2
            return number
        number = 2
    if tab[0] == tab[2] and tab2.count(1) == 1 :
        if tab[0] != gracz:
            number = 1
            return number
        number = 1
    if tab[1] == tab[2] and tab2.count(0) == 1 :
        if tab[1] != gracz:
            number = 0
            return number
        number = 0
    if tab[3] == tab[4] and tab2.count(5) == 1 :
        if tab[3] != gracz:
            number = 5
            return number
        number = 5
    if tab[3] == tab[5] and tab2.count(4) == 1 :
        if tab[3] != gracz:
            number = 4
            return number
        number = 4
    if tab[4] == tab[5] and tab2.count(3) == 1 :
        if tab[4] != gracz:
            number = 3
            return number
        number = 3
    if tab[6] == tab[7] and tab2.count(8) == 1 :
        if tab[6] != gracz:
            number = 8
            return number
        number = 8
    if tab[6] == tab[8] and tab2.count(7) == 1 :
        if tab[6] != gracz:
            number = 7
            return number
        number = 7
    if tab[7] == tab[8] and tab2.count(6) == 1 :
        if tab[7] != gracz:
            number = 6
            return number
        number = 6
    #pion
    if tab[0] == tab[3] and tab2.count(6) == 1 :
        if tab[0] != gracz:
            number = 6
            return number
        number = 6
    if tab[0] == tab[6] and tab2.count(3) == 1 :
        if tab[0] != gracz:
            number = 3
            return number
        number = 3
    if tab[3] == tab[6] and tab2.count(0) == 1:
        if tab[3] != gracz:
            number = 0
            return number
        number = 0
    if tab[1] == tab[4] and tab2.count(7) == 1 :
        if tab[1] != gracz:
            number = 7
            return number
        number = 7
    if tab[1] == tab[7] and tab2.count(4) == 1 :
        if tab[1] != gracz:
            number = 4
            return number
        number = 4
    if tab[4] == tab[7] and tab2.count(1) == 1 :
        if tab[4] != gracz:
            number = 1
            return number
        number = 1
    if tab[2] == tab[5] and tab2.count(8) == 1 :
        if tab[2] != gracz:
            number = 8
            return number
        number = 8
    if tab[2] == tab[8] and tab2.count(5) == 1 :
        if tab[2] != gracz:
            number = 5
            return number
        number = 5
    if tab[5] == tab[8] and tab2.count(2) == 1 :
        if tab[5] != gracz:
            number = 2
            return number
        number = 2
    #skos
    if tab[0] == tab[4] and tab2.count(8) == 1 :
        if tab[0] != gracz:
            number = 8
            return number
        number = 8
    if tab[0] == tab[8] and tab2.count(4) == 1 :
        if tab[0] != gracz:
            number = 4
            return number
        number = 4
    if tab[4] == tab[8] and tab2.count(0) == 1:
        if tab[4] != gracz:
            number = 0
            return number
        number = 0
    if tab[2] == tab[4] and tab2.count(6) == 1 :
        if tab[2] != gracz:
            number = 6
            return number
        number = 6
    if tab[2] == tab[6] and tab2.count(4) == 1 :
        if tab[2] != gracz:
            number = 4
            return number
        number = 4
    if tab[4] == tab[6] and tab2.count(2) == 1 :
        if tab[4] != gracz:
            number = 2
            return number
        number = 2
    if tab[4] == 4:
        number = 4

    return number

def CPUdiff():
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    easy = Button(root, text="Easy",padx=40, pady=10,bg = "white", command=lambda : wybor("CPU1")).place(x=141, y=100)
    medium = Button(root, text="Medium",padx=40, pady=10,bg = "white", command=lambda : wybor("CPU2")).place(x=130, y=160)
    hard = Button(root, text="Hard",padx=40, pady=10,bg = "white", command=lambda : wybor("CPU3")).place(x=140, y=220)

def win(who):
    root.attributes("-disabled",True)
    root2 = Tk()
    positionRight = int(root2.winfo_screenwidth() / 2 - 180)
    positionDown = int(root2.winfo_screenheight() / 2 - 200)
    root2.geometry("+{}+{}".format(positionRight, positionDown))
    label1 = Label(root2,text = str(who),font = 16).grid(row = 0,column = 1)
    label2 = Label(root2,text = "czy chcesz zagrac jeszcze raz").grid(row = 1,column =1)
    exit = Button(root2,text = "Wyjscie",bg = "white",command = sys.exit).grid(row = 2,column = 2)
    wroc = Button(root2, text="Wroc do menu",bg = "white", command=lambda : wejdzdomenu(root2)).grid(row=2, column=1)
    again = Button(root2,text = "Jeszcze raz",bg = "white",command =lambda : close(root2)).grid(row = 2,column = 0)
    root2.protocol("WM_DELETE_WINDOW",donothing)
    root2.mainloop()
def wejdzdomenu(root2):
    root.attributes("-disabled", False)
    root2.destroy()
    multi()
def close(root2):
    root.attributes("-disabled", False)
    root2.destroy()
    start(gracz,przeciwnik)

def start(gracze,przeciwni):
    global count,tab,tab2,gracz,przeciwnik,scorex,scoreo
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    gracz = gracze
    przeciwnik = przeciwni
    if gracz == "o" and przeciwnik == "CPU1":
        temp = random.choice([0,2,8])
        tab[temp] = "x"
        tab2.remove(temp)
    elif gracz == "o" and przeciwnik == "CPU2":
        temp = random.choice([4, 5, 6])
        tab[temp] = "x"
        tab2.remove(temp)
    elif gracz == "o" and przeciwnik == "CPU3":
        temp = random.choice([1, 3, 7])
        tab[temp] = "x"
        tab2.remove(temp)
    count = 1
    list = root.place_slaves()
    for l in list:
        l.destroy()
        
    Label1 = Label(root,text = "X",font = 20,padx = 35,pady = 20).grid(row = 2,column = 0)
    Label2 = Label(root,text = "O",font = 20,padx = 35,pady = 20).grid(row = 2,column = 9)
    score1 = Label(root, text=scorex, font=20, padx=35, pady=20).grid(row=4, column=0)
    score2 = Label(root, text=scoreo, font=20, padx=35, pady=20).grid(row=4, column=9)
    Labelempty1 = Label(root,padx = 30,pady = 10).grid(row = 0,column = 0)
    Labelempty2 = Label(root).grid(row=5, column=5)
    if gracz =="o" and przeciwnik == "CPU1" and len(tab2)==8 and temp == 0:
        button1 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button1 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button1, count, 1, gracz, przeciwnik))
    button1.grid(row=2, column=2)
    if gracz == "o" and przeciwnik == "CPU3" and len(tab2) == 8 and temp == 1:
        button2 = Button(root, text="X", padx=28, pady=20,bg = "white")
    else:
        button2 = Button(root, text="   ", padx=28, pady=20,bg = "white",
                         command=lambda: change(button2, count, 2, gracz, przeciwnik))
    button2.grid(row=2, column=3)
    if gracz =="o" and przeciwnik == "CPU1" and len(tab2)==8 and temp == 2:
        button3 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button3 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button3, count, 3, gracz, przeciwnik))
    button3.grid(row=2, column=4)
    if gracz == "o" and przeciwnik == "CPU3" and len(tab2) == 8 and temp == 3:
        button4 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button4 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button4, count, 4, gracz, przeciwnik))
    button4.grid(row=3, column=2)
    if gracz == "o" and przeciwnik == "CPU2" and len(tab2) == 8 and temp == 4:
        button5 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button5 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button5, count, 5, gracz, przeciwnik))
    button5.grid(row=3, column=3)
    if gracz == "o" and przeciwnik == "CPU2" and len(tab2) == 8 and temp == 5:
        button6 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button6 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button6, count, 6, gracz, przeciwnik))
    button6.grid(row=3, column=4)
    if gracz == "o" and przeciwnik == "CPU2" and len(tab2) == 8 and temp == 6:
        button7 = Button(root, text="X", padx=28, pady=20,bg = "white")
    else:
        button7 = Button(root,text = "   ",padx = 28,pady = 20,bg = "white",command = lambda : change(button7,count,7,gracz,przeciwnik))
    button7.grid(row=4, column=2)
    if gracz == "o" and przeciwnik == "CPU3" and len(tab2) == 8 and temp == 7:
        button8 = Button(root, text="X", padx=28, pady=20,bg = "white")
    else:
        button8 = Button(root, text="   ", padx=28, pady=20,bg = "white",
                         command=lambda: change(button8, count, 8, gracz, przeciwnik))
    button8.grid(row=4, column=3)
    if gracz =="o" and przeciwnik == "CPU1" and len(tab2)==8 and temp == 8:
        button9 = Button(root,text = "X",padx = 28,pady = 20,bg = "white")
    else:
        button9 = Button(root, text="   ", padx=28, pady=20,bg = "white",command=lambda: change(button9, count, 9, gracz, przeciwnik))
    button9.grid(row=4, column=4)

def gracz1(dane,enemy):
    temp1 = random.choice(['x','o'])
    if dane == "x":
        if enemy == "Gracz":
            start("x","Gracz")
        elif enemy == "CPU1":
            start("x","CPU1")
        elif enemy == "CPU2":
            start("x","CPU2")
        elif enemy == "CPU3":
            start("x","CPU3")
    elif dane == "o":
        if enemy == "Gracz":
            start("o", "Gracz")
        elif enemy == "CPU1":
            start("o", "CPU1")
        elif enemy == "CPU2":
            start("o","CPU2")
        elif enemy == "CPU3":
            start("o","CPU3")
    elif dane == "los":
        if enemy == "CPU1":
            start(temp1, "CPU1")
        elif enemy == "CPU2":
            start(temp1,"CPU2")
        elif enemy == "CPU3":
            start(temp1,"CPU3")

def multi():
    global scorex,scoreo
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    scorex = 0
    scoreo = 0
    Label1 = Label(root,text = "Wybierz tryb",font = 15).place(x = 145,y = 60)
    buttongracz = Button(root, text="Gracz vs Gracz", padx=40, pady=10,bg = "white", command=lambda : gracz1("x","Gracz")).place(x=120, y=160)
    buttonCPU = Button(root, text="Gracz vs CPU", padx=40, pady=10,bg = "white", command= CPUdiff).place(x=123, y=220)

def wyjscie():
    sys.exit()


Labeltitle = Label(root, text="TIC TAC TOE ", font=20).place(x=145, y=60)
buttonstart = Button(root, text="Start", padx=40, pady=10,bg = "white", command=multi).place(x=150, y=160)
buttonwyjscie = Button(root, text="Wyjscie", padx=40, pady=10,bg = "white", command=wyjscie).place(x=143, y=220)
root.mainloop()
