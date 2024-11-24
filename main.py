import argparse
import filebee

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Process some arguments.")
    file_handler = filebee.FileBeeeeee('testiranje.txt')

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
