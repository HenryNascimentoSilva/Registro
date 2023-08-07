# Tkinter Lib
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Database
from src.database import *

# Pillow
from PIL import ImageTk, Image

# Colors
import src.colors as colors

global image, image_string, l_image

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
app_lg = Image.open("resources/logo.png")
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(
    frame_logo,
    image=app_lg,
    text="   Student  Registration  System",
    width=850,
    compound=LEFT,
    anchor=NW,
    font=("Verdana 15"),
    bg=colors.co6,
    fg=colors.co1,
)
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


# CRUD
def add():
    global image, image_string, l_image

    # Getting Info
    name = e_name.get()
    email = e_mail.get()
    tel = e_tel.get()
    gender = c_gender.get()
    date = datebirth.get()
    adress = e_adress.get()
    course = c_course.get()
    img = image_string

    list = [name, email, tel, gender, date, adress, course, img]

    # Checking List
    for i in list:
        if i == "":
            messagebox.showerror("Field cannot be NULL")
            return

        # Registering Values
    registersystem.create(list)

    # Cleaning Entry Fields
    name = e_name.delete(0, END)
    email = e_mail.delete(0, END)
    tel = e_tel.delete(0, END)
    gender = c_gender.delete(0, END)
    date = datebirth.delete(0, END)
    adress = e_adress.delete(0, END)
    course = c_course.delete(0, END)

    # Showing Values
    ShowStudents()


# Search Function
def search():
    global image, image_string, l_image

    # Getting ID
    id_student = int(e_search.get())

    data = registersystem.search(id_student)

    # Cleaning Entry Fields
    name = e_name.delete(0, END)
    email = e_mail.delete(0, END)
    tel = e_tel.delete(0, END)
    gender = c_gender.delete(0, END)
    date = datebirth.delete(0, END)
    adress = e_adress.delete(0, END)
    course = c_course.delete(0, END)

    # Inserting Entry Fields
    name = e_name.insert(END, data[1])
    email = e_mail.insert(END, data[2])
    tel = e_tel.insert(END, data[3])
    gender = c_gender.insert(END, data[4])
    date = datebirth.insert(END, data[5])
    adress = e_adress.insert(END, data[6])
    course = c_course.insert(END, data[7])

    # Image
    image = data[8]
    image_string = image

    image = Image.open(image)
    image = image.resize((130, 130))
    image = ImageTk.PhotoImage(image)

    l_image = Label(frame_details, image=image, bg=colors.co1, fg=colors.co4)
    l_image.place(x=390, y=10)


def update():
    global image, image_string, l_image

    # Getting ID
    student_ID = int(e_search.get())

    # Getting Info
    name = e_name.get()
    email = e_mail.get()
    tel = e_tel.get()
    gender = c_gender.get()
    date = datebirth.get()
    adress = e_adress.get()
    course = c_course.get()
    img = image_string

    list = [name, email, tel, gender, date, adress, course, img, student_ID]

    # Checking List
    for i in list:
        if i == "":
            messagebox.showerror("Field cannot be NULL")
            return
    registersystem.update(list)

    # Cleaning Entry Fields
    name = e_name.delete(0, END)
    email = e_mail.delete(0, END)
    tel = e_tel.delete(0, END)
    gender = c_gender.delete(0, END)
    date = datebirth.delete(0, END)
    adress = e_adress.delete(0, END)
    course = c_course.delete(0, END)
    
    image = Image.open("resources/logo.png")
    image = image.resize((130, 130))
    image = ImageTk.PhotoImage(image)
    l_image = Label(frame_details, image=image, bg=colors.co1, fg=colors.co4)
    l_image.place(x=390, y=10)

    ShowStudents()


def delete():
    global image, image_string, l_image

    # Getting ID
    student_ID = int(e_search.get())

    # Deleting Student
    registersystem.delete(student_ID)

    # Cleaning Entry Fields
    name = e_name.delete(0, END)
    email = e_mail.delete(0, END)
    tel = e_tel.delete(0, END)
    gender = c_gender.delete(0, END)
    date = datebirth.delete(0, END)
    adress = e_adress.delete(0, END)
    course = c_course.delete(0, END)

    e_search.delete(0, END)
    
    image = Image.open("resources/logo.png")
    image = image.resize((130, 130))
    image = ImageTk.PhotoImage(image)
    
    l_image = Label(frame_details, image=image, bg=colors.co1, fg=colors.co4)
    l_image.place(x=390, y=10)

    ShowStudents()


# Entry Fields

# Name Field
l_name = Label(
    frame_details, text="Name", anchor=NW, font=("Ivy 10"), bg=colors.co1, fg=colors.co4
)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify="left", relief=SOLID)
e_name.place(x=7, y=40)

