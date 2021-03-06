import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        return self.lastName

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastname < other.lastName

    def __str__(self):
        return self.name
