# source: https://www.youtube.com/watch?v=NKVl_1h9CCk

from tkinter import *
import math

root = Tk()
root.title("Scientific calculator")

entry = Entry(
    root,
    width=50,
    borderwidth=5,
    relief=RIDGE,
    bg="black",
    fg="white"
)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

def click(to_print):
    old = entry.get()
    entry.delete(0, END)
    entry.insert(0, old + to_print)
    return

def sc(event):
    key = event.widget
    text = key['text']
    no = entry.get()
    result = ""
    if text == "deg":
        result = str(math.degrees(float(no)))
    if text == "sin":
        result = str(math.sin(float(no)))
    if text == "cos":
        result = str(math.cos(float(no)))
    if text == "tan":
        result = str(math.tan(float(no)))
    if text == "lg":
        result = str(math.log10(float(no)))
    if text == "ln":
        result = str(math.log(float(no)))
    if text == "sqrt":
        result = str(math.sqrt(float(no)))
    if text == "x!":
        result = str(math.factorial(float(no)))
    if text == "1/x":
        result = str(math.factorial(float(no)))
    if text == "pi":
        if no == "":
            result = str(math.pi)
        else:
            result = str(float(no) * math.pi)
    if text == "e":
        if no == "":
            result = str(math.e)
        else:
            result = str(math.e**float(no))

    entry.delete(0, END)
    entry.insert(0, result)


def clear():
    entry.delete(0, END)
    return

def backspace():
    current = entry.get()
    length = len(current) - 1
    entry.delete(length, END)

def evaluate():
    answer = entry.get()
    answer = eval(answer)
    entry.delete(0, END)
    entry.insert(0, answer)


lg = Button(
    root,
    text="lg",
    padx=30,
    pady=10,
    height=1,
    width=2,
    relief=RAISED,
    bg="black",
    fg="white",
    command=lambda: click("lg")
)
lg.bind("<Button-1>", sc)
lg.grid(row=1, column=0)

ln = Button(
    root,
    text="ln",
    padx=30,
    pady=10,
    height=1,
    width=2,
    relief=RAISED,
    bg="black",
    fg="white",
    command=lambda: click("ln")
)
ln.bind("<Button-1>", sc)
ln.grid(row=1, column=1)


parenthasis1 = Button(root, text="(", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("("))
parenthasis1.grid(row=1, column=2)
parenthasis2 = Button(root, text=")", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click(")"))
parenthasis2.grid(row=1, column=3)

dot = Button(root, text=".", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("."))
dot.grid(row=1, column=4)

exp = Button(root, text="^", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white")
exp.grid(row=2, column=0)

degb = Button(root, text="deg", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("deg"))
degb.bind("<Button-1>", sc)
degb.grid(row=2, column=1)

sinb = Button(root, text="sin", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("sin"))
sinb.bind("<Button-1>", sc)
sinb.grid(row=2, column=2)

cosb = Button(root, text="cos", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("cos"))
cosb.bind("<Button-1>", sc)
cosb.grid(row=2, column=3)

tanb = Button(root, text="tan", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("tan"))
tanb.bind("<Button-1>", sc)
tanb.grid(row=2, column=4)

sqrtm = Button(root, text="sqrt", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("sqrt"))
sqrtm.bind("<Button-1>", sc)


ac = Button(root, text="ac", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="dark red", fg="white", command=clear)
bcspc = Button(root, text="bcspc", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="dark red", fg="white", command=backspace)
mod = Button(root, text="mod", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white")
div = Button(root, text="/", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("/"))

fact = Button(root, text="x!", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("x!"))
fact.bind("<Button-1>", sc)

seven = Button(root, text="7", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("7"))
eight = Button(root, text="8", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("8"))
nine = Button(root, text="9", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("9"))
mult = Button(root, text="*", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("*"))


frac = Button(root, text="1/x", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("1/x"))
frac.bind("<Button-1>", sc)
four = Button(root, text="4", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("4"))
five = Button(root, text="5", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("5"))
six = Button(root, text="6", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("6"))
minus = Button(root, text="-", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("-"))


pib = Button(root, text="pi", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("pi"))
pib.bind("<Button-1>", sc)
one = Button(root, text="1", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("1"))
two = Button(root, text="2", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("2"))
three = Button(root, text="3", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("3"))
plus = Button(root, text="+", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white", command=lambda: click("+"))

e_b = Button(root, text="e", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="black", fg="white")
pib.bind("<Button-1>", sc)
zero = Button(root, text="0", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="grey", fg="white", command=lambda: click("0"))
equal = Button(root, text="=", padx=30, pady=10, height=1, width=2, relief=RAISED, bg="dark green", fg="white", command=evaluate)


zero = Button(
    root,
    text="0",
    padx=30,
    pady=10, 
    height=1, 
    width=2,
    relief=RAISED,
    bg="grey",
    fg="white",
    command=lambda: click("0")
)
zero.grid(row=7, column=2)

sqrtm.grid(row=3, column=0)
ac.grid(row=3, column=1)
bcspc.grid(row=3, column=2)
mod.grid(row=3, column=3)
div.grid(row=3, column=4)

fact.grid(row=4, column=0)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
mult.grid(row=4, column=4)

frac.grid(row=5, column=0)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
minus.grid(row=5, column=4)

pib.grid(row=6, column=0)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
plus.grid(row=6, column=4)

e_b.grid(row=7, column=1)
equal.grid(row=7, column=3)


root.mainloop()