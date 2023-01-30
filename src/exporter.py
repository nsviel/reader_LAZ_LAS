#---------------------------------------------
from src import ply
from tkinter.filedialog import askdirectory


def create_directory(path):
    if(os.path.isdir(path) == False):
        os.makedirs(path)

def export_cloud_set(path_dir, path_file, list_cloud):
    create_directory(path_dir)
    field_names = ['x', 'y', 'z', 'intensity']

    cpt = 0
    for cloud in list_cloud:
        path_export = path_dir + "/" + path_file + "_" + str(cpt) + ".ply"
        ply.write_ply(path_export, [cloud["xyz"], cloud["I"]], field_names)
        cpt = cpt + 1

    print("[\033[1;34m#\033[0m] Cloud set saved at '\033[1;32m%s\033[0m'"% path_dir)

def export_cloud(path_dir, cloud):
    if(path_dir == "" or type(path_dir)==tuple):
        print("[\033[1;31merror\033[0m] Exporter - No path given")
        return;
    if(cloud == None):
        print("[\033[1;31merror\033[0m] Exporter - No cloud data")
        return;
    if(len(cloud["xyz"]) == 0 or len(cloud["I"]) == 0):
        print("[\033[1;31merror\033[0m] Exporter - Cloud to export lake data")
        return;

    field_names = ['x', 'y', 'z', 'intensity']
    path = path_dir + "/" + cloud["name"]
    ply.write_ply(path, [cloud["xyz"], cloud["I"]], field_names)

    print("[\033[1;34m#\033[0m] Exporter - Cloud saved at '\033[1;32m%s\033[0m'"% path)

def gui_dir_saveas():
    path_dir = askdirectory(initialdir= "../")
    if(path_dir == ""):
        print("[\033[1;31merror\033[0m] Exporter - No path given")
        exit(0)
    return path_dir
