from tkinter import *
from tkinter import messagebox
from tkinter import ttk

List = []

class Doto:
    def __init__(self, AName, Gender, Type):
        self.AName = AName
        self.Gender = Gender
        self.Type = Type

    def getName(self):
        return self.AName

    def getGender(self):
        return self.Gender
    
    def getAnimal(self):
        return self.Type


def add():
    global List
    global tview
    List.append(Doto(e1.get(), e2.get(), e3.get()))
    messagebox.showinfo("Message", "Data has been added!")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    for dat in List:
        tview.insert('', 'end',values=(dat.AName,dat.Gender,dat.Type))

    List.clear()

def update():
    selected_item = tview.selection()[0]
    tview.item(selected_item, values=(e1.get(), e2.get(), e3.get()))
    messagebox.showinfo("Message", "Data has been changed!")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

def content(event):
    print(tview.selection())

    for ph in tview.selection():
        AName, Gender, Type  = tview.item(ph, 'values')
        e1.insert(END, AName)
        e2.insert(END, Gender)
        e3.insert(END, Type)


    

def delete():
    selected_item = tview.selection()[0]
    tview.delete(selected_item)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


    
window = Tk()
window.title("Simple System")
window.configure(bg="#fcba03")



label1 = Label(window, text="Name: ",bg="#fcba03")
label1.grid(row=0, column=0, padx=10, pady=5)

label2 = Label(window, text="Gender: ",bg="#fcba03")
label2.grid(row=1, column=0, padx=10, pady=5)

label3 = Label(window, text="Animal: ",bg="#fcba03")
label3.grid(row=2, column=0, padx=10, pady=5)



e1 = Entry()
e1.grid(row=0, column=1, padx=10, pady=5)

e2 = Entry()
e2.grid(row=1, column=1, padx=10, pady=5)

e3 = Entry()
e3.grid(row=2, column=1, padx=10, pady=5)



b1=Button(window,text="Add",bg="#c9a74f", width=10, command=add)
b1.grid(row=0, column=2, padx=10, pady=5)

b2=Button(window,text="Change", bg="#c9a74f", width=10, command=update)
b2.grid(row=1, column=2, padx=10, pady=5)

b3=Button(window,text="Remove", bg="#c9a74f", width=10, command=delete)
b3.grid(row=2, column=2, padx=10, pady=5)

b4=Button(window,text="Exit", bg="#cc7149", width=10, command =window.destroy)
b4.grid(row=3, column=2, padx=10, pady=5)



tview = ttk.Treeview(window, height = 15)
tview.grid(row =6, columnspan = 3)

tview["columns"] = ("Name","Gender","Animal")
tview.column("#0", width=0, stretch=NO)
tview.column("Name")
tview.column("Gender")
tview.column("Animal")


tview.heading("#1",text="Name",anchor=W)
tview.heading("#2", text="Gender", anchor=W)
tview.heading("#3", text="Animal", anchor=W)

tview.bind("<<TreeviewSelect>>", content)

window.mainloop()
