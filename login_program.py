import tkinter as tk
import sqlite3 as lite, sys

# Main application class - contains all frames
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginGUI, LINonAdminGUI, LIAdminGUI, Register):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0,column=0,sticky="nsew")

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

    # Checks if username and password is correct
    def isCorrect(self):
        # 3 times
        self.c.execute("SELECT * FROM 'logins'")
        users = self.c.fetchall()
        usernames = [r[1] for r in users]
        passwords = [r[2] for r in users]
        admins = [r[1] for r in users if r[3]==1]

        security = 0
        if self.unEntry.get() in usernames and self.pwEntry.get() in passwords:
            if usernames.index(self.unEntry.get()) == passwords.index(self.pwEntry.get()):
                if self.unEntry.get() in admins:
                    self.controller.show_frame("LIAdminGUI") # shows the logged in frame
                else:
                    self.controller.show_frame("LINonAdminGUI") # shows the logged in frame
                    
                self.messageLabel["text"] = "" # clears any "access denied" text
                self.security = 3
            else:
                self.messageLabel["text"] = "Access Denied" # access denied, wrong un/pw
                self.security-=1
                print(self.security)
        else:
            self.messageLabel["text"] = "Access Denied" # access denied, wrong un/pw
            self.security-=1
            print(self.security)
        if self.security == 0:
            self.controller.destroy()
            sys.exit()

    def register(self):
        self.unEntry.delete(0,"end")
        self.unEntry.insert(0,"")
        self.pwEntry.delete(0,'end')
        self.pwEntry.insert(0,"")

        self.controller.show_frame("Register")
        
            
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.db = lite.connect("logins.db")
        self.c = self.db.cursor()

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

    def createLogin(self):
        un = self.newUnEntry.get()
        pw = self.newPwEntry.get()

        self.c.execute("INSERT INTO logins(username, passwd, admin) VALUES(?,?,?)", (un, pw, 0))
        self.db.commit()
        self.controller.show_frame("LoginGUI")
        


# Logged in Frame
class LINonAdminGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        loggedInLabel = tk.Label(self, text="You are logged in as a regular user")
        loggedInLabel.grid(row=0)

        logOutBtn = tk.Button(self, text="Log Out", command=lambda: controller.show_frame("LoginGUI"))
        logOutBtn.grid(row=1, column=0)


class LIAdminGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        adminLabel = tk.Label(self, text="You are logged in as an admin")
        adminLabel.grid(row=0)

        adminLogOutBtn = tk.Button(self, text="Log Out", command=lambda: controller.show_frame("LoginGUI"))
        adminLogOutBtn.grid(row=1, column=0)

def main():
    app = MainApp()
    app.geometry("200x150")
    app.mainloop()

main()
