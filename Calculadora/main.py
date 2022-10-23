#import tkinter
from tkinter import *
from tkinter import ttk

#colors
color1 = "#3b3b3b" #black
color2 = "#feffff"  #white
color3 = "#38576b" #blue
color4 = "#b1b2b3" #grey
color5 = "#e0813d" #orange

#create window
window = Tk()
window.title("Calculator")
window.geometry("235x308")
window.config(bg=color1)

#create frame
frame_screen = Frame(window, width=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)

#create body
frame_body = Frame(window, width=235, height=270)
frame_body.grid(row=1, column=0)

#create label
text_value = StringVar()
app_label = Label(frame_screen, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=("ivy 18"), bg=color3, fg=color2)
app_label.place(x=0, y=0)

#var all values
all_values = ""

#function to enter values
def enter_values(x):

    global all_values 
    all_values = all_values + str(x)
    #pass a value to screen
    text_value.set(all_values)


#function to calculate
def calculate():
    global all_values
    result = eval(all_values)
    text_value.set(result)


#function to clear
def clear():
    global all_values
    all_values = ""
    text_value.set("")



#create buttons
b_clear = Button(frame_body, command=clear , text="C", width=11, height=2, bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)
b_module = Button(frame_body, command=lambda: enter_values("%")  , text="%", width=5, height=2, bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_module.place(x=120, y=0)
b_division = Button(frame_body, command=lambda: enter_values("/")  , text="/", width=5, height=2,  bg=color5, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_division.place(x=180, y=0)

b_7 = Button(frame_body, text="7", command=lambda: enter_values("7")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=51)
b_8 = Button(frame_body, text="8", command=lambda: enter_values("8")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=51)
b_9 = Button(frame_body, text="9", command=lambda: enter_values("9")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=51)
b_mult = Button(frame_body, text="*", command=lambda: enter_values("*")  , width=5, height=2,  bg=color5, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=180, y=51)

b_4 = Button(frame_body, text="4", command=lambda: enter_values("4")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=103)
b_5 = Button(frame_body, text="5", command=lambda: enter_values("5")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=103)
b_6 = Button(frame_body, text="6", command=lambda: enter_values("6")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=103)
b_minus = Button(frame_body, text="-", command=lambda: enter_values("-")  , width=5, height=2,  bg=color5, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_minus.place(x=180, y=103)

b_3 = Button(frame_body, text="3", command=lambda: enter_values("3")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=0, y=155)
b_2 = Button(frame_body, text="2", command=lambda: enter_values("2")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=60, y=155)
b_1 = Button(frame_body, text="1", command=lambda: enter_values("1")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=120, y=155)
b_plus = Button(frame_body, text="+", command=lambda: enter_values("+")  , width=5, height=2,  bg=color5, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_plus.place(x=180, y=155)

b_0 = Button(frame_body, text="0", command=lambda: enter_values("0")  , width=11, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=207)
b_dot = Button(frame_body, text=".", command=lambda: enter_values(".")  , width=5, height=2,  bg=color4, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_dot.place(x=120, y=207)
b_equal = Button(frame_body, command=calculate, text="=", width=5, height=2,  bg=color5, fg=color1, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_equal.place(x=180, y=207)



#show window
window.mainloop()

