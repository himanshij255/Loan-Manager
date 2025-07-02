# pjct strt.py
from tkinter import *
from dbms import con, cur
from datetime import datetime
from tkinter import messagebox

# Database connection
con = sqlite3.connect("mydb")
cur = con.cursor()

# Date format
DATE_FORMAT = "%d/%m/%Y"

# GUI setup
root = Tk()
root.configure(bg="sky blue")
root.title("Loan Manager")

# Labels and Entry fields
fields = [
    "NAME", "ID", "LOAN NO.", "START DATE", "END DATE",
    "AMOUNT TAKEN", "AMOUNT RETURNED", "RATE OF INTEREST",
    "NO INTEREST DAYS", "TOTAL SI"
]
entries = []

for i, label in enumerate(fields):
    Label(root, text=label, relief=RIDGE, width=20, bg="light green", fg="blue").grid(row=i, column=0)
    e = Entry(root, relief=SUNKEN, width=30, bg="light yellow")
    e.grid(row=i, column=2)
    entries.append(e)

n, idd, l, strt_date, end_date, p, artrn, r, intrst, si_display = entries

# Button functions
def insert():
    try:
        data = (
            n.get(), idd.get(), l.get(),
            datetime.strptime(strt_date.get(), DATE_FORMAT).strftime("%Y-%m-%d"),
            datetime.strptime(end_date.get(), DATE_FORMAT).strftime("%Y-%m-%d"),
            float(p.get()), float(artrn.get()), float(r.get()), int(intrst.get())
        )
        cur.execute("INSERT INTO records(name, id, lno, sdate, edate, pr, ramt, rate, no_intrst) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        con.commit()
        messagebox.showinfo("Success", "Record inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete():
    try:
        cur.execute("DELETE FROM records WHERE lno=?", (l.get(),))
        con.commit()
        messagebox.showinfo("Deleted", "Record deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def calcu():
    try:
        a = datetime.strptime(end_date.get(), DATE_FORMAT).date()
        b = datetime.strptime(strt_date.get(), DATE_FORMAT).date()
        delta = (a - b).days - int(intrst.get())
        si = float(artrn.get()) * float(r.get()) * float(delta) / 36500
        si_display.delete(0, END)
        si_display.insert(0, f"{si:.2f}")
        cur.execute("UPDATE records SET si=? WHERE id=? AND lno=?", (si, idd.get(), l.get()))
        con.commit()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear():
    for entry in entries:
        entry.delete(0, END)

def search():
    try:
        t = (idd.get(), l.get())
        cur.execute("SELECT * FROM records WHERE id=? AND lno=?", t)
        record = cur.fetchone()
        if record:
            clear()
            for entry, value in zip(entries, record):
                entry.insert(0, value)
        else:
            messagebox.showinfo("Not Found", "No record found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Buttons
Button(root, text="INSERT", height=1, width=10, bg="pink", command=insert).grid(row=10, column=0, padx=20, pady=10)
Button(root, text="DELETE", height=1, width=10, bg="pink", command=delete).grid(row=10, column=1, padx=20, pady=10)
Button(root, text="SEARCH", height=1, width=10, bg="pink", command=search).grid(row=10, column=2, padx=20, pady=10)
Button(root, text="CALCULATE", height=1, width=10, bg="pink", command=calcu).grid(row=10, column=3, padx=20, pady=10)
Button(root, text="CLEAR", height=1, width=10, bg="pink", command=clear).grid(row=11, column=1, padx=20, pady=10)
Button(root, text="EXIT", height=1, width=10, bg="pink", command=root.destroy).grid(row=11, column=2, padx=20, pady=10)

root.mainloop()
con.close()


