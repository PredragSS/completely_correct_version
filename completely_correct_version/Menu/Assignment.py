import os

class assignment:
    def __init__(self, file, dir):
        self.file=file
        self.dir=dir
        self.curse_code=file[0:6]
        self.assignment_owner=file[6:len(file)-2]
        self.line_of_codes=self.add_lines()

    def add_lines(self):    #####Read all lines of code
        os.chdir(self.dir)
        line_arr=[]
        f=open(self.file,'r')
        line=f.readline()
        while line!='':
            line_arr.append(line[0:len(line)-1])
            line=f.readline()
        return line_arr