import nltk
import glob
from nltk.tokenize import *


#glob.glob  pour lister les fichier de dossier
list_doc = glob.glob('L:tp_ri\data\Corpus\document\*')
list_tag = glob.glob('L:tp_ri\data\Test\Pos-tagger\*')

#crée les  listes
documents = []
doc_tagge = []

#remplir les listes
for x in list_doc :
    documents.append(open(x, 'r'))
for y in list_tag :
    doc_tagge.append(open(y, 'w'))

#crée les objet
tokken = TweetTokenizer()

i = 0
for file in documents:
    file_tagge = doc_tagge[i]
    for line in file:
          tokeniii = tokken.tokenize(line)
          tagged = nltk.pos_tag(tokeniii)
          for g in tagged:
              file_tagge.write(str(g)+"\n")
    i = i + 1


for f in documents:
    f.close()
for h in doc_tagge:
    h.close()
