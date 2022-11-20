# compact_muc_5_gly
# compact mucin2 structure with five percent glycosylation
#To attach certain percentage of suagrs, generate their co-ordinates, definations and bonds
# attach_final_corr_newcut4.py
#there was a small bug in the bond line, to modify this, run the following program (I might later change the 
#attach_final_corr_newcut4.py program)
# rem_extra_space.py
#the dihedrals were not written using attach_final_corr_newcut4.py, so to write dihedrals the following
#program is used
# write_dihedrals.py
#To create the index file:
# make_index.py
#To modify the topology file:
# adjust_top.py (Add NB_2 line after modifying)
#To modify the co-ordinates (gro) file:
# adjust_gro.py (Modify the number of atoms line at the second topmost line)
