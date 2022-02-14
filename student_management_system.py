from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
#import mysql.connector
import time

root = Tk()
root.title('***STUDENT MANAGEMENT SYSTEM***')
root.configure(bg='gold')
root.geometry('1150x1200+100+10')


root.resizable(False, False)
# Left Frame
############################################################################
DataentryFrame = Frame(root, bg='gold2', relief=RIDGE, borderwidth='5')
DataentryFrame.place(x=1, y=90, width=510, height=630)
############################################################################


def connectdb():
    def submitdb():
        global con, mycursor
        #host = hostval.get() # Akash
        #user = userval.get() # root@localhost
        #password = passwordval.get() #Akash@123
        try:
            con = mysql.connector.connect(
                host='Akash', user='root@localhost', password='Akash@123')
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                'Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            str1 = 'create database studentmanagementsystem1'
            mycursor.execute(str1)
            str1 = 'use studentmanagementsystem1'
            mycursor.execute(str1)
            str1 = 'create table studentdata1(id int(10) primary key,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50))'
            mycursor.execute(str1)
            messagebox.showinfo(
                'Notification', 'database created and now you are connected connected to the database ....', parent=dbroot)

        except:
            str1 = 'use studentmanagementsystem1'
            mycursor.execute(str1)
            messagebox.showinfo(
                'Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()  # New window
    dbroot.grab_set()    # till the current window closes nothing else on the screen will be clicked
    dbroot.geometry('470x250+800+130')
    dbroot.resizable(False, False)
    dbroot.configure(bg="navy blue")
    # ---------------------------------------------------------------------database-labels
    hostlabel = Label(dbroot, text="Enter host: ", font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13,
                      bg='Gold2', anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User: ", font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13,
                      bg='Gold2', anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter password: ", font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13,
                          bg='Gold2', anchor='w')
    passwordlabel.place(x=10, y=130)

    hostval = StringVar()  # storing value of host entry
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman Bold', 15), borderwidth=5,
                      textvariable=hostval)  # anchor->to place the text on left side
    hostentry.place(x=240, y=10)

    userentry = Entry(dbroot, font=('roman Bold', 15),
                      borderwidth=5, textvariable=userval)
    userentry.place(x=240, y=70)

    passwordentry = Entry(dbroot, font=('roman Bold', 15),
                          borderwidth=5, textvariable=passwordval)
    passwordentry.place(x=240, y=130)

    # -------------------------------------Connecct database button
    submitbutton = Button(dbroot, text='Submit', font=('times', 15, 'bold'), borderwidth=5, width=20,
                          activebackground='blue', activeforeground='white', command=submitdb)
    submitbutton.place(x=140, y=190)

    dbroot.mainloop()

###########################################################################

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        try:
            str1 = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(str1, (id, name, mobile, email,
                                    address, gender, dob, addeddate))
            con.commit()
            a = messagebox.askyesnocancel(
                'Notificatrions', 'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id, name), parent=addroot)
            if(a == True):  # so that it doesnot vanishes (parent)
                idval.set('')  # to empty the entry boxes
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror(
                'Notifications', 'Id Already Exist try another id...', parent=addroot)
        str1 = 'select * from studentdata1'
        mycursor.execute(str1)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            # This will go start to end-"  '',End  "
            studenttable.insert('', END, values=a)

    addroot = Toplevel(master=DataentryFrame)
# Grab_set it prevents the user by clicking everywhere it holds that screen
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.configure(bg='blue')
    addroot.resizable(False, False)

# -----------------------Add student Labels
    idlabel = Label(addroot, text='Enter ID:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

# --------------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

# ----------------Add button
    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()

def searchstudent():
    def submitsearch():
        id1 = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")

        if(id1 != ''):
            str1 = "select * from studentdata1 where id like '{}'".format(id1)
            mycursor.execute(str1, id1)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)
        elif(name != ''):
            str1 = "select * from studentdata1 where name like '{}'".format(
                name)
            mycursor.execute(str1, name)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)
        elif(mobile != ''):
            str1 = "select * from studentdata1 where mobile like '{}'".format(
                mobile)
            mycursor.execute(str1, mobile)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)
        elif(email != ''):
            str1 = "select * from studentdata1 where email like '{}'".format()
            mycursor.execute(str1, email)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)
        elif(address != ''):
            str1 = "select * from studentdata1 where address like '{}'".format(
                address)
            mycursor.execute(str1, address)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)
        elif(gender != ''):
            str1 = "select * from studentdata1 where gender like '{}'".format(
                gender)
            mycursor.execute(str1, gender)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)

        elif(dob != ''):
            str1 = "select * from studentdata1 where dob like '{}'".format(dob)
            mycursor.execute(str1, dob)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)

        elif(addeddate != ''):
            str1 = "select * from studentdata1 where addeddate like '{}'".format(addeddate)
            mycursor.execute(str1, addeddate)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=a)

        else:
            pass

    searchroot = Toplevel(master=DataentryFrame)
 # Grab_set-> it prevents the user by clicking everywhere it holds that screen
    searchroot.grab_set()
    searchroot.geometry('470x530+220+200')
    searchroot.title('Student Management System')
    searchroot.configure(bg='blue')
    searchroot.resizable(False, False)

# ---------------Add student Labels
    idlabel = Label(searchroot, text='Enter ID:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Mail:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter gender:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

# ------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

 # ------------------Add button
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                activeforeground='white', bg='red', command=submitsearch)
    submitbtn.place(x=150, y=480)

    searchroot.mainloop()

