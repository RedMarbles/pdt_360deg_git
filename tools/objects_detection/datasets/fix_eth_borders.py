#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script will modify all images a folder,
by inpaint the borders (by assuming a border size.
"""


from __future__ import print_function

import sys
sys.path.append("..")
sys.path.append("../data_sequence")
sys.path.append("../helpers")

from query_yes_no import query_yes_no

import os.path
from optparse import OptionParser

try:
    import Image
except ImportError, exc:
    raise SystemExit("PIL must be installed to run this application")

from multiprocessing import Pool, cpu_count


def parse_arguments():

        parser = OptionParser()
        parser.description = \
            "This program takes a folder with images and modify them"

        parser.add_option("-i", "--input", dest="input_path",
                          metavar="FILE", type="string",
                          help="path to the .data_sequence file")

        (options, args) = parser.parse_args()
        #print (options, args)

        if options.input_path:
            if not os.path.exists(options.input_path):
                parser.error("Could not find the input file")
        else:
            parser.error("'input' option is required to run this program")

        return options


def fix_top_border(pixels, width, height, border):

    top_border_y = border
    for y in range(0, top_border_y):
        for x in range(0, width):
            pixels[x, y] = pixels[x, top_border_y]

    return top_border_y


def fix_bottom_border(pixels, width, height, border):

    bottom_border_y = (height - 1) - border
    for y in range(bottom_border_y + 1, height):
        for x in range(0, width):
            pixels[x, y] = pixels[x, bottom_border_y]

    return bottom_border_y


def fix_left_border(pixels, width, height, border):

    left_border_x = border
    for y in range(0, height):
        for x in range(0, left_border_x - 1):
            pixels[x, y] = pixels[left_border_x, y]

    return left_border_x


def fix_right_border(pixels, width, height, border):

    right_border_x = (width - 1) - border
    for y in range(0, height):
        for x in range(right_border_x + 1, width):
            pixels[x, y] = pixels[right_border_x, y]

    return right_border_x


def fix_image_borders(image_file_path):

    image = Image.open(image_file_path)

    pixels = image.load()
    width, height = image.size
    border = 3

    fix_top_border(pixels, width, height, border)
    fix_bottom_border(pixels, width, height, border)
    fix_left_border(pixels, width, height, border)
    fix_right_border(pixels, width, height, border)

    image.save(image_file_path)

    print(".", end="")
    return


def main():

    options = parse_arguments()

    yes_should_continue = query_yes_no(
        "All the images in %s will be modified.\n"
        "No backup will be created, ARE YOU SURE?" % options.input_path,
        default="no")

    if not yes_should_continue:
        print("End of game. No file has been edited.")
        return

    filenames = [os.path.join(options.input_path, x)
        for x in os.listdir(options.input_path)]

    use_multithreads = True
    #use_multithreads = False
    if use_multithreads:
        # multithreaded processing of the files
        num_processes = cpu_count() + 1
        pool = Pool(processes=num_processes)
        pool.map(fix_image_borders, filenames)
    else:
        for filename in filenames:
            fix_image_borders(filename)

    print("\nEnd of game. Have a nice day")
    return


if __name__ == "__main__":

    # Import Psyco if available
    try:
        import psyco
        psyco.full()
    except ImportError:
        #print("(psyco not found)")
        pass
    else:
        print("(using psyco)")

    main()


# end of file
