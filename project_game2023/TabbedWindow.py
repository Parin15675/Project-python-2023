import tkinter as tk
from tkinter import ttk

class TabbedWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tabbed Window")
        self.geometry("400x400")

        # Create the tab bar (Notebook)
        self.tab_bar = ttk.Notebook(self)
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

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    tabbed_window = TabbedWindow(root)
    root.mainloop()
