import c_body
from tkinter import *

calendar = []
status = []
checkbuttons = []
textlist = []


def config():
    global listback, okno_glowne, button_display_list, button_add_task, button_delete_task, button_delete_all_done, button_exit_app
    okno_glowne = Tk()
    okno_glowne.title('Lista zadan')
    okno_glowne.geometry("500x500")
    button_display_list = Button(okno_glowne, text='Display Tasks', width=12, command=display)
    button_display_list.grid(column=0, row=4)
    button_add_task = Button(okno_glowne, text='Add Task', width=12, command=add)
    button_add_task.grid(column=0, row=0)
    button_delete_task = Button(okno_glowne, text='Delete Task', width=12)
    button_delete_task.grid(column=0, row=1)
    button_delete_all_done = Button(okno_glowne, text='Delete All Done', width=12)
    button_delete_all_done.grid(column=0, row=2)
    button_exit_app = Button(okno_glowne, text='EXIT', width=12, command=exit_window)
    button_exit_app.grid(column=0, row=3)


def exit_window():
    okno_glowne.destroy()


def add():
    global task, button_add
    insert_root = Tk()
    insert_root.title('Dodaj zadanie:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)

    def add_task():
        global task_obj, calendar
        date = c_body.CalendarObj.nowDate()
        time = c_body.CalendarObj.nowTime()
        task_obj = c_body.CalendarObj(task.get(), date, time)
        calendar.append(task_obj)
        insert_root.destroy()

    button_add = Button(insert_root, text='dodaj zadanie', command=add_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    insert_root.mainloop()


def callback_on_checkbutton_click():
    print("One of the Checkbuttons clicked!")
    for i in range(len(calendar)):
        print('\tOld calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
        calendar[i].stat = status[i].get()
        print('\t\tNew calendar[' + str(i) + '] state: ' + calendar[i].displayObj())


def display():
    for i in range(len(calendar)):
        lp = i + 1
        print("status dla:", lp, calendar[i].stat)
        x = (str(lp) + '. ' + calendar[i].displayObj())
        textlist.append(x)
        status.append(BooleanVar())
        if calendar[i].stat == False:
            print("display() called. For index i: ", i, ' setting checkbutton value to checked (onvalue=0)')
            status[i].set(False)
        elif calendar[i].stat == True:
            print("display() called. For index i: ", i, ' setting checkbutton value to unchecked (offvalue=1)')
            status[i].set(True)
        checkbuttons.append(
            Checkbutton(
                master=okno_glowne,
                text=textlist[i],
                variable=status[i],
                onvalue=True,
                offvalue=False,
                command=callback_on_checkbutton_click
            )
        )

        checkbuttons[i].grid(column=1, row=i, sticky=W)


config()
okno_glowne.mainloop()
"""def delete():
    lp = input('delete task number: ')
    i = int(lp) - 1
    calendar.remove(calendar[i])
    """

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
    
    def callback_on_checkbutton_click():
    print("One of the Checkbuttons clicked!")
    for i in range(len(calendar)):
        print('\tOld calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
        calendar[i].stat = status[i].get() == 1
        print('\t\tNew calendar[' + str(i) + '] state: ' + calendar[i].displayObj())
    """