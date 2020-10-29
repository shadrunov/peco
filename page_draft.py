#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Oct 22, 2020 06:30:56 PM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import page_draft_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    page_draft_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    page_draft_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1000x600+387+146")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(0,  0)
        top.title("peco")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.BtnFrame = tk.Frame(top)
        self.BtnFrame.place(x=0, y=0, height=600, width=130)
        self.BtnFrame.configure(background="#C5E1A5")
        self.BtnFrame.configure(highlightbackground="#d9d9d9")
        self.BtnFrame.configure(highlightcolor="black")

        self.BackBtn = tk.Button(self.BtnFrame)
        self.BackBtn.place(x=30, y=30, height=72, width=72)
        self.BackBtn.configure(activebackground="#ffffff")
        self.BackBtn.configure(activeforeground="#000000")
        self.BackBtn.configure(background="white")
        self.BackBtn.configure(borderwidth="0")
        self.BackBtn.configure(disabledforeground="#a3a3a3")
        self.BackBtn.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.BackBtn.configure(foreground="#333333")
        self.BackBtn.configure(highlightbackground="#d9d9d9")
        self.BackBtn.configure(highlightcolor="black")
        self.BackBtn.configure(overrelief="flat")
        self.BackBtn.configure(pady="0")
        self.BackBtn.configure(relief="flat")
        self.BackBtn.configure(text='''Back''')

        self.BtnFrame_1 = tk.Frame(top)
        self.BtnFrame_1.place(x=130, y=0, height=600, width=870)
        self.BtnFrame_1.configure(background="#e8e8e8")
        self.BtnFrame_1.configure(highlightbackground="#d9d9d9")
        self.BtnFrame_1.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.BtnFrame_1)
        self.Entry1.place(x=30, y=30, height=60, width=810)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief="ridge")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.BackBtn_1 = tk.Button(self.BtnFrame_1)
        self.BackBtn_1.place(x=790, y=40, height=42, width=42)
        self.BackBtn_1.configure(activebackground="#ffffff")
        self.BackBtn_1.configure(activeforeground="#000000")
        self.BackBtn_1.configure(background="#333333")
        self.BackBtn_1.configure(borderwidth="0")
        self.BackBtn_1.configure(disabledforeground="#a3a3a3")
        self.BackBtn_1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.BackBtn_1.configure(foreground="#333333")
        self.BackBtn_1.configure(highlightbackground="#d9d9d9")
        self.BackBtn_1.configure(highlightcolor="black")
        self.BackBtn_1.configure(overrelief="flat")
        self.BackBtn_1.configure(pady="0")
        self.BackBtn_1.configure(relief="flat")
        self.BackBtn_1.configure(text='''Back''')

        self.Listbox1 = tk.Listbox(self.BtnFrame_1)
        self.Listbox1.place(x=30, y=110, height=188, width=384)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")

if __name__ == '__main__':
    vp_start_gui()




