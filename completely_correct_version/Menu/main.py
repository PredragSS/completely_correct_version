from tkinter import *#####Modify
from tkinter import filedialog
from tkinter import messagebox
import os
import StaticReqConf
from Assignment import assignment

from AuxiliarFunctions import *
from StaticReqConf import Config
from Run import RunTest
from config_aux import *
'''
Shape of assignmen: DVA321PredragLba1
Type of files: c,py,cs
'''

'''
I am not handle case when you choose multiple folders of assignments
Errors that occured is bad handled code of listbox of tkinter but they occured just in terminal
'''

class MainMenu:
    def __init__(self,constraint_start,constraint_end,number_of_labs):#####x and y are constraints that need to be changed by values from configuration.txt
        ##########################################################################
        self.test_array=[]##############
        self.test_saver=None
        self.num_labs=number_of_labs
        ##########################################################################
        self.constraint_start=constraint_start
        self.constraint_end=constraint_end
        self.desired_dir=None#When you want to search for desired folder where are assignments
        self.menu_dir=os.getcwd()#Path to the this project directory
        self.dir_of_project=os.getcwd().replace("Menu",'')

        path_to_configurations = self.dir_of_project + "Configuration"
        read_configurations(path_to_configurations)

        self.existing_configurations=read_configurations(self.dir_of_project+"Configuration")######Read all existing system configurations
        self.static_requirements=read_configurations(self.dir_of_project+"Requirements")###Read just once all requirements
        self.arr=[]##############Mozda brisat
        self.requirements=None
        self.all_assignments=None
        #####Table position
        ###Positions of tables
        #It needs to be changed in %
        self.x = 130
        self.y = 295
        ###################
        ####Window configuration####
        self.root = Tk()
        self.root.title("Assignment Analiser MainMenu")
        self.root.resizable(False, True)
        self.size_x=700
        self.size_y=547

        self.root.geometry("700x547")#####This needs to be changed

        self.root.configure(bg='white')
        self.c = 0  #####Auxiliary value

        self.left_side()
        self.middle_space()
        self.bottom_side()

        self.root.mainloop()
    def left_side(self):
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 1, weight=1)
        path_to_requirements=self.dir_of_project+"Requirements"
        b1 = Button(self.root, text="Static \nRequirements \nConfiguration", compound='c', height=10, width=10,
                    fg="black", borderwidth=2, relief=SOLID, command= lambda :Config.StaticConfig(path_to_requirements))#,command=lambda: Config.StaticConfig(str(self.dir_of_project,"Requirements")))

        #b1.place(x=0, y=0)
        b1.grid(row=0,column=0,sticky="NSEW")
        b2 = Button(self.root, text="Dynamic \nRequirements \nConfiguration", compound='c', height=10, width=10,
                    fg="black", borderwidth=2, relief=SOLID)
        #b2.place(x=0, y=180)
        b2.grid(row=1,column=0,sticky="NSEW")
        #b2.place(x=0,y=self.size_y-(self.size_y/2))

        b2 = Button(self.root, text="Run Test", compound='c', height=10, width=10, fg="black", borderwidth=2,
                    relief=SOLID, command=lambda : RunTest.Run(self.arr, self.requirements, (self.dir_of_project+"Requirements"),self.desired_dir,self.test_array))#command=lambda: self.testing()   RunTest.Run() print(self.requirements,'  \n',self.arr)
        #b2.place(x=0, y=360)
        b2.grid(row=3,column=0,sticky="NSEW")
    ###############################################
    def middle_space(self):
        label1 = Label(self.root, text="Setting manual system configuration", font='Arial 18 bold', bg="white")
        label1.place(x=130, y=10)

        create_btn = Button(self.root, text="Manual", bg="#D3D3D3", height=1, width=10, font='Arial 10 bold')#command=lambda: self.select_requirements()
        create_btn.place(x=130, y=60)

        label1 = Label(self.root, text="Select existing configurations", font='Arial 18 bold', bg="white")
        label1.place(x=130, y=100)
        self.clicked=StringVar()
        self.clicked.set("None")
        drop=OptionMenu(self.root,self.clicked,*self.existing_configurations)
        drop.config(bg="white")
        drop.place(x=130,y=140)

    def bottom_side(self):
        names = ["Name", "No. requirements", "Edit"]
        self.first_part_table()
        upload_btn=Button(self.root, text="Upload", bg="#D3D3D3", height=1, width=10, font='Arial 10 bold', command = lambda:self.second_part_table())#.place(x=self.size_x-100,y=self.size_y-100)
        upload_btn.grid(row=3,column=3)

    def upload(self):#####Mozda promeniti u return
        a = self.clicked.get()
        if a=='None':
            messagebox.showerror("Error","You didn't select configuration")
            return False

        lines=read_config_file(self.dir_of_project+"Configuration",a)

        self.type_assignment_entry=extensions(lines[1])##########################Position 1 is info. Take all extensions
        ###########IZMENITI sign1,2 u dinamicki niz
        const=constraints(lines[0],"CourseCode","Lab")#####################On position 0 is info about constraints


        self.constraint_start=const[0]
        self.constraint_end=const[1]
        self.const_lab_start=None
        self.const_lab_end=None
        if len(const)>2:
            self.const_lab_start=int(const[2])
            self.const_lab_end=int(const[3])

        filename = filedialog.askopenfilename()
        if len(filename)==0:
            return False
        self.desired_dir=os.path.dirname(filename.strip())#######Taking dir path of assignments folder
        return True
    def onclick(self, event, pos):
        w = event.widget
        index = w.get(w.curselection()[0])
        self.selected1=index
        self.requirements[pos] = index####Making list of requirements in the dropbox
    def onselect(self,selected,pos):
        if not selected==None:
            self.requirements[pos]=selected
    def SS(self,selected):
        self.test_array[self.pos][self.pos_in_arr]=selected
    def setSelection(self,curr,pos,p):
        self.test_saver=curr
        self.pos=pos
        self.pos_in_arr=p
        #print(self.test_saver,'  ',self.pos,'  ',self.pos_in_arr)
    def addRequirement(self, req, assignment, pos):
        self.test_array[pos][self.save_assignments[pos].index(assignment)]=req

    def first_part_table(self):
        names = ["Name", "No. requirements", "Options"]
        ####Drawing first row
        for i in range(0, 3):  ######Fixed on three columns
            self.e = Text(self.root, width=20, height=2, bg="#D3D3D3")
            self.e.place(x=self.x + 150 * i, y=self.y)
            self.e.tag_configure("tag_name", justify='center', font=("Arial 10 bold"))
            self.e.insert("1.0", names[i])
            self.e.tag_add("tag_name", "1.0", "end")
    def SS(self,selected):
        self.test_array[self.pos][self.pos_in_arr]=selected
    def second_part_table(self):
        a=self.upload()
        if a==False:
            return
        self.pos=None
        arr=make_arr_files(self.type_assignment_entry,self.desired_dir,self.constraint_start,self.constraint_end)##########################Change
        requirements=read_folder((self.dir_of_project+"Requirements"),'.txt')######Requirments need to txt extension
        self.requirements=[0 for i in range(len(arr))]

        self.test_array = [[[None] for j in range(self.num_labs)] for i in range(len(arr))]

        self.arr=arr
        c = 0
        t = 0####Auxilliary variables for drawing
        s = 0
        self.save_assignments=[[] for j in range(len(self.arr))]#This is auxiliary variable and contains only name of assignments(assignment.file)

        count = 0
        for rows in arr:
            for j in rows:
                print(j.file)
        curr_size_x=0
        curr_size_y=0
        for rows in arr:
            log = False
            cols=0
            temp_arr=[]#We use this to check does lab appear more than onec
            count2=0
            while cols<len(rows):
                #print(rows[cols].file,'   ',cols)
                for j in range(3):
                    e = Text(self.root, width=20, height=2)
                    curr_size_x=self.x + 150 * j
                    curr_size_y=self.y + 40 * (c + 1)
                    e.place(x=curr_size_x, y=curr_size_y)
                    if not log and j == 0:
                        e.insert("1.0", rows[cols].file[self.constraint_start:self.constraint_end])  ####0 and 6 are constraints
                        e.tag_add(rows[cols].file[self.constraint_start:self.constraint_end], "1.0", "end")
                        e.tag_configure(rows[cols].file[self.constraint_start:self.constraint_end], justify='center')
                        #self.save_assignments.append(rows[cols].file[self.constraint_start:self.constraint_end])
                        self.save_assignments[count].append(rows[cols].file[self.constraint_start:self.constraint_end])
                        #print(self.save_assignments[count][cols],"     DD   ",rows[cols].file)
                        cols-=1
                    elif j == 0:
                        e.insert("1.0",rows[cols].file[self.const_lab_start:self.const_lab_end])  ####0 and 6 are constraints
                        e.tag_add(rows[cols].file[self.const_lab_start:self.const_lab_end], "1.0", "end")
                        e.tag_configure(rows[cols].file[self.const_lab_start:self.const_lab_end], justify='center')
                        self.save_assignments[count].append(rows[cols].file[self.const_lab_start:self.const_lab_end])
                    elif j==1 and not log:
                        e.insert("1.0", len(rows))  ####0 and 6 are constraints
                        e.tag_add(len(rows), "1.0", "end")
                        e.tag_configure(len(rows), justify='center')
                        log = True####For the course name
                    elif j==2:
                        selected = StringVar()
                        selected.set("None")
                        drop = OptionMenu(self.root, selected, *self.static_requirements, command=lambda assignment=selected,req=self.save_assignments[count][count2], pos=count, ss=cols: self.addRequirement(assignment,req,pos)).place(x=self.x + 170 * j,y=self.y + 40 * (t + 1))####DONT TOUCH THIS
                        # drop = OptionMenu(self.root, selected, *self.static_requirements, command= lambda sel=selected, pos=s:self.onselect(sel,pos)).place(x=self.x + 170 * j, y=self.y + 40 * (t + 1))#####Change name of static requirements
                        t += 1
                    if curr_size_y > self.size_y-300:
                        self.size_y = curr_size_y+200
                        self.root.geometry("{x}x{y}".format(x=self.size_x, y=self.size_y))
                cols+=1
                c+=1
                count2+=1
            count+=1


a=MainMenu(0,3,5)