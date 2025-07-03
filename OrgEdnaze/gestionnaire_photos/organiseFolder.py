import os
import shutil

source_folder = os.path.join(os.environ['USERPROFILE'], 'Pictures')

# Liste tous les fichiers dans le dossier source
for filename in os.listdir(source_folder):
    if os.path.isfile(os.path.join(source_folder, filename)):
        # Vérifie si le nom commence par une année
        if len(filename) >= 4 and filename[:4].isdigit():
            year = filename[:4]
            year_folder = os.path.join(source_folder, year)
            # Crée le dossier de l'année s'il n'existe pas
            os.makedirs(year_folder, exist_ok=True)
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(year_folder, filename)
            shutil.move(src_path, dst_path)