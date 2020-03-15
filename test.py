from tkinter import *
import tkinter.messagebox
import sqlite3
from PIL import Image,ImageTk
import time
import calendar
import datetime


def Clock():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text = current_time)
    clock.after(100, Clock)


def exitApp():
    opt_ex = tkinter.messagebox.askquestion('Exit application', 'Are you sure?')
    if opt_ex == 'yes':
        root.destroy()

def about():
    tkinter.messagebox.showinfo("About page", "This is a registration page")


def database():
    firstname = ent_fn.get()
    lastname = ent_ln.get()
    email = ent_em.get()
    password = ent_pass.get()
    state = var.get()
    gendr = rb1.get()
    d = var1.get()
    m = var2.get()
    y = var3.get()


    if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showwarning('Cannot register', 'Please fill up empty fields')

    else:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS user (firstName TEXT, lastName TEXT, mail TEXT, password TEXT, state TEXT, gendre TEXT, day TEXT, month TEXT, year TEXT)')
        cur.execute('INSERT INTO user (firstName, lastName, mail, password, state, gendre, day, month, year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(firstname, lastname, email, password, state, gendr, d, m, y,))
        conn.commit()
        conn.close()


def third_window():
    window2 = Toplevel()
    window2.geometry('300x100')
    window2.title('Password Recovery')
    photo = PhotoImage(file = 'wallpaper.png')
    label = Label(window2, image = photo)
    label.pack()


    ent_rec = StringVar()

    def recover():

        rec = ent_rec.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        read = cur.fetchall()


        for i in read:
            if rec == i[2]:
                tkinter.messagebox.showinfo ("Success","Successfully sent! Password saved in 'your_password.txt' file")
                with open('your_password.txt','w') as file:
                    file.write(i[3])
                    window2.destroy()
                    break

        else:
            mail_n_f = tkinter.messagebox.askquestion('Not found','Email not found, do you want to try again?')
            if mail_n_f == 'no':
                window2.destroy()


    label_rc = Label(window2, text = ' Enter your email ', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12))
    label_rc.place(x = 10, y = 28)
    entry_rec = Entry(window2, textvar = ent_rec)
    entry_rec.place(x = 140, y = 30)
    button_rec = Button(window2, text = 'Resend', bg = 'red', fg = 'white', width = 13, relief = 'raised', font = ('arial', 10), command = recover)
    button_rec.place(x = 145, y = 60)

    window2.mainloop()


def second_window():
    window = Toplevel()
    window.geometry('400x400')
    window.title('Login Page')
    photo = PhotoImage(file = 'wallpaper.png')
    label = Label(window, image = photo)
    label.pack()

    ent_lg_em = StringVar()
    ent_lg_pass = StringVar()

    def login():
        e_mail = ent_lg_em.get()
        password = ent_lg_pass.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        read = cur.fetchall()


        for i in read:
            if e_mail == i[2] and password == i[3]:
                tkinter.messagebox.showinfo("Success", "Login successfull, check 'result.txt' file")
                with open('result.txt','w') as file:
                    file.write(str(i))
                    window.destroy()
                    break
        else:
            if len(e_mail) == 0 and len(password) == 0:
                tkinter.messagebox.showwarning("Failed", "Please fill up empty fields")

            else:
                tkinter.messagebox.showwarning("Failed", "Wrong email or password")



    label_w2 = Label(window, text= ' Enter your email and password ', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 14))
    label_w2.place(x = 20, y = 100)
    label_w3 = Label(window, text = ' Email ', bg = '#004038', fg = 'white', font = ('arial', 12), relief = 'raised')
    label_w3.place(x = 30, y = 200)
    label_w4 = Label(window, text = ' Password ', bg = '#004038', fg = 'white', font = ('arial', 12), relief = 'raised')
    label_w4.place(x = 30, y = 250)
    label_rec = Label(window, text = "Forget password? ", bg = '#004038', fg = 'white', relief = 'sunken', font = ('arial',10,'bold'))
    label_rec.place(x = 210, y = 373)

    entry_w3 = Entry(window ,textvar = ent_lg_em)
    entry_w3.place(x = 120, y = 202)
    entry_w4 = Entry(window, show = "*", textvar = ent_lg_pass)
    entry_w4.place(x = 120, y = 252)
    btn_login = Button(window, text = 'Login', bg = 'red', fg = 'white', width = 7, font = ('bold',10), command = login)
    btn_login.place(x = 125, y = 300)
    btn_cancel = Button(window, text = 'Cancel', bg = 'red', fg = 'white', width = 7, font = ('bold',10), command = window.destroy)
    btn_cancel.place(x = 190, y = 300)
    btn_rec = Button(window, text = 'Click here', bg = 'red', fg = 'white', relief = 'raised', command = third_window)
    btn_rec.place(x = 335 , y = 370)



    window.mainloop()


root = Tk()
root.geometry('600x620')
root.title('Register Page')
photo = PhotoImage(file = 'wallpaper.png')
label = Label(root, image=photo)
label.pack()

