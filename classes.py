import tkinter as tk
import csv
###########################################################
""" image processing """
images_dict = {"backButton_image": ["./images/back.png", None],
              "searchButton_image": ["./images/search.png", None],
              "paper_ico": ["./images/waste/paper_ico.png", None],
              "iron_ico": ["images/waste/iron_ico.png", None],
              "pet_ico": ["images/waste/pet_ico.png", None],
              "closeButton_image": ["images/close.png", None]}

def get_image(name):
    """
    this function returns tk.PhotoImage object that was requested with id number or name (as in csv)
    :param name: equals to name or id in csv
    :return: tk.PhotoImage object
    """
    if str(name).isdigit():  # here we check if we got a number
        # print("isdigit")
        with open("test.csv", encoding="utf-8") as f:
            first_search_dict = list(csv.DictReader(f))
            for i in first_search_dict:
                # print(i["id"], name)
                if i["id"] == name:
                    name = i["path"]
                    # print(name)
    if name in images_dict:  # now name is actually the name string and we can see it in csv name field
        # print("yes name is in image_dict")
        if images_dict[name][1] is None:
            # print(("yes images_dict is none"))
            images_dict[name][1] = tk.PhotoImage(file=images_dict[name][0])
        return images_dict[name][1]  # return a tk.PhotoImage object
    # print("return none")
    return None
###########################################################


def get_text(id):
    with open("test_text.csv", encoding="utf-8") as f_text:
        text_dict = csv.reader(f_text)
        for line in text_dict:
            if line[0] == id:
                return line[1]
        return "Not found"



class Layout:
    """
    this class describes the initialisation of our app - some frames and buttons
    """

    def __init__(self, root):
        # create the main window
        root.title("peco")
        root.configure(background="#ffffff")

        # two frames
        self.ButtonFrame = tk.Frame(root)
        self.ButtonFrame.grid(column=0, row=0, sticky="N" + "S" + "W")
        self.ButtonFrame.configure(background="#388E3C")

        self.MainFrame = tk.Frame(root, background='grey80')
        self.MainFrame.grid(column=1, row=0, sticky="N" + "S" + "E")

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)

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

    :parameter waste_id: an id number set to the button in change_search_results function
    """
    def __init__(self, frame, col_num=0, row_num=0):
        """
        initialisation occurs in SuggestButtons generation
        :param frame: parental widget
        :param col_num: column number
        :param row_num: row number
        """
        tk.Button.__init__(self, frame,
                           relief="flat",
                           background="grey60",
                           activebackground="grey60",
                           borderwidth=0)
        self.grid(column=col_num, row=row_num,
                  pady=10, padx=10)
    # this number changes as user types
    waste_id = 0


class WasteFrame(tk.Frame):
    """
    This class will create a frame with information
    """
    def __init__(self, root):
        """
        initialisation
        we create a frame, a label with text, an image
        :param root: parental widget is top
        """
        tk.Frame.__init__(self, root)
        self.text = tk.Text(self, wrap="word", height=8, width=40, font=("Segoe UI", 14))
        self.text.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        self.image_canvas = tk.Canvas(self, bg="grey", width=160, height=160)
        self.image_canvas.grid(column=0, row=0, padx=20, pady=20, sticky="nw")
        self.label = tk.Label(self, text="labellllllllll")
        self.label.grid(column=1, row=0, padx=10, pady=10)
        self.rowconfigure(0, minsize=100)
    def show(self, id, app):
        """

        :param id: this comes from go_waste_function and there it had come from change_search_results function
        :return: no
        """
        # we show the frame (self)
        self.grid(column=1, row=0, sticky="N" + "S" + "E")
        # this stores a tk.PhotoImage object with current image
        self.img = get_image(id)
        # we show image
        self.image_canvas.create_image(0, 0, anchor="nw", image=self.img)
        # we show text
        self.text.insert(1.0, "get_text(id)")
        self.text.configure(state = "disabled")
        # we hide MainFrame
        app.MainFrame.grid_remove()
        # we change the button back to button close
        app.BackBtn.grid_remove()
        # button Close
        self.CloseBtn = tk.Button(app.ButtonFrame)
        self.CloseBtn.grid(column=0, row=0, padx=20, pady=15, sticky="N")
        self.CloseBtn.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=get_image("closeButton_image"),
                               width=72, height=72,
                               command=lambda: self.close(app))

    def close(self, app):
        self.grid_remove()
        app.MainFrame.grid()
        self.CloseBtn.grid_remove()
        app.BackBtn.grid()
