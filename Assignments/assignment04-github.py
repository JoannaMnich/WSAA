import git
from config import cfg  

# CONFIGURATION
FILE_PATH = "example.txt"  
YOUR_NAME = "Joanna"

# Open local REPO 
repo = git.Repo(".")  
origin = repo.remotes['origin']

# Checking for uncommited changes before pull
if repo.is_dirty(untracked_files=True):
    print("Repo has uncommited changes. Please commit or stash them before pulling.")
else:
# Pull with rebase to avoid merge commits
    origin.pull(rebase=True)
    print("Pull wykonany pomyślnie!")

# Open the file and replace "Andrew" with YOUR_NAME
with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Andrew", YOUR_NAME)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f'Changed all instances of "Andrew" to "{YOUR_NAME}".')

# Add, commit and push changes
repo.index.add([FILE_PATH])
repo.index.commit(f'Replace "Andrew" with {YOUR_NAME}')

# Push to GitHub
# Use token in URL for authentication (not recommended for long-term use, but works for this assignment)
remote_url = f"https://JoannaMnich:{cfg['githubkey']}@github.com/JoannaMnich/WSAA/Assignments.git"
origin.set_url(remote_url)  
origin.push()
print("Changes pushed to GitHub successfully!")

# Optional: Reset origin URL to original after push
origin.set_url(f"https://github.com/JoannaMnich/WSAA.git")
