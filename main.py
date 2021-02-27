from classes import *


def change_search_results(*args):
    """
    This function changes search results
    It adds up to 3 big buttons and up to 6 small buttons with right images 
    If you click them, frame with actual search information will appear
    :param args: Вообще-то мы не используем никакие из переданных аргументов, но обработчик изменения строки поиска 
    что-то передаёт при вызове этой функции, и мы должны это поддерживать
    :return: None
    """
    counter = 0  # how many buttons are already on the screen
    counter_small = [0, 0, 0]  # very complex counter for small buttons
    request = main_frame.cur_search.get().strip().casefold()  # we read string from search line
    buf = []  # what items have already been used

    if len(request) < 2:  # show nothing if request is too short
        main_frame.CurSearchFrame.grid_remove()  # so we hide frames with button
        main_frame.SmallSearchFrame.grid_remove()
    else:
        for row in search_dict:  # go through the dictionary
            if request in row["name"] and row["id"] not in buf:  # this row matches with search request and hasn't been used yet
                buf.append(row["id"])
                if row["small"] != "small":  # show big button
                    main_frame.CurSearchFrame.grid()  # show frame with big buttons
                    # set right image into the button
                    SuggestButtons[counter % 3].configure(image=icons_dict.get(row["id"]),
                                                                          width=160, height=160)
                    # set waste_id attribute of button equal to id from dictionary
                    SuggestButtons[counter % 3].waste_id = row["id"]
                    # bind func with button
                    SuggestButtons[counter % 3].configure(command=lambda q=row["id"]: go_waste(q))
                    SuggestButtons[counter % 3].grid()  # show button
                    counter += 1
                else:
                    main_frame.SmallSearchFrame.grid()  # show frame with small buttons
                    # set image
                    SmallButtons[counter_small[0]][counter_small[1]].configure(image=icons_dict.get(row["id"]),
                                                                               width=160, height=60)
                    SmallButtons[counter_small[0]][counter_small[1]].waste_id = row["id"]  # set id number and bind with function
                    SmallButtons[counter_small[0]][counter_small[1]].configure(command=lambda q=row["id"]: go_waste(q))
                    SmallButtons[counter_small[0]][counter_small[1]].grid()  # show on the screen
                    counter_small[1] += 1  # counter! as we show small buttons in two rows and three columns,
                    counter_small[2] += 1  # counter_small[0] is the number of column, and counter_small[1] is the number of row
                    if counter_small[1] == 3:
                        counter_small[1] = 0
                        counter_small[0] += 1
                    if counter_small[0] == 2:
                        counter_small[0] = 0
        if counter == 0:  # no big buttons so we hide frame with them
            main_frame.CurSearchFrame.grid_remove()
        for p in range(counter, 3):  # if less then 3 big buttons remove unused buttons
            SuggestButtons[p].grid_remove()
        if counter_small[2] < 6:  # if less then 6 small buttons remove unused ones as well
            for i in range(counter_small[1], 3):  # in the current row
                SmallButtons[counter_small[0]][i].grid_remove()
            for i in range(counter_small[0]+1, 2):  # and in all rows below
                for j in range(3):
                    SmallButtons[i][j].grid_remove()


def go_waste(waste_id_local):
    """
    This function raises up the frame with search response
    :param waste_id_local: id of waste, comes from the pressed button
    :return:
    """
    waste_frame.show(waste_id_local, main_frame)

# top is root element in the main_frame
top = tk.Tk()
waste_frame = WasteFrame(top)
main_frame = MainFrame(top)  # main_frame is our main_frame - class MainFrame instance
search_dict = create_search_dict()  # creates dict with all supported search requests

SuggestButtons, SmallButtons = create_buttons(main_frame)  # two lists with buttons
if __name__ == '__main__':
    

    # cur_search это StringVar
    main_frame.cur_search.trace_add('write', change_search_results)  # обработчик на изменение строки
    top.mainloop()
