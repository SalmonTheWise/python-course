__author__ = 'jack-a-lynn'
import argparse
import subprocess
import os.path
import shutil

parser = argparse.ArgumentParser(description="Saves current state of file or folder"
                                             "and runs util diff for checking differences"
                                             "between current and saved states of the selected file or folder")

parser.add_argument('cmd',
                    type=str,
                    choices=['store', 'diff'],
                    help="store - saves current state of file or folder"
                    "diff - runs standard util diff for current and saved states of file or folder")


parser.add_argument('path',
                    type=str,
                    help="Path to the selected file or folder")

argts = parser.parse_args()
cmd = argts.cmd
path = argts.path

home = '/home/jack-a-lynn/.sad/'
name = path.split('/')[-1]
new_path = home + name
n_p = str(new_path)

if cmd == 'store':
    if os.path.isfile(path):
        shutil.copy(path, home)
    elif os.path.isdir(path):
        shutil.copytree(path, home)

elif cmd == 'diff':
    diff_cmd = 'diff ' + n_p + ' ' + str(path)
    print(subprocess.call(diff_cmd, shell=True))

