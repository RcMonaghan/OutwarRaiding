import tkinter
root = tkinter.Tk()

def clicked(label1):
    displayImage = PhotoImage(file = "upload.jpg")
    label1.configure(image = displayImage)


label1 = tkinter.Label(root, text = "")
label1.pack()

b1 = tkinter.Button(root, text = "Display", command = lambda: clicked(label1))
b1.pack()
root.mainloop()
