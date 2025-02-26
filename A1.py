student_deatail={'id1':
{'Name':['Rishal'],
 'Class':['V'],
 'Subject-Integration':['Science,Math,English']},
 'id2':
{'Name':['David'],
 'Class':['V'],
 'Subject-Integration':['Arts,IT,Commerce']},
'id3':
{'Name':['Rishal'],
 'Class':['V'],
 'Subject-Integration':['Science,Math,English']},
 'id4':
{'Name':['Sara'],
 'Class':['V'],
 'Subject-Integration':['Agriculture,Health,English']}
 }
results={}
for key,value in student_deatail.items():
    if value not in results.values():
        results[key]=value

print(results)        