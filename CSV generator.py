import csv
import time
start = time.time()

with open('C:/Py/testDemo.txt','r')as f:
    reader = csv.reader(f,dialect='excel',delimiter='$')
    tableDe = list(reader)
    
with open('C:/Py/testDrug.txt','r')as f:
    reader = csv.reader(f,dialect='excel',delimiter='$')
    tableDr = list(reader)

with open('C:/Py/testOut.txt','r')as f:
    reader = csv.reader(f,dialect='excel',delimiter='$')
    tableOut = list(reader)

with open('C:/Py/testRea.txt','r')as f:
    reader = csv.reader(f,dialect='excel',delimiter='$')
    tableRea = list(reader)

with open('C:/Py/testTher.txt','r')as f:
    reader = csv.reader(f,dialect='excel',delimiter='$')
    tableTher = list(reader)


def convDate(temp):
    date = temp[0:4] + '-' + temp[4:6] + '-' + temp[6:8]
    return date

def convSerious(temp):
    if temp == 'DE':
        return 'SeriousResultsInDeath'
    elif temp == 'LT':
        return 'SeriousIsLifeThreatening'
    elif temp == 'HO':
        return 'SeriousResultsInHospitalization'
    elif temp == 'DS':
        return 'SeriousResultsInDisability'
    elif temp == 'CA':
        return 'SeriousIsBirthDefect'
    elif temp == 'RI':
        return 'SeriousRequiresPreventImpairment'
    elif temp == 'OT':
        return 'Serious'
    else:
        return ''
def textSerious(t):
    if t == 'SeriousResultsInDeath':
        return 'Results in death.'
    elif t == 'SeriousIsLifeThreatening':
        return 'Is Life-threatening.'
    elif t == 'SeriousResultsInHospitalization':
        return 'Requires inpatient hospitalization or causes prolongation of existing hospitalization.'
    elif t == 'SeriousResultsInDisability':
        return 'Results in persistent or significant disability/incapacity.'
    elif t == 'SeriousIsBirthDefect':
        return 'Is a congenital anomaly/birth defect.'
    elif t == 'SeriousRequiresPreventImpairment':
        return 'Requires intervention to prevent permanent impairment or damage (i.e., an important medical event that requires medical judgement).'
    elif t == 'Serious':
        return 'Serious.'
    else:
        return ''

def convSex(temp):
    if temp == 'F':
        return 'female'
    elif temp == 'M':
        return 'male'
    elif temp == 'UNK':
        return 'unknown'
    else:
        return ''




frame = [['identifier',
           'actuality',
           'category',
           'event',
           'subject.patient.sex',
           'subject.patient.age',
           'encouter',
           'dateTime',
           'detected',
           'recordDate',
           'resultingCondition',
           'location',
           'seriousness',
           'severity',
           'outcome',
           'recorder',
           'contributer',
           'suspectEntity',
           'instance.Medication.code',
           'instance.Medication.identifier',
           'instance.Medication.isActive',
           'instance.Medication.lotNumber',
           'instance.Medication.expirationDate',
           'instance.MedicationAdministration.dosage',
           'instance.MedicationAdministration.dosage.dose',
           'instance.MedicationStatement.effective[x].start',
           'instance.MedicationStatement.effective[x].end',
           'causality',
           'assessment',
           'productRelatedness',
           'author',
           'method',
           'subjectMedicalHistory',
           'referenceDocument',
           'study'
           ]]

def write(id):
    c = [tableDe[[row[0] for row in tableDe].index(id)][0],
         'actual',
         '',
         tableRea[[row[0] for row in tableRea].index(id)][2],
         convSex(tableDe[[row[0] for row in tableDe].index(id)][16]),
         tableDe[[row[0] for row in tableDe].index(id)][13],
         '',
         convDate(tableDe[[row[0] for row in tableDe].index(id)][4]),
         '',
         convDate(tableDe[[row[0] for row in tableDe].index(id)][6]) ,
         '',
         tableDe[[row[0] for row in tableDe].index(id)][24],
         convSerious(tableOut[[row[0] for row in tableOut].index(id)][2]),
         '',
         '',
         '',
         '',
         '',
         tableDr[[row[0] for row in tableDr].index(id)][2],
         tableDr[[row[0] for row in tableDr].index(id)][4],
         tableDr[[row[0] for row in tableDr].index(id)][5],
         tableDr[[row[0] for row in tableDr].index(id)][13],
         tableDr[[row[0] for row in tableDr].index(id)][14],
         tableDr[[row[0] for row in tableDr].index(id)][8],
         tableDr[[row[0] for row in tableDr].index(id)][17],
         tableTher[[row[0] for row in tableTher].index(id)][3],
         tableTher[[row[0] for row in tableTher].index(id)][4],
         '',
         '',
         '',
         '',
         '',
         '',
         tableDr[[row[0] for row in tableDr].index(id)][12],
         '']
    frame.append(c)


temp = [b[0] for b in tableDe]

for i in range(1,len(temp)):
    write(temp[i])

with open("C:/Py/result/toltal result.csv",'w',newline='')as f:
    cw = csv.writer(f)
    cw.writerows(frame)
    
print("--- %s seconds ---" % (time.time() - start))
