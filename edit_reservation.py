# edit_reservation.py
import tkinter as tk
from tkinter import messagebox
from database import connect_db

def open_edit_page(master, reservation):
    edit_window = tk.Toplevel(master)
    edit_window.title("Edit Reservation")
    edit_window.geometry("600x500")
    edit_window.configure(bg="#f0f8ff")
    edit_window.resizable(False, False)

    # عنوان الصفحة
    tk.Label(
        edit_window,
        text="Edit Reservation",
        font=("Helvetica", 16, "bold"),
        fg="#333",
        bg="#f0f8ff"
    ).pack(pady=20)

    form_frame = tk.Frame(edit_window, bg="#f0f8ff")
    form_frame.pack(pady=10)

    labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label + ":", bg="#f0f8ff", font=("Arial", 11), anchor="w").grid(row=i, column=0, sticky="w", padx=10, pady=8)
        entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
        entry.insert(0, reservation[i+1])  # نبدأ من index 1 لأن index 0 هو الـ ID
        entry.grid(row=i, column=1, padx=10, pady=8)
        entries.append(entry)

    def update_reservation():
        updated_values = [e.get().strip() for e in entries]

        if "" in updated_values:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        """, (*updated_values, reservation[0]))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation updated successfully.")
        edit_window.destroy()

    tk.Button(
        edit_window,
        text="Update",
        font=("Arial", 12),
        bg="#007acc",
        fg="white",
        activebackground="#005f99",
        activeforeground="white",
        padx=15,
        pady=6,
        bd=0,
        cursor="hand2",
        command=update_reservation
    ).pack(pady=20)
