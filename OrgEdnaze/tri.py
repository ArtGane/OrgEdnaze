import os
import shutil
import glob

# Obtenir les chemins des dossiers natifs
downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
pictures_folder = os.path.join(os.environ['USERPROFILE'], 'Pictures')
videos_folder = os.path.join(os.environ['USERPROFILE'], 'Videos')
documents_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')
music_folder = os.path.join(os.environ['USERPROFILE'], 'Music')


# Rechercher toutes les Images dans le dossier "Téléchargements"
png_files = glob.glob(os.path.join(downloads_folder, '*.png'))
jpg_files = glob.glob(os.path.join(downloads_folder, '*.jpg'))
jpeg_files = glob.glob(os.path.join(downloads_folder, '*.jpeg'))
gif_files = glob.glob(os.path.join(downloads_folder, '*.gif'))
bmp_files = glob.glob(os.path.join(downloads_folder, '*.bmp'))
tif_files = glob.glob(os.path.join(downloads_folder, '*.tif'))
tiff_files = glob.glob(os.path.join(downloads_folder, '*.tiff'))
webp_files = glob.glob(os.path.join(downloads_folder, '*.webp'))
heic_files = glob.glob(os.path.join(downloads_folder, '*.heic'))
heif_files = glob.glob(os.path.join(downloads_folder, '*.heif'))
svg_files = glob.glob(os.path.join(downloads_folder, '*.svg'))
eps_files = glob.glob(os.path.join(downloads_folder, '*.eps'))
ico_files = glob.glob(os.path.join(downloads_folder, '*.ico'))
xcf_files = glob.glob(os.path.join(downloads_folder, '*.xcf'))

# Rechercher toutes les vidéos dans le dossier "Téléchargements"
mp4_files = glob.glob(os.path.join(downloads_folder, '*.mp4'))
avi_files = glob.glob(os.path.join(downloads_folder, '*.avi'))
mov_files = glob.glob(os.path.join(downloads_folder, '*.mov'))
mkv_files = glob.glob(os.path.join(downloads_folder, '*.mkv'))
wmv_files = glob.glob(os.path.join(downloads_folder, '*.wmv'))
flv_files = glob.glob(os.path.join(downloads_folder, '*.flv'))

# Rechercher tous les documents dans le dossier "Téléchargements"
doc_files = glob.glob(os.path.join(downloads_folder, '*.doc'))
docx_files = glob.glob(os.path.join(downloads_folder, '*.docx'))
pdf_files = glob.glob(os.path.join(downloads_folder, '*.pdf'))
txt_files = glob.glob(os.path.join(downloads_folder, '*.txt'))
xlsx_files = glob.glob(os.path.join(downloads_folder, '*.xlsx'))
pptx_files = glob.glob(os.path.join(downloads_folder, '*.pptx'))
zip_files = glob.glob(os.path.join(downloads_folder, '*.zip'))
rar_files = glob.glob(os.path.join(downloads_folder, '*.rar'))
exe_files = glob.glob(os.path.join(downloads_folder, '*.exe'))
msi_files = glob.glob(os.path.join(downloads_folder, '*.msi'))

# Rechercher tous les fichiers de code dans le dossier "Téléchargements"
py_files = glob.glob(os.path.join(downloads_folder, '*.py'))
js_files = glob.glob(os.path.join(downloads_folder, '*.js'))
html_files = glob.glob(os.path.join(downloads_folder, '*.html'))
css_files = glob.glob(os.path.join(downloads_folder, '*.css'))
java_files = glob.glob(os.path.join(downloads_folder, '*.java'))

# Rechercher tous les fichiers audio dans le dossier "Téléchargements"
mp3_files = glob.glob(os.path.join(downloads_folder, '*.mp3'))
wav_files = glob.glob(os.path.join(downloads_folder, '*.wav'))
flac_files = glob.glob(os.path.join(downloads_folder, '*.flac'))
aac_files = glob.glob(os.path.join(downloads_folder, '*.aac'))
ogg_files = glob.glob(os.path.join(downloads_folder, '*.ogg'))

# Combiner tous les fichiers d'images dans une liste
all_images = (png_files + jpg_files + jpeg_files + gif_files + bmp_files + 
              tif_files + tiff_files + 
              webp_files + heic_files + heif_files + svg_files + eps_files + 
              ico_files + xcf_files)

# Combiner tous les fichiers de vidéos dans une liste
all_videos = mp4_files + avi_files + mov_files + mkv_files + wmv_files + flv_files

# Combiner tous les fichiers de documents dans une liste
all_docs = (doc_files + docx_files + pdf_files + txt_files + xlsx_files + pptx_files +
            zip_files + rar_files + exe_files + py_files + js_files + html_files + 
            css_files + java_files)

# Combiner tous les fichiers audio dans une liste
all_audio = mp3_files + wav_files + flac_files + aac_files + ogg_files

# Déplacer chaque image  vers le dossier "Images"
for file_path in all_images:
    file_name = os.path.basename(file_path)
    destination = os.path.join(pictures_folder, file_name)
    shutil.move(file_path, destination)
    print(f"Image déplacé : {file_path} -> {destination}")
    
# Déplacer chaque vidéo vers le dossier "Vidéos"
for file_path in all_videos:
    file_name = os.path.basename(file_path)
    destination = os.path.join(videos_folder, file_name)
    shutil.move(file_path, destination)
    print(f"Vidéo déplacé : {file_path} -> {destination}")
    
# Déplacer chaque document vers le dossier "Documents"
for file_path in all_docs:
    file_name = os.path.basename(file_path)
    destination = os.path.join(documents_folder, file_name)
    shutil.move(file_path, destination)
    print(f"Document déplacé : {file_path} -> {destination}")

# Déplacer chaque fichier audio vers le dossier "Musique"
for file_path in all_audio:
    file_name = os.path.basename(file_path)
    destination = os.path.join(music_folder, file_name)
    shutil.move(file_path, destination)
    print(f"Audio déplacé : {file_path} -> {destination}")