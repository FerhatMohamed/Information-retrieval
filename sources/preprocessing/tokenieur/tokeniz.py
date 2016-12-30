import glob
from nltk.tokenize import *


list_doc = glob.glob('L:tp_ri\data\Corpus\document\*')
list_token = glob.glob('L:tp_ri\data\Test\Tokeniseur\*')


documents = []
doc_token = []

for x in list_doc :
    documents.append(open(x, 'r'))
for y in list_token :
    doc_token.append(open(y, 'w'))



tokken = TweetTokenizer()

i = 0
for file in documents :
    file_toke = doc_token[i]
    for line in file :
        for g in tokken.tokenize(line):
            file_toke.write(g + "\n")
    i = i + 1


for f in documents:
    f.close()
for h in doc_token:
    h.close()