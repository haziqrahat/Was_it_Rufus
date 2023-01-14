# Import the existing packages
import os
import sys
import subprocess


# Create a helper method that prints specifics about a local repository


def get_git_info(git_dir):
    os.chdir(git_dir)
    # Use subprocess to run the 'git' command and retrieve the output
    active_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
    local_changes = subprocess.check_output(
        ['git', 'status', '--porcelain']).strip()
    recent_commit = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%ad', '--since="yesterday"']).strip()
    blame_Rufus = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%an']).strip()
    # CHECK
    # Print the active branch
    print('active branch:', active_branch.decode())

    # Print whether repository files have been modified
    print("local changes:", local_changes.decode() != '')

    # Print whether the current head commit was authored in the last week
    print("recent commit:", recent_commit.decode() != '')

    # Print whether the current head commit was authored by Rufus
    print("blame Rufus:", blame_Rufus.decode() == 'Rufus ')


if __name__ == '__main__':

    # Error handling to ensure path's correctness
    path = sys.argv
    if len(path) < 2:
        print('Error: Path not provided')
    elif not os.path.isdir(path[1]):
        print('Error : Path provided is not a valid directory')
    elif not os.path.exists(os.path.join(path[1], '.git')):
        print('Error : Path provided is not a valid git directory')
    else:
        # Calling the helper method from main
        get_git_info(path[1])
