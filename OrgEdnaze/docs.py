import os
import shutil
import glob

documents_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')
docs = glob.glob(os.path.join(documents_folder, "*.*"))

for logiciel in docs:
    logiciels_dir = os.path.join(documents_folder, "Logiciels")
    if not os.path.exists(logiciels_dir):
        os.makedirs(logiciels_dir)
    if logiciel.endswith(".msi") or logiciel.endswith(".exe"):
        shutil.move(logiciel, logiciels_dir)
    print(f"Logiciel déplacé dans le dossier")
    
for pdf in docs:
    pdf_dir = os.path.join(documents_folder, "A Trier")
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    if pdf.endswith(".pdf"):
        base_name = os.path.basename(pdf)
        new_name = base_name
        counter = 1
        while os.path.exists(os.path.join(pdf_dir, new_name)):
            name, ext = os.path.splitext(base_name)
            sanitized_name = name.replace('-', '_')
            new_name = f"{sanitized_name}_{counter}{ext}"
            counter += 1
        shutil.move(pdf, os.path.join(pdf_dir, new_name))
    print(f"PDF déplacé dans le dossier")
