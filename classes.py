import tkinter as tk
import csv
###########################################################
""" image processing """
images_dict = {"backButton_image": ["./images/back.png", None],
              "searchButton_image": ["./images/search.png", None],
              "paper_ico": ["./images/waste/paper_ico.png", None],
              "iron_ico": ["images/waste/iron_ico.png", None],
              "pet_ico": ["images/waste/pet_ico.png", None]}

def get_image(name):
    if name in images_dict:
        if images_dict[name][1] is None:
            images_dict[name][1] = tk.PhotoImage(file=images_dict[name][0])
        return images_dict[name][1]
    return None
###########################################################


class Layout:
    """
    this class describes the initialisation of our app - some frames and buttons
    """

    def __init__(self, root):
        # create the main window
        root.title("peco")
        root.configure(background="#ffffff")

        # two frames
        #
        self.ButtonFrame = tk.Frame(root)
        self.ButtonFrame.grid(column=0, row=0, sticky="N" + "S" + "W")
        self.ButtonFrame.configure(background="#388E3C")

        self.MainFrame = tk.Frame(root, background='grey80')
        self.MainFrame.grid(column=1, row=0, sticky="N" + "S" + "E")

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        # buttons at 1 frame
        self.BackBtn = tk.Button(self.ButtonFrame)
        self.BackBtn.grid(column=0, row=0, padx=20, pady=15, sticky="N")
        self.BackBtn.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=get_image("backButton_image"),
                               width=72, height=72,
                               command=self.go_back)

        self.cur_search = tk.StringVar()
        self.SearchBox = tk.Entry(self.MainFrame,
                                  textvariable=self.cur_search,
                                  width=35,
                                  font=("Segoe UI", 20, "bold"),
                                  background="white",
                                  relief="flat",
                                  borderwidth="0")
        self.SearchBox.grid(column=0, row=0, ipady=8, pady=0, padx=30, sticky="S")

        self.SearchBtn = tk.Button(self.MainFrame,
                                   image=get_image("searchButton_image"),
                                   background="#ffffff",
                                   borderwidth="0",
                                   activebackground="white",
                                   relief="flat",
                                   cursor="hand2")
        self.SearchBtn.grid(column=0, row=0, pady=0, padx=30, sticky="E" + "S")

        self.CurSearchFrame = tk.Frame(self.MainFrame, background='grey60')
        self.CurSearchFrame.grid(column=0, row=1, sticky='W' + 'N' + 'E', pady=10, padx=30)
        self.CurSearchFrame.grid_remove()

        self.MainFrame.rowconfigure(0, minsize=80)
        self.MainFrame.rowconfigure(1, minsize=380)



    # back button handler - clears the SearchBox
    def go_back(self):
        self.cur_search.set('')




class CurSearchButton(tk.Button):
    """
    this class helps to add buttons with waste instances, which you can click and go to
    the new right frame
    """
    def __init__(self, frame, col_num=0, row_num=0):
        tk.Button.__init__(self, frame,
                           relief="flat",
                           background="grey60",
                           activebackground="grey60",
                           borderwidth=0)
        self.grid(column=col_num, row=row_num)

