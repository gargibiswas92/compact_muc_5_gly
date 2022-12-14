import sys

infile1 = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/new_attach/check2_cutoff_3/test2/glycan_5_bond_mod.txt", "r")
outfile = open("/home_b/gargi/project_muc/compact_muc2/5_percent_gly/new_attach/check2_cutoff_3/test2/muc_5percent_gly2.ndx", "w")

prot_res = []
sug_res = []
count_bond = 0

for line in infile1:
    a = line[0:5]
    b = line[8:13]
    #print(a, b)
    sug_res.append(int(a))
    prot_res.append(int(b))
    count_bond = count_bond + 1


sz1 = ["[ 1 ]", "\n"]
outfile.writelines(sz1)
count1 = 0
for j in range(1,1207):
    count1 = count1 + 1
    if count1 <= 15:
        sm1 = [str(j), " "]
        outfile.writelines(sm1)
    else:
        sm2 = ["\n"]
        outfile.writelines(sm2)
        count1 = 0
        continue

sz2 = ["\n", "[ 2 ]", "\n"]
outfile.writelines(sz2)
count2 = 0
for j in range(1207,2413):
    count2 = count2 + 1
    if count2 <= 15:
        sm3 = [str(j), " "]
        outfile.writelines(sm3)
    else:
        sm4 = ["\n"]
        outfile.writelines(sm4)
        count2 = 0
        continue

sz3 = ["\n", "[ 3 ]", "\n"]
outfile.writelines(sz3)
count3 = 0
for j in range(2413,3619):
    count3 = count3 + 1
    if count3 <= 15:
        sm5 = [str(j), " "]
        outfile.writelines(sm5)
    else:
        sm6 = ["\n"]
        outfile.writelines(sm6)
        count3 = 0
        continue

sz4 = ["\n", "[ 4 ]", "\n"]
outfile.writelines(sz4)
count4 = 0
for j in range(3619,4825):
    count4 = count4 + 1
    if count4 <= 15:
        sm7 = [str(j), " "]
        outfile.writelines(sm7)
    else:
        sm8 = ["\n"]
        outfile.writelines(sm8)
        count4 = 0
        continue

sz5 = ["\n", "[ 5 ]", "\n"]
outfile.writelines(sz5)
count5 = 0
for j in range(4825,6031):
    count5 = count5 + 1
    if count5 <= 15:
        sm9 = [str(j), " "]
        outfile.writelines(sm9)
    else:
        sm10 = ["\n"]
        outfile.writelines(sm10)
        count5 = 0
        continue    

sz6 = ["\n", "[ 6 ]", "\n"]
outfile.writelines(sz6)
count6 = 0
for j in range(6031,7237):
    count6 = count6 + 1
    if count6 <= 15:
        sm11 = [str(j), " "]
        outfile.writelines(sm11)
    else:
        sm12 = ["\n"]
        outfile.writelines(sm12)
        count6 = 0
        continue

sz7 = ["\n", "[ 7 ]", "\n"]
outfile.writelines(sz7)
count7 = 0
for j in range(7237, 8443):
    count7 = count7 + 1
    if count7 <= 15:
        sm13 = [str(j), " "]
        outfile.writelines(sm13)
    else:
        sm14 = ["\n"]
        outfile.writelines(sm14)
        count7 = 0
        continue

sz8 = ["\n", "[ 8 ]", "\n"]
outfile.writelines(sz8)
count8 = 0
for j in range(8443, 9649):
    count8 = count8 + 1
    if count8 <= 15:
        sm15 = [str(j), " "]
        outfile.writelines(sm15)
    else:
        sm16 = ["\n"]
        outfile.writelines(sm16)
        count8 = 0
        continue

sz9 = ["\n", "[ 9 ]", "\n"]
outfile.writelines(sz9)
count9 = 0
for j in range(9649, 10855):
    count9 = count9 + 1
    if count9 <= 15:
        sm17 = [str(j), " "]
        outfile.writelines(sm17)
    else:
        sm18 = ["\n"]
        outfile.writelines(sm18)
        count9 = 0
        continue

sz10 = ["\n", "[ 10 ]", "\n"]
outfile.writelines(sz10)
count10 = 0
for j in range(10855, 12061):
    count10 = count10 + 1
    if count10 <= 15:
        sm19 = [str(j), " "]
        outfile.writelines(sm19)
    else:
        sm20 = ["\n"]
        outfile.writelines(sm20)
        count10 = 0
        continue

sz11 = ["\n", "[ 11 ]", "\n"]
outfile.writelines(sz11)
count11 = 0
for j in range(12061, 13266):
    count11 = count11 + 1
    if count11 <= 15:
        sm21 = [str(j), " "]
        outfile.writelines(sm21)
    else:
        sm22 = ["\n"]
        outfile.writelines(sm22)
        count11 = 0
        continue

sz12 = ["\n", "[ 12 ]", "\n"]
outfile.writelines(sz12)
count12 = 0
for j in range(13267, 14472):
    count12 = count12 + 1
    if count12 <= 15:
        sm23 = [str(j), " "]
        outfile.writelines(sm23)
    else:
        sm24 = ["\n"]
        outfile.writelines(sm24)
        count12 = 0
        continue

sz13 = ["\n", "[ 13 ]", "\n"]
outfile.writelines(sz13)
count13 = 0
for j in range(14473, 15679):
    count13 = count13 + 1
    if count13 <= 15:
        sm25 = [str(j), " "]
        outfile.writelines(sm25)
    else:
        sm26 = ["\n"]
        outfile.writelines(sm26)
        count13 = 0
        continue

sz14 = ["\n", "[ 14 ]", "\n"]
outfile.writelines(sz14)
count14 = 0
for j in range(15679, 16885):
    count14 = count14 + 1
    if count14 <= 15:
        sm27 = [str(j), " "]
        outfile.writelines(sm27)
    else:
        sm28 = ["\n"]
        outfile.writelines(sm28)
        count14 = 0
        continue

sz15 = ["\n", "[ 15 ]", "\n"]
outfile.writelines(sz15)
count15 = 0
for j in range(16885, 19823):
    count15 = count15 + 1
    if count15 <= 15:
        sm29 = [str(j), " "]
        outfile.writelines(sm29)
    else:
        sm30 = ["\n"]
        outfile.writelines(sm30)
        count15 = 0
        continue

