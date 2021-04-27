import datetime

class CalendarObj:
    def __init__(self, task, date, time, stat = True):
        self.task = task
        self.stat = stat
        self.date = date
        self.time = time
        self.stat = stat
    def displayObj(self):
        return self.task + ' ' +  self.date  + ' ' + self.time
    def nowDate():
        date = datetime.datetime.today().strftime("%d %B")
        return date
    def nowTime():
        time = datetime.datetime.today().strftime("%H:%M")
        return time

