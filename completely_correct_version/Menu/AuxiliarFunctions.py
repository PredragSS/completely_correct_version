from Assignment import assignment
from tkinter import filedialog
import os
####This function is auxilliary function for make_arr_files
def take_pos(name, curr_pos, arr, constraint_start, constraint_end): #constraint is used for finding what is course, lab... For example DVA334MarkoMarkovic  we want name of course DVA334, for Lab1StevanStevanovic we want Lab1...It will be specified in CONFIGURATION
    c = 0
    for i in range(curr_pos, len(arr)):
        a = arr[i]
        if name[constraint_start:constraint_end] == a.file[constraint_start:constraint_end]:
            c = i
    return c

####This function is used to group assignments by coursename, lab... in matrix shape
###[0]DVA332   =>  MarkoMarkovic, StevanStevanovic
###[1]CDT653   =>  IvanIvanovic
###...
def make_arr_files(file_type, file_name, constraint_start, constraint_end):
    temp_arr=[]
    arr=[]
    i=0
    for file in os.listdir(file_name):
        for i in file_type:
            if file.endswith(('.'+i)):
                arr.append(assignment(file, file_name))
    curses=[[] for i in range(len(arr))]
    for i in range(0,len(arr)):
        curses[take_pos(arr[i].file,i,arr,constraint_start,constraint_end)].append(arr[i])
    return curses

def counter(curr_dir, course_code, type_of_file, constraint_start,constraint_end):
    c=0
    for file in os.listdir(curr_dir):
        if file.endswith(type_of_file) and course_code[constraint_start:constraint_end]==file[constraint_start:constraint_end]:
            c+=1
    return c
def read_folder(path, type_of_file):####type_of_file needs to be array of required files
    arr=[]
    for i in os.listdir(path):
        if i.endswith(type_of_file):
            arr.append(i)
    return arr
def read_configurations(path):
    arr=[]
    for i in os.listdir(path):
        arr.append(i)
    return arr
def read_config_file(path, name):
    os.chdir(path)
    file=open(name,'r')
    lines=[]
    line=file.readline()
    while not line=='':
        lines.append(line)
        line=file.readline()
    return lines
#a=make_arr_files('c','/home/predrag/Test2')
#print(a)