countt1 = 0
st1 = ["\n"]
outfile.writelines(st1)
for i in range(count_bond):
    if prot_res[i] >= 16885 and prot_res[i] <= 19822:
        countt1 = countt1 + 1
        if countt1 <= 15:
            sm31 = [str(sug_res[i]), " "]
            outfile.writelines(sm31)
        else:
            sm32 =["\n"]
            outfile.writelines(sm32)
            countt1 = 0
            continue

sz16 = ["\n", "[ 16 ]", "\n"]
outfile.writelines(sz16)
count16 = 0
for j in range(19823, 22762):
    count16 = count16 + 1
    if count16 <= 15:
        sm33 = [str(j), " "]
        outfile.writelines(sm33)
    else:
        sm34 = ["\n"]
        outfile.writelines(sm34)
        count16 = 0
        continue

countt2 = 0
st2 = ["\n"]
outfile.writelines(st2)
for i in range(count_bond):
    if prot_res[i] >= 19823 and prot_res[i] <= 22761:
        countt2 = countt2 + 1
        if countt2 <= 15:
            sm35 = [str(sug_res[i]), " "]
            outfile.writelines(sm35)
        else:
            sm36 =["\n"]
            outfile.writelines(sm36)
            countt2 = 0
            continue


sz17 = ["\n", "[ 17 ]", "\n"]
outfile.writelines(sz17)
count17 = 0
for j in range(22672, 25700):
    count17 = count17 + 1
    if count17 <= 15:
        sm37 = [str(j), " "]
        outfile.writelines(sm37)
    else:
        sm38 = ["\n"]
        outfile.writelines(sm38)
        count17 = 0
        continue

countt3 = 0
st3 = ["\n"]
outfile.writelines(st3)
for i in range(count_bond):
    if prot_res[i] >= 22762 and prot_res[i] <= 25699:
        countt3 = countt3 + 1
        if countt3 <= 15:
            sm39 = [str(sug_res[i]), " "]
            outfile.writelines(sm39)
        else:
            sm40 =["\n"]
            outfile.writelines(sm40)
            countt3 = 0
            continue

sz18 = ["\n", "[ 18 ]", "\n"]
outfile.writelines(sz18)
count18 = 0
for j in range(25700, 28639):
    count18 = count18 + 1
    if count18 <= 15:
        sm41 = [str(j), " "]
        outfile.writelines(sm41)
    else:
        sm42 = ["\n"]
        outfile.writelines(sm42)
        count18 = 0
        continue

countt4 = 0
st4 = ["\n"]
outfile.writelines(st4)
for i in range(count_bond):
    if prot_res[i] >= 25700 and prot_res[i] <= 28638:
        countt4 = countt4 + 1
        if countt4 <= 15:
            sm43 = [str(sug_res[i]), " "]
            outfile.writelines(sm43)
        else:
            sm44 =["\n"]
            outfile.writelines(sm44)
            countt4 = 0
            continue

sz19 = ["\n", "[ 19 ]", "\n"]
outfile.writelines(sz19)
count19 = 0
for j in range(28639, 31577):
    count19 = count19 + 1
    if count19 <= 15:
        sm45 = [str(j), " "]
        outfile.writelines(sm45)
    else:
        sm46 = ["\n"]
        outfile.writelines(sm46)
        count19 = 0
        continue

countt5 = 0
st5 = ["\n"]
outfile.writelines(st5)
for i in range(count_bond):
    if prot_res[i] >= 28639 and prot_res[i] <= 31576:
        countt5 = countt5 + 1
        if countt5 <= 15:
            sm47 = [str(sug_res[i]), " "]
            outfile.writelines(sm47)
        else:
            sm48 =["\n"]
            outfile.writelines(sm48)
            countt5 = 0
            continue

sz20 = ["\n", "[ 20 ]", "\n"]
outfile.writelines(sz20)
count20 = 0
for j in range(31577, 34516):
    count20 = count20 + 1
    if count20 <= 15:
        sm49 = [str(j), " "]
        outfile.writelines(sm49)
    else:
        sm50 = ["\n"]
        outfile.writelines(sm50)
        count20 = 0
        continue

countt6 = 0
st6 = ["\n"]
outfile.writelines(st6)
for i in range(count_bond):
    if prot_res[i] >= 31577 and prot_res[i] <= 34515:
        countt6 = countt6 + 1
        if countt6 <= 15:
            sm51 = [str(sug_res[i]), " "]
            outfile.writelines(sm51)
        else:
            sm52 =["\n"]
            outfile.writelines(sm52)
            countt6 = 0
            continue

sz21 = ["\n", "[ 21 ]", "\n"]
outfile.writelines(sz21)
count21 = 0
for j in range(34516, 37454):
    count21 = count21 + 1
    if count21 <= 15:
        sm53 = [str(j), " "]
        outfile.writelines(sm53)
    else:
        sm54 = ["\n"]
        outfile.writelines(sm54)
        count21 = 0
        continue

countt7 = 0
st7 = ["\n"]
outfile.writelines(st7)
for i in range(count_bond):
    if prot_res[i] >= 34516 and prot_res[i] <= 37453:
        countt7 = countt7 + 1
        if countt7 <= 15:
            sm55 = [str(sug_res[i]), " "]
            outfile.writelines(sm55)
        else:
            sm56 =["\n"]
            outfile.writelines(sm56)
            countt7 = 0
            continue


sz22 = ["\n", "[ 22 ]", "\n"]
outfile.writelines(sz22)
count22 = 0
for j in range(37454, 40393):
    count22 = count22 + 1
    if count22 <= 15:
        sm57 = [str(j), " "]
        outfile.writelines(sm57)
    else:
        sm58 = ["\n"]
        outfile.writelines(sm58)
        count22 = 0
        continue

countt8 = 0
st8 = ["\n"]
outfile.writelines(st8)
for i in range(count_bond):
    if prot_res[i] >= 37454 and prot_res[i] <= 40392:
        countt8 = countt8 + 1
        if countt8 <= 15:
            sm59 = [str(sug_res[i]), " "]
            outfile.writelines(sm59)
        else:
            sm60 =["\n"]
            outfile.writelines(sm60)
            countt8 = 0
            continue

sp_0 = ["\n", "[ body ]","\n"]
outfile.writelines(sp_0)
count1 = 0 
for j in range(1,16885):
    count1 = count1 + 1
    if count1 <= 15:
        sp_1 = [str(j), " "]
        outfile.writelines(sp_1)
    else:
        sp_2 = ["\n", str(j), " "]
        outfile.writelines(sp_2)
        count1 = 0
        continue

