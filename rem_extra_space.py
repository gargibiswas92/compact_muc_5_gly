#!/usr/bin/python

import sys

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/new_attach/check2_cutoff_3/test2/glycan_5_bond4.txt", "r")
outfile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/new_attach/check2_cutoff_3/test2/glycan_5_bond_mod.txt", "w")

for line in infile1:
    a = line[0:1]
    b = line[1:-1]
    ss = [b, "\n"]
    outfile1.writelines(ss)
    
infile1.close()
outfile1.close()
