# all my math imports including indivusal mathematical functions along with pythons default GUI kit (tkinter)
import math 
import tkinter as tk 
import tkinter.messagebox
from tkinter.constants import SUNKEN
from tkinter import *
from tkinter import ttk
from math import pow
from math import sin
from math import cos
from math import tan
from math import pi
from math import e
from math import sinh
from math import cosh
from math import tanh
from math import log10
from math import log

#dimensions of generated window
MAX_SIZE = 99.0
MIN_SIZE = 1.0
INCREMENT = 2.0

COMPUTATION_DISTANCE = 0.001
ASYMPTOTE = 2.0

formula = ""
view_size = 20.0

#labbeling what is displayed on the calculkater entrance commands, including veiwsize settings in the decimal format and the position of the command tab
def print_formula(pre_text):
    Label(root, text=pre_text + "[{0:.0f}".format(view_size) + "f(x)]" + formula, relief=RIDGE,
          width=1).grid(row=1, column=0, columnspan=5, sticky=W + E)

#translate() method returns a string where some specified characters are replaced with the character described in a dictionary
def translate(x_current, y_current):
    tc = [0, 0]
    x_mul = int(canvas["width"]) / (view_size * 2)
    y_mul = (int(canvas["height"]) / (view_size * -2))
    x_current = (x_current + view_size) * x_mul
    y_current = (y_current + view_size) * y_mul + int(canvas["height"])
    tc[0] = x_current
    tc[1] = y_current
    return tc

# drawing the  physical grid with any specified color
def draw_line(x_from, y_from, x_to, y_to, colour):
    from_coord = translate(x_from, y_from)
    to_coord = translate(x_to, y_to)
    if y_to - y_from > view_size * ASYMPTOTE or y_from - y_to > view_size * ASYMPTOTE:
        from_coord = to_coord
        # canvas used to create graphics
    canvas.create_line(from_coord[0], from_coord[1], to_coord[0], to_coord[1], fill=colour)

#color choice 
def draw_grid():
    draw_line(view_size * -1, 0, view_size, 0, "skyblue")
    draw_line(0, view_size * -1, 0, view_size, "skyblue")


def draw_graph(event):
    canvas.delete("all")
    draw_grid()
    y_previous = 0.0
    x = view_size * -1
    while x <= view_size:
        try:
            #eval,evaluates arbitrary Python expressions from a string-based or compiled-code-based input. in this case we evaluate our fourmla input
            y = eval(formula)
        except ValueError:
            # it will not evalute the fourmla if the inputed number were to exceed the expression seen below
            y = 1000000
            x = COMPUTATION_DISTANCE * view_size
            # if the evaluted fourmla is less than 0 then multiply and reasign to -1 
            if eval(formula) < 0:
                y *= -1
        # do not proceed if what has been inputed produces a syntrax error
        except:
            print_formula("SYNTAX ERROR   ")
            # terminate loop and go to the try statement if this is not the case
            break
       # displaying the line on our graph
        try:
            draw_line(x - COMPUTATION_DISTANCE * view_size, y_previous, x, y, "red")
       # the only exeception to the above command is if something is rasied to a negative exponent 
        except:
            print_formula("NON-INT PWR (dbl click ^)   ")
            break
        # terminate loop if this is not the case
        y_previous = y
        x += COMPUTATION_DISTANCE * view_size

# thing in python is essesially a obkect but in this case we refer to it as a potential value. if the fourmla ends wwith a point and thing is equal to the point then accsess elements from the first position
def append_formula(thing):
    global formula
    if formula.endswith('.') and thing == '.':
        formula = formula[:-1]
        formula += ","
    else:
        formula += thing
    print_formula("")

#function clear 1
def clear_formula():
    global formula
    while formula != "":
        delete_formula()
    print_formula("")

#function to delete fourmla elements (-1 repersents one space back) and print new fourmla 
def delete_formula():
    global formula
    formula = formula[:-1]
    print_formula("")

#zoomin in fucntion on calculater with grid location 
def zoom_in():
    global view_size, btn_zoom_in, btn_zoom_out
    btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out()).grid(row=8, column=3)
    if view_size > MIN_SIZE:
        view_size /= INCREMENT
        draw_graph("event")
    if view_size == MIN_SIZE:
        btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in(), state=DISABLED).grid(row=8, column=2)
    draw_graph(None)

#zooming out on calculater function, with grid location
def zoom_out():
    global view_size, btn_zoom_out, btn_zoom_in
    btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in()).grid(row=8, column=2)
   # if veiw size is less then the max size the reassign it to the increment (changing value of variable to increase thus zooming the veiw of graph inwards)
    if view_size < MAX_SIZE:
        view_size *= INCREMENT
        draw_graph("event")
        #zoom out function
    if view_size == MAX_SIZE:
        btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out(),
                                  state=DISABLED).grid(row=8, column=3)
    draw_graph(None)

#endswith() method returns True if a string ends with the given suffix (i,e,x,etc), otherwise returns False
def correct_ending_no_number(name):
    return name.endswith('x') or name.endswith('e') or (name.endswith('i') and name[-2:] != "si") or name.endswith(')')

#function for correct ending of our value
def correct_ending(thing):
    #cuts the string to omit the last character and returns true and flase judging on weather our value is a digit 
    return thing[-1:].isdigit() or correct_ending_no_number(thing)


