#---------------------------------------------
import os


def compute_merging(clouds):
    if(len(clouds) == 2):
        if(merge_two_las(clouds[0], clouds[1])):
            clouds = []
            clouds.append(clouds[0])

def ask_for_new_name():
    while True:
        try:
            name = str(input("[\033[1;34m#\033[0m] Merger - What is the new cloud name ? "))
            if(name != ""):
                return name
        except ValueError:
            print("[\033[1;31merror\033[0m] Merger - Sorry, I didn't understand that.")
            continue
        else:
            break

def ask_for_merging(name_1, name_2):
    while True:
        try:
            resp = str(input("[\033[1;34m#\033[0m] Merger - Do you want to merge \033[1;32m%s\033[0m and \033[1;32m%s\033[0m ? [y/N]"% (name_1, name_2)))
            if(resp == "true" or resp == "True" or resp == "y" or resp == "Y" or resp == "yes"):
                return True
            if(resp == "" or resp == "false" or resp == "False" or resp == "n" or resp == "N" or resp == "no"):
                return False
        except ValueError:
            print("[\033[1;31merror\033[0m] Merger - Sorry, I didn't understand that.")
            continue
        else:
            break

def merge_two_las(cloud_1, cloud_2):
    if(ask_for_merging(cloud_1["name"], cloud_2["name"])):
        print("[\033[1;34m#\033[0m] Merging \033[1;32m%s\033[0m and \033[1;32m%s\033[0m"% (cloud_1["name"], cloud_2["name"]))
        cloud_1["xyz"] = np.concatenate((cloud_1["xyz"], cloud_2["xyz"]), axis=1)
        cloud_1["I"] = np.concatenate((cloud_1["I"], cloud_2["I"]), axis=1)
        print("[\033[1;32mok\033[0m] Merging done")
        cloud["name"] = ask_for_new_name()
        return True
    return False
