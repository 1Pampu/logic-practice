# * I'm celebrating! I've published my first book:
#  * "Git y GitHub desde cero"
# * - Paperback: mouredev.com/libro-git
# * - eBook: mouredev.com/ebook-git
# *
# * Did you know you can read information about Git and GitHub from most programming languages?
# *
# * Create a program that reads the last 10 commits from this repository and displays:
# * - Hash
# * - Author
# * - Message
# * - Date and Time
# *
# * Example output:
# * Commit 1 (most recent) | 12345A | MoureDev | This is a commit | 24/04/2023 21:00
# *
# * You're allowed to use libraries that facilitate this task.

from github import Github

g = Github()

repo = g.get_repo("mouredev/retos-programacion-2023")
commits = repo.get_commits()
last_ten = list(commits[:10])

for commit in last_ten:
    print(f"Commit {last_ten.index(commit) + 1} | {commit.sha} | {commit.commit.author.name} | {commit.commit.message} | {commit.commit.author.date}")
    print("-------------------------------------------------")