# Shared functions for AOC 2023

# from decorators import print_debugger
# import os
# from pathlib import Path
from math import sqrt

def data_filename(aoc_day):
    """Return the (string) name of the puzzle data file appropriate to today's Advent of Code puzzle."""
    if aoc_day < 10:
        aoc_day = "0" + str(aoc_day)
    else:
        aoc_day - str(aoc_day)
    readfile = "day_" + aoc_day + "_input.txt"
    return readfile


# def data_filename(aoc_day):  # ToDo: fix this so it works from the wrapper script
#     """Return a path object pointing to the data file appropriate to today's Advent of Code puzzle."""
#      working_directory =
#      readfile = Path.joinpath(working_directory), aoc_filename(aoc_day), aoc_filename(aoc_day) + "_input.txt")
#      return readfile



def fetch_string_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = str(line)
            rawdata.append(line)
    return rawdata


def fetch_rstrip_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file),
    retaining spaces."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            line = str(line)
            rawdata.append(line)
    return rawdata


def fetch_raw_data(filename):
    """Reads a text file and returns its contents as a list (one element per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            rawdata.append(line)
    return rawdata


def array_print(array_name):
    """Prints a list with one element per line rather than comma-separated"""
    for line in array_name:
        print(line)


def pause():
    input("Press return to continue... ")
    return


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_neighbors(coordinate_pair):
    neighbors = []
    x, y = coordinate_pair
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            neighbors.append((i, j))
    neighbors.remove((x, y))
    return neighbors
