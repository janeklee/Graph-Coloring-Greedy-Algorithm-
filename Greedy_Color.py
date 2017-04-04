import csv, os
import string
string.ascii_lowercase


os.chdir('C:\Users\Phillip\Box Sync\Boorman Lab\Experimental Tasks\Latent Cause Representation\Stims')


files=csv.DictReader(open('Stims Similarities.csv','r+'))
files=list(files)

#letters
letters=list(string.ascii_lowercase)


for i in files[0:5]:
    #update our dicts to have neighbor entry
    i.update({'MatchingLetter':[]})
    
    if files.index(i)==0:
        i['MatchingLetter']=letters[0]
    else:
        #look through all the files
        for l in files:
            if l['STIMULUS NAME'] in i['SIMILAR IN COLOR'] or l['STIMULUS NAME'] in i['SIMILAR IN SHAPE']:
                i['MatchingLetter'].append(l['STIMULUS NAME'])
            
            