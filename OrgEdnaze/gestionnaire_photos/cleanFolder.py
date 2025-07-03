import os
import glob
import shutil
from PIL import Image
import imagehash

pictures_folder = os.path.join(os.environ['USERPROFILE'], 'Pictures')

# Récupérer tous les dossiers dans le dossier Images
folders = [f for f in glob.glob(os.path.join(pictures_folder, '*')) if os.path.isdir(f)]

# Déplacer les fichiers des dossiers dans le dossier Images
for folder in folders:
    # Récupérer tous les fichiers dans le dossier
    files = glob.glob(os.path.join(folder, '*'))
    if files == []:
        # Si le dossier est vide, le supprimer
        os.rmdir(folder)
        continue
    for file in files:
        if not os.path.exists(file):
            print(f"Le fichier {file} n'existe pas, il sera ignoré.")
            continue

        print(f"Traitement du fichier : {file}")
        base, ext = os.path.splitext(os.path.basename(file))
        destination = os.path.join(pictures_folder, os.path.basename(file))
        counter = 1
        while os.path.exists(destination):
            new_file_name = f"{base}_{counter}{ext}"
            destination = os.path.join(pictures_folder, new_file_name)
            counter += 1

        print(f"Déplacement vers : {destination}")
        shutil.move(file, destination)

# Supprimer le dossier vide
os.rmdir(folder)

