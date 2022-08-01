from matplotlib import pyplot as plt
# import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum
# from collections import Counter

okt = Okt()
hannamu = Hannanum()
a = open('C:\\Users\\Kosmo\\Desktop\\Test\\wangja.txt',encoding='utf-8')
doc = a.read()

def build_bag_of_words(document):
    document = document.replace('.', '')
    print(document)
    tokenized_document = okt.morphs(document)
    
    word_to_index = {}
    bow = []
    for word in tokenized_document:
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)
            bow.insert(len(word_to_index) - 1, 1)
        else:
            index = word_to_index.get(word)
            bow[index] = bow[index] +1
        return word_to_index, bow
    
a = open('C:\\Users\\Kosmo\\Desktop\\Test\\wangja.txt',encoding='utf-8')
doc = a.read()
vocab, bow = build_bag_of_words(doc)
print("vocabulary: ",vocab)
print("bag of words vector :", bow)

