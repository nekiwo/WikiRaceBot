def parse_page_titles(titles):
    # input: ["word1, word2", "word3", "word4's word5", "word6 word7 word8"]
    # output: [["word1", "word2"], ["word3"], ["word4s", "word5"], ["word6", "word7", "word8"]]
    new_titles = []

    for title in titles:
        new_title = title.replace("'", "").replace(",", "").replace("-", " ")
        new_title_arr = new_title.split()
        new_titles.append(new_title_arr)

    return new_titles
