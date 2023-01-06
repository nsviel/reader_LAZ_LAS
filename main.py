#---------------------------------------------
import loader
import exporter

#TODO:
# - Faire function pour merge si plusieurs
# - Chunk load/ save
# - centrage du nuage

print("--- \033[1;32mStart program\033[0m ---")
#---------------------------

path = loader.gui_file_selection()
cloud = loader.open_file(path)
path = exporter.gui_file_saveas()
exporter.export_cloud(path, cloud)

#---------------------------
print("--- \033[1;32mClose program\033[0m ---")
