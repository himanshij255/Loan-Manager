# 🏦 Loan Manager GUI App (Tkinter + SQLite)
A simple desktop GUI application to manage loan records — built with Python's Tkinter for the interface and SQLite for storing data locally.

## 📁 Project Structure
Loan-Manager/
├── dbms.py               # Database connection module (shared across scripts)
├── create table.py       # Creates the 'records' table if it doesn't exist
├── pjct strt.py          # Main GUI app with Tkinter
├── mydb                  # SQLite database file (binary)
└── README.md             # You are here!

## ⚙️ Requirements
Python 3.x

Built-in modules only:

tkinter

sqlite3

datetime

✅ No third-party packages needed.

## ▶️ How to Run
🧩 Step 1: Clone or download the repo
git clone https://github.com/himanshij255/Loan-Manager.git
cd Loan-Manager

🧩 Step 2: Create the database table (run once)
python create\ table.py

🧩 Step 3: Launch the application
python pjct\ strt.py

This opens a GUI window where you can:

Add new loan entries

Delete records by loan number

Search records by ID or loan number

Calculate Simple Interest (SI)

## 🧠 How the App Works
dbms.py: Handles SQLite connection (con) and cursor (cur).

create table.py: Creates the records table.

pjct strt.py: GUI for interacting with loan data.

The records table includes:

Column

Description

name

Borrower's name

id

Unique borrower ID

lno

Loan number

sdate

Start date (DD/MM/YYYY)

edate

End date (DD/MM/YYYY)

pr

Principal amount

ramt

Amount returned

rate

Rate of interest

no_intrst

Interest-free days

si

Simple Interest (auto-calculated)

## ✨ Features
📝 Insert, delete, and search loan records

🧮 Automatically calculate Simple Interest

💾 Store all data locally using SQLite

🎨 User-friendly Tkinter interface

📦 Modular code with shared DB logic in dbms.py

## 🖼️ Screenshot
## 🚀 Future Improvements
Display records in a table/grid

Export data to CSV or Excel

Use calendar widget (tkcalendar) for better date input

Add login/authentication system

Support updating/editing existing records

## 🙋‍♀️ Created By
Himanshi Jain

If you find this project helpful, consider ⭐ starring the repo and sharing it with others!
