__author__ = 'jack-a-lynn'
import argparse
import subprocess
import os.path


parser = argparse.ArgumentParser(description="Collect warnings and errors from logs")

parser.add_argument('cmd',
                    type=str,
                    choices=['W', 'E', 'WE'],
                    help="W - collect warnings only"
                    "E - collect errors only"
                    "WE - collect warnings and errors")

parser.add_argument('path',
                    type=str,
                    help="Path to the selected file or folder")

parser.add_argument('f', type=str,
                    nargs='?',
                    help="result file")


argts = parser.parse_args()
cmd = argts.cmd
path = argts.path


name = path.split('/')[-1]
grp = 'grep -iE '
grpf = 'grep -iEr '
warn = '"warn" '
err = '"err" '
warn_err = '"warn\|err" '
wrt = ' > warn.log'

if argts.f is None:

    if not os.path.exists(path):
        print("file or folder doesn't exist")

    else:
        if os.path.isfile(path):
            if cmd == 'W':
                comm = grp + warn + name
                print(subprocess.call(comm, shell=True))
            elif cmd == 'E':
                comm = grp + err + name
                print(subprocess.call(comm, shell=True))
            elif cmd == 'WE':
                comm = grp + warn_err + name
                print(subprocess.call(comm, shell=True))

        elif os.path.isdir(path):
            if cmd == 'W':
                comm = grpf + warn + name
                print(subprocess.call(comm, shell=True))
            elif cmd == 'E':
                comm = grpf + err + name
                print(subprocess.call(comm, shell=True))
            elif cmd == 'WE':
                comm = grpf + warn_err + name
                print(subprocess.call(comm, shell=True))

else:
    if not os.path.exists(path):
        print("file or folder doesn't exist")

    else:
        if os.path.isfile(path):
            if cmd == 'W':
                comm = grp + warn + name + wrt
                subprocess.call(comm, shell=True)
            elif cmd == 'E':
                comm = grp + err + name + wrt
                subprocess.call(comm, shell=True)
            elif cmd == 'WE':
                comm = grp + warn_err + name + wrt
                subprocess.call(comm, shell=True)

        elif os.path.isdir(path):
            if cmd == 'W':
                comm = grpf + warn + name + wrt
                subprocess.call(comm, shell=True)
            elif cmd == 'E':
                comm = grpf + err + name + wrt
                subprocess.call(comm, shell=True)
            elif cmd == 'WE':
                comm = grpf + warn_err + name + wrt
                subprocess.call(comm, shell=True)


