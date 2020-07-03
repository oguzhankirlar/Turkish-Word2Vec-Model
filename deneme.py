from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load_word2vec_format('/home/oguzhan/PycharmProjects/OguzModel/trmodel', binary=True)

print(word_vectors.most_similar(positive=["kral","kadın"],negative=["erkek"]))

