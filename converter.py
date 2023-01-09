#!/usr/bin/env python3
import sys
import traceback
import laspy
import os



def write_laz_to_las(in_laz, out_las):
    las = laspy.read(in_laz)
    las = laspy.convert(las)
    las.write(out_las)

def convert_laz_to_las(path):
    if(path.endswith('.laz')):
        print('[\033[1;32mok\033[0m] Converter - working on file \033[1;32m%s\033[0m'% path)
        out_las = path.replace('.laz', '.las')
        write_laz_to_las(path, out_las)
        path = out_las

        print("[\033[1;32mok\033[0m] Converter - file LAZ to LAS finished")
    else:
        print("[\033[1;31merror\033[0m] Converter - file is not in LAZ format")

    return path;
