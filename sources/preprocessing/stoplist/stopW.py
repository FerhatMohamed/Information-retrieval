
# ferhat mohamed

import glob
from nltk.corpus import stopwords
from nltk.tokenize import *

#glob.glob  pour lister les fichier de dossier
list_stem = glob.glob('L:tp_ri\data\Test\Stemmer\*')
list_SW = glob.glob('L:tp_ri\data\Test\Stoplist\*')



#crée les  listes
doc_stem = []
doc_SW = []

#remplir les listes
for x in list_stem:
    doc_stem.append(open(x, 'r'))
for y in list_SW:
    doc_SW.append(open(y, 'w'))


stop_words = set(stopwords.words('english')+[':',';',',','.','A','The','I','?','We','In','(',')','"','—',"'",'Our','How'])


#crée les objet
tokken = TweetTokenizer()

i = 0
for file in doc_stem:
    file_SW = doc_SW[i]
    for line in file:
        fer = tokken.tokenize(line)
        for word in fer:
            if word not in stop_words:
                   file_SW.write(word+'\n')
    i = i + 1


for f in doc_stem :
    f.close()
for h in doc_SW :
    h.close()