import tkinter as tk

class AdvBtn(tk.Button):
    def __init__(self):
        tk.Button.__init__(self)
        self.grid()
        print(self.atr)
    atr = 0








top = tk.Tk()

b = AdvBtn()

print(b.atr)

top.mainloop()