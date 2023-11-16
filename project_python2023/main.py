import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar
from PIL import Image, ImageTk

import time
import datetime
import pygame
import random

from MusicPlayer import MusicPlayer

class TabbedWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tabbed Window")
        self.geometry("400x400")

        # Create the tab bar (Notebook)
        self.tab_bar = tk.Notebook(self)
        self.tab_bar.pack(expand=True, fill=tk.BOTH)

        # Create Help tab
        self.help_frame = tk.Frame(self.tab_bar)
        self.tab_bar.add(self.help_frame, text="Help")
        self.help_label = tk.Label(self.help_frame, text="This is the Help tab.")
        self.help_label.pack(pady=20)

        # Create Settings tab
        self.settings_frame = tk.Frame(self.tab_bar)
        self.tab_bar.add(self.settings_frame, text="Settings")
        self.settings_label = tk.Label(self.settings_frame, text="This is the Settings tab.")
        self.settings_label.pack(pady=20)



class SummaryWindow:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(self.parent)
        self.root.title("Work Summary")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Enter your work summary:")
        self.label.pack(pady=10)

        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_summary)
        self.save_button.pack(pady=10, side=tk.LEFT, padx=5)

        self.open_button = tk.Button(self.root, text="Open", command=self.open_summary)
        self.open_button.pack(pady=10, side=tk.LEFT, padx=5)

    def save_summary(self):
        summary = self.text_area.get("1.0", tk.END).strip()
        if summary:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")], initialfile="work_summary.txt")
            if not file_path:  # If the user cancels the save dialog
                return
            with open(file_path, "w") as file:
                file.write(summary + "\n\n")
            messagebox.showinfo("Success", "Summary saved successfully!")
            self.root.destroy()
        else:
            messagebox.showwarning("Warning", "Please enter your summary before saving.")

    def open_summary(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)  # Clear the text area
                    self.text_area.insert(tk.END, content)  # Insert the content of the file
            except FileExistsError:
                print("error")


class DateSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,bg='#113946')
        self.place(x=30, y=70)
        self.calendar = Calendar(self)
        self.calendar.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)


class DailyQuote:
    def __init__(self, parent):
        self.parent = parent
        self.quotes = [
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "The best way to predict the future is to create it. - Abraham Lincoln",
            "Life is what happens when you’re busy making other plans. - John Lennon",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "The purpose of our lives is to be happy. - Dalai Lama"
        ]
        self.show_quote()

    def show_quote(self):
        quote = random.choice(self.quotes)
        messagebox.showinfo("Daily Quote", quote)
    


class Timer:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.second = tk.StringVar()
        self.break_time = tk.StringVar()

    def start_time(self):
            self.running = True
            count = 0
            if not self.remaining_time:
                try:
                    self.remaining_time = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.second.get())
                except ValueError:
                    messagebox.showerror("Error", "Please input valid values.")
                    return

            while self.remaining_time >= 0 and self.running:  # Check if timer is running
                mins, secs = divmod(self.remaining_time, 60)
                hours = 0

                if mins > 60:
                    hours, mins = divmod(mins, 60)

                self.hour.set("{0:02d}".format(hours))
                self.minute.set("{0:02d}".format(mins))
                self.second.set("{0:02d}".format(secs))

                self.update()
                time.sleep(1)

                if self.remaining_time == 0:
                    messagebox.showinfo("Time Countdown", "Time's up")
                    pygame.mixer.music.stop()
                    break

                self.remaining_time -= 1
                count += 1
                if count == int(self.break_time.get())*60:  # Convert break_time to integer
                    messagebox.showinfo(" ", "Break time")
                    count = 0  # Reset the count after showing the break message


    def pause_time(self):
            self.running = False  # Pause the timer

    def stop_time(self):
            self.running = False  # Stop the timer
            self.remaining_time = None  # Reset the remaining time
            self.hour.set("00")   # Reset the timer
            self.minute.set("00")
            self.second.set("00")

    def continue_time(self):
            if not self.running and self.remaining_time:
                self.start_time()  # Continue the timer

    def update_timer(self):
            if self.temp >= 0:
                mins, secs = divmod(self.temp, 60)
                hours = 0

                if mins > 60:
                    hours, mins = divmod(mins, 60)

                self.hour.set("{0:02d}".format(hours))
                self.minute.set("{0:02d}".format(mins))
                self.second.set("{0:02d}".format(secs))

                self.temp -= 1
                self.count += 1
                if self.count == 10:
                    messagebox.showinfo(" ", "Break time")
                    self.count = 0

                # Schedule the next update after 1000ms (1 second)
                self.after(1000, self.update_timer)
            else:
                messagebox.showinfo("Time Countdown", "Time's up")
            
    def plus_one_hour(self):
            x = int(self.hour.get()) + 1
            self.hour.set("{0:02d}".format(x))

    def take_one_hour(self):
            x = int(self.hour.get()) - 1
            if x >= 0:
                self.hour.set("{0:02d}".format(x))

    def plus_one_minutes(self):
            x = int(self.minute.get()) + 1
            self.minute.set("{0:02d}".format(x))

    def take_one_minutes(self):
            x = int(self.minute.get()) - 1
            if x >= 0:
                self.minute.set("{0:02d}".format(x))
        
    def plus_one_second(self):
            x = int(self.second.get()) + 1
            self.second.set("{0:02d}".format(x))

    def take_one_second(self):
            x = int(self.second.get()) - 1
            if x >= 0:
                self.second.set("{0:02d}".format(x))