sp_02 = ["\n","[ tails ]","\n"]
outfile.writelines(sp_02)
countp = 0
for j in range(16885,40502):
    countp = countp + 1
    if countp <= 15:
        sp_p = [str(j), " "]
        outfile.writelines(sp_p)
    else:
        sp_pp = ["\n", str(j), " "]
        outfile.writelines(sp_pp)
        countp = 0
        continue


sp_01 = ["\n","[ system ]","\n"]
outfile.writelines(sp_01)
count11 = 0 
for j in range(1,40502):
    count11 = count11 + 1
    if count11 <= 15:
        sp_11 = [str(j), " "]
        outfile.writelines(sp_11)
    else:
        sp_21 = ["\n", str(j), " "]
        outfile.writelines(sp_21)
        count11 = 0
        continue

count_line_x = 0
ss_x = ["\n","[ tail_a1 ]", "\n"]
outfile.writelines(ss_x)
for i in range(count_bond):
    if prot_res[i] >= 20261 and prot_res[i] <= 20761:
        count_line_x = count_line_x + 1
        if count_line_x <= 15:
            ss0x = [str(sug_res[i]), " "]
            outfile.writelines(ss0x)
        else:
            ss1x =["\n"]
            outfile.writelines(ss1x)
            count_line_x = 0
            continue
ss_0 = ["\n"]
outfile.writelines(ss_0)
count_line_y = 0
for j in range(20261,20761):
    count_line_y = count_line_y + 1
    if count_line_y <= 15:
        ss0_0y = [str(j), " "]
        outfile.writelines(ss0_0y)
    else:
        ss1_0y = ["\n"]
        outfile.writelines(ss1_0y)
        count_line_y = 0
        continue

count_line = 0
ss = ["\n","[ tail_a2 ]", "\n"]
outfile.writelines(ss)
for i in range(count_bond):
    if prot_res[i] >= 20761 and prot_res[i] <= 21261:
        count_line = count_line + 1
        if count_line <= 15:
            ss0 = [str(sug_res[i]), " "]
            outfile.writelines(ss0)
        else:
            ss1 =["\n"]
            outfile.writelines(ss1)
            count_line = 0
            continue
ss_0 = ["\n"]
outfile.writelines(ss_0)
count_line = 0 
for j in range(20761,21262):
    count_line = count_line + 1
    if count_line <= 15:
        ss0_0 = [str(j), " "]
        outfile.writelines(ss0_0)
    else:
        ss1_0 = ["\n"]
        outfile.writelines(ss1_0)
        count_line = 0
        continue
    
            
count_line1 = 0
ss_a = ["\n", "\n", "[ tail_a4 ]", "\n"]
outfile.writelines(ss_a)
for i in range(count_bond):
    if prot_res[i] >= 21761 and prot_res[i] <= 22261:
        count_line1 = count_line1 + 1
        if count_line1 <= 15:
            #print(prot_res[i])
            ss2 = [str(sug_res[i]), " "]
            outfile.writelines(ss2)
        else:
            ss3 =["\n"]
            outfile.writelines(ss3)
            count_line1 = 0
            continue
ss_1 = ["\n"]
outfile.writelines(ss_1)
count_line1 = 0 
for j in range(21761,22262):
    count_line1 = count_line1 + 1
    if count_line1 <= 15:
        ss2_0 = [str(j), " "]
        outfile.writelines(ss2_0)
    else:
        ss3_0 = ["\n"]
        outfile.writelines(ss3_0)
        count_line1 = 0
        continue
            
count_line2 = 0
ss_b = ["\n", "\n", "[ tail_a5 ]", "\n"]
outfile.writelines(ss_b)
for i in range(count_bond):
    if prot_res[i] >= 22261 and prot_res[i] <= 22761:
        count_line2 = count_line2 + 1
        if count_line2 <= 15:
            #print(prot_res[i])
            ss4 = [str(sug_res[i]), " "]
            outfile.writelines(ss4)
        else:
            ss5 =["\n"]
            outfile.writelines(ss5)
            count_line2 = 0
            continue
ss_2 = ["\n"]
outfile.writelines(ss_2)
count_line2 = 0 
for j in range(22261,22762):
    count_line2 = count_line2 + 1
    if count_line2 <= 15:
        ss4_0 = [str(j), " "]
        outfile.writelines(ss4_0)
    else:
        ss5_0 = ["\n"]
        outfile.writelines(ss5_0)
        count_line2 = 0
        continue
            
count_line3 = 0
ss_c = ["\n", "\n", "[ tail_a3 ]", "\n"]
outfile.writelines(ss_c)
for i in range(count_bond):
    if prot_res[i] >= 21261 and prot_res[i] <= 21761:
        count_line3 = count_line3 + 1
        if count_line3 <= 15:
            #print(prot_res[i])
            ss6 = [str(sug_res[i]), " "]
            outfile.writelines(ss6)
        else:
            ss7 =["\n"]
            outfile.writelines(ss7)
            count_line3 = 0
            continue
ss_3 = ["\n"]
outfile.writelines(ss_3)
count_line3 = 0 
for j in range(21261,21762):
    count_line3 = count_line3 + 1
    if count_line3 <= 15:
        ss6_0 = [str(j), " "]
        outfile.writelines(ss6_0)
    else:
        ss7_0 = ["\n"]
        outfile.writelines(ss7_0)
        count_line3 = 0
        continue
            
count_line4 = 0
ss_d = ["\n", "\n", "[ tail_b1 ]", "\n"]
outfile.writelines(ss_d)
for i in range(count_bond):
    if prot_res[i] >= 26138 and prot_res[i] <= 26638:
        count_line4 = count_line4 + 1
        if count_line4 <= 15:
            #print(prot_res[i])
            ss8 = [str(sug_res[i]), " "]
            outfile.writelines(ss8)
        else:
            ss9 =["\n"]
            outfile.writelines(ss9)
            count_line4 = 0
            continue
ss_4 = ["\n"]
outfile.writelines(ss_4)
count_line4 = 0 
for j in range(26138,26639):
    count_line4 = count_line4 + 1
    if count_line4 <= 15:
        ss8_0 = [str(j), " "]
        outfile.writelines(ss8_0)
    else:
        ss9_0 = ["\n"]
        outfile.writelines(ss9_0)
        count_line4 = 0
        continue
            
