class FileBeeeeee:
    def __init__(self, name):
        self.filename = name

    def line_list(self):
        with open(self.filename, 'r') as reader:
            return reader.readlines()

    def write_to_doc(self, lines):
        with open(self.filename, 'w') as writer:
            writer.writelines(lines)

    def format_date(self, date):
        return 'dddd' + date

    def print_day(self, date):
        lines = self.line_list()
        date_formatted = self.format_date(date)
        day_start = -1
        for index, line in enumerate(lines):
            if date_formatted in line.strip():
                day_start = index
                break
        if day_start == -1:
            print('Date not found')
        else:
            print(date)
            counter = 1
            for line in lines[day_start + 1:]:
                if 'dddd' in line:
                    break
                print(f'{counter}. {line.strip().replace("[===done===]", "[done]")}')
                counter += 1

    def return_date_index(self, date):
        lines = self.line_list()
        date_formatted = self.format_date(date)
        for index, line in enumerate(lines):
            if date_formatted in line.strip():
                return index
        return -1

    def finish_task(self, index, date):
        lines = self.line_list()
        date_index = self.return_date_index(date)
        if date_index == -1:
            print('Date does not exist')
            return
        task_index = date_index + index
        if '[===done===]' not in lines[task_index]:
            lines[task_index] = lines[task_index].strip() + '[===done===]\n'
        self.write_to_doc(lines)
