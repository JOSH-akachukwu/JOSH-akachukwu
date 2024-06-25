from tkinter import*
root = Tk()
root.wm_geometry

class values:
    def __init__ (self,name1,name2,name3):
        self.nameentry = name1
        self.name2entry = name2
        self.name3entry = name3
    def getvalue(self):
        print(self.nameentry,self.name2entry,self.name3entry)

def getvals():
    print('Accepted')
    x = values(namevalue,name2value,name3value)
    x.getvalue()


Label(root, text='Welcome to Josh Environment').grid(row= 0, column = 2)

name = Label(root, text='Name').grid(row = 3, column= 2)
name2 = Label(root, text='SSID').grid(row = 4, column= 2)
name3= Label(root, text='Class').grid(row = 5,column= 2)

namevalue = StringVar
name2value = StringVar
name3value = StringVar
checkbnt = IntVar

nameentry = Entry(textvariable = namevalue)
name2entry =Entry(textvariable= name2value)
name3entry =Entry(textvariable= name3value)

nameentry.grid(row = 3, column = 3)
name2entry.grid(row =4, column = 3)
name3entry.grid(row =5, column = 3)

checkbnt = Checkbutton(root, text='click me',variable= checkbnt)
checkbnt.grid(row= 7,column= 3,)

Button(text='submit', command=getvals).grid(row= 8, column= 2)
Button(text= 'Exit',command=root.destroy).grid(row= 8,column= 3)

root.mainloop()