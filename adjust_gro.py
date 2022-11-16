#!/usr/bin/python

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/start_conf.gro.original", "r")
infile2 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/glycan_5_gro.txt", "r")
outfile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/muc2_5percent_gly.gro", "w")

count_line = 0
line_num = []

for lines in infile1:
    count_line = count_line + 1
    line_num.append(count_line)
infile1.close()

max_num = max(line_num)

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/start_conf.gro.original", "r")
count_line = 0
for lines in infile1:
    count_line = count_line + 1
    if count_line <= max_num - 1:
       outfile1.writelines(lines)
infile1.close()

for lines2 in infile2:
    outfile1.writelines(lines2)

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/start_conf.gro.original", "r")
count_line = 0
for lines in infile1:
    count_line = count_line + 1
    if count_line == max_num:
       outfile1.writelines(lines)
infile1.close()
infile2.close()
outfile1.close()
