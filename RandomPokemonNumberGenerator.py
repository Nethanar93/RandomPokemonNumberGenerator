from Tkinter import *
from random import randint

root = Tk()

root.title("Pokemon Number Generator")

main = Frame(root)
main.pack(padx=15, pady=15)

Label(root, text="Pokemon Number:").pack(in_=main)

resultLabel = Label(root, text="", font=("Helvetica", 50))

resultLabel.pack(in_=main)

button_row = Frame(root)
button_row.pack(in_=main,pady=10)

def gen_1():
    number = randint(1, 152)
    resultLabel.configure(text=number)

def gen_2():
    number = randint(151, 252)
    resultLabel.configure(text=number)

def gen_3():
    number = randint(251, 387)
    resultLabel.configure(text=number)

def gen_4():
    number = randint(386, 494)
    resultLabel.configure(text=number)

def gen_5():
    number = randint(493, 650)
    resultLabel.configure(text=number)

def gen_6():
    number = randint(649, 722)
    resultLabel.configure(text=number)

def gen_7():
    number = randint(721, 808)
    resultLabel.configure(text=number)

def gen_all():
    number = randint(1, 808)
    resultLabel.configure(text=number)

Button(root, text="Gen 1", command=gen_1).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 2", command=gen_2).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 3", command=gen_3).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 4", command=gen_4).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 5", command=gen_5).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 6", command=gen_6).pack(in_=button_row, side=LEFT, padx=5)
Button(root, text="Gen 7", command=gen_7).pack(in_=button_row, side=LEFT, padx=5)

Button(root, text="All gens", command=gen_all).pack(in_=main)


root.mainloop()