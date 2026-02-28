import git
from config import cfg  # cfg = {"githubkey": "twój_token"} w config.py

# CONFIGURATION
FILE_PATH = "example.txt"  # plik do edycji
YOUR_NAME = "Joanna"

# OTWÓRZ LOKALNE REPO – folder, w którym jest .git
repo = git.Repo(".")  # "." = bieżący folder

origin = repo.remotes['origin']
# 1️⃣ Sprawdź, czy są niezatwierdzone zmiany
if repo.is_dirty(untracked_files=True):
    print("Repo ma niezatwierdzone zmiany! Zacommituj je lub użyj stash przed pull.")
else:
    # 2️⃣ Pull z rebase, żeby zsynchronizować zdalne zmiany
    origin.pull(rebase=True)
    print("Pull wykonany pomyślnie!")

# 3️⃣ Otwórz plik i zastąp "Andrew" własnym imieniem
with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Andrew", YOUR_NAME)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f'Zmieniono wszystkie wystąpienia "Andrew" na "{YOUR_NAME}".')

# 4️⃣ Dodaj i commituj zmiany
repo.index.add([FILE_PATH])
repo.index.commit(f'Replace "Andrew" with {YOUR_NAME}')

# 5️⃣ Push na GitHub
# Używamy HTTPS z tokenem do autoryzacji (nie ujawniamy tokena w repo)
remote_url = f"https://JoannaMnich:{cfg['githubkey']}@github.com/JoannaMnich/WSAA/Assignments.git"
origin.set_url(remote_url)  # tymczasowo ustaw URL z tokenem
origin.push()
print("Zmiany zostały wypchnięte na GitHub!")

# 6️⃣ Opcjonalnie: przywróć oryginalny URL bez tokena
origin.set_url(f"https://github.com/JoannaMnich/WSAA.git")
