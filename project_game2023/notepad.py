import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import Calendar

class MusicPlayer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=1, column=0, padx=430, pady=400)

        self.load_button = tk.Button(self, text="Load Music")
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        self.play_button = tk.Button(self, text="Play")
        self.play_button.grid(row=0, column=1, padx=10, pady=10)

        self.pause_button = tk.Button(self, text="Pause")
        self.pause_button.grid(row=0, column=2, padx=10, pady=10)

        self.resume_button = tk.Button(self, text="Resume")
        self.resume_button.grid(row=0, column=3, padx=10, pady=10)

        self.stop_button = tk.Button(self, text="Stop")
        self.stop_button.grid(row=0, column=4, padx=10, pady=10)

        self.name_music_label = tk.Label(parent, text="", font=("Arial", 12))
        self.name_music_label.place(x=580, y=450)

        self.time_label = tk.Label(self, text="", font=("Arial", 12))
        self.time_label.grid(row=1, column=0, columnspan=5)

class DateSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=30, y=70)
        self.calendar = Calendar(self)
        self.calendar.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("800x600")
        
        self.timer_label = tk.Label(self, text="00:00:00", font=("LilyUPC", 80))
        self.timer_label.place(x=430, y=50)
        
        self.open_timer_button = tk.Button(self, text="Set Time", font=("LilyUPC", 20))
        self.open_timer_button.place(x=560, y=150)
        
        self.confirm_button = tk.Button(self, height=2, width=5, text="Select", font=("LilyUPC", 20))
        self.confirm_button.place(x=135, y=330)
        
        self.summary_window_button = tk.Button(self, text="Open", font=("LilyUPC", 20))
        self.summary_window_button.place(x=140, y=520)

        self.open_shortnote = tk.Label(self, text="Open note", font=("LilyUPC", 50))
        self.open_shortnote.place(x=80, y=450)
        
        self.date_selector = DateSelector(self)
        self.music_player = MusicPlayer(self)

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
