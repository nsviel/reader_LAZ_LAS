#---------------------------------------------
import numpy as np
import pylas
from tkinter.filedialog import askopenfilenames
import os
import converter
import merger
from pathlib import Path


def get_format(path):
    try:
        filename, format = os.path.splitext(path)
    except:
        format = ""
    return format.casefold()

def check_file_format(path, format_1, format_2):
    format = get_format(path)
    if(format.casefold() == format_1 or format.casefold() == format_2):
        return True
    else:
        return False

def open_selected_files(paths):
    clouds = []
    for path in paths:
        # Check file format
        if(check_file_format(path, ".las", ".laz") == False):
            print("[\033[1;31merror\033[0m] Format not accepted [laz, las]")
            return;

        # If LAZ file, convert it into LAS file
        format = get_format(path)
        if(format == ".laz"):
            path = converter.convert_laz_to_las(path)

        # Get data from file
        cloud = retrieve_cloud_data(path)
        clouds.append(cloud)

    return clouds;

def retrieve_cloud_data(path):
    with pylas.open(path) as f:
        # Read file and display some stats
        print("[\033[1;32mok\033[0m] Opening file \033[1;32m%s\033[0m"% path)
        las = f.read()

        dim = list(las.point_format.dimension_names)
        print("[\033[1;34m#\033[0m] Dimensions are: \033[1;32m%s\033[0m"% dim)
        print("[\033[1;34m#\033[0m] Number of points \033[1;32m%s\033[0m"% len(las.points))

        X = las.X / float(10000)
        Y = las.Y / float(10000)
        Z = las.Z / float(10000)
        I = las.intensity / float(255)

        x = np.array([X])
        y = np.array([Y])
        z = np.array([Z])

        xyz = np.concatenate((x, y, z), axis=0)

        cloud =	{
            "name": "",
            "xyz": 0,
            "I": 0
        }

        cloud["name"] = Path(path).stem
        cloud["xyz"] = xyz.transpose()
        cloud["I"] = I.transpose()

        return cloud

def gui_file_selection():
    path = askopenfilenames(initialdir= "../")
    if(path == ""):
        print("[\033[1;31merror\033[0m] Loader - No path given")
        exit(0)
        return;
    return path
