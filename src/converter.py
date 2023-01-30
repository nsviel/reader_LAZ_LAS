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
    if(path.endswith('.laz') or path.endswith('.LAZ')):
        print('[\033[1;34m#\033[0m] Converter - working on file \033[1;32m%s\033[0m'% path)

        if(path.endswith('.laz')):
            out_las = path.replace('.laz', '.las')
        if(path.endswith('.LAZ')):
            out_las = path.replace('.LAZ', '.las')
        write_laz_to_las(path, out_las)
        path = out_las

        print("[\033[1;34m#\033[0m] Converter - file LAZ to LAS finished")
    else:
        print("[\033[1;31merror\033[0m] Converter - file is not in LAZ format")

    return path;
