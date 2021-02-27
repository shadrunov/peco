import tkinter as tk
import tkinter.messagebox
import csv
from dataclasses import dataclass

FILE_name_id = "csv/name_id.csv"
FILE_id_iconpath = "csv/id_iconpath.csv"
FILE_text = "csv/id_label_text.csv"


@dataclass
class Image:
    """
    This class stores pictures
    Has two attributes: path and tk.PhotoImage instance
    """
    path: str = None
    obj: tk.PhotoImage = None

    def get(self):
        """
        This function creates if needed and returns PhotoImage object
        :return: tk.PhotoImage
        """
        if self.obj is None:
            self.obj = tk.PhotoImage(file=self.path)
        return self.obj


class ImageStorage(dict):
    """
    This class stores instances of Image class
    Derived from dict type.
    Get method is overridden.
    """
    def __init__(self):
        dict.__init__(self)
        self.update({"backButton_image": Image("./images/back.png"),
                     "searchButton_image": Image("./images/search.png"),
                     "closeButton_image": Image("./images/close.png"),
                     "infoButton_image": Image("./images/info.png")})
        with open(FILE_id_iconpath, encoding="utf-8") as f:
            t = list(csv.DictReader(f))
            for row in t:
                self.add(row)
        # {'id': '1', 'path': './images/waste/paper_ico.png'}

    def add(self, row):
        """
        Add new element
        :param row: row in csv file, smth like this: {'id': '1', 'path': './images/waste/paper_ico.png'}
        :return:
        """
        self[row["id"]] = Image(row["path"])

    def get(self, key):
        """
        Returns an PhotoImage object
        :param key: name or id
        :return: tk.PhotoImage object, if found, else None
        """
        if key in self:
            return self[key].get()
        return None


class TextStorage:
    """
    This class provides methods to access the labels and text information
    """
    def get_text(self, rid):
            """
            This function returns search result as text
            :param rid: id of item
            :return: str
            """
            with open(FILE_text, encoding="utf-8") as f_text:
                text_dict = csv.reader(f_text)
                for line in text_dict:
                    if line[0] == rid:
                        return line[2]
                return "Not found"


    def get_label(self, rid):
            """
            This function returns label of waste result
            :param rid: id of item
            :return: str
            """
            with open(FILE_text, encoding="utf-8") as f_text:
                text_dict = csv.reader(f_text)
                for line in text_dict:
                    if line[0] == rid:
                        return line[1]
                return "Not found"

# access text & labels
text_storage = TextStorage()
# store icons
icons_dict = ImageStorage()

class MainFrame:
    """
    This class describes main_frame - main elements of our app
    """
    def __init__(self, root):
        """
        Creates all elements of main_frame
        :param root:
        """
        # create the main window
        root.title("peco")
        root.configure(background="#ffffff")

        # left panel
        self.ButtonFrame = tk.Frame(root)
        self.ButtonFrame.grid(column=0, row=0, sticky="N" + "S" + "W" + "E")
        self.ButtonFrame.configure(background="#388E3C")

        # main panel
        self.MainFrame = tk.Frame(root, background='grey80')
        self.MainFrame.grid(column=1, row=0, sticky="N" + "S" + "E" + "W")

        root.columnconfigure(0, weight=0)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1, minsize=500)

        # buttons in the left panel
        self.BackBtn = tk.Button(self.ButtonFrame)
        self.BackBtn.grid(column=0, row=0, padx=20, pady=15, sticky="N")
        self.BackBtn.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=icons_dict.get("backButton_image"),
                               width=72, height=72,
                               command=self.go_back)

        self.InfoButton = tk.Button(self.ButtonFrame)
        self.InfoButton.grid(column=0, row=1, padx=20, pady=0, sticky="N")
        self.InfoButton.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=icons_dict.get("infoButton_image"),
                               width=72, height=72,
                               command=self.show_info)


        # search field
        self.cur_search = tk.StringVar()
        self.SearchBox = tk.Entry(self.MainFrame,
                                  textvariable=self.cur_search,
                                  width=35,
                                  font=("Segoe UI", 20, "bold"),
                                  background="white",
                                  relief="flat",
                                  borderwidth="0")
        self.SearchBox.grid(column=0, row=0, ipady=8, pady=25, padx=30, sticky="W")

        # big buttons
        self.CurSearchFrame = tk.Frame(self.MainFrame, background='grey80')
        self.CurSearchFrame.grid(column=0, row=1, sticky='W' + 'N' + 'E', pady=0, padx=30)
        self.CurSearchFrame.grid_remove()

        # small buttons
        self.SmallSearchFrame = tk.Frame(self.MainFrame, background='grey80')
        self.SmallSearchFrame.grid(column=0, row=2, sticky='W' + 'N' + 'E', pady=0, padx=30)
        self.SmallSearchFrame.grid_remove()

    # back button handler - clears the SearchBox
    def go_back(self):
        """ Clears search request """
        self.cur_search.set('')

    # info button handler
    def show_info(self):
        """Shows information when info button is pressed"""
        tk.messagebox.showinfo("Информация", """Это приложение поможет вам понять, можно ли отправить на переработку \
тот или иной предмет. Просто напишите его название в поле поиска. \n\nКредиты: \nИнформация о переработке расположена \
на сайте проекта "Собиратор": sobirator.ru/ \nIcons made by Vitaly \
Gorbachev, Pixel perfect, Freepik, Good Ware and many others from www.flaticon.com \
\nApp created by Aleksey Shadrunov in 2020""", parent=self.MainFrame)


