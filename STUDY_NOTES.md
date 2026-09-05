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

`id_ed25519`

This stays on my Mac. I must never share, upload, or copy its contents.

### Public Key

`id_ed25519.pub`

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
2. Which command lists my files?
3. Which command runs a Python file?
4. Which command selects changes for a commit?
5. Which command saves a local checkpoint?
6. Which command uploads commits to GitHub?
7. Which SSH key must remain private?
8. What does “working tree clean” mean?