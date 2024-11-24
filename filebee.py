from datetime import datetime
class FileBeeeeee:
    def __init__(self, name):
        self.filename = name

    def line_list(self):
        with open(self.filename, 'r') as reader:
            return reader.readlines()

    def split_done(self):
        """ Splits lines based on presence of '[done]'
            Returns tuple of done and in_progress lists"""
        lines = self.line_list()
        in_progress = []
        done = []

        for line in lines:
            if '[done]' in line:
                done.append(line)
            else:
                in_progress.append(line)

        return in_progress, done

    def write_to_doc(self, lines):
        with open(self.filename, 'w') as writer:
            writer.writelines(lines)


    def add_task(self, task, index=None):
        in_progress, done = self.split_done()

        if index is None or index > len(in_progress) or index <= 0:
            in_progress.append(task)
        else:
            in_progress.insert(index-1, task)

        lines = in_progress + done

        self.write_to_doc(lines)




