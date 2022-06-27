import gensim
model = gensim.models.Word2Vec.load_word2vec_format('path-to-vectors.txt', binary=False)

def rank_pages(pages):
    vectors = [model[w] for w in pages]
    new_pages = []
    return pages