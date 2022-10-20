import tkinter as tk
from tkinter import ttk
from tkinter.constants import  RAISED

# Importing the user defined module.
import Functionality as fn

def main():

    # Root window
    main_window = tk.Tk()
    main_window.title("Downtube")               # Title of the window
    main_window.minsize(600, 400)             # Default Window size
    main_window.rowconfigure(0,weight=1)        # Rowconfiguration of root window in order to expand widgets, when window is is resized.
    main_window.columnconfigure(0, weight= 1)   # Rowconfiguration of root window in order to expand widgets, when window is is resized.
    main_window.rowconfigure(1,weight=1)        # Rowconfiguration of root window in order to expand widgets, when window is is resized. ###
    main_window.columnconfigure(1, weight= 1)   # Rowconfiguration of root window in order to expand widgets, when window is is resized. ###
    main_window.configure(bg= "white")          # Background color for root window

# Parent Frame widgets:

    # Input frame widget.
    main_frame = tk.Frame(main_window,  borderwidth= 2,bg= "white")
    main_frame.grid(row= 0, column= 0, columnspan= 3, rowspan= 4)

    # Configuration of row and column of "main_frame" in order to expand widgets, when window is is resized.
    main_frame.columnconfigure(0, weight= 1)
    main_frame.columnconfigure(1, weight= 1)
    main_frame.columnconfigure(2, weight= 1)
    main_frame.rowconfigure(0, weight= 1)
    main_frame.rowconfigure(1, weight= 1)
    main_frame.rowconfigure(2, weight= 1)
    main_frame.rowconfigure(3, weight= 1)

# main_frame widgets

    # Display label indicating --> 'paste the youtube link'.
    linke_label = tk.Label(main_frame, text= "Paste the YouTube link", width= 40, borderwidth= 1, anchor= "w", bg= "white")
    linke_label.grid(row= 0, column= 1, sticky="WE", pady= 2)

    # Display  label indicating --> 'Browse to save the file'.
    linke_label = tk.Label(main_frame, text= "Browse to save the file", bg= "white", width= 40, anchor= "w")
    linke_label.grid(row= 2, column= 1)

    # Display  label indicating --> 'Choose the resolution'.
    resolution_lb = tk.Label(
                        main_frame, text= "Choose the resolution", width= 15,
                        height= 1, anchor= "w", bg= "white"
                        )
    resolution_lb.grid(row=4, column= 1, pady=2, sticky= "we")


    # Entry Widget --> Getting youtube link.
    link = tk.StringVar()
    get_link = tk.Entry(main_frame, textvariable= link, bg= "white")
    get_link.grid(row= 1, column= 1, sticky= "wE", pady= 2)

    # Entry Widget --> Getting Directory to save file.
    directory = tk.StringVar()
    get_dir = tk.Entry(main_frame,textvariable= directory, bg= "white", fg= "grey")
    get_dir.grid(row= 3, column= 1, sticky= "wE")
    get_dir.insert(0, "Choose a folder")

    # Combo box Widget --> Shows the options(Resolution) available.
    my_string_var = tk.StringVar()
    resolution_box = ttk.Combobox(
                            main_frame, textvariable=my_string_var,
                            values=["360p", "720p"])
    resolution_box.grid(row=5, column= 1, pady=2, sticky= "we")

    # Button widget --> Clear the Input field of youtube entry widget
    clear_bt = tk.Button(
                        main_frame, text= "Clear",
                        width= 10, height= 1,
                        bg= "grey",
                        command= lambda: fn.clear(link, get_link)
                        )
    clear_bt.grid(row= 1, column= 2, pady= 2)

    # Button widget --> Opens file explorer to save the file
    temp_bt = tk.Button(
                        main_frame, text= "Browse",
                        relief= RAISED, width= 10,
                        height= 1, bg= "grey",
                        command= lambda :fn.browse_folder(get_dir)
                        )
    temp_bt.grid(row=3, column= 2, pady=2)

    # Button widget --> Downloads the video
    download_file = tk.Button(
                        main_frame, text= "Download",
                        relief= RAISED, width= 10,
                        height= 1, bg= "grey", anchor= "center",
                        command= lambda :fn.download_bt(link.get(), get_link, resolution_box.get(), directory.get(), get_dir, resolution_box)
                        )
    download_file.grid(row=5, column= 2, pady=2)

    main_window.mainloop()

if __name__ == '__main__':
    main()
