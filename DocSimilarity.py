import collections


# Returns a float between 0 and 1 representing how
# similar two documents are to each other
def get_similarity(doc1, doc2):
    word_match_occurrence = 0

    doc1_word_map, doc1_word_count = get_word_map(doc1)
    doc2_word_map, doc2_word_count = get_word_map(doc2)

    # Iterate through each key value pair of doc1 word map
    # and check if the key is doc2 word map
    for key, value in doc1_word_map.items():

        # If the value is present then add twice the lowest value to the word match occurrence counter.
        # (This is the total number of times that word appears in BOTH bodies of text)
        if key in doc2_word_map:
            word_match_occurrence += min(value, doc2_word_map[key]) * 2

    # Return the ratio between the occurrence of the word matches and the count of all words
    return word_match_occurrence / (doc1_word_count + doc2_word_count)


# Returns a map and count of words appearing in a given document
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
