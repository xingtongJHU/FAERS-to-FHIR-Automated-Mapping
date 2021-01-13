import csv
import random
import time
start = time.time()

tableDe = [['primaryid', 'caseid', 'caseversion', 'i_f_code', 'event_dt', 'mfr_dt', 'init_fda_dt', 'fda_dt', 'rept_cod', 'auth_num', 'mfr_num', 'mfr_sndr', 'lit_ref', 'age', 'age_cod', 'age_grp', 'sex', 'e_sub', 'wt', 'wt_cod', 'rept_dt', 'to_mfr', 'occp_cod', 'reporter_country', 'occr_country']]
tableDr = [['primaryid', 'caseid', 'drug_seq', 'role_cod', 'drugname', 'prod_ai', 'val_vbm', 'route', 'dose_vbm', 'cum_dose_chr', 'cum_dose_unit', 'dechal', 'rechal', 'lot_num', 'exp_dt', 'nda_num', 'dose_amt', 'dose_unit', 'dose_form', 'dose_freq']]
tableOut = [['primaryid', 'caseid', 'outc_cod']]
tableRea = [['primaryid', 'caseid', 'pt', 'drug_rec_act']]
tableTher = [['primaryid', 'caseid', 'dsg_drug_seq', 'start_dt', 'end_dt', 'dur', 'dur_cod']]

for i in range(1,3):
    id = []
    with open('C:/Py/DEMO19Q'+ str(i) + '.txt','r',encoding='UTF-8')as f:
        reader = csv.reader(f,dialect='excel',delimiter='$')
        tableDEMO = list(reader)
        for j in range(50):
            r = random.choice(tableDEMO)
            
            tableDe.append(r)
            id.append(r[0])
    with open('C:/Py/DRUG19Q'+ str(i) + '.txt','r',encoding='UTF-8')as f:
        reader = csv.reader(f,dialect='excel',delimiter='$')
        tableDRUG = list(reader)
        tableDRUGid = [b[0] for b in tableDRUG]
        for j in range(50):
            for a in tableDRUGid:
                if id[j] == a:
                    tableDr.append(tableDRUG[tableDRUGid.index(a)])
                    break
    with open('C:/Py/OUTC19Q'+ str(i) + '.txt','r',encoding='UTF-8')as f:
        reader = csv.reader(f,dialect='excel',delimiter='$')
        tableOUT = list(reader)
        tableOUTid = [b[0] for b in tableOUT]
        for j in range(50):
            t = False
            for a in tableOUTid:
                if id[j] == a:
                    tableOut.append(tableOUT[tableOUTid.index(a)])
                    t = True
                    break
            if t != True:
                tableOut.append([id[j],'',''])

    with open('C:/Py/REAC19Q'+ str(i) + '.txt','r',encoding='UTF-8')as f:
        reader = csv.reader(f,dialect='excel',delimiter='$')
        tableREAC = list(reader)
        tableREACid = [b[0] for b in tableREAC]
        for j in range(50):
            for a in tableREACid:
                if id[j] == a:
                    tableRea.append(tableREAC[tableREACid.index(a)])
                    break
    with open('C:/Py/THER19Q'+ str(i) + '.txt','r',encoding='UTF-8')as f:
        reader = csv.reader(f,dialect='excel',delimiter='$')
        tableTHER = list(reader)
        tableTHERid = [b[0] for b in tableTHER]
        for j in range(50):
            t = False
            for a in tableTHERid:
                if id[j] == a:
                    tableTher.append(tableTHER[tableTHERid.index(a)])
                    t = True
                    break
            if t != True:
                tableTher.append([id[j],'','','','','',''])

print(len(tableDe))
print(len(tableDr))
print(len(tableOut))
print(len(tableRea))
print(len(tableTher))



with open('C:/Py/testDemo.txt','w',newline='')as f:
    cw = csv.writer(f,delimiter="$")
    cw.writerows(tableDe)

with open('C:/Py/testDrug.txt','w',newline='')as f:
    cw = csv.writer(f,delimiter="$")
    cw.writerows(tableDr)
    
with open('C:/Py/testOut.txt','w',newline='')as f:
    cw = csv.writer(f,delimiter="$")
    cw.writerows(tableOut)
    
with open('C:/Py/testRea.txt','w',newline='')as f:
    cw = csv.writer(f,delimiter="$")
    cw.writerows(tableRea)
    
with open('C:/Py/testTher.txt','w',newline='')as f:
    cw = csv.writer(f,delimiter="$")
    cw.writerows(tableTher)


        




