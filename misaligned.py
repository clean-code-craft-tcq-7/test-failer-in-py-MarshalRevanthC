
from value_lib import *

def final_index():
    global dict_allingment
    final_nth_index = dict_allingment[-1]
    return final_nth_index

def Index_limits():
    global major_index, minor_index
    return major_index * 5 + minor_index + 1

def print_allignment(major, minor):
    global major_index, minor_index
    print(f'{Index_limits()} | {major} | {minor}')
    return Index_limits()

def access_color_map():
    global major_index, minor_index, dict_allingment
    for major in major_colors:
        for minor in minor_colors:
            major_index, minor_index = major_colors.index(major), minor_colors.index(minor)
            dict_allingment.append(print_allignment(major, minor))
    return len(major_colors) * len(minor_colors), final_index()

result, final_nth_index_mul = access_color_map()
assert(result == final_nth_index_mul)
print("All is well (maybe!)\n")

