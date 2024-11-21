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
        return 'dddd' + newdate

    def print_day(self, date):
        lines = self.line_list()
        date_formated = self.date_dis(date)
        day_start = -1
        for index, line in enumerate(lines):
            if date_formated in line:
                day_start = index
        if day_start == -1:
            print('Date not found')
        else:
            print(date)
            counter = 1
            for line in lines[day_start+1:]:
                if 'dddd' in line:
                    break
                else:
                    print(f'{counter}. {line.replace('[===done===]', '[done]')}')
                    counter+=1







