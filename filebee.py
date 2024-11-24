from datetime import datetime
from os import linesep


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
            self.list_tasks()

    def add_task(self, task: str, index=None):
        """ Adds task to specified index, if no index specified it adds it to the end of uncompleted tasks """
        in_progress, done = self.split_done()
        task = task + '\n'
        if  index is None or index >= len(in_progress) or index < 0:
            in_progress.append(task)
        else:
            in_progress.insert(index, task)

        lines = in_progress + done

        self.write_to_doc(lines)

    def finish_task(self, index):
        """Moves task from in_progress to done before merging and adds done to the task"""

        in_progress, done = self.split_done()

        if index >= len(in_progress) or index < 0:
            print("Task does not exist")
            self.list_tasks()
        else:
            finished_task = in_progress.pop(index).strip()+' [done]\n'
            done.append(finished_task)
            lines = in_progress + done
            self.write_to_doc(lines)

    def clear_done(self):
        '''Clears all finished task from the document leaving only'''

        in_progress, done = self.split_done()
        self.write_to_doc(in_progress)
        print("Completed tasks have been cleared.")


    def list_tasks(self):
        in_progress, done = self.split_done()

        for index, task in enumerate(in_progress):
            print(f'{index + 1}. {task.strip()}')
        for task in done:
            print(task.strip())



