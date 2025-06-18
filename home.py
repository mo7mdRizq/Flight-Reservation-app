# home.py
import tkinter as tk
from booking import open_booking_page
from reservastions import open_reservations_page

class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#f0f8ff")

        self.frame = tk.Frame(master, bg="#f0f8ff")
        self.frame.pack(expand=True)

        tk.Label(
            self.frame,
            text="Flight Reservation System",
            font=("Helvetica", 18, "bold"),
            fg="#333",
            bg="#f0f8ff"
        ).pack(pady=30)

        button_style = {
            "width": 20,
            "font": ("Arial", 12),
            "bg": "#007acc",
            "fg": "white",
            "bd": 0,
            "activebackground": "#005f99",
            "activeforeground": "white",
            "cursor": "hand2",
            "pady": 5
        }

        tk.Button(self.frame, text="Book Flight", command=lambda: open_booking_page(master), **button_style).pack(pady=10)
        tk.Button(self.frame, text="View Reservations", command=lambda: open_reservations_page(master), **button_style).pack(pady=10)
