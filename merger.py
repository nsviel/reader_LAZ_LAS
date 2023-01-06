#!/usr/bin/env python3
import sys
import traceback
import laspy
import os
import converter


def append_to_las(path_1, path_2):
    with laspy.open(path_2, mode='a') as outlas:
        with laspy.open(path_1) as inlas:
            for points in inlas.chunk_iterator(2_000_000):
                outlas.append_points(points)

def merge_two_las(path_1, path_2):
    print("[\033[1;32mok\033[0m] Merging \033[1;32m%s\033[0m and \033[1;32m%s\033[0m"% (path_1, path_2))
    path_1 = convert_laz_to_las(path_1)
    path_2 = convert_laz_to_las(path_2)
    append_to_las(in_las, out_las)
    print("[\033[1;32mok\033[0m] Merging done")
    return path_2
