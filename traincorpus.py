from __future__ import print_function
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    inputFile = sys.argv[1] # preprocess.py dosyasından elde ettiğimiz wiki.tr.txt dosyasının linkinin input olarak yazabilirsiniz ya da consoldan input olarak verebilirsiniz
    outputFile = "trmodel"
    model = Word2Vec(LineSentence(inputFile), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.wv.save_word2vec_format(outputFile, binary=True)
