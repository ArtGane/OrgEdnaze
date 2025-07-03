import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS

image_folder = os.path.join(os.environ['USERPROFILE'], 'Pictures')

def get_image_properties(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                properties = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
                return properties
            else:
                return {}
    except Exception as e:
        print(f"Error reading image properties: {e}")
        return {}

def rename_image_with_date(image_path):
    properties = get_image_properties(image_path)
    date = properties.get("DateTime", None)
    if date:
        formatted_date = date.split(" ")[0].replace(":", "-")
        file_extension = os.path.splitext(image_path)[1]
        new_name = f"{formatted_date}{file_extension}"
        new_path = os.path.join(image_folder, new_name)
        try:
            os.rename(image_path, new_path)
            print(f"Renamed {image_path} to {new_path}")
        except Exception as e:
            print(f"Error renaming {image_path}: {e}")
    else:
        print(f"No DateTime metadata found for {image_path}")

for image_file in glob.glob(os.path.join(image_folder, '**', '*.*'), recursive=True):
    rename_image_with_date(image_file)