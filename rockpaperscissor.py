from tkinter import *
import random
import pygame
import time



root = Tk()
root.geometry("600x600")
root.configure(background='#DAF7A6')
winner = ''


def stone(event):
    winner = evaldata("rock")
    panel1.configure(text=winner)


def paper(event):
    winner = evaldata("paper")
    panel1.configure(text=winner)


def scissor(event):
    winner = evaldata("scissor")
    panel1.configure(text=winner)


def instructions(event):
    panel2.configure(text='''1.choose any of the following by clicking on it
    2. figure i is stone
    3. figure ii is paper
    4. figure iii is scissor''')


result = ["Tie", "player wins", "computer wins"]


def outcome(cmoves):
    panel3.configure(text='computer choosed:' + cmoves)


def evaldata(pmoves):
    moves = ["rock", "paper", "scissor"]
    cmoves = random.choice(moves)
    result = ["Tie", "player wins", "computer wins"]
    if(cmoves == pmoves):
        winner = result[0]
    elif(cmoves == 'rock' and pmoves == 'paper'):
        winner = result[1]
    elif(cmoves == 'rock' and pmoves == 'scissor'):
        winner = result[2]
    elif(cmoves == 'paper' and pmoves == 'stone'):
        winner = result[2]
    elif(cmoves == 'paper' and pmoves == 'scissor'):
        winner = result[1]
    elif(cmoves == 'scissor' and pmoves == 'stone'):
        winner = result[1]
    else:
        winner = result[2]
    results(winner)
    outcome(cmoves)
    return winner


# layout of game

def results(winner):
    # if the player wins
    if winner == "computer wins":
        pygame.init()
        pygame.mixer.music.load('you-lose.mp3')
        pygame.mixer.music.play(2)
        time.sleep(1)
    # if the computer wins
    elif winner == "player wins":

        pygame.init()
        pygame.mixer.music.load('faded-alan.mp3')
        pygame.mixer.music.play()
        time.sleep(2)
    # button4 to quit
    else :
        button4 = Button(root , text ='Quit' , font = ('times' , 25 , 'bold italic') , bg='#900C3F')
        button4.place(relx=0.5 , x=100 , rely=1 , y=-100 , anchor=CENTER)
        button4.bind('<Button-1>' , quit)
        time.sleep(2)

# button1 for rock
photo1 = PhotoImage(file="stone.png")
button1 = Button(root, text="STONE", image=photo1, width=150, height=150)
button1.place(x=110, y=20, anchor=N)
button1.bind('<Button-1>', stone)
# button2 for paper
photo2 = PhotoImage(file="paper.png")
button2 = Button(root, text="PAPER", image=photo2, width=150, height=150)
button2.place(relx=0.5, rely=0, y=20, anchor=N)
button2.bind('<Button-1>', paper)
# button3 for scissor
photo3 = PhotoImage(file="scissor.png")
button3 = Button(root, text="SCISSOR", image=photo3, width=150, height=150)
button3.place(relx=1, x=-110, rely=0, y=20, anchor=N)
button3.bind('<Button-1>', scissor)
# button5 for instructions
button5 = Button(root, text='Instructions', font=('times', 20, 'bold italic'), bg='#900C3F')
button5.place(relx=0.5, x=-150, rely=0.5, y=200, anchor=CENTER)
button5.bind('<Button-1>', instructions)
# panel1  for displaying result of the game
panel1 = Label(root, font=('times', 20, 'bold'), command=results(result))
panel1.place(relx=0.5, rely=0.5, x=100, anchor=N)
# panel2 for displaying the instructions
panel2 = Label(root, font=('times', 12, 'italic'))
panel2.place(relx=0.5, rely=0.5, x = -110, y=40, anchor=N)

panel3 = Label(root, font=('times', 20, 'italic'))
panel3.place(relx=0.5, rely=0.5, y=120, anchor=N)

mainloop()
