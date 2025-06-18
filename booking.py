# booking.py
import tkinter as tk
from tkinter import messagebox
from database import connect_db

def open_booking_page(master):
    booking_window = tk.Toplevel(master)
    booking_window.title("Book Flight")
    booking_window.geometry("1000x700")
    booking_window.configure(bg="#f0f8ff")
    booking_window.resizable(False, False)

    # عنوان الصفحة
    tk.Label(
        booking_window,
        text="Book a Flight",
        font=("Helvetica", 16, "bold"),
        fg="#333",
        bg="#f0f8ff"
    ).pack(pady=20)

    # إطار يحتوي على الحقول بشكل مرتب
    form_frame = tk.Frame(booking_window, bg="#f0f8ff")
    form_frame.pack(pady=10)

    labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label + ":", bg="#f0f8ff", anchor="w", font=("Arial", 11)).grid(row=i, column=0, sticky="w", padx=10, pady=8)
        entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
        entry.grid(row=i, column=1, padx=10, pady=8)
        entries.append(entry)

    # زر الحجز
    def save_booking():
        values = [e.get().strip() for e in entries]
        if "" in values:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, values)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Flight booked successfully.")
        booking_window.destroy()

    # زرار Submit
    tk.Button(
        booking_window,
        text="Submit",
        font=("Arial", 12),
        bg="#007acc",
        fg="white",
        activebackground="#005f99",
        activeforeground="white",
        padx=15,
        pady=6,
        bd=0,
        cursor="hand2",
        command=save_booking
    ).pack(pady=20)
