import tkinter as tk
import csv

class Window:
    def __init__(self, root):
        # root.geometry('1000x600')
        root.title("peco")
        root.configure(background="#ffffff")

        # declaring images for buttons
        global backImage, searchImage
        backImage = tk.PhotoImage(file="./images/back.png")
        searchImage = tk.PhotoImage(file="./images/search.png")

        self.paper_ico = tk.PhotoImage(file="./images/waste/paper_ico.png")
        self.iron_ico = tk.PhotoImage(file="images/waste/iron_ico.png")
        self.pet_ico = tk.PhotoImage(file="images/waste/pet_ico.png")
        self.WasteIcons = {1: self.paper_ico,
                           2: self.iron_ico,
                           3: self.pet_ico}
        # two frames
        self.BtnFrame = tk.Frame(root)
        self.BtnFrame.grid(column=0, row=0, sticky="N" + "S" + "W")
        self.BtnFrame.configure(background="#388E3C")
        # self.BtnFrame.configure(highlightbackground="#d9d9d9")
        # self.BtnFrame.configure(highlightcolor="black")

        self.MainFrame = tk.Frame(root, background='grey80')
        self.MainFrame.grid(column=1, row=0, sticky="N" + "S" + "E")
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        # buttons at 1 frame
        self.BackBtn = tk.Button(self.BtnFrame)
        self.BackBtn.grid(column=0, row=0, padx=20, pady=15, sticky="N")
        self.BackBtn.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=backImage, width=72, height=72,
                               command=lambda: self.go_back)

        self.cur_search = tk.StringVar()
        self.SearchBox = tk.Entry(self.MainFrame,
                                  textvariable=self.cur_search,
                                  width=35,
                                  font="Helvetica 20")
        self.SearchBox.grid(column=0, row=0, ipady=8, pady=0, padx=30, sticky="S")
        self.SearchBox.configure(background="white",
                                 relief="flat",
                                 borderwidth="0")

        self.SearchBtn = tk.Button(self.MainFrame,
                                   image=searchImage)
        self.SearchBtn.grid(column=0, row=0, pady=0, padx=30, sticky="E" + "S")
        self.SearchBtn.configure(background="#ffffff",
                                 borderwidth="0",
                                 activebackground="white",
                                 relief="flat",
                                 cursor="hand2")

        self.CurSearchFrame = tk.Frame(self.MainFrame, background='grey60')
        self.CurSearchFrame.grid(column=0, row=1, sticky='W' + 'N' + 'E', pady=10, padx=30)
        self.CurSearchFrame.grid_remove()

        # self.SuggestBtn1 = tk.Button(self.CurSearchFrame, relief="flat", background="grey60", activebackground="grey60", borderwidth=0)
        # self.SuggestBtn1.grid(column=0, row=0)
        #
        # self.SuggestBtn2 = tk.Button(self.CurSearchFrame, relief="flat", background="grey60", activebackground="grey60", borderwidth=0)
        # self.SuggestBtn2.grid(column=1, row=0)
        #
        # self.SuggestBtn3 = tk.Button(self.CurSearchFrame, relief="flat", background="grey60", activebackground="grey60", borderwidth=0)
        # self.SuggestBtn3.grid(column=3, row=0)

        # self.cur_SearchLabel = tk.StringVar()
        # # self.SearchLabel = tk.Label(self.MainFrame, height=20, textvariable=self.cur_SearchLabel)
        # # self.SearchLabel.grid(column=0, row=1, sticky='W' + 'N' + 'E', pady=10, padx=30)

        self.MainFrame.rowconfigure(0, minsize=80)
        self.MainFrame.rowconfigure(1, minsize=380)

        # self.SuggestButtons = [self.SuggestBtn1, self.SuggestBtn2, self.SuggestBtn3]


# class mybutton():
#     def __init__(self, frame, k):
#         self.button = tk.Button(frame,
#                                 relief="flat",
#                                 background="grey60",
#                                 activebackground="grey60",
#                                 borderwidth=0,
#                                 text="ssssss",
#                                 command=lambda: self.pressed())
#         self.id = i
#         self.button.grid(row=k+1, column=0)
#         print(self.id)
#
#     def pressed(self):
#         print(self.id)



class CurSearchButton(tk.Button):
    def __init__(self, frame, col_num=0, row_num=0):
        tk.Button.__init__(self, frame,
                           relief="flat",
                           background="grey60",
                           activebackground="grey60",
                           borderwidth=0)
        self.grid(column=col_num, row=row_num)

