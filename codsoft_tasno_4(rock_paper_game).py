from tkinter import *
from random import randint
from tkinter import ttk
from tkinter import PhotoImage
root = Tk()
root.title("Roxk_paper_Scissor")
root.geometry("500x380")

#rock = PhotoImage(file = "D:\Programming Folder Python\CODSOFT\Rock_paper_game\srock.jpg")
#paper = PhotoImage(file = 'D:\Programming Folder Python\CODSOFT\Rock_paper_game\paper.png')

#scissor = PhotoImage(file = 'D:\Programming Folder Python\CODSOFT\Rock_paper_game\scissor.png')
choices = ["rock", "paper", "scissor"]
pick_no = randint(0, 2)
root.config(bg = "#003")

def spin():
    pick_no = randint(0, 2)
    image_label.config(text = choices[pick_no], background= "#fff", font= ("Garamond",18, "bold"), bg= "#003", fg= "white")
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "paper":
        user_choice_value = 1
    elif user_choice.get():
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_no == 0:
            win_loss_lbl.config(text = "Its' Tie")
        elif pick_no == 1:
            win_loss_lbl.config(text = "Paper covers rock you lose!")
        elif pick_no == 2:
            win_loss_lbl.config(text = "Rock smashes scissor you won!")

    if user_choice_value == 1:
        if pick_no == 0:
            win_loss_lbl.config(text = "paper covers rock you win!")
        elif pick_no == 1:
            win_loss_lbl.config(text = "It's Tie")
        elif pick_no == 2:
            win_loss_lbl.config(text = "scissor cuts paper you lose!")

    if user_choice_value == 2:
        if pick_no == 0:
            win_loss_lbl.config(text = "Rock smashes scissor you lose!")
        elif pick_no == 1:
            win_loss_lbl.config(text = "scissor cuts paper you win!")
        elif pick_no == 2:
            win_loss_lbl.config(text = "It's Tie")
txt  = Label(root, text = "Select choice :", font = ("Garamond", 12), bg = "#003" , fg = "white")
txt.place(x = 75, y = 20)

txt  = Label(root, text = "Computer      :", font = ("Garamond", 12), bg = "#003" , fg = "white")
txt.place(x = 75, y = 85)
user_choice = ttk.Combobox(root, value = ("Rock", "paper", "scissor"))
user_choice.current(0)
user_choice.pack(pady = 20)
image_label = Label(root, text = "", bg = "#003")
image_label.pack(pady = 20)
spin_button = Button(root, text = "Play!", command = spin, width= 4, height= 0, font=("Garamond", 16, "bold"), bg= "#fff")
spin_button.pack(pady = 10)
#for win or lose
win_loss_lbl = Label(root, text = "", font = ("Garamond", 18))
win_loss_lbl.pack(pady = 50)
win_loss_lbl.config(text = "Start the game!")
root.mainloop()