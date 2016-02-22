#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Feb 04, 2016 05:14:07 PM
# Implemented by HJ Kiela Opteq mechatronics BV Febr 2016
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import About_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('About_SWM_GUI')
    geom = "329x188+414+189"
    root.geometry(geom)
    w = About_SWM_GUI (root)
    About_support.init(root, w)
    root.mainloop()

w = None
def create_About_GUI(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('About_SWM_GUI')
    geom = "329x188+414+189"
    w.geometry(geom)
    w_win = About_SWM_GUI (w)
    About_support.init(w, w_win, param)
    return w_win

def destroy_About_SWM_GUI():
    global w
    w.destroy()
    w = None


class About_SWM_GUI:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background="#d9d9d9")


        self.btn_close = Button(master)
        self.btn_close.place(relx=0.46, rely=0.05, height=31, width=131)
        self.btn_close.configure(activebackground="#d9d9d9")
        self.btn_close.configure(activeforeground="#000000")
        self.btn_close.configure(background=_bgcolor)
        self.btn_close.configure(command=About_support.do_close)
        self.btn_close.configure(disabledforeground="#a3a3a3")
        self.btn_close.configure(foreground="#000000")
        self.btn_close.configure(highlightbackground="#d9d9d9")
        self.btn_close.configure(highlightcolor="black")
        self.btn_close.configure(pady="0")
        self.btn_close.configure(text='''Close''')
        self.btn_close.configure(width=131)

        self.TLabel1 = ttk.Label(master)
        self.TLabel1.place(relx=0.0, rely=0.0, height=118, width=135)
        self.TLabel1.configure(background=_bgcolor)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Tlabel''')
        self.TLabel1.configure(width=135)
        self._img1 = PhotoImage(file="./logo.gif")
        self.TLabel1.configure(image=self._img1)

        self.Label1 = Label(master)
        self.Label1.place(relx=0.03, rely=0.74, height=19, width=180)
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''(c) Jan 2016 Opteq mechatronics BV''')

        self.Label2 = Label(master)
        self.Label2.place(relx=0.03, rely=0.85, height=19, width=284)
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''For questions and remarks, contact us at hkiela@opteq.nl''')

        self.Label3 = Label(master)
        self.Label3.place(relx=0.43, rely=0.27, height=19, width=152)
        self.Label3.configure(background=_bgcolor)
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''SWM GUI with UDP connection''')

        self.Label4 = Label(master)
        self.Label4.place(relx=0.43, rely=0.37, height=19, width=28)
        self.Label4.configure(background=_bgcolor)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''V0.1''')

        self.Label5 = Label(master)
        self.Label5.place(relx=0.43, rely=0.48, height=19, width=161)
        self.Label5.configure(background=_bgcolor)
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Feel free to modify this software''')
        self.Label5.configure(width=161)

        self.Label6 = Label(master)
        self.Label6.place(relx=0.43, rely=0.59, height=19, width=174)
        self.Label6.configure(background=_bgcolor)
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''And post your work back on Github''')






if __name__ == '__main__':
    vp_start_gui()



