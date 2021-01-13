import json
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

def write(id):
    identifier = { 'type':'Business Identifier',
                   'value':'<'+ tableDe[[row[0] for row in tableDe].index(id)][0] +'>'}
    actuality = '<'+'actual'+'>'
    category = [{}]
    event ={'coding':[{'system':'https://www.meddra.org/', 'text':'<'+ tableRea[[row[0] for row in tableRea].index(id)][2] +'>'}]}
    
    subject ={'Patient.gender':convSex(tableDe[[row[0] for row in tableDe].index(id)][16]) , 'Patient.age':tableDe[[row[0] for row in tableDe].index(id)][13]}
    encouter = '{Reference(Encounter)}'
    dateTime = '<' + convDate(tableDe[[row[0] for row in tableDe].index(id)][4]) +'>'
    detected = '<>'
    recordDate = '<'+ convDate(tableDe[[row[0] for row in tableDe].index(id)][6]) + '>'
    resultCon = '{Reference(Condition)}'
    location = {'Location.contry':tableDe[[row[0] for row in tableDe].index(id)][24]}
    serious = {'coding':convSerious(tableOut[[row[0] for row in tableOut].index(id)][2]), 'text': '<'+ textSerious(convSerious(tableOut[[row[0] for row in tableOut].index(id)][2]))+'>'}
    severity = {}
    outcome = {}
    recorder = '{Reference(Patient|Practitioner|PractitionerRole|RelatedPerson)}'
    contributer = '{ Reference(Practitioner|PractitionerRole|Device)}'
    suspectEntity = [{
        'instance' : {'Medication.code':tableDr[[row[0] for row in tableDr].index(id)][2],
                    'Medication.identifier':tableDr[[row[0] for row in tableDr].index(id)][4],
                    'Medication.isActive':tableDr[[row[0] for row in tableDr].index(id)][5],
                    'Medication.lotNumber':tableDr[[row[0] for row in tableDr].index(id)][13],
                    'Medication.expirationDate':tableDr[[row[0] for row in tableDr].index(id)][14],
                    'MedicationAdministration.dosage':tableDr[[row[0] for row in tableDr].index(id)][8],
                    'MedicationAdministration.dosage.dose':tableDr[[row[0] for row in tableDr].index(id)][17],
                    'MedicationStatement.effective[x].start':tableTher[[row[0] for row in tableTher].index(id)][3],
                    'MedicationStatement.effective[x].end':tableTher[[row[0] for row in tableTher].index(id)][4]
            },
        'causality' : [{
            'assessment' : '{}',
            'productRelatedness' : '<>',
            'author' : '{ Reference(Practitioner|PractitionerRole)}',
            'method' : '{}'
            }]
        }]
    subjectMedicalHistory = '[{ Reference(Condition|Observation|AllergyIntolerance|FamilyMemberHistory|Immunization|Procedure|Media|DocumentReference) }]'
    referenceDocument = [{ 'DocumentReference.identifier': tableDr[[row[0] for row in tableDr].index(id)][12]}]
    study = '[{ Reference(ResearchStudy) }]'
    
    data = {'resourceType':'AdverseEvent',
            'identifier':identifier,
            'actuality':actuality,
            'category':category,
            'event':event,
            'subject':subject,
            'encouter':encouter,
            'dateTime':dateTime,
            'detected':detected,
            'recordDate':recordDate,
            'resultingCondition':resultCon,
            'location':location,
            'seriousness':serious,
            'severity':severity,
            'outcome':outcome,
            'recorder':recorder,
            'contributer':contributer,
            'suspectEntity':suspectEntity,            
            'subjectMedicalHistory':subjectMedicalHistory,
            'referenceDocument':referenceDocument,
            'study':study}

    open("C:/Py/result/"+ id +".json","w").write(json.dumps(data,indent = 2))

temp = [b[0] for b in tableDe]

for i in range(1,len(temp)):
    write(temp[i])

print("--- %s seconds ---" % (time.time() - start))
