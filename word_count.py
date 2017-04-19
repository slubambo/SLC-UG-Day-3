from collections import Counter
# Imported Library

# Function works perfectly in Python 3.6


def word_count(string_input):

    word_count_dict = Counter(string_input.split())

    # converting to regular dictionary 
    out_put = dict(word_count_dict)

    print(out_put)
