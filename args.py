import argparse

parser = argparse.ArgumentParser()
parser.add_argument("tasks", help="perform specified task and all it's dependancies",
                     metavar="task", nargs = '*')
parser.add_argument('-l', '--list-tasks', help = "List the tasks",
                     action =  'store_true')
parser.add_argument('-f', '--file',
                     help = "Build file to read the tasks from. 'build.py' is default value assumed if this argument is unspecified",
                     metavar = "file", default =  "build.py")
parser.parse_args("[--file]") # this line should throw SystemExit
