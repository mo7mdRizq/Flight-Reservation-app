# ✈️ Flight Reservation System - Desktop App

This is a simple desktop application to manage flight reservations.  
It is built using **Python**, **Tkinter** for the GUI, and **SQLite** for the database.

---

## ✅ Features

- Book new flight reservations
- View all existing bookings
- Edit a reservation
- Delete a reservation
- Easy-to-use graphical interface

---

## 🛠️ Tools & Technologies

- Python 3
- Tkinter
- SQLite
- PyInstaller (for converting to .exe)

---

## ▶️ How to Run the App

1. Make sure Python 3 is installed.
2. Open terminal or command prompt inside the project folder.
3. Install dependencies (optional):
    ```
    pip install -r requirements.txt
    ```
4. Run the application:
    ```
    python main.py
    ```

---

## 🧱 Project Files Structure

flight_reservation_app/
├── main.py
├── database.py
├── home.py
├── booking.py
├── reservations.py
├── edit_reservation.py
├── flights.db
├── requirements.txt
├── README.md


---

## 🗃️ Database Schema

**Table: reservations**
- id (primary key)
- name
- flight_number
- departure
- destination
- date
- seat_number

---

## 🧪 To Convert to .EXE

If you want to generate a Windows executable file:

pip install pyinstaller
pyinstaller --onefile main.py


The file will be created inside the `dist/` folder.

---

## 👨‍💻 Developed By

Mohamed Ibrahim  
SprintUP Python developement – Final Project  

