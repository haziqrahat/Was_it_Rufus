# Import the existing packages
import os
import sys
import subprocess


# Create a helper method that prints specifics about a local repository


def get_git_info(local_repo_path):
    os.chdir(local_repo_path)
    # Use subprocess to run the 'git' command and retrieve the output
    active_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
    local_changes = subprocess.check_output(
        ['git', 'status', '--porcelain']).strip()
    recent_commit = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%ad', '--since="a week ago"', '--before="this week"']).strip()
    blame_Rufus = subprocess.check_output(
        ['git', 'log', '-1', '--pretty=%an']).strip()

    # Print the active branch
    print('active branch:', active_branch.decode())

    # Print whether repository files have been modified
    print("local changes:", local_changes.decode() != '')

    # Print whether the current head commit was authored in the last week
    print("recent commit:", recent_commit.decode() != '')

    # Print whether the current head commit was authored by Rufus
    print("blame Rufus:", blame_Rufus.decode() == 'Rufus ')


if __name__ == '__main__':
    # Call the helper method from main
    get_git_info(sys.argv[1])
