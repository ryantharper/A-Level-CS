"""
NOTES/To-Do:
    - Enter UserID, plot sales over time


"""

import tkinter as tk
import sqlite3 as lite, sys

#import matplotlib.pylot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Main application class - contains all frames
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initalise tk and frames
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginGUI, LINonAdminGUI, LIAdminGUI, Register, UserSales):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        # Show default frame
        self.show_frame("LoginGUI")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# FRAME GUIS:

# Login Frame
class LoginGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.db = lite.connect('logins.db')
        self.c = self.db.cursor()
    
        # Labels, Entry Boxes, Buttons 
        self.unLabel = tk.Label(self, text="Username").grid(row=0)
        self.pwLabel = tk.Label(self, text="Password").grid(row=1)
    
        self.unEntry = tk.Entry(self)
        self.unEntry.grid(row=0, column=1)

        self.pwEntry = tk.Entry(self, show="*")
        self.pwEntry.grid(row=1, column=1)

        self.loginButton = tk.Button(self, text="Login", command=self.callback)
        self.loginButton.grid(row=2)

        self.registerButton = tk.Button(self, text="Register", command=self.register)
        self.registerButton.grid(row=2,column=1)

        self.messageLabel = tk.Label(self, text="")
        self.messageLabel.grid(row=3, column=1)

        # Security Measure Variable
        self.security = 3

    def callback(self):
        print("Username: " + self.unEntry.get())
        print("Password: " + self.pwEntry.get())
        self.isCorrect()
        # Delete entry fields
        self.unEntry.delete(0,"end")
        self.unEntry.insert(0,"")
        self.pwEntry.delete(0,'end')
        self.pwEntry.insert(0,"")

    # Checks if username and password are correct
    def isCorrect(self):
        # 3 times
        self.c.execute("SELECT * FROM 'logins'")
        users = self.c.fetchall()
        # Create Lists of Usernames, Passwords and Admins from DB Query.
        usernames = [r[1] for r in users]
        passwords = [r[2] for r in users]
        admins = [r[1] for r in users if r[3]==1]

        print(usernames)
        print(passwords)
        print(admins)
        
        if self.unEntry.get() in usernames and self.pwEntry.get() in passwords:
            # if password entered is same index as username
            if self.pwEntry.get() == passwords[usernames.index(self.unEntry.get())]:
                if self.unEntry.get() in admins:
                    self.controller.show_frame("LIAdminGUI") # shows the logged in frame for ADMINS
                else:
                    self.controller.show_frame("LINonAdminGUI") # shows the logged in frame for Non-Admins
                    
                self.messageLabel["text"] = "" # clears any "access denied" text
                self.security = 3
            else:
                self.messageLabel["text"] = "Access Denied, " + str(self.security-1) + " tries left." # access denied
                self.security-=1
                print(self.security)
        else:
            self.messageLabel["text"] = "Access Denied, " + str(self.security-1) + " tries left." # access denied
            self.security-=1
            print(self.security)
        if self.security == 0:
            tk.messagebox.showerror("EXITING", "Wrong Username/Password Entered 3 times. Exiting Program.")
            self.controller.destroy()
            sys.exit()

    # Function that clears entry boxes + shows register frame
    def register(self):
        self.unEntry.delete(0,"end")
        self.unEntry.insert(0,"")
        self.pwEntry.delete(0,'end')
        self.pwEntry.insert(0,"")

        self.controller.show_frame("Register")
        
# Register frame            
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # connect to db
        self.db = lite.connect("logins.db")
        self.c = self.db.cursor()

        # Labels, Entry Boxes, Buttons
        self.newUnLabel = tk.Label(self, text="Username")
        self.newUnLabel.grid(row=0)

        self.newUnEntry = tk.Entry(self)
        self.newUnEntry.grid(row=0,column=1)
        
        self.newPwLabel = tk.Label(self, text="Password")
        self.newPwLabel.grid(row=1)

        self.newPwEntry = tk.Entry(self, show='*')
        self.newPwEntry.grid(row=1, column=1)

        self.registerBtn = tk.Button(self, text="Register", command=self.createLogin)
        self.registerBtn.grid(row=2)

        self.backBtn = tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("LoginGUI"))
        self.backBtn.grid(row=2,column=1)

    def createLogin(self):
        un = self.newUnEntry.get()
        pw = self.newPwEntry.get()       
        
        ifExists_OrEmpty = self.ifExists(un, pw)
        # if username exists and un or pw entry is not empty
        if ifExists_OrEmpty == False:        
            self.c.execute("INSERT INTO logins(username, passwd, admin) VALUES(?,?,?)", (un, pw, 0))
            self.db.commit()
            self.controller.show_frame("LoginGUI")
        # if username exists or un/pw entry box is empty
        else:
            tk.messagebox.showerror("ERROR", ifExists_OrEmpty)
            # Clear Username and Password entry boxes.
            self.newPwEntry.delete(0, "end")
            self.newPwEntry.insert(0, "")
            self.newUnEntry.delete(0, "end")
            self.newUnEntry.insert(0, "")
            
    # Function that determines whether the username the user entered
    # already exists or whether the username/password box is empty.
    def ifExists(self, un, pw):
        self.c.execute("SELECT username FROM 'logins'")
        usernames = self.c.fetchall()
        usernames = [y for x in usernames for y in x]
        print(usernames)

        if un in usernames:
            return "Username already exists"
        elif un.strip() == "" or pw.strip() == "":
            return "The username or password box is empty."
        else:
            False

