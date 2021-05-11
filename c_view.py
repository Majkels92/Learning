import c_body
from tkinter import *

calendar = []
status = []
checkbuttons = []
textlist = []
def config():
    global button_frame, main_root, button_display_list, button_add_task, button_delete_task, button_delete_all_done, button_exit_app, check_frame
    main_root = Tk()
    main_root.title('Lista zadan')
    main_root.geometry("500x500")
    button_frame = Frame(main_root)
    button_frame.grid(column=0, row=1)
    button_add_task = Button(button_frame, text='Add Task', width=12, command=add)
    button_add_task.grid(column=0, row=0)
    button_delete_task = Button(button_frame, text='Delete Task', width=12, command=delete)
    button_delete_task.grid(column=0, row=1)
    button_delete_all_done = Button(button_frame, text='Delete All Done', width=12, command=del_all_done)
    button_delete_all_done.grid(column=0, row=2)
    button_exit_app = Button(button_frame, text='EXIT', width=12, command=exit_window)
    button_exit_app.grid(column=0, row=3)
    check_frame = Frame(main_root)
    check_frame.grid(column=1, row=1)
def add():
    insert_root = Toplevel()
    insert_root.title('Dodaj zadanie:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)
    def add_task():
        global task_obj, calendar
        date = c_body.CalendarObj.nowDate()
        time = c_body.CalendarObj.nowTime()
        task_obj = c_body.CalendarObj(task.get(), date, time)
        calendar.append(task_obj)
        textlist.append(StringVar())
        status.append(BooleanVar())
        display()
        insert_root.destroy()
    button_add = Button(insert_root, text='dodaj zadanie', command=add_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    insert_root.mainloop()
def delete():
    if len(calendar) > 0 :
        delete_root = Toplevel()
        delete_root.title('Delete task:')
        deltask = Entry(delete_root, width=80)
        deltask.grid(column=0, row=0, padx=20, pady=20)
        def del_task():
            i = int(deltask.get()) - int(1)
            status.remove(status[i])
            textlist.remove(textlist[i])
            calendar.remove(calendar[i])
            display()
            delete_root.destroy()
        button_add = Button(delete_root, text='delete task', command=del_task)
        button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
        delete_root.mainloop()
    elif len(calendar) == 0:
        delete_info_root = Toplevel()
        delete_info_root.geometry("300x100")
        delete_info_root.title('Error information:')
        text_info = Label(delete_info_root, text = "YOU SHALL NOT PASS,\n YOU CAN'T DELETE ANYTHING FROM EMPTY LIST!!")
        text_info.pack()
        def exit_root():
            delete_info_root.destroy()
        button_ok = Button(delete_info_root, text='OK, SORRY', command=exit_root)
        button_ok.pack()
        delete_info_root.mainloop()
def del_all_done():
    def check_if_true():
        for i in range(len(calendar)):
            if calendar[i].stat == True:
                return True
    if check_if_true() == True:
        global calendar, status, textlist
        bufor_calendar = []
        bufor_status = []
        bufor_textlist = []
        for i in range(len(calendar)):
            if calendar[i].stat == False:
                bufor_calendar.append(calendar[i])
                bufor_status.append(status[i])
                bufor_textlist.append(textlist[i])
        calendar = bufor_calendar
        status = bufor_status
        textlist = bufor_textlist
        display()

    else:
        delete_info_root = Toplevel()
        delete_info_root.geometry("300x100")
        delete_info_root.title('Error information:')
        text_info = Label(delete_info_root, text="YOU SHALL NOT PASS,\n YOU CAN'T DELETE ANYTHING WHEN YOU HAVE WORK TO DO!!!!!!")
        text_info.pack()

        def exit_root():
            delete_info_root.destroy()

        button_ok = Button(delete_info_root, text='OK, SORRY', command=exit_root)
        button_ok.pack()
        delete_info_root.mainloop()
def display():
    global calendar, textlist, status, checkbuttons, check_frame
    def callback_on_checkbutton_click():
        for i in range(len(calendar)):
            calendar[i].stat = status[i].get()
    checkbuttons.clear()
    check_frame.destroy()
    check_frame = Frame(main_root)
    check_frame.grid(column=1, row=1)
    for i in range(len(calendar)):
        lp = i + 1
        x = (str(lp) + '. ' + calendar[i].displayObj())
        textlist[i].set(x)
        if calendar[i].stat == False:
            status[i].set(False)
        elif calendar[i].stat == True:
            status[i].set(True)
        checkbuttons.append(
            Checkbutton(
                master=check_frame,
                textvariable=textlist[i],
                variable=status[i],
                onvalue=True,
                offvalue=False,
                command=callback_on_checkbutton_click
            )
        )
        checkbuttons[i].grid(column=1, row=i, sticky=W)

def exit_window():
    main_root.destroy()
if __name__ == '__main__':
    config()
    main_root.mainloop()


"""def del_all_done():
    global calendar, status, checkbuttons, textlist
    bufor_calendar = []
    bufor_status = []
    bufor_checkbuttons = []
    bufor_textlist = []
    for i in range(len(calendar)):
        if calendar[i].stat is not False:
            bufor_calendar.append(i)
            bufor_status.append(i)
            bufor_checkbuttons.append(i)
            bufor_textlist.append(i)
        checkbuttons[i].destroy()
    calendar = bufor_calendar
    status = bufor_status
    checkbuttons = bufor_checkbuttons
    textlist = bufor_textlist
    return calendar, status, checkbuttons, textlist
    """
"""def del_all_done():
    global calendar
    bufor_list = []
    for i in calendar:
        if i.stat is False:
            bufor_list.append(i)
        elif i.stat is True:
            del status[-1]
            del textlist[-1]
    calendar = bufor_list

    return calendar"""
"""def change_status():
    calendar.stat = not calendar.stat
def update():
    okno_glowne.after(100, display)
def del_all_done():
    global calendar
    bufor_list = []
    for i in calendar:
        if i.stat is False:
            bufor_list.append(i)
    calendar = bufor_list
    return calendar

    """