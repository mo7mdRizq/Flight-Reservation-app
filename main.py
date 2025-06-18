# main.py
import tkinter as tk
from database import create_table
from home import HomePage

if __name__ == "__main__":
    create_table()

    root = tk.Tk()
    root.title("Flight Reservation System")
    #root.geometry("1000x700")

    window_width = 1000
    window_height = 700

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = HomePage(root)
    root.mainloop()
