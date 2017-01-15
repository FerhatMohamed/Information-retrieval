
# ferhat mohamed

import glob
from nltk.tokenize import *
from nltk.stem import *

#glob.glob  pour lister les fichier de dossier
list_token = glob.glob('L:tp_ri\data\Test\Tokeniseur\*')
list_stem = glob.glob('L:tp_ri\data\Test\Stemmer\*')


#crée les  listes
doc_token = []
doc_stem = []

#remplir les listes
for x in list_token:
    doc_token.append(open(x, 'r'))
for y in list_stem:
    doc_stem.append(open(y, 'w'))

#crée les objet
tokken = TweetTokenizer()
sttemm = PorterStemmer()


i = 0
for file in doc_token:
    file_stem = doc_stem[i]
    for line in file:
        fer = tokken.tokenize(line)
        for word in fer:
            file_stem.write(sttemm.stem(word) + '\n')
    i = i + 1



for f in doc_token :
    f.close()
for h in doc_stem :
    h.close()