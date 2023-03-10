#---------------------------------------------
from src import loader
from src import exporter
from src import merger
from src import centerer

#TODO:
# - Faire function pour merge si plusieurs
# - Chunk load/ save
# - centrage du nuage


print("--- \033[1;34mStart program\033[0m ---")
#---------------------------

path_file = loader.gui_file_selection()
clouds = loader.open_selected_files(path_file)
merger.compute_merging(clouds)
path_export = exporter.gui_dir_saveas()
for cloud in clouds:
    centerer.recenter_cloud(cloud)
    exporter.export_cloud(path_export, cloud)

#---------------------------
print("--- \033[1;34mClose program\033[0m ---")
