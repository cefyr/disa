#!/usr/bin/env python
# Disa is a visualisation program for braid/lace parts of knitting patterns

import re

input_string = "8r\n1r, 3a, 3r, 1a\n4r, 4a"

# Should handle number + letter(s)
stitch_dict = {"r": "-", "a": "x"}

re_digit = re.compile("\d+")



units = [[u for u in row.split(", ")] for row in input_string.split("\n")]

output_string = ""

for row in units:
    for u in row:
        repeat = re_digit.match(u).group()
        stitch = u.split(repeat)[1]
        if stitch in stitch_dict:
            output_string += int(repeat) * stitch_dict[stitch]
    output_string += "\n"

print("START\n{}END".format(output_string))
