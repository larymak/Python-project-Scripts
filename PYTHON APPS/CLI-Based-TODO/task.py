import time,os,sys 

usage = "Usage :-\n$ ./task add 2 'hello world'    # Add a new item with priority 2 and text \"hello world\" to the list\n$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n$ ./task del INDEX            # Delete the incomplete item with the given index\n$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n$ ./task help                 # Show usage\n$ ./task report               # Statistics ( list complete/incomplete task )"

def func():
    try:

        # printing help
        if sys.argv[1]=="help":
            print(usage)
            return usage

        # lisiting all the task
        if sys.argv[1]=="ls":
            try:
                f = open("path/to/plans/task.txt",'r')
                data = f.read()
                datalist = data.split("\n")
                datalist = sorted(datalist)
                datalist = datalist[1:]
                # print(datalist)
                for i in range(len(datalist)):
                    print(f"{i+1}. {datalist[i][2:]} [{datalist[i][0:1]}]")

            except:
                print("Error: Missing file")



        # adding the task
        if sys.argv[1]=="add":
            try:
                with open("path/to/plans/task.txt",'a',encoding = 'utf-8') as f:
                    res = f.write(f"{sys.argv[2]} {sys.argv[3]}\n")
            except:
                print("Error: Missing tasks string. Nothing added!")
            else:
                print(f"Added task: \"{sys.argv[3]}\" with priority {sys.argv[2]}")



        # deleting the task
        if sys.argv[1]=="del":
            lineno = int(sys.argv[2])
            try:
                with open("path/to/plans/task.txt","r+") as f:
                    new_f = f.readlines()
                    new_f = sorted(new_f)
                    # print(new_f)
                    del_f = new_f.pop(lineno-1)
                    # print(new_f)

                    f.seek(0)
                    for line in new_f:
                        if  del_f not in line:
                            f.write(line)
                    f.truncate()
            except:
                print(f"Error: item with index {lineno} does not exist. Nothing deleted.")



        # marking done
        if sys.argv[1]=="done":
            lineno = int(sys.argv[2])
            try:
                with open("path/to/plans/task.txt","r+") as f:
                    new_f = f.readlines()
                    new_f = sorted(new_f)
                    # print(new_f)
                    del_f = new_f.pop(lineno-1)
                    # print(new_f)

                    f.seek(0)
                    for line in new_f:
                        if  del_f not in line:
                            f.write(line)
                    with open("path/to/plans/completed.txt","a") as r:
                        r.write(del_f)
                    f.truncate()
                


            except:
                print(f"Error: no incomplete item with index #0 exists.")
            else:
                print(f"Marked item as done.")


        # generating the report
        if sys.argv[1]=="report":
            try:
                task = open("path/to/plans/task.txt",'r')
                data = task.read()
                datalist = data.split("\n")
                datalist = sorted(datalist)
                datalist = datalist[1:]
                print(f"Pending : {len(datalist)}")
                for i in range(len(datalist)):
                    print(f"{i+1}. {datalist[i][2:]} [{datalist[i][0:1]}]")
                
                compt = open("path/to/plans/completed.txt",'r')
                data = compt.read()
                datalist = data.split("\n")
                datalist = sorted(datalist)
                datalist = datalist[1:]
                print(f"Completed : {len(datalist)}")
                for i in range(len(datalist)):
                    print(f"{i+1}. {datalist[i][2:]} [{datalist[i][0:1]}]")
            except:
                print("Error: Missing file")

    except:
        print(usage)
        return usage.encode('utf8')

func()