class CurSearchButton(tk.Button):
    """
    Extended tk.Button class
    This class helps to add buttons with waste instances, which you can click and go to
    the frame with results
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
                           background="grey80",
                           activebackground="grey80",
                            borderwidth=0)
        self.grid(column=col_num, row=row_num,
                  pady=5, padx=10)
    # this number changes as user types
    waste_id = 0


class WasteFrame(tk.Frame):
    """
    Extended tk.Frame class
    Search result frame
    Contains label and text information
    """
    def __init__(self, root):
        """
        Creates a frame, a label with text, an image
        :param root: parental widget is top
        """
        tk.Frame.__init__(self, root, background='grey80')

        # text information
        self.text = tk.Text(self, wrap="word",
                            height=14, width=58,
                            font=("Segoe UI", 14),
                            bd=0, relief="flat")
        self.text.grid(column=0, row=1,
                       padx=20, pady=10, sticky="NWS")

        # title
        self.label = tk.Label(self, font=("Segoe UI", 24, "bold"),
                              anchor="w", bg="grey80", bd=0)
        self.label.grid(column=0, row=0,
                        padx=20, pady=25,
                        sticky="WN")


    def show(self, id, app):
        """
        Shows frame with search results
        :param id: waste id number
        :return: None
        """
        # we show the frame (self)
        self.grid(column=1, row=0, sticky="N" + "S" + "E" + "W")

        # we show text
        self.text.insert(1.0, text_storage.get_text(id))
        self.text.configure(state="disabled")
        self.label.configure(text=text_storage.get_label(id))

        app.MainFrame.grid_remove()  # hide MainFrame
        app.BackBtn.grid_remove()  # hide Back button
        self.CloseBtn = tk.Button(app.ButtonFrame)  # show Close button
        self.CloseBtn.grid(column=0, row=0, padx=20, pady=15, sticky="N")
        self.CloseBtn.configure(background="#388E3C",
                               borderwidth="0",
                               activebackground="#388E3C",
                               relief="flat",
                               image=icons_dict.get("closeButton_image"),
                               width=72, height=72,
                               command=lambda: self.close(app))


    def close(self, app):
        """
        Closes current search result frame
        :param app:
        :return:
        """
        self.grid_remove()
        app.MainFrame.grid()
        self.CloseBtn.grid_remove()
        app.BackBtn.grid()
        self.text.configure(state="normal")
        self.text.delete('1.0', tk.END)



def create_search_dict():
    """
    Creates dictionary with all possible search requests.
    When user enters anything, we iterate on this dict
    :return search_dict: dict
    """
    # прочитали названия всех мусоров, чтобы осуществлять по ним поиск
    with open(FILE_name_id, encoding="utf-8") as f:
        search_dict = list(csv.DictReader(f))
    return search_dict


def create_buttons(main_frame):
    """
    Creates two lists of big and small buttons
    :param main_frame: main_frame
    :return SuggestButtons, SmallButtons: (list, list)
    """
    # we create a list of suggested buttons
    amount_of_buttons = 3  # BIG buttons
    SuggestButtons = []
    for i in range(amount_of_buttons):
        SuggestButtons.append(CurSearchButton(main_frame.CurSearchFrame, col_num=i))

    amount_of_small_buttons = (2, 3)  # SMALL buttons
    SmallButtons = []
    for i in range(amount_of_small_buttons[0]):
        SmallButtons.append([])
        for k in range(amount_of_small_buttons[1]):
            SmallButtons[i].append(CurSearchButton(main_frame.SmallSearchFrame, col_num=k, row_num=i))
    return SuggestButtons, SmallButtons




