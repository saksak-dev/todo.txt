from fileinput import filename


class FileBeeeeee:
    def __init__(self, name):
        self.filename = name

    def line_list(self):
        with open(self.filename, 'r') as reader:
            lines = reader.readlines()
        return lines

    def date_dis(self,date):
        newdate = date.replace('.','')
        newdate = newdate.replace('.','')
        return newdate

    def print_day(self, date):
        lines = self.line_list()



