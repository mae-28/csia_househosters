import tkinter
from tkinter import ttk

base_price = 5
season = 0

ratings = 0


prop1 = 7
prop2 = 10
prop3 = 30

calculating_window = tkinter.Tk()
calculating_window.title("Calculations page")

frame = tkinter.Frame(calculating_window)
frame.pack()

calculating_window = tkinter.LabelFrame(frame, text="input factors")
calculating_window.grid(row=0, column=0, padx=20, pady=20)

app_label = tkinter.Label(calculating_window, text="Put in all of the factors:")
app_label.grid(row=0, column=0)

email_label = tkinter.Label(calculating_window, text="base price :")
email_label.grid(row=1, column=0)

email_entry = tkinter.Entry(calculating_window)
email_entry.grid(row=2, column=0)

result_label = tkinter.Label(text="", fg="black")
result_label.pack()

season_label = tkinter.Label(calculating_window, text="Season:")
season_combobox = ttk.Combobox(calculating_window, values=["low", "mid / normal", "high"])
season_label.grid(row=3, column=0)  # Fix here
season_combobox.grid(row=4, column=0)



calculating_window.mainloop()
