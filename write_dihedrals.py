#!/usr/bin/python

import sys
infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/glycan_5_bond_mod.txt", "r")
outfile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_5_dihedral.txt", "w")
prot_res = []
sug_res = []
count_bond = 0

for line in infile1:
    a = line[0:5]
    b = line[8:13]
    sug_res.append(int(a))
    prot_res.append(int(b))
    count_bond = count_bond + 1
    
for i in range(count_bond):
    ss1 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        1.089800000e+03 1.000000000e+00 1{}'.format(sug_res[i], prot_res[i], prot_res[i]-1, prot_res[i]-2, "\n")
    ss2 = '{:>5d}   {:>5d}   {:>5d}   {:>5d}   1        3.269400000e+03 5.000000000e-01 3{}'.format(sug_res[i], prot_res[i], prot_res[i]-1, prot_res[i]-2, "\n")
    outfile1.writelines(ss1)
    outfile1.writelines(ss2)
    
infile1.close()
outfile1.close()
