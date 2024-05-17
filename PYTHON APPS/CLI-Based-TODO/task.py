#!/usr/bin/env python3
# Python todo list

import os
from argparse import ArgumentParser as aparse

# change the path of the files here to the actual desired paths
taskTxt = "task.txt"
completedTxt = "completed.txt"

def create_parser():
    parser = aparse(description="""Command Line task list""")
    parser.add_argument("toDo", default="ls", choices=['usage', 'ls', 'add', 'del', 'done', 'report'], help="Enter command: usage, ls, add, del, done, report.")
    parser.add_argument("-p", required=False, type=int, help="item priority")
    parser.add_argument("-i", required=False, type=str, help="List item to add, remove, or mark done.")
    return parser

def func():
    args = create_parser().parse_args()

    # check if files exist, create if not
    if not os.path.exists(taskTxt):
        with open(taskTxt, "w") as filet:
            pass

    if not os.path.exists(completedTxt):
        with open(completedTxt, "w") as filec:
            pass
    
    if args.toDo == "ls":
        lister(read_list())

    # adding the task
    if args.toDo == "add":
        if args.i == '' or args.p == '':
            raise ValueError('An item and priority must be entered')
        taskList = read_list()
        taskList.insert((args.p - 1), args.i)
        with open(taskTxt, "w") as f:
            for line in taskList:
                f.write(line + "\n")


    # deleting the task
    if args.toDo == "del":
        if args.i == '' or args.p == '':
            raise ValueError('An item or priority must be entered')
        taskList = read_list()
        if args.p:
            index = args.p - 1
            delete_item(index, taskList)
        else:
            try:
                index = taskList.index(args.i)
                delete_item(index, taskList)
                exit(0)
            except(ValueError):
                print(f"Item {args.i} not found. Maybe run ls and try again?")
                exit(0)

    # marking done
    if args.toDo == "done":
        if args.i == '' or args.p == '':
            raise ValueError('An item or priority must be entered')
        taskList = read_list()
        if args.p:
            index = args.p - 1
            do_item(index, taskList)
        else:
            try:
                index = taskList.index(args.i)
                do_item(index, taskList)
                exit(0)
            except(ValueError):
                print(f"Item {args.i} not found. Maybe run ls and try again?")
                exit(0)

    # generating the report
    if args.toDo == "report":
        print("\n")
        print("To do:")
        lister(read_list())
        print("\n")
        print("Done:")
        lister(read_complete())

def read_list():
    with open(taskTxt, "r") as file:
        task_list = file.readlines()
    # all the newlines added during file writing must be removed otherwise printing is messed up
    strip_list = []
    for item in task_list:
        strip_list.append(item.strip())
    filtered_list = [item for item in strip_list if item != ""]
    return filtered_list

def read_complete():
    with open(completedTxt, "r") as file:
        completed_list = file.readlines()
    # all the newlines added during file writing must be removed otherwise printing is messed up
    strip_list = []
    for item in completed_list:
        strip_list.append(item.strip())
    filtered_list = [item for item in strip_list if item != ""]
    return filtered_list

def delete_item(index, taskList):
    print("\n")
    print(f"Do you want to delete {taskList[index]}?")
    answer = input("Enter y or n: ")
    if answer == "y":
        taskList.pop(index)
        with open(taskTxt, "w") as f:
            for line in taskList:
                f.write(line + "\n")
        print("Item Deleted")
        exit(0)
    print("No item deleted")
    exit(0)

def do_item(index, taskList):
    print("\n")
    print(f"Do you want to move {taskList[index]} to done?")
    answer = input("Enter y or n: ")
    if answer == "y":
        task = taskList.pop(index)
        with open(taskTxt, "w") as f:
            for line in taskList:
                f.write(line + "\n")
        completed = read_complete()
        completed.append(task)
        with open(completedTxt, "w") as f:
            for line in completed:
                f.write(line + "\n")
        print("Item marked done")
        exit(0)
    print("No item changed")
    exit(0)

def lister(items):
    for item, line in enumerate(items, 1):
            print(f"{item}: {line.strip()}")

if __name__ == "__main__":
    func()
