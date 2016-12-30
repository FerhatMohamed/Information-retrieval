import glob
from nltk.tokenize import *
from nltk.stem import *

#glob.glob  pour lister les fichier de dossier
list_doc = glob.glob('L:tp_ri\data\Corpus\document\*')
list_stem = glob.glob('L:tp_ri\data\Test\Stemmer\*')
print(list_doc)

#crée les  listes
document = []
doc_stem = []

#remplir les listes
for x in list_doc:
    document.append(open(x, 'r'))
for y in list_stem:
    doc_stem.append(open(y, 'w'))

#crée les objet
tokken = TweetTokenizer()
sttemm = PorterStemmer()


i = 0
for file in document:
    file_stem = doc_stem[i]
    for line in file:
        fer = tokken.tokenize(line)
        for word in fer:
            file_stem.write(sttemm.stem(word)+'\n')
    i = i + 1



for f in document :
    f.close()
for h in doc_stem :
    h.close()
