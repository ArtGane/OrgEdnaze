import os
import glob
import shutil
from PIL import Image
import imagehash

pictures_folder = os.path.join(os.environ['USERPROFILE'], 'Pictures')

# Fonction pour calculer le hash d'une image
def get_image_hash(image_path):
    try:
        with Image.open(image_path) as img:
            return imagehash.average_hash(img)
    except Exception as e:
        print(f"Erreur lors du traitement de l'image {image_path}: {e}")
        return None

# Récupérer tous les fichiers dans le dossier Images
files = glob.glob(os.path.join(pictures_folder, '**', '*.*'), recursive=True)
hashes = {}
duplicates = []

for file in files:
    if not os.path.isfile(file):
        continue

    image_hash = get_image_hash(file)
    if image_hash is None:
        continue

    # Vérifier si le hash existe déjà
    if image_hash in hashes:
        print(f"Doublon détecté : {file} est un doublon de {hashes[image_hash]}")
        duplicates.append(file)
    else:
        hashes[image_hash] = file

# Supprimer les doublons détectés
for duplicate in duplicates:
    print(f"Suppression du doublon : {duplicate}")
    os.remove(duplicate)