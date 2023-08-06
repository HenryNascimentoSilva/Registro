# Tkinter Lib
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Calendar
from tkcalendar import Calendar,DateEntry
from datetime import date

# Pillow
from PIL import ImageTk, Image

# Colors
import colors

# Window
window = Tk()
window.title("")
window.geometry("810x535")
window.configure(background=colors.co1)
window.resizable(width=FALSE, height=FALSE)

# Styles
style = Style(window)
style.theme_use("clam")

# Frames

# Logo Frame
frame_logo = Frame(window, width=850, height=52, bg=colors.co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

# Logo Image
app_lg = Image.open('resources/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Student Registration System", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=colors.co6, fg=colors.co1)
app_logo.place(x=5, y=0)

# Buttons Frame
frame_buttons = Frame(window, width=100, height=200, bg=colors.co1, relief=RAISED)
frame_buttons.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Details Frame
frame_details = Frame(window, width=800, height=100, bg=colors.co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

# Tabel Frame
frame_tabel = Frame(window, width=800, height=100, bg=colors.co1, relief=SOLID)
frame_tabel.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Input Field

# Name Field
l_name = Label(frame_details, text='Name', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_name.place(x=7, y=40)

# E-mail Field
l_name = Label(frame_details, text='E-mail', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_name.place(x=4, y=70)
e_name = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_name.place(x=7, y=100)

# Telephone Field
l_tel = Label(frame_details, text='Telephone', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief=SOLID)
e_tel.place(x=7, y=160)

# Gender Field
l_gender = Label(frame_details, text='Gender', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_gender.place(x=127, y=130)
c_gender = Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify=CENTER)
c_gender['values'] = ('M', 'F')
c_gender.place(x=130, y=160)

# Date Field
l_date = Label(frame_details, text='Birth Date', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_date.place(x=220, y=10)
datebirth = DateEntry(frame_details, width=18, justify=CENTER, background='darkblue', foreground='white', borderwidth=2, year=2023)
datebirth.place(x=224, y=40)

# Adress Field
l_adress = Label(frame_details, text='Adress', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_adress.place(x=220, y=70)
e_adress = Entry(frame_details, width=15, justify='left', relief=SOLID)
e_adress.place(x=224, y=100)

# Course Field
course = ['Engineering', 'Medicine', 'Social', 'Mathematics', 'Other']

l_course = Label(frame_details, text='Course', anchor=NW, font=('Ivy 10'), bg=colors.co1, fg=colors.co4)
l_course.place(x=220, y=130)
c_course = Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify=CENTER)
c_course['values'] = course
c_course.place(x=224, y=160)


# Window main loop  
window.mainloop()