def deletestudent():
    a = studenttable.focus()
    content = studenttable.item(a)
    b = content['values'][0]
    str1 = "delete from studentdata1 where id like '{}'".format(b)
    # Focus#        # it will select the place of selected
    mycursor.execute(str1, b)
    # Item#         # it will get the data of selected
    messagebox.showinfo(
        'Notification', 'Id{} deleted successfully...'.format(b))
    str1 = 'select * from studentdata1'
    mycursor.execute(str1)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        studenttable.insert('', END, values=a)

def updatestudent():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()

        str1 = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s where id=%s'
        mycursor.execute(str1, (name, mobile, email,
                                address, gender, dob, date, id))
        con.commit()
        messagebox.showinfo(
            'Notification', 'Id{} Updated successfully...'.format(id), parent=updateroot)
        str1 = 'select * from studentdata1'
        mycursor.execute(str1)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            studenttable.insert('', END, values=a)

    updateroot = Toplevel(master=DataentryFrame)
 # Grab_set-> it prevents the user by clicking everywhere it holds that screen
    updateroot.grab_set()
    updateroot.geometry('470x540+220+180')
    updateroot.title('Student Management System')
    updateroot.configure(bg='blue')
    updateroot.resizable(False, False)

# --------------Add student Labels
    idlabel = Label(updateroot, text='Enter ID:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Mail:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter gender:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date:', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)
# -------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

# ----------------Add button
    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=submitupdate)
    submitbtn.place(x=150, y=490)

    # fetching the data and placing in the entry boxes

    a = studenttable.focus()
    content = studenttable.item(a)
    b = content['values']
    if(len(b)) != 0:
        idval.set(b[0])
        nameval.set(b[1])
        mobileval.set(b[2])
        emailval.set(b[3])
        addressval.set(b[4])
        genderval.set(b[5])
        dobval.set(b[6])
        dateval.set(b[7])

    updateroot.mainloop()

def showstudent():
    str1 = 'select * from studentdata1'
    mycursor.execute(str1)
    datas = mycursor.fetchall()
    # 1st delete the data then again fetch's all
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        a = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        # This will go start to end-"  '',End  "
        studenttable.insert('', END, values=a)

def exitstudent():
    # Message Box to ask Yes or No or cancel
    res = messagebox.askyesnocancel('Notification', 'Do want to Exit?')
    if res == True:
        # To close the window
        root.destroy()

# ************************************   DATA ENTRY FRAME INTRO   #LEFT

frontlabel = Label(DataentryFrame, text='--------------------Welcome--------------------',
                   width=25, font=('chiller 3', 20, 'bold'), bg='gold2')
frontlabel.pack(side='top', expand=True)

addbtn = Button(DataentryFrame, text='1. Add Student', width=25, font=('chiller ', 20, 'bold'), bd=6,
                bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=addstudent)
addbtn.pack(side='top', expand=True)

searchbtn = Button(DataentryFrame, text='2. Search Student', width=25, font=('chiller ', 20, 'bold'), bd=6,
                   bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=searchstudent)
searchbtn.pack(side='top', expand=True)

delbtn = Button(DataentryFrame, text='3. Delete Student', width=25, font=('chiller ', 20, 'bold'), bd=6,
                bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=deletestudent)
delbtn.pack(side='top', expand=True)

updatebtn = Button(DataentryFrame, text='4. Update Student', width=25, font=('chiller ', 20, 'bold'), bd=6,
                   bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=updatestudent)
updatebtn.pack(side='top', expand=True)

showbtn = Button(DataentryFrame, text='5. Show All', width=25, font=('chiller ', 20, 'bold'), bd=6,
                 bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=showstudent)
showbtn.pack(side='top', expand=True)

exitbtn = Button(DataentryFrame, text='6. Exit', width=25, font=('chiller ', 20, 'bold'), bd=6,
                 bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='White', command=exitstudent)
exitbtn.pack(side='top', expand=True)

# Show data frame       #Right Frame
showdataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth='5')
showdataFrame.place(x=530, y=90, width=620, height=630)

# Show dataFrame Info
# Scroll BAR Horizontal
scroll_x = Scrollbar(showdataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(showdataFrame, orient=VERTICAL)

studenttable = Treeview(showdataFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

studenttable.pack(fill='both', expand=True)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

# when we move scrollbar the data should move
scroll_x.configure(command=studenttable.xview)
scroll_y.configure(command=studenttable.yview)

studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable['show'] = 'headings'

studenttable.column('Id', width=100)
studenttable.column('Name', width=200)
studenttable.column('Mobile No', width=200)
studenttable.column('Email', width=300)
studenttable.column('Address', width=200)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date', width=150)
studenttable.pack(fill=BOTH, expand=1)

# "SLIDER"
ss = "STUDENT MANGEMENT SYSTEM"
mainlabel = Label(root, text=ss, font=('Verdana', 28, 'bold'),
                  relief=RIDGE, borderwidth='2', width=28, bg='Blue')
mainlabel.place(x=205, y=5)
###########################################################################
# Connection to database
###########################################################################  "Connect database"
connectbutton = Button(root, text='Connect to database', width=23, font=('Verdana', 12), relief=RIDGE, borderwidth='4',
                       bg='yellow', activebackground="black", activeforeground="blue", command=connectdb)
connectbutton.place(x=420, y=55)

root.mainloop()