class Setting_window:
    def open_help_window(self):
        self.help_window = tk.Toplevel(self)
        self.help_window.title("Help")
        self.help_window.geometry("1000x600")

        bg = '#113946'
        # List of image paths
        image_paths = [
            r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\app_instructions.png"
        ]

        # Assuming you want to use the first image in the list
        image_path = image_paths[0]

        # Load the image
        raw_image = Image.open(image_path)
        resized_image = raw_image.resize((1000, 600))  # Adjust the size as needed
        self.random_image = ImageTk.PhotoImage(resized_image)  # Store as instance variable

        # Display the image
        self.image_label = tk.Label(self.help_window, image=self.random_image)  # Changed from self.main_ui to self.help_window
        self.image_label.place(x=0, y=0)  # Adjusted the position to (0, 0) for better placement

    
    
    def open_settings_window(self):
        # Create a new window for settings
        self.settings_window = tk.Toplevel(self)
        self.settings_window.title("Settings")
        self.settings_window.geometry("150x130")

        label = tk.Label(self.settings_window, text="break time in minutes")
        label.place(x=18,y=3)

        label = tk.Label(self.settings_window, textvariable=self.break_time,font=("Arial", 10))
        label.pack(pady=20)


            
        # Place the buttons on the settings window
        self.plus_one_mm_break_button = tk.Button(self.settings_window, text="+", relief=tk.RAISED, bg='#113946', fg="white", command=self.plus_one_m_break)
        self.plus_one_mm_break_button.place(x=42, y=50)

        self.minus_one_mm_break_button = tk.Button(self.settings_window, text="-", relief=tk.RAISED, bg='#113946', fg="white", command=self.take_one_m_break)
        self.minus_one_mm_break_button.place(x=92, y=50)

    def plus_one_m_break(self):
        # Assuming self.break_time is an instance of tkinter's StringVar
        current_value = int(self.break_time.get())
        self.break_time.set(str(current_value + 1))

    def take_one_m_break(self):
        current_value = int(self.break_time.get())
        self.break_time.set(str(current_value - 1))


class Calender:
    def on_date(self):
        selected_date_str = self.date_selector.calendar.get_date()
        selected_date = datetime.datetime.strptime(selected_date_str, "%m/%d/%y").date()  # Convert string to date
        today = datetime.date.today()
        days_left = (selected_date - today).days

        if days_left > 0:
            self.message = f"{selected_date_str} is in {days_left} days left."
        elif days_left == 0:
            self.message = f"{selected_date_str} is today!"
        else:
            self.message = f"{selected_date_str} was {-days_left} days ago."

        self.empthy = tk.Label(self, text=" ",bg="#113946")
        self.empthy.place(x=10, y=30,width=400,height=40)
        self.selected_date_show = tk.Label(self, text=self.message, font=("LilyUPC", 35),bg='#113946',fg = "white")
        self.selected_date_show.place(x=15, y=30)  # Adjust the position as needed
        
    def clear_date(self):
        self.selected_date_show.config(text="")

