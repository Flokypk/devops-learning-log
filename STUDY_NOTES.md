# Week 0 Study Notes: Terminal, Python, Git, and GitHub

## 1. Terminal

The Terminal allows me to control my computer by typing commands.

### Commands I Learned

| Command | Meaning |
|---|---|
| `pwd` | Shows which folder I am currently inside |
| `ls` | Lists the files inside my current folder |
| `cd folder-name` | Moves me into a folder |
| `mkdir` | Creates a new folder |
| `code .` | Opens my current folder in VS Code |
| `python3 file.py` | Runs a Python file |
| `clear` | Clears old Terminal text |

### Important Symbols

- `~` means my home folder: `/Users/rickyflores`
- `/` means go inside a folder
- `.` means my current folder
- `%` means the Terminal is ready for a new command

Correct:

`~/.ssh`

Incorrect:

`~.ssh`

The incorrect version is missing `/`.

---

## 2. Python

I created a Python file named `day1.py`.

### Code Concepts

`print()` displays information.

Example:

`print("DevOps Learning Log")`

A variable stores information.

Example:

`daily_goal = 120`

`input()` asks the user a question.

Example:

`input("How many minutes did you practice? ")`

`input()` normally produces text. `int()` converts that text into a whole number.

Example:

`completed = int(input("How many minutes did you practice? "))`

Python can use variables in calculations.

Example:

`remaining = daily_goal - completed`

If `daily_goal` is 120 and `completed` is 30:

`remaining = 120 - 30`

The result is 90.

### Running a Python File

`python3 day1.py`

---

## 3. Git and GitHub

Git and GitHub are related, but they are not the same thing.

### Git

Git runs on my computer. It records the history of my project.

### GitHub

GitHub is an online website where I store and display my Git repositories.

### Repository

A repository is a project folder that Git tracks.

---

## 4. The Main Git Workflow

`Files → git add → git commit → git push → GitHub`

### git add

`git add` selects files for my next checkpoint.

Memory trick: Put the files into a box.

Example:

`git add README.md day1.py`

### git commit

`git commit` saves a named checkpoint on my computer.

Memory trick: Seal and label the box.

Example:

`git commit -m "Start DevOps learning log"`

### git push

`git push` uploads my saved commits to GitHub.

Memory trick: Ship the box online.

Example:

`git push`

Only `git push` makes my committed changes appear on GitHub.

---

## 5. Other Git Commands

### Start Git

`git init`

This turns my current folder into a Git repository. It does not upload anything.

### Check My Files

`git status`

Possible messages:

- `Untracked` means Git sees a file but is not tracking it yet.
- `Changes to be committed` means the file is staged.
- `Working tree clean` means everything has been committed.
- `U` means untracked.
- `A` means added to the staging area.

### View Commit History

`git log --oneline`

My first commit was:

`54bf932 Start DevOps learning log`

The letters and numbers are the commit’s unique identification number.

### Connect Git to GitHub

`git remote add origin git@github.com:Flokypk/devops-learning-log.git`

- `remote` means an online repository.
- `origin` is the nickname for my GitHub repository.
- `main` is my current branch.

### First Push

`git push -u origin main`

The `-u` connects my local `main` branch to GitHub’s `main` branch.

After the first push, I normally only need:

`git push`

---

## 6. SSH Security

SSH allows my Mac to communicate securely with GitHub.

### Private Key

no no no silly

This stays on my Mac. I must never share, upload, or copy its contents.

### Public Key

no no silly

The `.pub` ending means public. This is the key that I added to GitHub.

### Passphrase

My passphrase protects my private key. Terminal does not display letters or dots while I type a password.

### GPG

A GPG key can sign commits as verified. It is optional and I do not need it yet.

---

## 7. My Normal Workflow From Now On

After changing project files:

1. Check what changed:

`git status`

2. Stage the specific files:

`git add filename`

3. Check before committing:

`git status`

4. Save a checkpoint:

`git commit -m "Short explanation of the change"`

5. Upload it:

`git push`

6. Confirm everything is saved:

`git status`

---

## Quick Memory Test

1. Which command shows my current folder?
pwd
2. Which command lists my files?
ls
3. Which command runs a Python file?
python3 filename.py
4. Which command selects changes for a commit?
git add filename
5. Which command saves a local checkpoint?
git commit -m "Describe the change"
6. Which command uploads commits to GitHub?
git push
7. Which SSH key must remain private?
id_ed25519
8. What does “working tree clean” mean?
Your branch is up to date with 'origin/main'.

Everyday Terminal Commands
Where am I?        → pwd
List my files?     → ls
Move into folder?  → cd folder-name
Create a folder?   → mkdir folder-name
Open VS Code here? → code .
Clear the screen?  → clear
Stop a command?    → Control + C

Git
Start Git here?       → git init
Check my changes?     → git status
Select a file?        → git add filename
Save a checkpoint?    → git commit -m "Message"
View commit history?  → git log --oneline
Upload commits?       → git push

Main memory pattern:
Select → Save   → Send
add    → commit → push

Where?  → pwd
List?   → ls
Run?    → python3 filename.py
Select? → git add filename
Save?   → git commit -m "Message"
Send?   → git push

## Day 2 - Variables and Conditionals

### In My Own Words

- `weekly_minutes` stores:
- `weekly_goal` stores:
- `>=` means:
- The `if` section runs when:
- The `else` section runs when:
- Python indentation is important because:
- My original comparison was wrong because:

### Practice Trace

minutes_per_day = 80
days_per_week = 5
weekly_goal = 600

weekly_minutes = 400
Condition is: 400 >= 600
True or False: False
Branch used: else
Minutes still needed: 200