
# ferhat mohamed

import nltk
import glob
from nltk.tokenize import *


#glob.glob  pour lister les fichier de dossier
list_SW = glob.glob('L:tp_ri\data\Test\Stoplist\*')
list_tag = glob.glob('L:tp_ri\data\Test\Pos-tagger\*')

#crée les  listes
doc_SW = []
doc_tagge = []

#remplir les listes
for x in list_SW :
    doc_SW.append(open(x, 'r'))
for y in list_tag :
    doc_tagge.append(open(y, 'w'))

#crée les objet
tokken = TweetTokenizer()

i = 0
for file in doc_SW:
    file_tagge = doc_tagge[i]
    for line in file:
          tokeniii = tokken.tokenize(line)
          tagged = nltk.pos_tag(tokeniii)
          for g in tagged:
              file_tagge.write(str(g)+"\n")
    i = i + 1


for f in doc_SW:
    f.close()
for h in doc_tagge:
    h.close()

