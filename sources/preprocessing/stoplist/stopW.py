import glob
from nltk.corpus import stopwords
from nltk.tokenize import *

#glob.glob  pour lister les fichier de dossier
list_doc = glob.glob('L:tp_ri\data\Corpus\document\*')
list_SW = glob.glob('L:tp_ri\data\Test\Stoplist\*')



#crée les  listes
document = []
doc_SW = []

#remplir les listes
for x in list_doc:
    document.append(open(x, 'r'))
for y in list_SW:
    doc_SW.append(open(y, 'w'))


stop_words = set(stopwords.words('english'))

#crée les objet
tokken = TweetTokenizer()


i = 0
for file in document:
    file_SW = doc_SW[i]
    for line in file:
        fer = tokken.tokenize(line)
        for word in fer:
            if word not in stop_words:
                   file_SW.write(word+'\n')
    i = i + 1


for f in document :
    f.close()
for h in doc_SW :
    h.close()