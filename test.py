from rembg import remove
from PIL import Image

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os



def select_file():
    filetypes = (
        ('jpg', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    showinfo(
        title='status',
        message='file is getting processed please wait'
    )
    


    img = Image.open(filename)
    output = remove(img)
    dir_name = os.path.dirname(filename)
    out_path = os.path.join(dir_name,'output.png')
    output.save(out_path)
    
    showinfo(
        title='status',
        message='file processing completed'
    )
    
try:
    root = tk.Tk()
    root.title('Choose file')
    root.resizable(False, False)
    root.geometry('300x150')



    # open button
    open_button = ttk.Button(
        root,
        text='Open a File',
        command=select_file
    )

    open_button.pack(expand=True)


    # run the application
    root.mainloop()
except Exception as e:
    with open('./remove_bg.log','a') as fp:
        fp.write(str(e) + '\n')
        
    
