import datetime


class CalendarTask:

    def __init__(self, task, date, time, stat=False):
        self.task = task
        self.stat = stat
        self.date = date
        self.time = time

    def displayObj(self):
        return self.task + ' ' + self.date + ' ' + self.time

    @staticmethod
    def nowDate():
        date = datetime.datetime.today().strftime("%d %B")
        return date

    @staticmethod
    def nowTime():
        time = datetime.datetime.today().strftime("%H:%M")
        return time
