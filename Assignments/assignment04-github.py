# assignment04-github.py
# Script: replaces "Andrew" with your name in a file in a repository and pushes the changes

import git
from config import config as cfg  # zawiera githubkey

# CONFIGURATION
REPO_URL = f"https://JoannaMnich:{cfg['githubkey']}@github.com/JoannaMnich/WSAA"
FILE_PATH = "example.txt"  # plik do modyfikacji
YOUR_NAME = "Joanna"

# OPEN LOCAL REPO 
repo = git.Repo(".") 
repo.remotes.origin.pull()

# MODIFY FILE
with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Andrew", YOUR_NAME)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

# COMMIT AND PUSH
repo.git.add(FILE_PATH)
repo.git.commit("-m", f"Replace 'Andrew' with {YOUR_NAME}")
repo.git.push("origin", "main")

print("File updated and pushed successfully!")
