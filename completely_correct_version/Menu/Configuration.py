import os
class config:
    def __init__(self, name):
        self.name=name
        self.words=[]
    def read_configurations(self, path):
        os.chdir(path)
        a=open(self.name,'r')
        lines=[]
        line=a.readline()
        while not a=='':
            lines.append(a)
            a=a.readline()
        return lines