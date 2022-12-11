from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Stats:
    def __init__(self, grades, assignments):###Grades is array of Pass/Fail
        self.grades=grades
        self.assignments=assignments
        self.root=Tk()
        self.root.title("Statistics")
        self.root.resizable(False, False)
        self.root.geometry('700x547')

        self.draw_table()
        self.root.mainloop()

    def draw_table(self):
        c=0
        color=None
        col_shift=0
        for i in range(len(self.assignments)):
            row_shift = 0

            if not self.assignments[i]==[]:
                for j in self.assignments[i]:
                    if self.grades[c]:
                        color="green"
                    else:
                        color="red"
                    btn=Button(self.root,text=j.file,height=2,width=20, bg=color)
                    btn.place(x=100+row_shift*200,y=50+col_shift*80)

                    c+=1
                    row_shift+=1
                col_shift+=1

