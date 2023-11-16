import tkinter as tk
from tkinter import messagebox
import random

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