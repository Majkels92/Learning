from tkinter import *
import c_body

calendar = []

def config():
    global okno_glowne

    okno_glowne = Tk()
    okno_glowne.title('Lista zadan')
    okno_glowne.geometry("400x400")
    button_display_list = Button(okno_glowne, text = 'Display Tasks', width = 12, command = display)
    button_display_list.grid(column=0, row=4)
    button_add_task= Button(okno_glowne, text = 'Add Task', width = 12, command = add)
    button_add_task.grid(column=0, row=0)
    button_delete_task= Button(okno_glowne, text = 'Delete Task', width = 12)
    button_delete_task.grid(column=0, row=1)
    button_delete_all_done = Button(okno_glowne, text = 'Delete All Done', width = 12)
    button_delete_all_done.grid(column=0, row=2)
    button_exit_app = Button(okno_glowne, text = 'EXIT', width = 12, command = exit_window)
    button_exit_app.grid(column=0, row=3)

def config_insert_box():
    insert_root = Tk()
    insert_root.title('Dodaj zadanie:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)
    button_add = Button(insert_root, text='dodaj zadanie', command=add)
    button_add.grid(column = 0, row = 1, sticky=E, padx=20, pady=20)

def add():
    insert_root = Tk()
    insert_root.title('Dodaj zadanie:')
    task = Entry(insert_root, width=80)
    task.grid(column=0, row=0, padx=20, pady=20)
    def add_task():
        date = c_body.CalendarObj.nowDate()
        time = c_body.CalendarObj.nowTime()
        task_obj = c_body.CalendarObj(task.get(), date, time)
        calendar.append(task_obj)
        insert_root.destroy()
    button_add = Button(insert_root, text='dodaj zadanie', command=add_task)
    button_add.grid(column=0, row=1, sticky=E, padx=20, pady=20)
    insert_root.mainloop()

def display():
    global check_task
    for i in range(len(calendar)):
        lp = i +1
        status = IntVar()
        status.set(1)
        check_task = Checkbutton(okno_glowne, text=str(lp) + '.' + calendar[i].displayObj(), variable=status)
        check_task.grid(column=1, row=0+i, sticky=W)

def exit_window():
    okno_glowne.destroy()
if __name__ == '__main__':
    config()
    okno_glowne.mainloop()


"""def delete():
    lp = input('delete task number: ')
    i = int(lp) - 1
    calendar.remove(calendar[i])
def del_all_done():
    global calendar
    bufor_list = []
    for i in calendar:
        if i.stat is False:
            bufor_list.append(i)
    calendar = bufor_list
    return calendar"""
