import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from quad import Quadratic
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from ttkbootstrap.dialogs import Messagebox

# Most variables are named a,b,c according to ax² + bx + c in a quadratic equation


def plot():

    # Collect all inputs
    a_entryInput  = a_entry.get()
    b_entryInput = b_entry.get()
    c_entryInput = c_entry.get()
    
    try:
        a = float(a_entryInput)
        b = float(b_entryInput)
        c = float(c_entryInput)
        eqn = Quadratic(a,b,c)

        #--------------------------------------------------------------------------
        # Background Graph Frame
        graph_frame = ScrolledFrame(root, width = 800, height = 500)
        graph_frame.grid(row = 1, column  = 0,pady = 10)

        fig = eqn.drawFigure()

        canvas = FigureCanvasTkAgg(figure = fig, master = graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, graph_frame)
        toolbar.update()

        canvas.get_tk_widget().pack()
        solution_label.config(text = "Solution : x₁ = {0}, x₂ = {1}".format(eqn.solveQuad()[0], eqn.solveQuad()[1]))
        
    except:
        Messagebox.show_error(title = "Error", message = "User entered wrong value")
 


# Base window widget
root = tb.Window(themename="vapor")
root.geometry("720x720")
root.title("Quadratic Equation Solver")

# Font data
font = ("Nunito", 12)

# Frame containig the entry for the three arguments
top_frame = tb.Frame(root)
top_frame.grid(row = 0, column = 0,padx  = 10, pady = 20)

# Entry for the three arguments
a_frame = tb.Frame(top_frame)
a_frame.grid(row = 0, column = 0, padx=5)

a_label = tb.Label(a_frame, text= "a =", font = font)
a_label.grid(row = 0, column = 0)

a_entry = tb.Entry(a_frame, width = 30, font = font)
a_entry.grid(row = 0, column = 1)

b_frame = tb.Frame(top_frame)
b_frame.grid(row = 0, column = 1, padx=5)

b_label = tb.Label(b_frame, text = "b =", font = font)
b_label.grid(row = 0, column = 0)

b_entry = tb.Entry(b_frame, width = 30, font = font)
b_entry.grid(row = 0, column = 1)

c_frame = tb.Frame(top_frame)
c_frame.grid(row = 0, column = 2, padx=5)

c_label = tb.Label(c_frame, text = "c =", font = font)
c_label.grid(row = 0, column = 0)

c_entry = tb.Entry(c_frame, width = 30, font = font)
c_entry.grid(row = 0, column = 1)


# Button to plot the matplotlib graph
plot_button = tb.Button(top_frame, width = 70, text = "Plot", command = plot)
plot_button.grid(row = 1, column = 1, pady = 15)

# Label containing the solution to the equation
solution_label = tb.Label(root,font = (font[0], 15), text = "")
solution_label.grid(row = 2, column = 0, pady = 10)

root.mainloop()