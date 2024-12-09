import gensim

pos = ["уазик_NOUN", "такси_NOUN"]
neg = []

file = 'C:/Users/я/Desktop/учеба/обработка языка/cbow.txt'

with open(f'C:/Users/я/Desktop/учеба/обработка языка/nlp/lab2/output.txt', 'w') as out:
    pass

word2vec = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)
dist = word2vec.most_similar(positive=pos, negative = neg)
with open(f'C:/Users/я/Desktop/учеба/обработка языка/nlp/lab2/output.txt', 'w', encoding='utf-8') as out:
    out.write('Сложение\n')
    for i in dist:
        out.write(f'{i[0]}  {str(i[1])}\n')


pos = ["уазик_NOUN"]
neg = ["такси_NOUN"]
word2vec = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)
dist = word2vec.most_similar(positive=pos, negative = neg)
with open(f'C:/Users/я/Desktop/учеба/обработка языка/nlp/lab2/output.txt', 'a', encoding='utf-8') as out:
    out.write('Вычитание\n')
    for i in dist:
        out.write(f'{i[0]}  {str(i[1])}\n')