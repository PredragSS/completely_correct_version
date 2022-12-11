from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
#########Somer
class StaticConfig:
    def __init__(self, dir_req):
        self.dir_req=dir_req
        os.chdir(self.dir_req)
        self.root=Tk()
        self.root.title("Static Requirement Configuration")
        self.root.resizable(False, False)
        self.root.geometry('400x400')

        self.root.configure(bg='white')

        self.draw_window()

        self.root.mainloop()

    def draw_window(self):
        lbl = Label(self.root, text="Name: ", bg="white", font="Arial 14 bold")
        lbl.place(x=50, y=50)
        self.txt = Entry(self.root)  #################################Name of the new file of requirements
        self.txt.place(x=120, y=50, width=250)

        lbl2 = Label(self.root, text="Requirements: ", bg="white", font="Arial 14 bold")
        lbl2.place(x=50, y=150)

        add_btn = Button(self.root, text="Create", font="Arial 11 bold", command=lambda: self.add())
        add_btn.place(x=280, y=147)

        must_have_label = Label(self.root, text="Must have: ", bg="white", font="Arial 12 bold")
        must_have_label.place(x=50, y=240)

        self.txt_must_have = Entry(self.root)
        self.txt_must_have.place(x=200, y=240)
        ###########################################################################################################################

        must_not_have_label = Label(self.root, text="Must not have: ", bg="white", font="Arial 12 bold")
        must_not_have_label.place(x=50, y=280)

        self.txt_must_not_have = Entry(self.root)
        self.txt_must_not_have.place(x=200, y=280)
        ###########################################################################################################################

        command_label = Label(self.root, text="Command: ", bg="white", font="Arial 12 bold")
        command_label.place(x=50, y=320)

        self.txt_command = Entry(self.root)
        self.txt_command.place(x=200, y=320)

        ############################################################################################################################
        save_btn = Button(self.root, text="Add", font="Arial 11 bold", command=lambda: self.save())
        save_btn.place(x=280, y=350)
################################################################
    def save_add_functionality(self, type_of_writing):

        if not (self.txt.get().endswith('.txt')):###############Requirements must end with .txt
            messagebox.showerror("Error","File must end with .txt extension {x}!!!".format(x=self.txt.get()))
            return False
        file = open(self.txt.get(), type_of_writing)

        txt_mh = self.txt_must_have.get()
        txt_mnh = self.txt_must_not_have.get()
        txt_command = self.txt_command.get()
        curr = None
        if len(txt_mh)>0:
            curr = 'Must have:{x}\n'.format(x=txt_mh)
            file.writelines(str(curr))
        if len(txt_mnh)>0:
            curr = "Must not have:{x}\n".format(x=txt_mnh)
            file.writelines(str(curr))
        if len(txt_command)>0:
            if ('{x}' not in txt_command):
                messagebox.showinfo("Command","Command aren't added because must be in format '{x}' for name of file")
                return False
            curr = "Command:{x}\n".format(x=txt_command)
            file.writelines(str(curr))
        return True

    def add(self):

        if(os.path.isfile(self.txt.get())):
            messagebox.showerror("Error", "File {x} exist. Try another option!!!".format(x=self.txt.get()))
            return
        if self.save_add_functionality('w'):###W for writing
            messagebox.showinfo("Creating", "You are create new file of requirements {x}".format(x=self.txt.get()))
    def save(self):#For creating new file
        if not (os.path.isfile(self.txt.get())):
            messagebox.showerror("Error", "File {x} doesn't exist. First create file!!!".format(x=self.txt.get()))
            return
        if self.save_add_functionality('a'):###A for appearing
            messagebox.showinfo("Adding","You are add new requirements in {x} file".format(x=self.txt.get()))

#a=StaticConfig("/home/predrag/PycharmProjects/projectRefactored/Requirements")