count_line5 = 0
ss_e = ["\n", "\n", "[ tail_b2 ]", "\n"]
outfile.writelines(ss_e)
for i in range(count_bond):
    if prot_res[i] >= 26638 and prot_res[i] <= 27138:
        count_line5 = count_line5 + 1
        if count_line5 <= 15:
            #print(prot_res[i])
            ss10 = [str(sug_res[i]), " "]
            outfile.writelines(ss10)
        else:
            ss11 =["\n"]
            outfile.writelines(ss11)
            count_line5 = 0
            continue
ss_5 = ["\n"]
outfile.writelines(ss_5)
count_line5 = 0 
for j in range(26638,27139):
    count_line5 = count_line5 + 1
    if count_line5 <= 15:
        ss10_0 = [str(j), " "]
        outfile.writelines(ss10_0)
    else:
        ss11_0 = ["\n"]
        outfile.writelines(ss11_0)
        count_line5 = 0
        continue
            
count_line6 = 0
ss_f = ["\n", "\n", "[ tail_b3 ]", "\n"]
outfile.writelines(ss_f)
for i in range(count_bond):
    if prot_res[i] >= 27138 and prot_res[i] <= 27638:
        count_line6 = count_line6 + 1
        if count_line6 <= 15:
            #print(prot_res[i])
            ss12 = [str(sug_res[i]), " "]
            outfile.writelines(ss12)
        else:
            ss13 =["\n"]
            outfile.writelines(ss13)
            count_line6 = 0
            continue
ss_6 = ["\n"]
outfile.writelines(ss_6)
count_line6 = 0 
for j in range(27138,27639):
    count_line6 = count_line6 + 1
    if count_line6 <= 15:
        ss12_0 = [str(j), " "]
        outfile.writelines(ss12_0)
    else:
        ss13_0 = ["\n"]
        outfile.writelines(ss13_0)
        count_line6 = 0
        continue
            
count_line7 = 0
ss_g = ["\n", "\n", "[ tail_b4 ]", "\n"]
outfile.writelines(ss_g)
for i in range(count_bond):
    if prot_res[i] >= 27638 and prot_res[i] <= 28138:
        count_line7 = count_line7 + 1
        if count_line7 <= 15:
            #print(prot_res[i])
            ss14 = [str(sug_res[i]), " "]
            outfile.writelines(ss14)
        else:
            ss15 =["\n"]
            outfile.writelines(ss15)
            count_line7 = 0
            continue
ss_7 = ["\n"]
outfile.writelines(ss_7)
count_line7 = 0 
for j in range(27638,28139):
    count_line7 = count_line7 + 1
    if count_line7 <= 15:
        ss14_0 = [str(j), " "]
        outfile.writelines(ss14_0)
    else:
        ss15_0 = ["\n"]
        outfile.writelines(ss15_0)
        count_line7 = 0
        continue
count_line8 = 0
ss_h = ["\n", "\n", "[ tail_b5 ]", "\n"]
outfile.writelines(ss_h)
for i in range(count_bond):
    if prot_res[i] >= 28138 and prot_res[i] <= 28638:
        count_line8 = count_line8 + 1
        if count_line8 <= 15:
            #print(prot_res[i])
            ss16 = [str(sug_res[i]), " "]
            outfile.writelines(ss16)
        else:
            ss17 =["\n"]
            outfile.writelines(ss17)
            count_line8 = 0
            continue
ss_8 = ["\n"]
outfile.writelines(ss_8)
count_line8 = 0 
for j in range(28138,28639):
    count_line8 = count_line8 + 1
    if count_line8 <= 15:
        ss16_0 = [str(j), " "]
        outfile.writelines(ss16_0)
    else:
        ss17_0 = ["\n"]
        outfile.writelines(ss17_0)
        count_line8 = 0
        continue
            
count_line9 = 0
ss_i = ["\n", "\n", "[ tail_c1 ]", "\n"]
outfile.writelines(ss_i)
for i in range(count_bond):
    if prot_res[i] >= 32015 and prot_res[i] <= 32515:
        count_line9 = count_line9 + 1
        if count_line9 <= 15:
            #print(prot_res[i])
            ss18 = [str(sug_res[i]), " "]
            outfile.writelines(ss18)
        else:
            ss19 =["\n"]
            outfile.writelines(ss19)
            count_line9 = 0
            continue
ss_9 = ["\n"]
outfile.writelines(ss_8)
count_line9 = 0 
for j in range(32015,32516):
    count_line9 = count_line9 + 1
    if count_line9 <= 15:
        ss18_0 = [str(j), " "]
        outfile.writelines(ss18_0)
    else:
        ss19_0 = ["\n"]
        outfile.writelines(ss19_0)
        count_line9 = 0
        continue
            
count_line10 = 0
ss_j = ["\n", "\n", "[ tail_c2 ]", "\n"]
outfile.writelines(ss_j)
for i in range(count_bond):
    if prot_res[i] >= 32515 and prot_res[i] <= 33015:
        count_line10 = count_line10 + 1
        if count_line10 <= 15:
            #print(prot_res[i])
            ss20 = [str(sug_res[i]), " "]
            outfile.writelines(ss20)
        else:
            ss21 =["\n"]
            outfile.writelines(ss21)
            count_line10 = 0
            continue
ss_10 = ["\n"]
outfile.writelines(ss_10)
count_line10 = 0 
for j in range(32515,33016):
    count_line10 = count_line10 + 1
    if count_line10 <= 15:
        ss20_0 = [str(j), " "]
        outfile.writelines(ss20_0)
    else:
        ss21_0 = ["\n"]
        outfile.writelines(ss21_0)
        count_line10 = 0
        continue
            
count_line11 = 0
ss_k = ["\n", "\n", "[ tail_c3 ]", "\n"]
outfile.writelines(ss_k)
for i in range(count_bond):
    if prot_res[i] >= 33015 and prot_res[i] <= 33515:
        count_line11 = count_line11 + 1
        if count_line11 <= 15:
            #print(prot_res[i])
            ss22 = [str(sug_res[i]), " "]
            outfile.writelines(ss22)
        else:
            ss23 =["\n"]
            outfile.writelines(ss23)
            count_line11 = 0
            continue
ss_11 = ["\n"]
outfile.writelines(ss_11)
count_line11 = 0 
for j in range(33015,33516):
    count_line11 = count_line11 + 1
    if count_line11 <= 15:
        ss22_0 = [str(j), " "]
        outfile.writelines(ss22_0)
    else:
        ss23_0 = ["\n"]
        outfile.writelines(ss23_0)
        count_line11 = 0
        continue
            
