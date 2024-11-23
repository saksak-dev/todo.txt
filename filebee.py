from datetime import datetime
class FileBeeeeee:
    def __init__(self, name):
        self.filename = name

    def line_list(self):
        with open(self.filename, 'r') as reader:
            return reader.readlines()

    def write_to_doc(self, lines):
        with open(self.filename, 'w') as writer:
            writer.writelines(lines)



