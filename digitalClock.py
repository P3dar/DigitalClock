# import
import tkinter as tk
import time
import pytz
import datetime

# IRL time created


def digital_clock1():
    clock1 = tk.Label()
    time_live = time.strftime("%H:%M:%S")
    clock1.config(text=time_live, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock1.after(200, digital_clock1)
    clock1.grid(row=2, column=0)


def digital_clock2():
    clock2 = tk.Label()
    time_tokyo = datetime.datetime.now(
        pytz.timezone("Asia/Tokyo")).strftime("%H:%M:%S")
    clock2.config(text=time_tokyo, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock2.after(200, digital_clock2)
    clock2.grid(row=2, column=1)


def digital_clock3():
    clock2 = tk.Label()
    time_shangai = datetime.datetime.now(
        pytz.timezone("Asia/Shanghai")).strftime("%H:%M:%S")
    clock2.config(text=time_shangai, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock2.after(200, digital_clock3)
    clock2.grid(row=2, column=2)


def digital_clock4():
    clock2 = tk.Label()
    time_toronto = datetime.datetime.now(
        pytz.timezone("America/Toronto")).strftime("%H:%M:%S")
    clock2.config(text=time_toronto, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock2.after(200, digital_clock4)
    clock2.grid(row=4, column=0)


def digital_clock5():
    clock2 = tk.Label()
    time_mex = datetime.datetime.now(
        pytz.timezone("America/Mexico_City")).strftime("%H:%M:%S")
    clock2.config(text=time_mex, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock2.after(200, digital_clock5)
    clock2.grid(row=4, column=1)


def digital_clock6():
    clock2 = tk.Label()
    time_sidney = datetime.datetime.now(
        pytz.timezone("Australia/Sydney")).strftime("%H:%M:%S")
    clock2.config(text=time_sidney, background="grey1",
                  foreground="white", font=("boulder", 11,))
    clock2.after(200, digital_clock6)
    clock2.grid(row=4, column=2)


# creating the window and its size
app_window = tk.Tk()
app_window.title("My Digital Clock")
w = 500  # Width
h = 200  # Height
app_window.configure(bg="grey1")
app_window.resizable(0, 0)

# move window to center
winWidth = app_window.winfo_screenwidth()
winHeight = app_window.winfo_screenheight()
x = (winWidth/2) - (w/2)
y = (winHeight/2) - (h/2)
app_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# creating labels for GUI
title = tk.Label(text="    ORARI DAL MONDO!", background="grey1",
                 foreground="white", font=("boulder", 18, "bold")).grid(row=0, column=1)

city1 = tk.Label(text=" ARMENO", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=1, column=0)

city2 = tk.Label(text="TOKYO", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=1, column=1)

city3 = tk.Label(text="SHANGAI", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=1, column=2)

city4 = tk.Label(text=" TORONTO", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=3, column=0)

city5 = tk.Label(text="CITTA' DEL MESSICO", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=3, column=1)

city6 = tk.Label(text=" SYDNEY", background="grey1",
                 foreground="white", font=("boulder", 16,)).grid(row=3, column=2)

# launching
digital_clock1()
digital_clock2()
digital_clock3()
digital_clock4()
digital_clock5()
digital_clock6()
app_window.mainloop()
