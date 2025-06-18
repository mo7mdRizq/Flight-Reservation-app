# reservations.py
import tkinter as tk
from tkinter import messagebox
from database import connect_db
from edit_reservation import open_edit_page

def open_reservations_page(master):
    reservations_window = tk.Toplevel(master)
    reservations_window.title("All Reservations")
    reservations_window.geometry("1000x700")
    reservations_window.configure(bg="#f0f8ff")
    reservations_window.resizable(False, False)

    # العنوان
    tk.Label(reservations_window, text="All Reservations", font=("Helvetica", 16, "bold"),
             fg="#333", bg="#f0f8ff").pack(pady=20)

    # قراءة البيانات
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    reservations = cur.fetchall()
    conn.close()

    if not reservations:
        tk.Label(reservations_window, text="No reservations found.",
                 font=("Arial", 12), bg="#f0f8ff", fg="#555").pack()
        return

    container = tk.Frame(reservations_window, bg="#f0f8ff")
    container.pack(pady=10)

    for res in reservations:
        card = tk.Frame(container, bg="white", relief=tk.RAISED, bd=1)
        card.pack(fill="x", padx=20, pady=8)

        info = f"ID: {res[0]} | {res[1]} - Flight {res[2]} | {res[3]} → {res[4]} | {res[5]} | Seat {res[6]}"
        tk.Label(card, text=info, font=("Arial", 11), bg="white", anchor="w", justify="left").pack(side=tk.LEFT, padx=10, pady=10)

        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(side=tk.RIGHT, padx=10)

        tk.Button(btn_frame, text="Edit", font=("Arial", 10), bg="#007acc", fg="white",
                  activebackground="#005f99", activeforeground="white", bd=0, padx=10,
                  command=lambda r=res: open_edit_page(master, r)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Delete", font=("Arial", 10), bg="#cc0000", fg="white",
                  activebackground="#990000", activeforeground="white", bd=0, padx=10,
                  command=lambda r_id=res[0]: delete_reservation(r_id, reservations_window)).pack(side=tk.LEFT)

def delete_reservation(reservation_id, window):
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
    if confirm:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Deleted", "Reservation deleted successfully.")
        window.destroy()
        open_reservations_page(window)
