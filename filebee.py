from fileinput import filename


class FileBeeeeee:
    def __init__(self, name):
        self.filename = name

    def line_list(self):
        with open(self.filename, 'r') as reader:
            lines = reader.readlines()
        return lines

    def write_to_doc(self, lines):
        with open(self.filename, 'w') as writer:
            for line in lines:
                writer.write(line + '\n')


    def date_dis(self,date):
        return 'dddd' + date

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


    def return_date_index(self, date):
        lines = self.line_list()
        date_formated = self.date_dis(date)
        day_start = -1
        for index, line in enumerate(lines):
            if date_formated in line:
                day_start = index
        return day_start


    def finish_task(self, index, date):
        lines=self.line_list()
        if self.return_date_index(date) == -1:
            print('Date does not exist')
            return
        lines[self.return_date_index(date)+index]+='[===done===]'
        self.write_to_doc(lines)
