import tkinter as tk
from tkcalendar import Calendar

class DateSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,bg='#113946')
        self.place(x=30, y=70)
        self.calendar = Calendar(self)
        self.calendar.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
        

    