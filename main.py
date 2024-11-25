import argparse
import filebee
import os
import json

CONFIG_DIR = os.path.expanduser("~/.config/todotxt")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DEFAULT_FILE_NAME = "todo.txt"


def get_file_location():

    # Ensure the config directory exists
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    # Check if the config file exists
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        saved_dir = config.get("file_directory")
        if saved_dir:
            return os.path.join(saved_dir, DEFAULT_FILE_NAME)

    # Prompt user for directory if not found
    directory = input("Enter directory to store tasks file (e.g., /home/user/documents): ").strip()
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"file_directory": directory}, f)
    return os.path.join(directory, DEFAULT_FILE_NAME)


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Process some arguments.")
    #TODO find better way to handle file location and name
    file_handler = filebee.FileBeeeeee(get_file_location())

    parser.add_argument('-ls', '--list', action='store_true', help="List all tasks")
    parser.add_argument('-a', '--add', type=str, help="Add new task")
    parser.add_argument('-i','--index', type=int, help="Index of task")
    parser.add_argument('-d', '--done', type=int, help='Finish task')
    parser.add_argument('-c', '--clear', action='store_true',help='Clear finished tasks from list')


    args = parser.parse_args()

    if args.list:
        file_handler.list_tasks()
    if args.add:
        if args.index:
            file_handler.add_task(args.add, args.index-1)
        else:
            file_handler.add_task(args.add)
    if args.done:
        file_handler.finish_task(args.done-1)
    if args.clear:
        file_handler.clear_done()


if __name__ == "__main__":
    main()