# Logged In Non-Admin Frame
class LINonAdminGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        

        # Labels + Buttons
        loggedInLabel = tk.Label(self, text="You are logged in as a regular user")
        loggedInLabel.grid(row=0)

        logOutBtn = tk.Button(self, text="Log Out", command=lambda: controller.show_frame("LoginGUI"))
        logOutBtn.grid(row=1, column=0)

# Logged In Admin frame
class LIAdminGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.db = lite.connect("logins.db")
        self.c = self.db.cursor()
        
        # Labels + Buttons
        adminLabel = tk.Label(self, text="You are logged in as an admin")
        adminLabel.grid(row=0)

        adminLogOutBtn = tk.Button(self, text="Log Out", command=lambda: controller.show_frame("LoginGUI"))
        adminLogOutBtn.grid(row=1, column=0)

        userSalesBtn = tk.Button(self,text="User Sales over Time", command=lambda: controller.show_frame("UserSales"))
        userSalesBtn.grid(row=2)

        self.makeGraph1()
        self.makeGraph2()

    def makeGraph1(self):
        # Get Sales Info -- Number of Sales:
        self.c.execute("SELECT userId, username FROM 'logins'")
        userInfo = self.c.fetchall()
        userIds = [i[0] for i in userInfo]
        usernames = [i[1] for i in userInfo]

        users_sales_dict = {}
        
        for uid in userIds:
            self.c.execute("SELECT SaleId FROM 'Sales' WHERE User=?",(uid,))
            users_sales_dict[uid] = [sId[0] for sId in self.c.fetchall()]

        labels = usernames
        sizes = [len(users_sales_dict[uid]) for uid in userIds]

        f = Figure(figsize=(3,2), dpi=100)
        a = f.add_subplot(111)

        a.pie(sizes, labels=labels, autopct='%1.1f%%',
              shadow=True, startangle=90)
        a.axis('equal')
        a.set_title('Percentage of the Number of Sales')
        canvas = FigureCanvasTkAgg(f,self)
        canvas.get_tk_widget().grid()

    def makeGraph2(self):
        # Get Sales Info -- Cumulated Sales Values
        self.c.execute("SELECT userId, username FROM 'logins'")
        userInfo = self.c.fetchall()
        userIds = [i[0] for i in userInfo]
        usernames = [i[1] for i in userInfo]

        users_saleVals = {}

        for uid in userIds:
            self.c.execute("SELECT SaleValue FROM 'Sales' WHERE User=?", (uid,))
            users_saleVals[uid] = [sV[0] for sV in self.c.fetchall()]

        labels = usernames
        sizes = [sum(users_saleVals[uid]) for uid in userIds]

        f = Figure(figsize=(3,2), dpi=100)
        a = f.add_subplot(111)

        a.pie(sizes, labels=labels, autopct='%1.1f%%',
              shadow=True, startangle=90)
        a.axis('equal')
        a.set_title('Percentage of the Cost of Sales')
        canvas = FigureCanvasTkAgg(f,self)
        canvas.get_tk_widget().grid()

class UserSales(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.db = lite.connect("logins.db")
        self.c = self.db.cursor()

        backBtn = tk.Button(self, text="Back to Admin Page", command=lambda: controller.show_frame("LIAdminGUI"))
        backBtn.grid()

        userIdEntry = tk.Entry(self)
        userIdEntry.grid(row=1,column=0)

        userIdBtn = tk.Button(self, text="Find User Sales over Time", command=self.userSalesOverTime)
        userIdBtn.grid(row=1,column=1)

    # PLOT USERS ON SAME PLOT
    # PLOT DATE AS X, SALE+VALUE AS Y
    def userSalesOverTime(self):
        self.c.execute("SELECT userId, username FROM 'logins'")
        

def main():
    app = MainApp()
    app.geometry("325x500")
    app.mainloop()

main()