class MainMenu(tk.Tk,Timer,Setting_window,Calender,DailyQuote,DateSelector,SummaryWindow,TabbedWindow):
    def __init__(self):
        super().__init__()
        self.title("Project learner")
        self.geometry("800x600")
        self.configure(bg='#113946')
        self.music_player = MusicPlayer(self, self)
        
         
        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.second = tk.StringVar()
        self.break_time = tk.StringVar()
        self.show_image = False

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        self.break_time.set("25")

        self.hour_entry = tk.Entry(self, width=0, font=("Arial", 60, ""),bg='#113946',fg="white", textvariable=self.hour)
        self.hour_entry.place(x=450, y=20)

        self.minute_entry = tk.Entry(self, width=0, font=("Arial", 60, ""),bg='#113946',fg="white", textvariable=self.minute)
        self.minute_entry.place(x=550, y=20)

        self.second_entry = tk.Entry(self, width=0, font=("Arial", 60, ""),bg='#113946',fg="white", textvariable=self.second)
        self.second_entry.place(x=650, y=20)

        self.h = tk.Label(self,text="hours",font=("LilyUPC", 14),bg='#113946',fg = "white")
        self.h.place(x=480,y=120)

        self.m = tk.Label(self,text="minute",font=("LilyUPC", 14),bg='#113946',fg = "white")
        self.m.place(x=580,y=120)

        self.s = tk.Label(self,text="second",font=("LilyUPC", 14),bg='#113946',fg = "white")
        self.s.place(x=680,y=120)

        # self.start_button = tk.Button(self, text="Start Countdown", bd='5', command=self.timer_app.start_time)
        # self.start_button.place(x=70, y=120)
        
        # hour_show = tk.Label(self, text="00:00:00", font=("LilyUPC", 10))
        # hour_show.place(x=200, y=30)
        
        
    #start_time
        
        start_time_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\start_time.png")
        resized_start_time_button_image = start_time_button_image_raw.resize((50, 50))
        self.start_time_button_image = ImageTk.PhotoImage(resized_start_time_button_image)
        self.start_time_button = tk.Button(self, image=self.start_time_button_image, bg='#113946', command=self.start_time)
        self.start_time_button.place(x=470, y=150)

    # Add buttons for pause and stop functionality
        
        play_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\play_botton.png")
        pause_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\pause_botton.png")    
        stop_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\stop_botton.png")

        resized_play_button_image = play_button_image.resize((50, 50))
        resized_pause_button_image = pause_button_image.resize((50, 50))
        resized_stop_button_image = stop_button_image.resize((50, 50))

        self.play_botton = ImageTk.PhotoImage(resized_play_button_image)
        self.pause_botton = ImageTk.PhotoImage(resized_pause_button_image)
        self.stop_botton = ImageTk.PhotoImage(resized_stop_button_image)

        self.pause_button = tk.Button(self, image=self.pause_botton,bg='#113946', command=self.pause_time)
        self.pause_button.place(x=540, y=150)

        self.cotinue_button = tk.Button(self, image=self.play_botton,bg='#113946',command=self.continue_time)
        self.cotinue_button.place(x=610, y=150)

        self.stop_button = tk.Button(self, image=self.stop_botton,bg='#113946', command=self.stop_time)
        self.stop_button.place(x=680, y=150)



    #date_calender
        date_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\date.png")
        resized_date_button_image = date_button_image_raw.resize((50, 50))
        self.date_button_image = ImageTk.PhotoImage(resized_date_button_image)
        self.date_button = tk.Button(self, image=self.date_button_image, bg='#113946', command=self.on_date)
        self.date_button.place(x=135, y=300)
        self.date_clear_botton = tk.Button(self, text="clear",bg='#113946',fg = "white", command=self.clear_date)
        self.date_clear_botton.place(x=145, y=357)
        
    #open_note
        notes_open_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\notes_open_botton.png")
        resized_notes_open_botton_image = notes_open_button_image_raw.resize((50, 50))
        self.notes_open_button_image = ImageTk.PhotoImage(resized_notes_open_botton_image)
        self.notes_open_button = tk.Button(self, image=self.notes_open_button_image, bg='#113946', command=self.summary_window_open)
        self.notes_open_button.place(x=100, y=465)
        # self.open_shortnote = tk.Label(self, text="Open note", font=("LilyUPC", 50),bg='#113946',fg="white")
        # self.open_shortnote.place(x=80, y=450)
        
    #open_file
        open_file_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\open_file.png")
        resized_open_file_botton_image = open_file_button_image_raw.resize((50, 50))
        self.open_file_button_image = ImageTk.PhotoImage(resized_open_file_botton_image)
        self.open_file_button = tk.Button(self, image=self.open_file_button_image, bg='#113946', command=self.open_summary)
        self.open_file_button.place(x=180, y=465)
        
        self.date_selector = DateSelector(self)
        self.daily_quote = DailyQuote(self)
        
        self.remaining_time = None
        self.running = False

    #botton number hour minutes second
        self.plus_one_hour_button = tk.Button(self, text="+",bg='#113946',fg = "white" , command=self.plus_one_hour)
        self.plus_one_hour_button.place(x=460, y=120)
        self.minus_one_hour_button = tk.Button(self, text="-",bg='#113946',fg = "white" , command=self.take_one_hour)
        self.minus_one_hour_button.place(x=520, y=120)

        self.plus_one_minutes_button = tk.Button(self, text="+",bg='#113946',fg = "white" , command=self.plus_one_minutes)
        self.plus_one_minutes_button.place(x=560, y=120)
        self.minus_one_minutes_button = tk.Button(self, text="-",bg='#113946',fg = "white" , command=self.take_one_minutes)
        self.minus_one_minutes_button.place(x=620, y=120)

        self.plus_one_second_button = tk.Button(self, text="+",bg='#113946',fg = "white" , command=self.plus_one_second)
        self.plus_one_second_button.place(x=660, y=120)
        self.minus_one_second_button = tk.Button(self, text="-",bg='#113946',fg = "white" , command=self.take_one_second)
        self.minus_one_second_button.place(x=720, y=120)

        settings_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\settings_botton.png")
        resized_settings_button_image = settings_button_image_raw.resize((70, 70))
        self.settings_button_image = ImageTk.PhotoImage(resized_settings_button_image)

        # Create a frame with the desired size
        self.settings_button_frame = tk.Frame(self, width=40, height=40, bg='#113946')  # Adjust width and height as needed
        self.settings_button_frame.place(x=760, y=0)
        self.settings_button_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its content

        # Create the button inside the frame
        self.settings_button = tk.Button(self.settings_button_frame, image=self.settings_button_image, bg='#113946', command=self.open_settings_window)
        self.settings_button.pack(fill=tk.BOTH, expand=True)

        #help button
        
        help_button_image_raw = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\help_button.png")
        resized_help_button_image = help_button_image_raw.resize((70, 70))
        self.help_button_image = ImageTk.PhotoImage(resized_help_button_image)

        self.help_button_frame = tk.Frame(self, width=40, height=40, bg='#113946')  # Adjust width and height as needed
        self.help_button_frame.place(x=760, y=40)
        self.help_button_frame.pack_propagate(False)
        
        self.help_button = tk.Button(self.help_button_frame, image=self.help_button_image, bg='#113946', command=self.open_help_window)
        self.help_button.pack(fill=tk.BOTH, expand=True)

    def open_tabbed_window(self):
        TabbedWindow(self)


    def summary_window_open(self):
        SummaryWindow(self)

    def summary_window_open(self):
        self.summary_window = SummaryWindow(self)
    
    def open_summary(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:  # Check if a file was selected
            with open(file_path, "r") as file:
                content = file.read()
                # Display the content. You can decide how you want to display it.
                # For instance, you can show it in a new window or a messagebox.
                messagebox.showinfo("Summary", content)

app = MainMenu()
app.mainloop()