count_line12 = 0
ss_l = ["\n", "\n", "[ tail_c4 ]", "\n"]
outfile.writelines(ss_l)
for i in range(count_bond):
    if prot_res[i] >= 33515 and prot_res[i] <= 34015:
        count_line12 = count_line12 + 1
        if count_line12 <= 15:
            #print(prot_res[i])
            ss24 = [str(sug_res[i]), " "]
            outfile.writelines(ss24)
        else:
            ss25 =["\n"]
            outfile.writelines(ss25)
            count_line12 = 0
            continue
ss_12 = ["\n"]
outfile.writelines(ss_12)
count_line12 = 0 
for j in range(33515,34016):
    count_line12 = count_line12 + 1
    if count_line12 <= 15:
        ss24_0 = [str(j), " "]
        outfile.writelines(ss24_0)
    else:
        ss25_0 = ["\n"]
        outfile.writelines(ss25_0)
        count_line12 = 0
        continue
count_line13 = 0
ss_m = ["\n", "\n", "[ tail_c5 ]", "\n"]
outfile.writelines(ss_m)
for i in range(count_bond):
    if prot_res[i] >= 34015 and prot_res[i] <= 34515:
        count_line13 = count_line13 + 1
        if count_line13 <= 15:
            #print(prot_res[i])
            ss26 = [str(sug_res[i]), " "]
            outfile.writelines(ss26)
        else:
            ss27 =["\n"]
            outfile.writelines(ss27)
            count_line13 = 0
            continue
ss_13 = ["\n"]
outfile.writelines(ss_13)
count_line13 = 0 
for j in range(34015,34516):
    count_line13 = count_line13 + 1
    if count_line13 <= 15:
        ss26_0 = [str(j), " "]
        outfile.writelines(ss26_0)
    else:
        ss27_0 = ["\n"]
        outfile.writelines(ss27_0)
        count_line13 = 0
        continue
            
count_line14 = 0
ss_n = ["\n", "\n", "[ tail_d1 ]", "\n"]
outfile.writelines(ss_n)
for i in range(count_bond):
    if prot_res[i] >= 37892 and prot_res[i] <= 38392:
        count_line14 = count_line14 + 1
        if count_line14 <= 15:
            #print(prot_res[i])
            ss28 = [str(sug_res[i]), " "]
            outfile.writelines(ss28)
        else:
            ss29 =["\n"]
            outfile.writelines(ss29)
            count_line14 = 0
            continue
ss_14 = ["\n"]
outfile.writelines(ss_14)
count_line14 = 0 
for j in range(37892,38393):
    count_line14 = count_line14 + 1
    if count_line14 <= 15:
        ss28_0 = [str(j), " "]
        outfile.writelines(ss28_0)
    else:
        ss29_0 = ["\n"]
        outfile.writelines(ss29_0)
        count_line14 = 0
        continue
            
count_line15 = 0
ss_o = ["\n", "\n", "[ tail_d2 ]", "\n"]
outfile.writelines(ss_o)
for i in range(count_bond):
    if prot_res[i] >= 38392 and prot_res[i] <= 38892:
        count_line15 = count_line15 + 1
        if count_line15 <= 15:
            #print(prot_res[i])
            ss30 = [str(sug_res[i]), " "]
            outfile.writelines(ss30)
        else:
            ss31 =["\n"]
            outfile.writelines(ss31)
            count_line15 = 0
            continue
ss_15 = ["\n"]
outfile.writelines(ss_15)
count_line15 = 0 
for j in range(38392,38893):
    count_line15 = count_line15 + 1
    if count_line15 <= 15:
        ss30_0 = [str(j), " "]
        outfile.writelines(ss30_0)
    else:
        ss31_0 = ["\n"]
        outfile.writelines(ss31_0)
        count_line15 = 0
        continue
            
count_line16 = 0
ss_p = ["\n", "\n", "[ tail_d3 ]", "\n"]
outfile.writelines(ss_p)
for i in range(count_bond):
    if prot_res[i] >= 38892 and prot_res[i] <= 39392:
        count_line16 = count_line16 + 1
        if count_line16 <= 15:
            #print(prot_res[i])
            ss32 = [str(sug_res[i]), " "]
            outfile.writelines(ss32)
        else:
            ss33 =["\n"]
            outfile.writelines(ss33)
            count_line16 = 0
            continue
ss_16 = ["\n"]
outfile.writelines(ss_16)
count_line16 = 0 
for j in range(38892,39393):
    count_line16 = count_line16 + 1
    if count_line16 <= 15:
        ss32_0 = [str(j), " "]
        outfile.writelines(ss32_0)
    else:
        ss33_0 = ["\n"]
        outfile.writelines(ss33_0)
        count_line16 = 0
        continue
            
count_line17 = 0
ss_q = ["\n", "\n", "[ tail_d4 ]", "\n"]
outfile.writelines(ss_q)
for i in range(count_bond):
    if prot_res[i] >= 39392 and prot_res[i] <= 39892:
        count_line17 = count_line17 + 1
        if count_line17 <= 15:
            #print(prot_res[i])
            ss34 = [str(sug_res[i]), " "]
            outfile.writelines(ss34)
        else:
            ss35 =["\n"]
            outfile.writelines(ss35)
            count_line17 = 0
            continue
ss_17 = ["\n"]
outfile.writelines(ss_17)
count_line17 = 0 
for j in range(39392,39893):
    count_line17 = count_line17 + 1
    if count_line17 <= 15:
        ss34_0 = [str(j), " "]
        outfile.writelines(ss34_0)
    else:
        ss35_0 = ["\n"]
        outfile.writelines(ss35_0)
        count_line17 = 0
        continue
            
count_line18 = 0
ss_r = ["\n", "\n", "[ tail_d5 ]", "\n"]
outfile.writelines(ss_r)
for i in range(count_bond):
    if prot_res[i] >= 39892 and prot_res[i] <= 40392:
        count_line18 = count_line18 + 1
        if count_line18 <= 15:
            #print(prot_res[i])
            ss36 = [str(sug_res[i]), " "]
            outfile.writelines(ss36)
        else:
            ss37 =["\n"]
            outfile.writelines(ss37)
            count_line18 = 0
            continue
