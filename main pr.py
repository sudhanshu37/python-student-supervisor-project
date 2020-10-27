import tkinter
top = tkinter.Tk()
def super():
    suu=tkinter.Tk()
    def logi():

        w=tkinter.Tk()
        f1=tkinter.Frame(w,bd=50)
        f1.pack()

        w.title('Login Page')
        tkinter.Label(f1, text="User    ").grid(row=0)
        tkinter.Label(f1, text = "Name").grid(row=1)
        us = tkinter.Entry(f1)
        nam =tkinter.Entry(f1)
        us.grid(row=0, column=1)
        nam.grid(row=1, column=1)
        tkinter.Button(f1, text='Login Now', command=w.destroy, bg='blue').grid(row=3, column=1, pady=4)
        tkinter.Button(f1, text='New User', command=w.destroy, bg='blue').grid(row=3, column=2, pady=4)

    def new_user():
        def reg():
            n = a.get()
            r = b.get()
            s = c.get()
            m = d.get()
            em = e.get()
    
            conn = sqlite3.connect('New_user.db')
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS newUser(name varchar,regNo int, specialization varchar, mobileNo int, email varhar)')
            cursor.execute('INSERT INTO newUser(name,regNo,specialization,mobileNo,email) VALUES(?,?,?,?,?)',(n,r,s,m,em))
            conn.commit()
            conn.close()
    
        root = tkinter.Tk()

        a = tkinter.StringVar()
        b = tkinter.IntVar()
        c = tkinter.StringVar()
        d = tkinter.IntVar()
        e = tkinter.StringVar()


        root.title('Registration Form')
        root.configure(background='darkgray')
        root.geometry("500x400")
        # Start of the GUI
        heading = tkinter.Label(root, text="New User Supervisor", bg="light green", font=('arial',20,'bold'))
        heading.place(x=140,y=30)

        l1 = tkinter.Label(root, text='Name', bg='darkgray', fg = 'black', font=('arial',15,'bold'))    #tkinter.label makes the text as label
        l1.place(x=110,y=90)            #label,Button and Entry is stored in Table form 
        e1 = tkinter.Entry(root, textvar=a, bd=3)
        e1.place(x=260,y=90)

        l2 = tkinter.Label(root, text='UID', bg='darkgray', fg = 'black', font=('arial',15,'bold'))    
        l2.place(x=110,y=140)
        e2 = tkinter.Entry(root, textvar=b, bd=3)                #Entry is used for text box in which user can enter a value
        e2.place(x=260,y=140)

        l3 = tkinter.Label(root, text='Specialization', bg='darkgray', fg = 'black', font=('arial',15,'bold'))
        l3.place(x=110,y=190)
        e3 = tkinter.Entry(root, textvar=c, bd=3)
        e3.place(x=260,y=190)

        l4 = tkinter.Label(root, text='Mobile no', bg='darkgray', fg = 'black', font=('arial',15,'bold'))
        l4.place(x=110,y=240)
        e4 = tkinter.Entry(root, textvar=d, bd=3)
        e4.place(x=260,y=240)

        l5 = tkinter.Label(root, text='Email Id', bg='darkgray', fg = 'black', font=('arial',15,'bold'))
        l5.place(x=110,y=290)
        e5 = tkinter.Entry(root, textvar=e, bd=3)
        e5.place(x=260,y=290)


        b1 = tkinter.Button(root, text='Register', bg='light green', fg = 'black', font=('arial',15,'bold'), command=reg)        #Button is used to create a button.
        b1.place(x=200,y=340)

    suu.title("Supervisor")
    suu.configure(background='Black')
    suu.geometry("400x300")

    b1 = tkinter.Button(suu, text='LogIn',command=logi, bg='light green', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
    b1.place(x=60,y=100)

    b2 = tkinter.Button(suu, text='New User',command=new_user, bg='light green', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
    b2.place(x=220,y=100)

    b1 = tkinter.Button(suu, text='Open Hours', bg='light green', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
    b1.place(x=40,y=170)

    b2 = tkinter.Button(suu, text='Select students', bg='light green', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
    b2.place(x=200,y=170)

def logi():

    w = tkinter.Tk()
    f1=tkinter.Frame(w,bd=50)
    f1.pack()

    w.title('Login Page')
    tkinter.Label(f1, text="User    ").grid(row=0)
    tkinter.Label(f1, text = "Name").grid(row=1)




    us = tkinter.Entry(f1)
    nam =tkinter.Entry(f1)



    us.grid(row=0, column=1)
    nam.grid(row=1, column=1)


    tkinter.Button(f1, text='Login Now', command=w.destroy, bg='blue').grid(row=3, column=1, pady=4)
    tkinter.Button(f1, text='New User', command=w.destroy, bg='blue').grid(row=3, column=2, pady=4)

def new():

    w = tkinter.Tk()
    f1=tkinter.Frame(w,bd=50)
    f1.pack()

    w.title('New User Student')
    tkinter.Label(f1, text="Name                          ").grid(row=0)
    tkinter.Label(f1, text = "Registration Number").grid(row=1)
    tkinter. Label(f1, text = "Specialisation             ").grid(row=2)
    tkinter. Label(f1, text = "Mobile Number         ").grid(row=3)
    tkinter. Label(f1, text = "E-mail id                      ").grid(row=4)



    nam = tkinter.Entry(f1)
    reg =  tkinter.Entry(f1)
    blank =  tkinter.Entry(f1)
    blank1 = tkinter.Entry(f1)
    blank2 =  tkinter.Entry(f1)


    nam.grid(row=0, column=1)
    reg.grid(row=1, column=1)
    blank.grid(row=2, column=1)
    blank1.grid(row=3, column=1)
    blank2.grid(row=4, column=1)

    tkinter.Button(f1, text='Register', command=w.destroy , bg='blue').grid(row=5, column=1, pady=4)



    

top.title("Supervisor")
top.configure(background='Black')
top.geometry("700x200")

b1 = tkinter.Button(top, text='LogIn', command=logi,  bg='light blue', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
b1.place(x=50,y=100)

b2 = tkinter.Button(top, text='New User', command=new, bg='light blue', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
b2.place(x=150,y=100)

b1 = tkinter.Button(top, text='Request for Supervisor',command=super, bg='light blue', fg = 'black', font=('arial',15,'bold'))        #Button is used to create a button.
b1.place(x=300,y=100)



top.mainloop()
