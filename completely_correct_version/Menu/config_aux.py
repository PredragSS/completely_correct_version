def extensions(extension):
    extension=(extension.replace("Extensions:","")).split(',')
    return extension
def constraints(form,sign1,sign2):
    form=(form.replace("Form of assignmnets name:","")).split("|")
    const=[]
    #print(form)
    for i in form:
        i=i.strip()
        if sign1 in i:
            i=i.replace(sign1,"")
        if sign2 in i:
            i=i.replace(sign2,"")
        i=i.replace("(","")
        i=i.replace(")","")
        #print(i)

        temp=i.split(',')
        for j in temp:
            const.append(int(j))
    return const