# E-mail Field
l_mail = Label(
    frame_details,
    text="E-mail",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_mail.place(x=4, y=70)
e_mail = Entry(frame_details, width=30, justify="left", relief=SOLID)
e_mail.place(x=7, y=100)

# Telephone Field
l_tel = Label(
    frame_details,
    text="Telephone",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify="left", relief=SOLID)
e_tel.place(x=7, y=160)

# Gender Field
l_gender = Label(
    frame_details,
    text="Gender",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_gender.place(x=127, y=130)
c_gender = Combobox(frame_details, width=7, font=("Ivy 8 bold"), justify=CENTER)
c_gender["values"] = ("M", "F")
c_gender.place(x=130, y=160)

# Date Field
l_date = Label(
    frame_details,
    text="Birth Date",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_date.place(x=220, y=10)
datebirth = DateEntry(
    frame_details,
    width=18,
    justify=CENTER,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    year=2023,
)
datebirth.place(x=224, y=40)

# Adress Field
l_adress = Label(
    frame_details,
    text="Adress",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_adress.place(x=220, y=70)
e_adress = Entry(frame_details, width=20, justify="left", relief=SOLID)
e_adress.place(x=224, y=100)

# Course Field
course = ["Engineering", "Medicine", "Social", "Mathematics", "Other"]

l_course = Label(
    frame_details,
    text="Course",
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_course.place(x=220, y=130)
c_course = Combobox(frame_details, width=20, font=("Ivy 8 bold"), justify=CENTER)
c_course["values"] = course
c_course.place(x=224, y=160)

# Default Image
image = Image.open("resources/logo.png")
image = image.resize((130, 130))
image = ImageTk.PhotoImage(image)
l_image = Label(frame_details, image=image, bg=colors.co1, fg=colors.co4)
l_image.place(x=390, y=10)


# Image Selector
def ChooseImage():
    global image, image_string, l_image

    image = fd.askopenfilename()

    image_string = image

    image = Image.open(image)
    image = image.resize((130, 130))
    image = ImageTk.PhotoImage(image)
    l_image = Label(frame_details, image=image, bg=colors.co1, fg=colors.co4)
    l_image.place(x=390, y=10)

    button_load["text"] = "Change Photo"


# Button Image
button_load = Button(
    frame_details,
    command=ChooseImage,
    text="Load Photo".upper(),
    width=20,
    compound=CENTER,
    anchor=CENTER,
    overrelief=RIDGE,
    font=("Ivy 7 bold"),
    bg=colors.co1,
    fg=colors.co0,
)
button_load.place(x=390, y=160)


# Students Table
def ShowStudents():
    # creating a treeview with dual scrollbars
    list_header = [
        "ID",
        "Name",
        "E-mail",
        "Telephone",
        "Gender",
        "Date",
        "Adress",
        "Course",
    ]

    # view all students
    df_list = registersystem.read()

    tree_student = ttk.Treeview(
        frame_tabel, selectmode="extended", columns=list_header, show="headings"
    )

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabel, orient="vertical", command=tree_student.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabel, orient="horizontal", command=tree_student.xview)

    tree_student.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_student.grid(column=0, row=1, sticky="nsew")
    vsb.grid(column=1, row=1, sticky="ns")
    hsb.grid(column=0, row=2, sticky="ew")
    frame_tabel.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_student.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
        tree_student.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_student.insert("", "end", values=item)


# Search Frame

frame_search = Frame(frame_buttons, width=40, height=50, bg=colors.co1, relief=RAISED)
frame_search.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
l_name = Label(
    frame_search,
    text="Search Student [ Entry ID ]",
    height=1,
    anchor=NW,
    font=("Ivy 10"),
    bg=colors.co1,
    fg=colors.co4,
)
l_name.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_search = Entry(
    frame_search, width=5, justify="center", relief="solid", font=("Ivy 10")
)
e_search.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

# Search Button
button_search = Button(
    frame_search,
    command=search,
    anchor=CENTER,
    text="Search",
    width=9,
    overrelief=RIDGE,
    font=("ivy 7 bold"),
    bg=colors.co1,
    fg=colors.co0,
)
button_search.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Buttons

# Add Image
app_img_add = Image.open("resources/add.png")
app_img_add = app_img_add.resize((25, 25))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(
    frame_buttons,
    command=add,
    image=app_img_add,
    text=" Add Student",
    width=100,
    compound=LEFT,
    relief=GROOVE,
    overrelief=RIDGE,
    font=("Ivy 11"),
    bg=colors.co1,
    fg=colors.co0,
)
app_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

# Update Image
app_img_att = Image.open("resources/update.png")
app_img_att = app_img_att.resize((25, 25))
app_img_att = ImageTk.PhotoImage(app_img_att)
app_att = Button(
    frame_buttons,
    command=update,
    image=app_img_att,
    text=" Update",
    width=100,
    compound=LEFT,
    relief=GROOVE,
    overrelief=RIDGE,
    font=("Ivy 11"),
    bg=colors.co1,
    fg=colors.co0,
)
app_att.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

# Delete Image
app_img_del = Image.open("resources/delete.png")
app_img_del = app_img_del.resize((25, 25))
app_img_del = ImageTk.PhotoImage(app_img_del)
app_del = Button(
    frame_buttons,
    command=delete,
    image=app_img_del,
    text=" Delete",
    width=100,
    compound=LEFT,
    relief=GROOVE,
    overrelief=RIDGE,
    font=("Ivy 11"),
    bg=colors.co1,
    fg=colors.co0,
)
app_del.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)


# Separator Line
l_line = Label(
    frame_buttons,
    relief=GROOVE,
    text="h",
    width=1,
    height=123,
    anchor=NW,
    font=("Ivy 1"),
    bg=colors.co1,
    fg=colors.co0,
)
l_line.place(x=240, y=15)

# Call Tabel
ShowStudents()

# Window main loop
window.mainloop()
