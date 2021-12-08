import calendar_task
from tkinter import *

calendar = []
statuses = []
check_buttons = []
texts = []


def config():
    global main_root, check_frame
    main_root = Tk()
    main_root.title('Tasks to do')
    main_root.geometry("600x600")
    button_frame = Frame(main_root)
    button_frame.grid(column=0, row=1)
    button_add_task = Button(button_frame, text='Add Task', width=12, command=add)
    button_add_task.grid(column=0, row=0)
    button_delete_task = Button(button_frame, text='Delete Task', width=12, command=delete)
    button_delete_task.grid(column=0, row=1)
    button_delete_all_done = Button(button_frame, text='Delete All Done', width=12, command=del_all_done)
    button_delete_all_done.grid(column=0, row=2)
    button_exit_app = Button(button_frame, text='Exit', width=12, command=exit_window)
    button_exit_app.grid(column=0, row=3)
    check_frame = Frame(main_root)
    check_frame.grid(column=1, row=1)


def add():
    insert_root = Toplevel()
    insert_root.title('Add task:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)

    def add_task():
        global task_obj, calendar
        date = calendar_task.CalendarTask.nowDate()
        time = calendar_task.CalendarTask.nowTime()
        task_obj = calendar_task.CalendarTask(task.get(), date, time)
        calendar.append(task_obj)
        texts.append(StringVar())
        statuses.append(BooleanVar())
        display()
        insert_root.destroy()

    button_add = Button(insert_root, text='add task', command=add_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    insert_root.mainloop()


def delete():
    if len(calendar) > 0:
        delete_root = Toplevel()
        delete_root.title('Delete task:')
        del_task_entry = Entry(delete_root, width=80)
        del_task_entry.grid(column=0, row=0, padx=20, pady=20)

        def delete_task():
            i = int(del_task_entry.get()) - int(1)
            statuses.remove(statuses[i])
            texts.remove(texts[i])
            calendar.remove(calendar[i])
            display()
            delete_root.destroy()

        button_add = Button(delete_root, text='delete task', command=delete_task)
        button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
        delete_root.mainloop()
    elif len(calendar) == 0:
        delete_info_root = Toplevel()
        delete_info_root.geometry("300x100")
        delete_info_root.title('Error information:')
        text_info = Label(delete_info_root, text="YOU SHALL NOT PASS,\n YOU CAN'T DELETE ANYTHING FROM EMPTY LIST!!")
        text_info.pack()

        def exit_root():
            delete_info_root.destroy()

        button_ok = Button(delete_info_root, text='OK, SORRY', command=exit_root)
        button_ok.pack()
        delete_info_root.mainloop()


def del_all_done():
    def check_if_true():
        for n in range(len(calendar)):
            if calendar[n].stat:
                return True

    if check_if_true():
        global calendar, statuses, texts
        buffer_calendar = []
        buffer_statuses = []
        buffer_texts = []
        for i in range(len(calendar)):
            if not calendar[i].stat:
                buffer_calendar.append(calendar[i])
                buffer_statuses.append(statuses[i])
                buffer_texts.append(texts[i])
        calendar = buffer_calendar
        statuses = buffer_statuses
        texts = buffer_texts
        display()

    else:
        delete_info_root = Toplevel()
        delete_info_root.geometry("400x100")
        delete_info_root.title('Error information:')
        text_info = Label(delete_info_root,
                          text="YOU SHALL NOT PASS,\n YOU CAN'T DELETE ANYTHING WHEN YOU HAVE WORK TO DO!!!!!!")
        text_info.pack()

        def exit_root():
            delete_info_root.destroy()

        button_ok = Button(delete_info_root, text='OK, SORRY', command=exit_root)
        button_ok.pack()
        delete_info_root.mainloop()


def display():
    global calendar, texts, statuses, check_buttons, check_frame

    def on_checkbutton_click():
        for j in range(len(calendar)):
            calendar[j].stat = statuses[j].get()

    check_buttons.clear()
    check_frame.destroy()
    check_frame = Frame(main_root)
    check_frame.grid(column=1, row=1)
    for i in range(len(calendar)):
        lp = i + 1
        x = (str(lp) + '. ' + calendar[i].displayObj())
        texts[i].set(x)
        statuses[i].set(calendar[i].stat)
        check_buttons.append(
            Checkbutton(
                master=check_frame,
                textvariable=texts[i],
                variable=statuses[i],
                onvalue=True,
                offvalue=False,
                command=on_checkbutton_click
            )
        )
        check_buttons[i].grid(column=1, row=i, sticky=W)


def exit_window():
    main_root.destroy()


if __name__ == '__main__':
    config()
    main_root.mainloop()