def append_implicit(thing):
    global formula
    if correct_ending(formula):
        if thing == "**":
            formula += thing
        else:
            formula += "*" + thing
    elif formula[-2:] == "**" and thing == "**":
        formula = formula[:-2]
        if correct_ending(formula):
            formula += "*pow(x,"
        else:
            formula += "pow(x,"
    else:
        formula += thing
    print_formula("")


def append_number_formula(thing):
    global formula
    if correct_ending_no_number(formula) and thing.isdigit():
        formula += "*"
    formula += thing
    print_formula("")

# parenthesses notation function
def append_closing_parentheses_formula(thing):
    global formula
    if correct_ending(formula) and thing == '(':
        formula += "*"
    formula += thing
    print_formula("")

def myclick(number):
    entry.insert(tk.END, number)
 
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    # dont proceed if a error box comes 
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
 
# the clearing function
def clear():
    entry.delete(0, tk.END)

root = Tk()

#title displayed when loaded 
root.wm_title("Graph Sketcher Mark 1-FAISAL")
root.resizable(width=False, height=False)

horizontal_screen = root.winfo_screenwidth() / 2 - root.winfo_reqwidth()
vertical_screen = root.winfo_screenheight() / 2 - root.winfo_reqheight()
root.geometry("+%d+%d" % (horizontal_screen, vertical_screen))

#canvas is used to add structured graphics 
canvas = Canvas(root)

print_formula(" ")


# each row seen below has the text displayed (Lambda can be inside any function that works as an anonymous f) and the psoition of where that specific button will be on the calculater 

#all the buttons for row 2, in varrying columns
ttk.Button(root, text="0", command=lambda: append_number_formula("0")).grid(row=2, column=0)
ttk.Button(root, text="1", command=lambda: append_number_formula("1")).grid(row=2, column=1)
ttk.Button(root, text="2", command=lambda: append_number_formula("2")).grid(row=2, column=2)
ttk.Button(root, text="3", command=lambda: append_number_formula("3")).grid(row=2, column=3)
ttk.Button(root, text="4", command=lambda: append_number_formula("4")).grid(row=2, column=4)

#all the buttons for row 3, in varrying columns
ttk.Button(root, text="5", command=lambda: append_number_formula("5")).grid(row=3, column=0)
ttk.Button(root, text="6", command=lambda: append_number_formula("6")).grid(row=3, column=1)
ttk.Button(root, text="7", command=lambda: append_number_formula("7")).grid(row=3, column=2)
ttk.Button(root, text="8", command=lambda: append_number_formula("8")).grid(row=3, column=3)
ttk.Button(root, text="9", command=lambda: append_number_formula("9")).grid(row=3, column=4)

#all the buttons for row 4, in varrying columns
ttk.Button(root, text="sin", command=lambda: append_implicit("sin(")).grid(row=4, column=0)
ttk.Button(root, text="cos", command=lambda: append_implicit("cos(")).grid(row=4, column=1)
ttk.Button(root, text="tan", command=lambda: append_implicit("tan(")).grid(row=4, column=2)
ttk.Button(root, text="π", command=lambda: append_implicit("pi")).grid(row=4, column=3)
ttk.Button(root, text="e", command=lambda: append_implicit("e")).grid(row=4, column=4)

#all the buttons for row 5, in varrying columns
ttk.Button(root, text="ln", command=lambda: append_implicit("log(")).grid(row=5, column=4)
ttk.Button(root, text="+", command=lambda: append_formula("+")).grid(row=5, column=0)
ttk.Button(root, text="-", command=lambda: append_formula("-")).grid(row=5, column=1)
ttk.Button(root, text="*", command=lambda: append_formula("*")).grid(row=5, column=2)
ttk.Button(root, text="÷", command=lambda: append_formula("/")).grid(row=5, column=3)
ttk.Button(root, text="^", command=lambda: append_implicit("**")).grid(row=5, column=4)

#all the buttons for row 6, in varrying columns
ttk.Button(root, text="(", command=lambda: append_closing_parentheses_formula("(")).grid(row=6, column=0)
ttk.Button(root, text=")", command=lambda: append_formula(")")).grid(row=6, column=1)
ttk.Button(root, text=".", command=lambda: append_formula(".")).grid(row=6, column=2)
ttk.Button(root, text="Delete", command=lambda: delete_formula()).grid(row=6, column=3)
ttk.Button(root, text="Clear", command=lambda: clear_formula()).grid(row=6, column=4)

#all the buttons for row 7, in varrying columns
ttk.Button(root, text="Exit", command=lambda: exit(0)).grid(row=7, column=4)
ttk.Button(root, text="x", command=lambda: append_implicit("x")).grid(row=7, column=0)
btn_enter = ttk.Button(root, text="Enter")
btn_enter.bind('<Button-1>', draw_graph)
btn_enter.grid(row=7, column=1)
btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in()).grid(row=7, column=2)
btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out()).grid(row=7, column=3)
canvas.grid(row=0, column=0, columnspan=5)
draw_grid()
draw_graph("graph")

#rooting the mainloop will loop forever waiting for inputs from the user until they physically exsit the program - the loop will terminate until ran again
root.mainloop()
