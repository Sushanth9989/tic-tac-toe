#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

playerx=IntVar()
playero=IntVar()

playerx.set(0)
playero.set(0)

buttons = StringVar()
click = True

def checker(buttons):
	global click
	if buttons["text"] == " " and click == True:
		buttons["text"] = "X"
		click = False
		scorekeeper()
	elif buttons["text"] == " " and click == False:
		buttons["text"] = "O"
		click = True
		scorekeeper()

def scorekeeper():
	if(button1["text"]=="X"and button2["text"]=="X" and button3["text"]=="X") :
		button1.configure(background ="cyan")
		button2.configure(background ="cyan")
		button3.configure(background ="cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
	if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X") :
		button4.configure(background ="cyan")
		button5.configure(background ="cyan")
		button6.configure(background ="cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
	if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X") :
		button7.configure(backgroung ="cyan")
		button8.configure(background ="cyan")
		button9.configure(background ="cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X", "You have just won a game")
	if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X") :
		button1.configure(background = "cyan")
		button5.configure(background = "cyan")
		button9.configure(background = "cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("WinnerX","You have just won a game")
	if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X") :
		button3.configure(background = "cyan")
		button5.configure(background = "cyan")
		button7.configure(background = "cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game")
	if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
		button1.configure(background ="cyan")
		button4.configure(background ="cyan")
		button7.configure(background ="cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game")
	if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
		button3.configure(background = "cyan")
		button6.configure(background = "cyan")
		button9.configure(background = "cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game")
	if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
		button2.configure(background = "cyan")
		button5.configure(background = "cyan")
		button8.configure(background = "cyan")
		n = float(playerx.get())
		score = (n+1)
		playerx.set(score)
		tkinter.messagebox.showinfo("WinnerX","You have just won a game")
	if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
		button1.configure(background = "magenta")
		button2.configure(background = "magenta")
		button3.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
		button4.configure(background = "magenta")
		button5.configure(background = "magenta")
		button6.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
		button7.configure(background = "magenta")
		button8.configure(background = "magenta")
		button9.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
		button1.configure(background = "magenta")
		button5.configure(background = "magenta")
		button9.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
		button3.configure(background = "magenta")
		button5.configure(background = "magenta")
		button7.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
		button1.configure(background = "magenta")
		button4.configure(background = "magenta")
		button7.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
		 button2.configure(background = "magenta")
		 button5.configure(background = "magenta")
		 button8.configure(background = "magenta")
		 n = float(playero.get())
		 score = (n+1)
		 playero.set(score)
		 tkinter.messagebox.showinfo("Winner O","You have just won a game")
	if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
		button1.configure(background = "magenta")
		button1.configure(background = "magenta")
		button1.configure(background = "magenta")
		n = float(playero.get())
		score = (n+1)
		playero.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game")
	elif():
		tkinter.messagebox.showinfo("Draw Match","It is a tie")
		
def reset():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    
    button1.configure(bg="black")
    button2.configure(bg="black")
    button3.configure(bg="black")
    button4.configure(bg="black")
    button5.configure(bg="black")
    button6.configure(bg="black")
    button7.configure(bg="black")
    button8.configure(bg="black")
    button9.configure(bg="black")
    
def newgame():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    
    button1.configure(bg="black")
    button2.configure(bg="black")
    button3.configure(bg="black")
    button4.configure(bg="black")
    button5.configure(bg="black")
    button6.configure(bg="black")
    button7.configure(bg="black")
    button8.configure(bg="black")
    button9.configure(bg="black")
    playerx.set(0)
    playero.set(0)


labelplayerx = Label( tk, text="Player X", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
labelplayerx.grid(row=0, column=1)
player1_name = Entry(tk, textvariable=playerx, bd=5)
player1_name.grid(row=0, column=2)

labelplayero = Label( tk, text="Player O", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
labelplayero.grid(row=1, column=1)
player2_name = Entry(tk, textvariable=playero, bd=5)
player2_name.grid(row=1, column=2)


reset = Button(tk, text="Reset ", font='Times 15 bold', bg='white', fg='black',height=1,width=10,command = reset)
reset.grid(row=0,column=0)

newgame = Button(tk, text="New Game", font='Times 15 bold', bg='white', fg='black',height=1,width=10,command =newgame)
newgame.grid(row=1,column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,command=lambda:checker(button9))
button9.grid(row=5, column=2)
tk.mainloop()


# In[ ]:




