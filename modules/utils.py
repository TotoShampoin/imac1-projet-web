import os

# Vérifier si c'est un fichier
def exists_and_is_file(path: str):
    return os.path.exists(path) and os.path.isfile(path)

# Vérifier si c'est un dossier
def exists_and_is_dir(path: str):
    return os.path.exists(path) and os.path.isdir(path)

