original_dic={'Codingal':2,'is':2,'the':3,'best':1,'for':5,'coding':7}
print("Original dictionary:"+str(original_dic))

k=2
res=0
for key in original_dic:
    if original_dic[key]==k:
        res=res+1
print("Frequency of K is:"+str(res))        