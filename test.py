from tkinter import *
import tkinter.messagebox
import sqlite3
from PIL import Image,ImageTk

def exitt():
    exit()

def about():
    tkinter.messagebox.showinfo ("About page", "This is a registration page")

def database():
    firstname = ent_fn.get()
    lastname = ent_ln.get()
    email = ent_em.get()
    password = ent_pass.get()
    state  =var.get()
    sex = rb1.get()
    d = var1.get()
    m = var2.get()
    y = var3.get()

    conn = sqlite3.connect ('database.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS user (firstName TEXT, lastName TEXT, mail TEXT, password TEXT, state TEXT, genre TEXT, day TEXT, month TEXT, year TEXT)')
    cur.execute('INSERT INTO user (firstName, lastName, mail, password, state, genre, day, month, year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(firstname, lastname, email, password, state, sex, d, m, y,))
    conn.commit()
    conn.close()

def second_window():
    window = Toplevel()
    window.geometry ('400x400')
    window.title ('Login Page')
    photo = PhotoImage (file = 'wallpaper.png')
    label = Label(window, image = photo)
    label.pack()

    ent_lg_em = StringVar()
    ent_lg_pass = StringVar()

    def login():
        e_mail = ent_lg_em.get()
        password = ent_lg_pass.get()

        conn = sqlite3.connect ('database.db')
        c = conn.cursor()
        c.execute ("SELECT * FROM user")
        read = c.fetchall()

        for i in read:
            if e_mail == i[2] and password == i[3]:
                tkinter.messagebox.showinfo (" Success", "Login Successfull")
                print(i)
                break
        else:
            print('Wrong UserName Or Password')
            tkinter.messagebox.showinfo ("Failed", "Wrong Email Or Password")


    label_w2 = Label (window, text= 'Enter your Email and Password', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
    label_w2.place (x = 20, y = 100)
    label_w3=Label (window, text = 'Email', bg = '#004038', fg = 'white', relief = 'raised')
    label_w3.place (x = 30, y = 200)
    label_w4 = Label (window, text = 'Password', bg = '#004038', fg = 'white', relief = 'raised')
    label_w4.place (x = 30, y = 250)
    
    entry_w3 = Entry (window ,textvar = ent_lg_em)
    entry_w3.place (x = 100, y = 200)
    entry_w4 = Entry (window, show = "*", textvar = ent_lg_pass)
    entry_w4.place (x = 100, y = 250)

    btn_login = Button (window, text = 'Login', bg = 'red', fg = 'white', command = login)
    btn_login.place (x = 280, y = 300)
    btn_cancel = Button (window, text = 'Cancel', bg = 'red', fg = 'white', command = window.destroy)
    btn_cancel.place (x = 330, y = 300)

    window.mainloop()

root = Tk()
root.geometry ('600x600')
root.title ('Register Page')
photo = PhotoImage (file = 'wallpaper.png')
label = Label (root, image=photo)
label.pack()

menu = Menu(root)
root.config (menu = menu)
submenu1 = Menu (menu)
menu.add_cascade (label = 'File', menu = submenu1)
submenu1.add_command (label = 'Exit', command = exitt)
submenu2 = Menu (menu)
menu.add_cascade (label = 'Options', menu = submenu2)
submenu2.add_command (label = 'About', command = about)

ent_fn = StringVar()
ent_ln = StringVar()
ent_em = StringVar()
ent_pass  =StringVar()
var = StringVar()
rb1 = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

label = Label (root, text = 'Register', bg = '#004038', fg = 'white', relief = 'raised', font = ('Times', 30))
label.place (x = 80, y = 100)
label2 = Label (root, text = 'First Name', bg = '#004038', fg = 'white', relief = 'raised', font = (20))
label2.place (x = 100, y = 200)
label3 = Label (root, text = 'Last Name', bg = '#004038', fg = 'white', relief = 'raised', font = (20))
label3.place (x = 100, y = 230)
label4 = Label (root, text = 'Email', bg = '#004038', fg = 'white', relief = 'raised', font = (20))
label4.place (x = 100, y = 260)
label_pw = Label (root, text = 'Password', bg = '#004038', fg = 'white', relief = 'raised', font = (20))
label_pw.place (x = 100, y = 290)
label5 = Label (root, text = 'Country', bg = '#004038', fg = 'white', relief = 'raised', font = (20))
label5.place (x = 100, y = 330)
label7 = Label (root, text = 'Genre', bg = '#004038', fg = 'white', relief = 'raised', font = ('Times', 12))
label7.place (x = 100, y = 400)
b_d = Label (root, text = 'Date Of Birth', bg = '#004038', fg = 'white', relief = 'raised', font = ('Times', 11))
b_d.place (x = 100, y = 365)
label8 = Label (root, text = 'If you are already registred, you can login here', bg = '#004038', fg = 'white', relief = 'raised', font = ('Times', 12))
label8.place (x = 100, y = 520)


entry2 = Entry (root, textvar = ent_fn)
entry2.place (x = 210, y = 200)
entry3 = Entry (root, textvar = ent_ln)
entry3.place (x = 210, y = 230)
entry4 = Entry (root, textvar = ent_em)
entry4.place (x = 210, y = 260)
entry_pw = Entry (root, show = '*', textvar = ent_pass)
entry_pw.place (x = 210, y = 290)


list_country = ['Serbia', 'Croatia', 'Bulgaria', 'Bosnia and Herzegovina', 'Romania', 'Montenegro', 'Albanija', 'Macedonia']
droplist = OptionMenu (root, var, *list_country)
var.set ('Select Country')
droplist.config (width = 12, bg = '#004038', fg = 'grey', relief = 'groove')
droplist.place (x = 210, y = 325)

day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
droplist = OptionMenu (root, var1, *day)
var1.set ('Select Day')
droplist.config (width = 10, bg = '#004038', fg = 'grey')
droplist.place (x = 210, y = 360)

month = ['January', 'February', 'March', 'April', 'May', 'July', 'Jul', 'August', 'September', 'October', 'November', 'December']
droplist = OptionMenu (root, var2, *month)
var2.set ('Select Month')
droplist.config (width = 12, bg = '#004038', fg = 'grey')
droplist.place (x = 290, y = 360)

year = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997' ,'1998', '1999', '2000']
droplist = OptionMenu (root, var3, *year)
var3.set ('Select Year')
droplist.config (width = 12, bg = '#004038', fg = 'grey')
droplist.place (x = 400, y = 360)


rbtn1 = Radiobutton (root, text = 'Male', value = 'Male', variable = rb1, bg = '#004038', fg = 'grey', relief = 'groove')
rbtn1.place (x = 210, y = 400)
rbtn2 = Radiobutton (root, text = 'Female', value = 'Female', variable = rb1, bg = '#004038', fg = 'grey', relief = 'groove')
rbtn2.place (x = 280, y = 400)




login_button = Button (root, text = 'Login', bg = 'red', fg = 'white', command = second_window)
login_button.place (x = 400, y = 520)
register_button = Button (root, text = 'Register', bg = 'red', fg = 'white', command = database)
register_button.place (x = 200, y = 460)
quit_button = Button (root, text = 'Quit', bg = 'red', fg = 'white', command = root.destroy)
quit_button.place (x = 300, y = 460)

if __name__ == '__main__':

    root.mainloop()