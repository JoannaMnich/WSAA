# assignment04-github.py
# Script: replaces "Andrew" with your name in a file in a repository and pushes the changes

import git
import os

# ------------------ CONFIGURATION ------------------
REPO_URL = "https://github.com/JoannaMnich/WSAA.git"         # URL of the repository
CLONE_DIR = "temp_repo"                                      # temporary folder for cloning
FILE_PATH = "Assignments/example.txt"                        # path to the file inside the repo
YOUR_NAME = "Joanna"                                         # name to replace "Andrew"
# ---------------------------------------------------

def main():
    # Clone the repository or pull latest changes if already cloned
    if not os.path.exists(CLONE_DIR):
        print("Cloning repository...")
        repo = git.Repo.clone_from(REPO_URL, CLONE_DIR)
    else:
        print("Repository exists, pulling latest changes...")
        repo = git.Repo(CLONE_DIR)
        repo.remotes.origin.pull()

    # Full path to the file
    file_full_path = os.path.join(CLONE_DIR, FILE_PATH)

    # Read file content
    with open(file_full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace "Andrew" with your name
    new_content = content.replace("Andrew", YOUR_NAME)

    # Write changes back to the file
    with open(file_full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Commit and push changes
    repo.index.add([FILE_PATH])
    repo.index.commit(f"Replaced 'Andrew' with '{YOUR_NAME}'")
    print("Pushing changes to the repository...")
    repo.remotes.origin.push()
    print("Done!")

if __name__ == "__main__":
    main()