ss_18 = ["\n"]
outfile.writelines(ss_18)
count_line18 = 0 
for j in range(39892,40393):
    count_line18 = count_line18 + 1
    if count_line18 <= 15:
        ss36_0 = [str(j), " "]
        outfile.writelines(ss36_0)
    else:
        ss37_0 = ["\n"]
        outfile.writelines(ss37_0)
        count_line18 = 0
        continue
            
count_line19 = 0
ss_s = ["\n", "\n", "[ tail_aa1 ]", "\n"]
outfile.writelines(ss_s)
for i in range(count_bond):
    if prot_res[i] >= 17322 and prot_res[i] <= 17822:
        count_line19 = count_line19 + 1
        if count_line19 <= 15:
            #print(prot_res[i])
            ss38 = [str(sug_res[i]), " "]
            outfile.writelines(ss38)
        else:
            ss39 =["\n"]
            outfile.writelines(ss39)
            count_line19 = 0
            continue
ss_19 = ["\n"]
outfile.writelines(ss_19)
count_line19 = 0 
for j in range(17322,17823):
    count_line19 = count_line19 + 1
    if count_line19 <= 15:
        ss38_0 = [str(j), " "]
        outfile.writelines(ss38_0)
    else:
        ss39_0 = ["\n"]
        outfile.writelines(ss39_0)
        count_line19 = 0
        continue
            
count_line20 = 0
ss_t = ["\n", "\n", "[ tail_aa2 ]", "\n"]
outfile.writelines(ss_t)
for i in range(count_bond):
    if prot_res[i] >= 17822 and prot_res[i] <= 18322:
        count_line20 = count_line20 + 1
        if count_line20 <= 15:
            #print(prot_res[i])
            ss40 = [str(sug_res[i]), " "]
            outfile.writelines(ss40)
        else:
            ss41 =["\n"]
            outfile.writelines(ss41)
            count_line20 = 0
            continue
ss_20 = ["\n"]
outfile.writelines(ss_20)
count_line20 = 0 
for j in range(17822,18323):
    count_line20 = count_line20 + 1
    if count_line20 <= 15:
        ss40_0 = [str(j), " "]
        outfile.writelines(ss40_0)
    else:
        ss41_0 = ["\n"]
        outfile.writelines(ss41_0)
        count_line20 = 0
        continue
            
count_line21 = 0
ss_u = ["\n", "\n", "[ tail_aa3 ]", "\n"]
outfile.writelines(ss_u)
for i in range(count_bond):
    if prot_res[i] >= 18322 and prot_res[i] <= 18822:
        count_line21 = count_line21 + 1
        if count_line21 <= 15:
            #print(prot_res[i])
            ss42 = [str(sug_res[i]), " "]
            outfile.writelines(ss42)
        else:
            ss43 =["\n"]
            outfile.writelines(ss43)
            count_line21 = 0
            continue
ss_21 = ["\n"]
outfile.writelines(ss_21)
count_line21 = 0 
for j in range(18322,18823):
    count_line21 = count_line21 + 1
    if count_line21 <= 15:
        ss42_0 = [str(j), " "]
        outfile.writelines(ss42_0)
    else:
        ss43_0 = ["\n"]
        outfile.writelines(ss43_0)
        count_line21 = 0
        continue
            
count_line22 = 0
ss_v = ["\n", "\n", "[ tail_aa4 ]", "\n"]
outfile.writelines(ss_v)
for i in range(count_bond):
    if prot_res[i] >= 18822 and prot_res[i] <= 19322:
        count_line22 = count_line22 + 1
        if count_line22 <= 15:
            #print(prot_res[i])
            ss44 = [str(sug_res[i]), " "]
            outfile.writelines(ss44)
        else:
            ss45 =["\n"]
            outfile.writelines(ss45)
            count_line22 = 0
            continue
ss_22 = ["\n"]
outfile.writelines(ss_22)
count_line22 = 0 
for j in range(18822,19323):
    count_line22 = count_line22 + 1
    if count_line22 <= 15:
        ss44_0 = [str(j), " "]
        outfile.writelines(ss44_0)
    else:
        ss45_0 = ["\n"]
        outfile.writelines(ss45_0)
        count_line22 = 0
        continue
            
count_line23 = 0
ss_w = ["\n", "\n", "[ tail_aa5 ]", "\n"]
outfile.writelines(ss_w)
for i in range(count_bond):
    if prot_res[i] >= 19322 and prot_res[i] <= 19822:
        count_line23 = count_line23 + 1
        if count_line23 <= 15:
            #print(prot_res[i])
            ss46 = [str(sug_res[i]), " "]
            outfile.writelines(ss46)
        else:
            ss47 =["\n"]
            outfile.writelines(ss47)
            count_line23 = 0
            continue
ss_23 = ["\n"]
outfile.writelines(ss_23)
count_line23 = 0 
for j in range(19322,19823):
    count_line23 = count_line23 + 1
    if count_line23 <= 15:
        ss46_0 = [str(j), " "]
        outfile.writelines(ss46_0)
    else:
        ss47_0 = ["\n"]
        outfile.writelines(ss47_0)
        count_line23 = 0
        continue
            
count_line24 = 0
ss_x = ["\n", "\n", "[ tail_bb1 ]", "\n"]
outfile.writelines(ss_x)
for i in range(count_bond):
    if prot_res[i] >= 23199 and prot_res[i] <= 23699:
        count_line24 = count_line24 + 1
        if count_line24 <= 15:
            #print(prot_res[i])
            ss48 = [str(sug_res[i]), " "]
            outfile.writelines(ss48)
        else:
            ss49 =["\n"]
            outfile.writelines(ss49)
            count_line24 = 0
            continue
ss_24 = ["\n"]
outfile.writelines(ss_24)
count_line24 = 0 
for j in range(23199,23700):
    count_line24 = count_line24 + 1
    if count_line24 <= 15:
        ss48_0 = [str(j), " "]
        outfile.writelines(ss48_0)
    else:
        ss49_0 = ["\n"]
        outfile.writelines(ss49_0)
        count_line24 = 0
        continue

count_line25 = 0
ss_y = ["\n", "\n", "[ tail_bb2 ]", "\n"]
outfile.writelines(ss_y)
for i in range(count_bond):
    if prot_res[i] >= 23699 and prot_res[i] <= 24199:
        count_line25 = count_line25 + 1
        if count_line25 <= 15:
            #print(prot_res[i])
            ss50 = [str(sug_res[i]), " "]
            outfile.writelines(ss50)
        else:
            ss51 =["\n"]
            outfile.writelines(ss51)
            count_line25 = 0
            continue
