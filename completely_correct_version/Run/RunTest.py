import os
from Statistics import statistics
from tkinter import messagebox
class Run:
    def __init__(self, assignments, requirements, path_of_requirements, path_of_assignments,testing):####In testing is new way for testing program. Implement it instead of requirements
        self.testing=testing
        self.assignments=assignments
        self.requirements=requirements
        self.path_of_requirements=path_of_requirements
        self.path_of_assignments=path_of_assignments
        self.array_of_errors=[[None] for i in assignments]
        if len(assignments)==0:
            messagebox.showerror("Error","You did not select any folder for testing. Please select and try again.")
            return

        os.chdir(self.path_of_requirements)
        self.grades=[True for i in range(len(self.requirements))]
        #print(self.assignments[0][0].file)
        c=0
        mistake_matrix=[]
        self.mistakes=[]
        c=1
        count = 0
        for i in range(len(self.assignments)):
            if not self.assignments[i] == []:
                c=1

                for j in range(0,len(self.assignments[i])):
                    if not self.testing[i][0]==[None]:
                        self.Test2(self.assignments[i][j],self.testing[i][0])
                        #print(self.testing[i][0],end=' ')
                    if not self.testing[i][c] == [None]:
                        self.Test2(self.assignments[i][j], self.testing[i][c])
                        #print(self.testing[i][c],end=' ')
                    #print()

                    mistake_matrix.append(self.mistakes)
                    if len(self.mistakes)>0:
                        self.grades[count]=False
                        #print(self.assignments[i][j].file,' =>  ',self.mistakes)
                    self.mistakes=[]
                    c+=1
                    count+=1

        #print(mistake_matrix)
        c=0
        for i in range(len(self.assignments)):

            if not self.assignments[i] == []:
                for j in range(0, len(self.assignments[i])):
                    print(self.assignments[i][j].file,'   ',mistake_matrix[c])
                    c+=1

        statistics.Stats(self.grades,self.assignments)
####################################
    def take_requirements(self, requ_name):
        os.chdir(self.path_of_requirements)
        not_have = []
        have = []
        command = []
        file = open(requ_name, "r")
        a = file.readline()
        while a != '':
            arr = a.split(':')
            if "Must not have" in arr[0]:######Making list instead of text
                not_have.append(arr[1])
            if "Must have" in arr[0]:
                have.append(arr[1])
            if "Command" in arr[0]:
                command.append(arr[1][:len(arr[1]) - 1])
            a = file.readline()
        return [not_have, have, command]

    def check_compilation(self, command):  ############
        os.chdir(self.path_of_assignments)
        if os.system(command) == 0:
            return True
        else:
            return False

    def match_keyword(self,line,must_not_have):
        must_not_have=must_not_have[0:len(must_not_have)-1]
        must_not_have=must_not_have.lstrip()
        arr=line.split(' ')
        if must_not_have in line:
                return True
        return False

    def match_keyword2(self,line,must_not_have):
        must_not_have=must_not_have[0:len(must_not_have)-1]
        must_not_have=must_not_have.lstrip()
        arr=line.split(' ')
        if must_not_have in line:
                return must_not_have
        return []

    def Test2(self,assignment,requirement):
        counter=0
        assignment_name=assignment.file
        req=self.take_requirements(requirement)####0:Must have 1:Must not have 2:Command
        if len(req[2])>0:#####Checking position for compilation. If exist test
            command=str((str(req[2][0]).format(x=assignment_name)))
            if not self.check_compilation(command):
                self.mistakes.append("Can not compile")
                '''print(assignment_name,' can not compile')
                return False'''
        if not req[0]==[]:
            for i in assignment.line_of_codes:
                for j in range(len(req[0])):
                    if '<' in req[0][j] or '>' in req[0][j]:
                        if self.comparison(req[0][0],i)==1:
                            self.mistakes.append(("Not required variables length ",(counter+1)))
                            #return False
                    elif self.match_keyword(i,req[0][j]):
                        self.mistakes.append(("Not required keyword {x}".format(x=i)," ",counter))
                counter+=1
        if req[1]==[]:
            return True
        log=False
        on_all_places=True
        for i in assignment.line_of_codes:
            if not req[1]==[]:
                if '<' in req[1][0] or '>' in req[1][0]:
                    if self.comparison(req[0][0],i)==0:
                        return False
                elif self.match_keyword(i,req[1][0]):
                    return True

        return False

    def comparison(self, sign, line):  #####-1 not variable | 1 True | 0 False
        if not self.is_variable(line):
            # print("Not variable ",line)#######sign=> variables >2####line= int a=123
            return -1
        line = line.split('=')
        a = line[0]#variablse >2
        if '>' in sign and len(a) > 1:#######
            a = a.split(' ')[1]
            num = sign.split('>')
            if len(a) > int(num[1]):
                return 1
            else:
                return 0
        elif '<' in sign and len(a) > 1:
            a = a.split(' ')[1]
            num = sign.split('<')
            if len(a) < int(num[1]):
                return 1
            else:
                return 0
        return -1

    def is_variable(self,line):
        if len(line) < 1:
            return False
        if 'return' in line:
            return False
        if '(' in line:
            return False
        if 'int' in line or 'float' in line or 'double' in line or 'String' in line or 'char' in line:
            return True

        return False




