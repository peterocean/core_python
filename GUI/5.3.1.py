#!/usr/bin python3


import tkinter

top = tkinter.Tk()
label = tkinter.Label(top,text = 'Hello World')
label.pack()

quit = tkinter.Button(top, text = 'Hello World',
                      command = top.quit,bg = 'red', fg = 'white')
quit.pack(fill = tkinter.X, expand = 1)

tkinter.mainloop()
