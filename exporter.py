#---------------------------------------------
import ply
from tkinter.filedialog import asksaveasfilename


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

    print("[\033[1;32mok\033[0m] Cloud set saved at '\033[1;32m%s\033[0m'"% path_dir)

def export_cloud(path, cloud):
    if(path == "" or type(path)==tuple):
        print("[\033[1;32merror\033[0m] Exporter - No path given")
        return;
    if(cloud == None):
        print("[\033[1;32merror\033[0m] Exporter - No cloud data")
        return;
    if(len(cloud["xyz"]) == 0 or len(cloud["I"]) == 0):
        print("[\033[1;32merror\033[0m] Exporter - Cloud to export lake data")
        return;

    field_names = ['x', 'y', 'z', 'intensity']
    ply.write_ply(path, [cloud["xyz"], cloud["I"]], field_names)

    print("[\033[1;32mok\033[0m] Exporter - Cloud saved at '\033[1;32m%s\033[0m'"% path)

def gui_file_saveas():
    path = asksaveasfilename(initialdir= "../")
    return path