menu = Menu(root)
root.config(menu = menu)
submenu1 = Menu(menu)
menu.add_cascade(label = 'File', menu = submenu1)
submenu1.add_command(label = 'Exit', command = root.destroy)
submenu2 = Menu(menu)
menu.add_cascade(label = 'Options', menu = submenu2)
submenu2.add_command(label = 'About', command = about)

ent_fn = StringVar()
ent_ln = StringVar()
ent_em = StringVar()
ent_pass = StringVar()
var = StringVar()
rb1 = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

label = Label(root, text = ' Registration ', bg = '#004038', fg = 'white', relief = 'ridge', font = ('Times', 30, 'bold'))
label.place(x = 50, y = 80)
label2 = Label(root, text = ' First name*', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label2.place(x = 100, y = 200)
label3 = Label(root, text = ' Last name*', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label3.place(x = 100, y = 230)
label4 = Label(root, text = ' E-mail*', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label4.place(x = 100, y = 260)
label_pw = Label(root, text = ' Password*', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label_pw.place(x = 100, y = 290)
label5 = Label(root, text = ' Country ', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label5.place(x = 100, y = 325)
label7 = Label(root, text = ' Gendre', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
label7.place(x = 100, y = 405)
b_d = Label(root, text = ' Date of birth', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12, 'bold'))
b_d.place(x = 100, y = 365)
label8 = Label(root, text = '      If you are already registred      ', bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 12))
label8.place(x = 190, y = 540)
label_r_pointer = Label(root, text = ' > > ', bg = '#004038', fg = 'white', relief = 'sunken', font = ('arial', 12, 'bold'))
label_r_pointer.place(x = 190 , y = 575 )


entry2 = Entry(root, font = ('arial', 10, 'bold'), textvar = ent_fn)
entry2.place(x = 210, y = 200)
entry3 = Entry(root, font = ('arial', 10, 'bold'), textvar = ent_ln)
entry3.place(x = 210, y = 230)
entry4 = Entry(root, font = ('arial', 10, 'bold'), textvar = ent_em)
entry4.place(x = 210, y = 260)
entry_pw = Entry(root, font = ('arial', 10, 'bold'), show = '*', textvar = ent_pass)
entry_pw.place(x = 210, y = 290)


list_country = ['Serbia', 'Croatia', 'Bulgaria', 'Bosnia and Herzegovina', 'Romania', 'Montenegro', 'Albanija', 'Macedonia']
droplist = OptionMenu(root, var, *list_country)
var.set('Select Country')
droplist.config(width = 14, bg = '#004038', fg = 'grey', font = ('arial', 9, 'bold'))
droplist.place(x = 210, y = 320)

day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
droplist = OptionMenu (root, var1, *day)
var1.set('Select Day')
droplist.config(width = 10, bg = '#004038', fg = 'grey', font = ('arial', 9, 'bold'))
droplist.place(x = 210, y = 360)

month = ['January', 'February', 'March', 'April', 'May', 'July', 'Jul', 'August', 'September', 'October', 'November', 'December']
droplist = OptionMenu(root, var2, *month)
var2.set('Select Month')
droplist.config(width = 12, bg = '#004038', fg = 'grey', font = ('arial', 9, 'bold'))
droplist.place(x = 300, y = 360)

year = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997' ,'1998', '1999', '2000']
droplist = OptionMenu(root, var3, *year)
var3.set('Select Year')
droplist.config(width = 10, bg = '#004038', fg = 'grey', font = ('arial', 9, 'bold'))
droplist.place(x = 400, y = 360)


rbtn1 = Radiobutton(root, text = 'Male', value = 'Male', variable = rb1, bg = '#004038', fg = 'grey', relief = 'groove', font = ('arial', 10, 'bold'))
rbtn1.place(x = 210, y = 405)
rbtn2 = Radiobutton(root, text = 'Female', value = 'Female', variable = rb1, bg = '#004038', fg = 'grey', relief = 'groove', font = ('arial', 10, 'bold'))
rbtn2.place(x = 300, y = 405)



login_button = Button(root, text = 'Login', bg = 'red', fg = 'white', width = 20, relief ='raised', font = ('arial', 11, 'bold'), command = second_window)
login_button.place(x = 235, y = 572)
register_button = Button(root, text = 'Register', bg = 'red', fg = 'white', width = 10, font = ('arial', 12, 'bold'), command = database)
register_button.place(x = 210, y = 470)
quit_button = Button(root, text = 'Quit', bg = 'red', fg = 'white', width = 10, font = ('arial', 12, 'bold'), command = exitApp)
quit_button.place(x = 320, y = 470)


clock = Label(root, bg = '#004038', fg = 'white', relief = 'raised', font = ('arial', 20, 'bold'))
clock.place(x = 450, y = 20)
date = Label(root, text=f"{datetime.datetime.now():%a, %b %d %Y}", fg="white", bg="#004038", relief = 'raised', font=("arial", 10, 'bold'))
date.place(x = 450, y = 60)



if __name__ == '__main__':
    Clock()
    root.mainloop()