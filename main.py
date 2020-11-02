import tkinter as tk
import csv
from classes import *

top = tk.Tk()  # top is root element to create an app
app = Layout(top)  # app is our app - class Layout instance

# переписали всё из файла в список словарей first_search_dict
# we use first_search_dict in change_search_results func to get waste item from its name
with open("test.csv", encoding="utf-8") as f:
    first_search_dict = list(csv.DictReader(f))
    print(first_search_dict)

# we create a list of suggested buttons - they lead us to the information about specific waste item
amount_of_buttons = 3  # how many buttons do we have maximum
SuggestButtons = []
for i in range(amount_of_buttons):
    SuggestButtons.append(CurSearchButton(app.CurSearchFrame, col_num=i))


# определим функцию, которая будет менять список результатов
def change_search_results(*args):
    counter = 0  # how many buttons are already on the screen
    request = app.cur_search.get().strip()  # we read user's request from search line and strip it

    if request == "":
        app.CurSearchFrame.grid_remove()  # we hide frame with results
    else:
        app.CurSearchFrame.grid()  # we show frame with results
        for row in first_search_dict:  # go through the whole dictionary
            if request in row["name"]:
                # set right image into the button
                SuggestButtons[counter % amount_of_buttons].configure(image=get_image(row["path"]),
                                                                      width=160, height=160)
                # set waste_id attribute of button equal to id from dictionary
                SuggestButtons[counter % amount_of_buttons].waste_id = row["id"]
                # print("button id is ", SuggestButtons[counter % amount_of_buttons].waste_id)
                # bind func with right parameters and the button
                SuggestButtons[counter % amount_of_buttons].configure(command=lambda q=row["id"]: go_waste(q))
                # show button
                SuggestButtons[counter % amount_of_buttons].grid()
                # print(row, SuggestButtons[counter % amount_of_buttons])
                #print(SuggestButtons[counter % amount_of_buttons].waste_id)
                counter += 1
    # print(counter)
    # if counter < amount_of_buttons: delete unused buttons
    for i in range(counter, amount_of_buttons):
        SuggestButtons[i].grid_remove()


# bind StringVar cur_search modification and func change_search_results
app.cur_search.trace_add('write', change_search_results)

# we create a WasteFrame instance - to show info and images
waste_frame = WasteFrame(top)


def go_waste(waste_id_local):
    """
    this function raises up the frame with useful information
    :param waste_id_local: this number comes from button waste id
    :return: nothing actually
    """
    # print("waste_id_local", waste_id_local)

    # and show waste frame which has been adjusted according to the waste id number
    # we send id number and the button to close
    waste_frame.show(waste_id_local, app)



# just loop
top.mainloop()
