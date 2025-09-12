# METHOD TO CREATE A FOLDER
import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day {i+1}")

# METHOD TO DELETE A WHOLE FOLDER
import os
import shutil

if os.path.exists("data"):
    shutil.rmtree("data")

# METHOD TO CLEAN INSIDE THE FILE BUT KEEP FOLDER

import os
import shutil

folder = "data"

if os.path.exists(folder):
    # Loop through all files & subfolders in "data"
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        # If it's a file → remove it
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        # If it's a folder → remove it and its contents
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
