
import git 

# CONFIGURATION
REPO_URL = "https://JoannaMnich:YOUR_TOKEN@github.com/JoannaMnich/aprivateone.git"
LOCAL_PATH = "temp_repo"  # temporary local folder for repo
FILE_PATH = "path/to/file.txt"  # file to modify inside repo
YOUR_NAME = "Joanna"

# OPEN REPO
try:
    repo = git.Repo(LOCAL_PATH)
    repo.remotes.origin.pull()
except:
    repo = git.Repo.clone_from(REPO_URL, LOCAL_PATH)

# MODIFY FILE
file_full_path = f"{LOCAL_PATH}/{FILE_PATH}"

with open(file_full_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Andrew", YOUR_NAME)

with open(file_full_path, "w", encoding="utf-8") as f:
    f.write(content)

# COMMIT AND PUSH
repo.git.add(FILE_PATH)
repo.git.commit("-m", f"Replace 'Andrew' with {YOUR_NAME}")
repo.git.push("origin", "main")

print("File updated and pushed successfully!")
