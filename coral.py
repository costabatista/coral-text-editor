from tkinter import *
from tkinter import filedialog

def doNothing():
    x = 0

def createMainWindow():
    root = Tk()
    root.title("Coral Text Editor")
    root.geometry();
    return root


def addTextWidget(mainWindow):
    text=Text(mainWindow)
    text.pack(fill=BOTH, expand=YES)
    return text


def addSaveButton(mainWindow):
    button = Button(mainWindow, text="Save", command=saveAs)
    button.pack(side=RIGHT, padx=5, pady=5)


def addOpenButton(mainWindow):
    button = Button (mainWindow, text="Open")
    button.grid()


def saveAs():
    global filePath
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
    filePath = savelocation


def save():
    global filePath
    t = text.get("1.0", "end-1c")
    file1 = open(filePath, "w+")

    file1.write(t)
    file1.close()

def setText(value):
    text.delete(1.0, END)
    text.insert(END, value)

def openFile():
    global filePath
    openlocation = filedialog.askopenfilename()
    with open(openlocation) as f: 
        t = f.read()
    setText(t)
    filePath = openlocation


def addMenuBar(root):
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save as", command=saveAs)
    fileMenu.add_command(label="Save", command=save)
    fileMenu.add_command(label="Exit", command=doNothing)
    

    settingsMenu = Menu(menubar, tearoff=0)
    settingsMenu.add_command(label="Change color scheme", command=doNothing)
    
    helpMenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Settings", menu=settingsMenu)
    menubar.add_cascade(label="Help", menu=helpMenu)
    return menubar

def main():
    global text, filePath
    mainWindow = createMainWindow();
    text = addTextWidget(mainWindow)

    menubar = addMenuBar(mainWindow)
    
    mainWindow.config(menu=menubar)
    mainWindow.mainloop()

    
if __name__ == '__main__':
    main()