ss_25 = ["\n"]
outfile.writelines(ss_25)
count_line25 = 0 
for j in range(23699,24200):
    count_line25 = count_line25 + 1
    if count_line25 <= 15:
        ss50_0 = [str(j), " "]
        outfile.writelines(ss50_0)
    else:
        ss51_0 = ["\n"]
        outfile.writelines(ss51_0)
        count_line25 = 0
        continue
            
count_line26 = 0
ss_z = ["\n", "\n", "[ tail_bb3 ]", "\n"]
outfile.writelines(ss_z)
for i in range(count_bond):
    if prot_res[i] >= 24199 and prot_res[i] <= 24699:
        count_line26 = count_line26 + 1
        if count_line26 <= 15:
            #print(prot_res[i])
            ss52 = [str(sug_res[i]), " "]
            outfile.writelines(ss52)
        else:
            ss53 =["\n"]
            outfile.writelines(ss53)
            count_line26 = 0
            continue
ss_26 = ["\n"]
outfile.writelines(ss_26)
count_line26 = 0 
for j in range(24199,24700):
    count_line26 = count_line26 + 1
    if count_line26 <= 15:
        ss52_0 = [str(j), " "]
        outfile.writelines(ss52_0)
    else:
        ss53_0 = ["\n"]
        outfile.writelines(ss53_0)
        count_line26 = 0
        continue
            
count_line27 = 0
ss_aa = ["\n", "\n", "[ tail_bb4 ]", "\n"]
outfile.writelines(ss_aa)
for i in range(count_bond):
    if prot_res[i] >= 24699 and prot_res[i] <= 25199:
        count_line27 = count_line27 + 1
        if count_line27 <= 15:
            #print(prot_res[i])
            ss54 = [str(sug_res[i]), " "]
            outfile.writelines(ss54)
        else:
            ss55 =["\n"]
            outfile.writelines(ss55)
            count_line27 = 0
            continue
ss_27 = ["\n"]
outfile.writelines(ss_27)
count_line27 = 0 
for j in range(24699,25200):
    count_line27 = count_line27 + 1
    if count_line27 <= 15:
        ss54_0 = [str(j), " "]
        outfile.writelines(ss54_0)
    else:
        ss55_0 = ["\n"]
        outfile.writelines(ss55_0)
        count_line27 = 0
        continue
            
count_line28 = 0
ss_bb = ["\n", "\n", "[ tail_bb5 ]", "\n"]
outfile.writelines(ss_bb)
for i in range(count_bond):
    if prot_res[i] >= 25199 and prot_res[i] <= 25699:
        count_line28 = count_line28 + 1
        if count_line28 <= 15:
            #print(prot_res[i])
            ss56 = [str(sug_res[i]), " "]
            outfile.writelines(ss56)
        else:
            ss57 =["\n"]
            outfile.writelines(ss57)
            count_line28 = 0
            continue
ss_28 = ["\n"]
outfile.writelines(ss_28)
count_line28 = 0 
for j in range(25199,25700):
    count_line28 = count_line28 + 1
    if count_line28 <= 15:
        ss56_0 = [str(j), " "]
        outfile.writelines(ss56_0)
    else:
        ss57_0 = ["\n"]
        outfile.writelines(ss57_0)
        count_line28 = 0
        continue
            
count_line29 = 0
ss_cc = ["\n", "\n", "[ tail_cc1 ]", "\n"]
outfile.writelines(ss_cc)
for i in range(count_bond):
    if prot_res[i] >= 29076 and prot_res[i] <= 29576:
        count_line29 = count_line29 + 1
        if count_line29 <= 15:
            #print(prot_res[i])
            ss58 = [str(sug_res[i]), " "]
            outfile.writelines(ss58)
        else:
            ss59 =["\n"]
            outfile.writelines(ss59)
            count_line29 = 0
            continue
ss_29 = ["\n"]
outfile.writelines(ss_29)
count_line29 = 0 
for j in range(29076,29577):
    count_line29 = count_line29 + 1
    if count_line29 <= 15:
        ss58_0 = [str(j), " "]
        outfile.writelines(ss58_0)
    else:
        ss59_0 = ["\n"]
        outfile.writelines(ss59_0)
        count_line29 = 0
        continue
            
count_line30 = 0
ss_dd = ["\n", "\n", "[ tail_cc2 ]", "\n"]
outfile.writelines(ss_dd)
for i in range(count_bond):
    if prot_res[i] >= 29576 and prot_res[i] <= 30076:
        count_line30 = count_line30 + 1
        if count_line30 <= 15:
            #print(prot_res[i])
            ss60 = [str(sug_res[i]), " "]
            outfile.writelines(ss60)
        else:
            ss61 =["\n"]
            outfile.writelines(ss61)
            count_line30 = 0
            continue
ss_30 = ["\n"]
outfile.writelines(ss_30)
count_line30 = 0 
for j in range(29576,30077):
    count_line30 = count_line30 + 1
    if count_line30 <= 15:
        ss60_0 = [str(j), " "]
        outfile.writelines(ss60_0)
    else:
        ss61_0 = ["\n"]
        outfile.writelines(ss61_0)
        count_line30 = 0
        continue
            
count_line31 = 0
ss_ee = ["\n", "\n", "[ tail_cc3 ]", "\n"]
outfile.writelines(ss_ee)
for i in range(count_bond):
    if prot_res[i] >= 30076 and prot_res[i] <= 30576:
        count_line31 = count_line31 + 1
        if count_line31 <= 15:
            #print(prot_res[i])
            ss62 = [str(sug_res[i]), " "]
            outfile.writelines(ss62)
        else:
            ss63 =["\n"]
            outfile.writelines(ss63)
            count_line31 = 0
            continue

ss_31 = ["\n"]
outfile.writelines(ss_31)
count_line31 = 0 
for j in range(30076,30577):
    count_line31 = count_line31 + 1
    if count_line31 <= 15:
        ss62_0 = [str(j), " "]
        outfile.writelines(ss62_0)
    else:
        ss63_0 = ["\n"]
        outfile.writelines(ss63_0)
        count_line31 = 0
        continue
            
