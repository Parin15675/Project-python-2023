import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import filedialog
import time
import pygame
import random
from PIL import Image, ImageTk
from tkinter import simpledialog


class MusicPlayer(tk.Frame):
    def __init__(self, parent, main_ui):
        super().__init__(parent,bg='#113946')
        self.main_ui = main_ui 
        self.grid(row=1, column=0, padx=430, pady=400)
        # self.number_loop_number = tk.StringVar()
        # self.number_loop_number.set("0")
        self.number_loop_number = 0
        
        pygame.init()
        pygame.mixer.init()
        
        self.music_file = None  # เพิ่มตัวแปรเพื่อจัดเก็บไฟล์เพลง
        self.paused = False     # เพิ่มตัวแปรสถานะการหยุดชั่วคราว
        self.current_music = None  # เพิ่มตัวแปรเก็บเพลงปัจจุบัน
        self.playing = False  # เพิ่มตัวแปรสถานะการเล่นเพลง
        self.show_random_image_check = False
        # โหลดรูปภาพ
        play_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\play_botton.png")
        pause_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\pause_botton.png")
        resume_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\play_botton.png")        
        stop_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\stop_botton.png")
        open_music_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\open_music.png")
        loop_button_image = Image.open(r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\loop_button.png")
        
        

        resized_play_button_image = play_button_image.resize((50, 50))
        resized_pause_button_image = pause_button_image.resize((50, 50))
        resized_resume_button_image = resume_button_image.resize((50, 50))
        resized_stop_button_image = stop_button_image.resize((50, 50))
        resized_open_music_button_image = open_music_button_image.resize((50, 50))
        resized_loop_music_button_image = loop_button_image.resize((50, 50))

        self.play_botton = ImageTk.PhotoImage(resized_play_button_image)
        self.pause_botton = ImageTk.PhotoImage(resized_pause_button_image)
        self.resume_botton = ImageTk.PhotoImage(resized_resume_button_image)
        self.stop_botton = ImageTk.PhotoImage(resized_stop_button_image)
        self.open_music = ImageTk.PhotoImage(resized_open_music_button_image)
        self.loop_music = ImageTk.PhotoImage(resized_loop_music_button_image)

        self.open_music_botton = tk.Button(self, image=self.open_music,bg="#113946", command=self.load_music)
        self.open_music_botton.grid(row=0, column=0, padx=5, pady=100)  # ใช้ grid แทน

        # self.play_image_button = tk.Button(self, image=self.play_botton, bg="#113946",command=self.play_music)
        # self.play_image_button.grid(row=0, column=1, padx=10, pady=100)
        
        self.pause_button_image_button = tk.Button(self, image=self.pause_botton,bg="#113946", command=self.pause_music)
        self.pause_button_image_button.grid(row=0, column=2, padx=5, pady=100)
        
        self.resume_button_image_botton = tk.Button(self, image=self.resume_botton,bg="#113946", command=self.resume_music)
        self.resume_button_image_botton.grid(row=0, column=3, padx=5, pady=10)  # ใช้ grid แทน
        
        self.stop_button = tk.Button(self, image=self.stop_botton,bg="#113946", command=self.stop_music)
        self.stop_button.grid(row=0, column=4, padx=5, pady=10)  # ใช้ grid แทน

        self.loop_button = tk.Button(self, image=self.loop_music, bg="#113946", command=self.ask_and_play_loop)
        self.loop_button.grid(row=0, column=5, padx=5, pady=10)  # Adjust the grid position as needed

        
        self.name_music_label = tk.Label(parent, text=self.number_loop_number, font=("Arial", 12), bg='#113946',fg ="white")
        self.name_music_label.grid(row=1, column=5, padx=5, pady=10)

        self.name_music_label = tk.Label(parent, text="", font=("Arial", 12), bg='#113946',fg ="white")
        self.name_music_label.place(x=430,y=450)  # แสดง Label ในหน้าต่างหลัก

        
        self.loop_music_label = tk.Label(parent, text=f"loop : {self.number_loop_number}", font=("Arial", 12), bg='#113946',fg ="white")
        self.loop_music_label.place(x=700,y=560)

        self.time_label = tk.Label(self, text="", font=("Arial", 12))
        self.time_label.grid(row=1, column=0, columnspan=5)  # แสดงเวลาที่อยู่ใน row 1

        
    def show_random_image(self):
        bg='#113946'
        # List of image paths
        image_paths = [
            r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b1.png"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b2.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b3.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b4.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b5.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b6.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b7.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b8.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b9.jpg"
            ,r"C:\Users\ASUS\OneDrive\เดสก์ท็อป\Se\python\project_game2023\image\b10.jpg"
        ]

        # Select a random image path
        random_image_path = random.choice(image_paths)

        # Load the image
        raw_image = Image.open(random_image_path)
        resized_image = raw_image.resize((350, 180))  # Adjust the size as needed
        self.random_image = ImageTk.PhotoImage(resized_image)  # Store as instance variable
        

        # Display the image
        self.image_label = tk.Label(self.main_ui, image=self.random_image)
        self.image_label.place(x=400, y=250)


            
    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            
    def resume_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            
    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False
        self.playing = False
        self.image_label.place_forget()  # Hide the image label
        self.name_music_label.place_forget()  # Hide the name music label

    def get_music_name(self):
        return self.music_file.split("/")[-1] if self.music_file else ""
    
    def load_music(self):
        pygame.mixer.init()  # Ensure the mixer is initialized

        self.music_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])

        # Check if a file was selected
        if not self.music_file:
            return

        try:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

            music_name = self.get_music_name()
            self.show_name_music(music_name)
            self.current_music = self.music_file
            self.paused = False
            self.playing = True
            # Show the random image
            self.show_random_image()
            self.name_music_label.place(x=430, y=450)  # Show the name music label again
        except pygame.error as e:
            print(f"Failed to play {self.music_file}. Error: {e}")
            
    def show_name_music(self, music_name):
        self.name_music_label.config(text=f"{music_name}")

    def play_music_loop(self):
        while True:
            if self.playing:
                pos = pygame.mixer.music.get_pos()
                if pos != -1:
                    minutes, seconds = divmod(pos // 1000, 60)
                    hours, minutes = divmod(minutes, 60)
                    self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.update()
            time.sleep(1)
    
    def play_music_loop(self, loops=1):
        """
        Play the music in a loop for a specified number of times.

        :param loops: Number of times to loop the music. Default is 0 (play once).
        """
        self.loops = 1
        
        if self.music_file:  # Check if a music file is loaded
            pygame.mixer.music.play(self.loops)
            # self.number_loop_number.set(f"{loops}")  # Play the music in a loop for the specified number of times
        

    def ask_and_play_loop(self):
        loops = simpledialog.askinteger("Loop Music", "How many times do you want to loop the music?", parent=self.main_ui)
        
        # Check if the user provided a value
        if loops is not None:
            self.loops = loops
            self.number_loop_number = loops
            self.loop_music_label.config(text=f"loop : {loops}")  # Update the loop label text
            
            # If music is currently playing, stop it and play the new looped music
            if self.playing:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(loops=self.loops-1)  # pygame counts the first play as one loop


        # Add a button to loop the music
