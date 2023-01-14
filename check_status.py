import subprocess
import os
import sys
from datetime import datetime, timedelta


def git_info(git_dir):
    os.chdir(git_dir)
    # Use subprocess to run the 'git' command and retrieve the output
    branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
    author = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%an']).strip()
    date = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%ad']).strip()

    # Print the active branch
    if branch.decode() == 'HEAD':
        print("Active branch: False")
    else:
        print("Active branch: True")

    # Print whether repository files have been modified
    status = subprocess.check_output(['git', 'status', '--porcelain']).strip()
    if status:
        print("Repository files have been modified: True")
    else:
        print("Repository files have been modified: False")

    # Print whether the current head commit was authored in the last week
    date = datetime.strptime(date.decode(), "%a %b %d %H:%M:%S %Y %z")
    if date > datetime.now() - timedelta(days=7):
        print("Current head commit was authored in the last week: True")
    else:
        print("Current head commit was authored in the last week: False")

    # Print whether the current head commit was authored by Rufus
    if author.decode() == "Rufus":
        print("Current head commit was authored by Rufus: True")
    else:
        print("Current head commit was authored by Rufus: False")


if __name__ == '__main__':
    git_info(sys.argv[1])
