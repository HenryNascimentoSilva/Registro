# Tkinter Lib
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

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
app_lg = Image.open('data/logo.png')
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
frame_details = Frame(window, width=800, height=100, bg=colors.co1, relief=SOLID)
frame_details.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)


# Window main loop  
window.mainloop()
