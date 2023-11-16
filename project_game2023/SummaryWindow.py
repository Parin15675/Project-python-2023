import tkinter as tk
from tkinter import messagebox, filedialog

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
