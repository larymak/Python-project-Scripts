import ttkbootstrap as ttk
import tkinter as tk
from configuration import TOP_LEVEL


class TopLevel(tk.Toplevel):
    def __init__(
            self, parent,
            hour_int, minute_int,
            ok_function, cancel_function
            ):
        super().__init__(master = parent)
        
        # set attributes
        
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('Clock')
        self.set_geometry(width = TOP_LEVEL['WIDTH'], height = TOP_LEVEL['HEIGHT'])
        
        # set data
        self.hour_int = hour_int
        self.minute_int = minute_int
        
        # set style
        self.top_level_style = ttk.Style()
        
        # The OK  button style
        self.top_level_style.configure(
                style = 'OK.TButton',
                anchor = 'center',
                background = '#303030',
                bordercolor = '#303030',
                font = ('Helvetica', 15, 'bold'),
                )
        self.top_level_style.map(
                style = 'OK.TButton',
                background = [('active', '#526170')],
                bordercolor = '#303030'
                )
        
        # The CANCEL button style
        self.top_level_style.configure(
                style = 'CANCEL.TButton',
                anchor = 'center',
                background = '#303030',
                bordercolor = '#303030',
                font = ('Helvetica', 15, 'bold'),
                )
        self.top_level_style.map(
                style = 'CANCEL.TButton',
                background = [('active', '#526170'), ],
                bordercolor = '#303030'
                )
        # The spinbox
        self.top_level_style.configure(
                style = 'PAUSE.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                
                )
        self.top_level_style.configure(
                style = 'Clock.TSpinbox',
                anchor = 'center',
                arrowsize = 30,
                )
        self.top_level_style.map(
                style = 'Clock.TSpinbox',
                )
        
        # create widgets
        
        # Create the Hour Spin
        self.hour_spin = ttk.Spinbox(
                master = self,
                style = 'Clock.TSpinbox',
                textvariable = self.hour_int,
                font = ('Helvetica', 20, 'bold'),
                from_ = 0,
                to = 23,
                )
        
        # Create the ":"
        self.space_label = ttk.Label(
                master = self,
                style = 'PAUSE.TLabel',
                text = ':'
                )
        
        # Create the Minute Spin
        self.minute_spin = ttk.Spinbox(
                master = self,
                style = 'Clock.TSpinbox',
                textvariable = self.minute_int,
                font = ('Helvetica', 20, 'bold'),
                from_ = 0,
                to = 59,
                )
        
        # Create the OK button
        self.ok_button = ttk.Button(
                master = self,
                text = 'OK',
                style = 'OK.TButton',
                command = ok_function
                
                )
        # Create the CANCEL button
        self.cancel_button = ttk.Button(
                master = self,
                text = 'Cancel',
                command = cancel_function,
                style = 'CANCEL.TButton',
                )
        
        # layout
        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
        
        # first row
        self.hour_spin.grid(row = 1, column = 0)
        self.space_label.grid(row = 1, column = 1)
        self.minute_spin.grid(row = 1, column = 2)
        
        # second row(the button)
        self.ok_button.grid(row = 2, column = 0, sticky = 'news')
        self.cancel_button.grid(row = 2, column = 2, sticky = 'news')
        
        # set the top level to be the main
        self.grab_set()
    
    def set_geometry(self, width: int, height: int) -> None:
        """
         It make the windows to be in the center of your desktop.
         The formula is down and you could found on the internet explained very well :)
        """
        desktop_height = self.winfo_screenheight()  # it take your desktop height
        desktop_width = self.winfo_screenwidth()  # it take your desktop width
        window_top = int((desktop_height - height) / 2)
        window_left = int((desktop_width - width) / 2)
        self.geometry(f'{width}x{height}+{window_left}+{window_top}')
