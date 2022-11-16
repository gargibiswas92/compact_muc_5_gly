#!/usr/bin/python
# Program to modify the topology file with 5 percent glycosylation
import sys

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_4dim.top", "r")
infile2 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/glycan_5_def.txt", "r")
infile3 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/glycan_5_bond_mod.txt", "r")
outfile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_5percent_gly.top", "w")
infile4 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_5_dihedral.txt")

count_line = 0
for lines in infile1:
    count_line = count_line + 1
    if "bonds" in lines:
       bond_line = count_line
    if "dihedrals" in lines:
       dihedral_line = count_line
    if "system" in lines:
       sys_line = count_line
print(sys_line)

infile1.close()
infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_4dim.top", "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w <= bond_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines2 in infile2:
    outfile1.writelines(lines2)
infile2.close()

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_4dim.top", "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= bond_line-1 and count_line_w <= dihedral_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines3 in infile3:
    outfile1.writelines(lines3)
infile3.close()

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_4dim.top", "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= dihedral_line-2 and count_line_w <= sys_line-2:
       outfile1.writelines(lines_w)
infile1.close()

for lines4 in infile4:
    outfile1.writelines(lines4)
infile4.close()

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_4dim.top", "r")
count_line_w = 0
for lines_w in infile1:
    count_line_w = count_line_w + 1
    if count_line_w >= sys_line-2:
       outfile1.writelines(lines_w)
infile1.close()
outfile1.close()
