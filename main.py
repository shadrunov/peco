import tkinter as tk
import csv
from classes import *

top = tk.Tk()
app = Layout(top)

# переписали всё из файла в список словарей first_search_dict
with open("test.csv", encoding="utf-8") as f:
    first_search_dict = list(csv.DictReader(f))
    print(first_search_dict)

# list of suggested buttons
amount_of_buttons = 3
SuggestButtons = []
for i in range(amount_of_buttons):
    SuggestButtons.append(CurSearchButton(app.CurSearchFrame, col_num=i))

# определим функцию, которая будет менять список результатов
def change_search_results(*args):
    counter = 0
    request = app.cur_search.get().strip()

    if request == "":
        app.CurSearchFrame.grid_remove()
    else:
        app.CurSearchFrame.grid()
        for row in first_search_dict:
            if request in row["name"]:
                SuggestButtons[counter % amount_of_buttons].configure(image=get_image(row["path"]),
                                                                      width=160, height=160)
                # SuggestButtons[counter % amount_of_buttons].configure(text=(row["path"]))
                SuggestButtons[counter % amount_of_buttons].grid()
                print(row, SuggestButtons[counter % amount_of_buttons])
                counter += 1
    print(counter)
    # if counter < amount_of_buttons: delete unused buttons
    for i in range(counter, amount_of_buttons):
        SuggestButtons[i].grid_remove()



# link StringVar cur_search modification and func change_search_results
app.cur_search.trace_add('write', change_search_results)

top.mainloop()