from tkinter import *
import random

#The first step is to import libraries. Here, we required two modules so we need to import Tkinter and random modules.

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissor')
root.config(bg ='#C3FFB9')

#Tk() use to initialized Tkinter to create window
#geometry() sets the window width and height
#bg = ‘’ use to set the color of the 

Label(root, text = 'Rock, Paper ,Scissor' , font='arial 20 bold', bg = 'grey').pack()

#Label() widget used when we want to display text that users can’t modify.
#root is the name of our window
#text which displays on the label as the title of that label
#font in which form the text is written
#pack used to the organized widget in form of block

user_take = StringVar()
Label(root, text = 'Type your move: Rock, Paper ,Scissor' , fg ='white', font='arial 15 bold', bg = 'black').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'yellow').place(x=90 , y = 130)

#user_take is a string type variable that stores the choice that the user enters.
#Entry() widget used when we want to create an input text field.



#If the computer choose 1,4,6,8 then the rock will set to comp_pick variable
#If the computer choose 2,3,5 then the paper will set to comp_pick variable
#If the computer choose 7,9,10 then scissors will set to comp_pick variable
# I have given so much options to decrease the probablity 




#Function to start a game:
Result = StringVar()

def play():
    user_pick = user_take.get()
    comp_pick = (random.randint(1,10))
    if comp_pick == 1 or comp_pick == 4 or comp_pick == 6 or comp_pick == 8:
        comp_pick = 'Rock'
    elif comp_pick ==2 or comp_pick == 3 or comp_pick == 5 :
        comp_pick = 'Paper'
    else:
        comp_pick = 'Scissor'
    
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'Rock' and comp_pick == 'Paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'Rock' and comp_pick == 'Scissor':
        Result.set('you win,computer select scissor')
    elif user_pick == 'Paper' and comp_pick == 'Scissor':
        Result.set('you loose,computer select scissor')
    elif user_pick == 'Paper' and comp_pick == 'Rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'Scissor' and comp_pick == 'Rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'Scissor' and comp_pick == 'Paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: Choose any one -- Rock, Paper, Scissor')



#Function to reset:
def Reset():
    Result.set("") 
    user_take.set("")

    
    
    
    
    
    
    
    


#Function to exit:
def Exit():
    root.destroy()


#Define buttons for games:
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='yellow',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()


#Button() widget used when we want to display a button.
#command called the specific function when the button will be clicked.
#root.mainloop() method executes when we run our program.