from Tkinter import Tk, Label, Button, Checkbutton, Entry, W,LEFT, RIGHT, CENTER
import Tkinter as tk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Celsius <-> Farenheit")

        self.var = tk.IntVar()

        self.label = Label(master, anchor=CENTER, text="Temperature Conversion")
        self.label.grid(columnspan=3, rowspan=2, sticky=W)

        #self.labelInput = Label(master, text="Enter temperature", borderwidth=2, relief="solid")
        #self.labelInput.grid(row=2, column=1)

        self.textEntry = Entry(master, text="enter temperature")
        self.textEntry.grid(row=2, column=1)

        self.calculate_button = Button(master, text="Convert", command=self.calc)
        self.calculate_button.grid(row=2, column=2)
        #self.labelInput.pack(side=LEFT)

        self.converstion_type = Checkbutton(master, text="Farenheit",  variable=var)
        self.converstion_type.grid(row=3, column=1)
        #self.labelInput.pack(side=RIGHT)

        self.output = Label(master, text="...")
        self.output.grid(row=3, column=3)

        self.outputInput = Label(master, text="Converted Temperature", borderwidth=2, relief="solid")
        #self.outputInput.grid(row=1, column=2)
        #self.outputInput.pack(side=RIGHT)

    def calc(self):
        entry = self.textEntry.get()
        if(entry != "" and var.get()==False):
            #convert celsius to celsius
            val =  5*(int(entry)-32)/9
            self.output.config(text=str(val))   

        elif(entry != "" and var.get()==True):
            #convert celsius to farenheit
            val =  9*(int(entry)/5) + 32
            self.output.config(text=str(val))


root = Tk()
var = tk.IntVar()
my_gui = MyFirstGUI(root)
root.mainloop()