count_line32 = 0
ss_ff = ["\n", "\n", "[ tail_cc4 ] ", "\n"]
outfile.writelines(ss_ff)
for i in range(count_bond):
    if prot_res[i] >= 30576 and prot_res[i] <= 31076:
        count_line32 = count_line32 + 1
        if count_line32 <= 15:
            #print(prot_res[i])
            ss64 = [str(sug_res[i]), " "]
            outfile.writelines(ss64)
        else:
            ss65 =["\n"]
            outfile.writelines(ss65)
            count_line32 = 0
            continue
ss_32 = ["\n"]
outfile.writelines(ss_32)
count_line32 = 0 
for j in range(30576,31077):
    count_line32 = count_line32 + 1
    if count_line32 <= 15:
        ss64_0 = [str(j), " "]
        outfile.writelines(ss64_0)
    else:
        ss65_0 = ["\n"]
        outfile.writelines(ss65_0)
        count_line32 = 0
        continue
            
count_line33 = 0
ss_gg = ["\n", "\n", "[ tail_cc5 ]", "\n"]
outfile.writelines(ss_gg)
for i in range(count_bond):
    if prot_res[i] >= 31076 and prot_res[i] <= 31576:
        count_line33 = count_line33 + 1
        if count_line33 <= 15:
            #print(prot_res[i])
            ss66 = [str(sug_res[i]), " "]
            outfile.writelines(ss66)
        else:
            ss67 =["\n"]
            outfile.writelines(ss67)
            count_line33 = 0
            continue
ss_33 = ["\n"]
outfile.writelines(ss_33)
count_line33 = 0 
for j in range(31076,31577):
    count_line33 = count_line33 + 1
    if count_line33 <= 15:
        ss66_0 = [str(j), " "]
        outfile.writelines(ss66_0)
    else:
        ss67_0 = ["\n"]
        outfile.writelines(ss67_0)
        count_line33 = 0
        continue
            
count_line34 = 0
ss_hh = ["\n", "\n", "[ tail_dd1 ]", "\n"]
outfile.writelines(ss_hh)
for i in range(count_bond):
    if prot_res[i] >= 34953 and prot_res[i] <= 35453:
        count_line34 = count_line34 + 1
        if count_line34 <= 15:
            #print(prot_res[i])
            ss68 = [str(sug_res[i]), " "]
            outfile.writelines(ss68)
        else:
            ss69 =["\n"]
            outfile.writelines(ss69)
            count_line34 = 0
            continue
ss_34 = ["\n"]
outfile.writelines(ss_34)
count_line34 = 0 
for j in range(34953,35454):
    count_line34 = count_line34 + 1
    if count_line34 <= 15:
        ss68_0 = [str(j), " "]
        outfile.writelines(ss68_0)
    else:
        ss69_0 = ["\n"]
        outfile.writelines(ss69_0)
        count_line34 = 0
        continue
            
count_line35 = 0
ss_ii = ["\n", "\n", "[ tail_dd2 ]", "\n"]
outfile.writelines(ss_ii)
for i in range(count_bond):
    if prot_res[i] >= 35453 and prot_res[i] <= 35953:
        count_line35 = count_line35 + 1
        if count_line35 <= 15:
            #print(prot_res[i])
            ss70 = [str(sug_res[i]), " "]
            outfile.writelines(ss70)
        else:
            ss71 =["\n"]
            outfile.writelines(ss71)
            count_line35 = 0
            continue
ss_35 = ["\n"]
outfile.writelines(ss_35)
count_line35 = 0 
for j in range(35453,35954):
    count_line35 = count_line35 + 1
    if count_line35 <= 15:
        ss70_0 = [str(j), " "]
        outfile.writelines(ss70_0)
    else:
        ss71_0 = ["\n"]
        outfile.writelines(ss71_0)
        count_line35 = 0
        continue
            
count_line36 = 0
ss_jj = ["\n", "\n", "[ tail_dd3 ]", "\n"]
outfile.writelines(ss_jj)
for i in range(count_bond):
    if prot_res[i] >= 35953 and prot_res[i] <= 36453:
        count_line36 = count_line36 + 1
        if count_line36 <= 15:
            #print(prot_res[i])
            ss72 = [str(sug_res[i]), " "]
            outfile.writelines(ss72)
        else:
            ss73 =["\n"]
            outfile.writelines(ss73)
            count_line36 = 0
            continue
ss_36 = ["\n"]
outfile.writelines(ss_36)
count_line36 = 0 
for j in range(35953,36454):
    count_line36 = count_line36 + 1
    if count_line36 <= 15:
        ss72_0 = [str(j), " "]
        outfile.writelines(ss72_0)
    else:
        ss73_0 = ["\n"]
        outfile.writelines(ss73_0)
        count_line36 = 0
        continue
            
count_line37 = 0
ss_kk = ["\n", "\n", "[ tail_dd4 ]", "\n"]
outfile.writelines(ss_kk)
for i in range(count_bond):
    if prot_res[i] >= 36453 and prot_res[i] <= 36953:
        count_line37 = count_line37 + 1
        if count_line37 <= 15:
            #print(prot_res[i])
            ss74 = [str(sug_res[i]), " "]
            outfile.writelines(ss74)
        else:
            ss75 =["\n"]
            outfile.writelines(ss75)
            count_line37 = 0
            continue
ss_37 = ["\n"]
outfile.writelines(ss_37)
count_line37 = 0 
for j in range(36453,36954):
    count_line37 = count_line37 + 1
    if count_line37 <= 15:
        ss74_0 = [str(j), " "]
        outfile.writelines(ss74_0)
    else:
        ss75_0 = ["\n"]
        outfile.writelines(ss75_0)
        count_line37 = 0
        continue
            
count_line38 = 0
ss_ll = ["\n", "\n", "[ tail_dd5 ]", "\n"]
outfile.writelines(ss_ll)
for i in range(count_bond):
    if prot_res[i] >= 36953 and prot_res[i] <= 37453:
        count_line38 = count_line38 + 1
        if count_line38 <= 15:
            #print(prot_res[i])
            ss76 = [str(sug_res[i]), " "]
            outfile.writelines(ss76)
        else:
            ss77 =["\n"]
            outfile.writelines(ss77)
            count_line38 = 0
            continue
ss_38 = ["\n"]
outfile.writelines(ss_38)
count_line38 = 0 
for j in range(36953,37454):
    count_line38 = count_line38 + 1
    if count_line38 <= 15:
        ss76_0 = [str(j), " "]
        outfile.writelines(ss76_0)
    else:
        ss77_0 = ["\n"]
        outfile.writelines(ss77_0)
        count_line38 = 0
        continue
infile1.close()
outfile.close()
