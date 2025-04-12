import os
import json
from PIL import Image
import cv2

# Folder path
folder_path = "./../sidecar_fav"
outdir = "./"

# Supported formats
image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}
video_exts = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}

# Output list
file_data = []

# Walk through folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    ext = os.path.splitext(filename)[1].lower()
    
    width, height = None, None
    
    try:
        if ext in image_exts:
            with Image.open(file_path) as img:
                width, height = img.size

        elif ext in video_exts:
            cap = cv.VideoCapture(file_path)
            if cap.isOpened():
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            cap.release()
        
        if width and height:
            file_data.append({
                "src": f"./sidecar_fav/{filename}",
                "width": width,
                "height": height
            })

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Export to JSON
output_path = os.path.join(outdir, "metadata.json")
with open(output_path, "w") as f:
    json.dump(file_data, f, indent=4)

print(f"Exported metadata to {output_path}")

