import csv, os
import string
string.ascii_lowercase

#point to a relative path
os.chdir(os.path.relpath('Stims', start='.')+'\\')


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
            
# format dictionary => all stim names in one list called [stims]

# create empty list called [finalStims] 

# choose random row in dictionary
# place stim name in [finalStims]
# remove strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] from [stims]
# remove those stims' rows from dictionary

# for number of elements in [finalStims] < 4, do
#    choose random row in dictionary 
#    place stim name in [finalStims]
#    compare strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] with [stims]
#       if matches, then
#          remove from [stims]
#          remove those stims' rows from dictionary
#       end if
# end for

# [final stims] should now be a list of 4 dissimilar fractals            
