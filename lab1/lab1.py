import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import pymorphy3

def word_check(word1, word2):
    if((morph.parse(word1)[0].tag.POS == 'NOUN' and morph.parse(word2)[0].tag.POS == 'ADJF') 
       or (morph.parse(word1)[0].tag.POS == 'ADJF' and morph.parse(word2)[0].tag.POS == 'NOUN')):
        return True
    else:
        return False

def check_grammer(word1, word2):
    gramm1 = morph.parse(word1)[0].tag
    gramm2 = morph.parse(word2)[0].tag
    if(gramm1.gender == gramm2.gender and gramm1.number == gramm2.number and gramm1.case == gramm2.case):
        return True
    else:
        return False

nltk.download('punkt_tab')
morph = pymorphy3.MorphAnalyzer()

with open(r'C:\Users\я\Desktop\учеба\обработка языка\lab1\lab1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

sentences = sent_tokenize(text, 'russian')

for sentence in sentences:
    words = word_tokenize(sentence, 'russian')
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if(word_check(word1, word2) and check_grammer(word1, word2)):
            print(morph.parse(word1)[0].normal_form, morph.parse(word2)[0].normal_form)