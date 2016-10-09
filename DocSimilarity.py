import collections


def get_similarity(doc1, doc2):
    document_distance = 0

    doc1_word_map, doc1_word_count = get_word_map(doc1)
    doc2_word_map, doc2_word_count = get_word_map(doc2)

    for key, value in doc1_word_map.items():

        if key in doc2_word_map:
            document_distance += min(value, doc2_word_map[key]) * 2

    return document_distance / (doc1_word_count + doc2_word_count)


def get_word_map(doc):
    word_map = collections.defaultdict(int)
    word_count = 0

    with open(doc, 'r') as f:
        for line in f:
            for word in line.split():
                word_map[word.lower()] += 1
                word_count += 1

    return word_map, word_count


print(get_similarity('text1.txt', 'text2.txt'))
