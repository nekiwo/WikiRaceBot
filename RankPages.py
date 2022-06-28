import gensim
import numpy

model = gensim.models.KeyedVectors.load_word2vec_format("bin/google_w2v/GoogleNews-vectors-negative300.bin",
                                                        binary=True)


def rank_pages(pages, end_article):
    # vectors = [model[w] for w in pages]
    vectors = []
    new_pages = []

    for page in pages:
        new_page = []
        vector = []

        for word in page:
            if word in model:
                combined_sim = 0
                new_page.append(word)
                # vector.append(model.most_similar(word, topn=2))

                for w in end_article.split():
                    if w in model:
                        combined_sim = combined_sim + model.similarity(word, w)
                        # print(word, w, model.similarity(word, w))

                vector.append(combined_sim / len(end_article.split()))
            else:
                pass
                # print("Word {} not in vocab".format(word))
                # vectors.append([0])
                # new_pages.append(word)

        new_pages.append(" ".join(new_page))
        vectors.append(numpy.sum(vector) / 3)

    print(new_pages[:10])
    print(vectors[:10])

    for val in new_pages:
        if val == "":
            index = new_pages.index(val)
            del new_pages[index]
            del vectors[index]

    new_pages = numpy.array(new_pages)
    vectors = numpy.array(vectors)
    indices = vectors.argsort()
    sorted_new_pages = new_pages[indices]

    print(sorted_new_pages[:10])

    return sorted_new_pages
