def remove_fragments(s1, s2, s3):
    sentences = combine_a_single_dict(s1, s2, s3)
    sentences = split_list_of_words(sentences)
    three_word_set = split_list_of_three_words(sentences)
    for word in three_word_set:
        if word in s1 and word in s2 and word in s3:
            return word


def split_list_of_three_words(sentences):
    three_words_sentences = set()
    for sentence in sentences:
        each_sentence = sentences[sentence]
        for word_index in range(len(each_sentence)):
            three_words_sentences.add(" ".join(each_sentence[word_index:word_index + 3]))
    return three_words_sentences


def split_list_of_words(sentences):
    for sentence in sentences:
        split_words = list()
        word = ""
        count = 1
        sentence_length = len(sentences[sentence])
        for char in sentences[sentence]:
            if char not in [" "] and count != sentence_length:
                word += char
            elif count == sentence_length:
                word += char
                split_words.append(word)
            else:
                split_words.append(word)
                word = ""
            count += 1
        sentences[sentence] = split_words
    return sentences


def combine_a_single_dict(s1, s2, s3):
    sentences = dict()
    for s in ['s1', 's2', 's3']:
        sentences[s] = eval(s)
    return sentences


s1 = "Everyone will do a assignment and it is easy"
s2 = "Honesty will do a wonder in all aspects"
s3 = "Practice will do a wonder in life."
print(remove_fragments(s1, s2, s3))
