"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    file = file.read()



    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    split_text_str = text_string.split()

    

    for idx in range(len(split_text_str) - 2):

        key = (split_text_str[idx], split_text_str[idx + 1])
        next_value = split_text_str[idx + 2]

        if key in chains:
            chains[key].append(next_value)
        else:
            chains[key] = [next_value]


    # for k, v in chains.items():
    #     print(k, ":", v)

    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    initial_key = choice(list(chains))
    words.append(initial_key)

    while True:

        key_1 = choice(list(chains[initial_key]))
        words.append(key_1)
        # print(random_value)
        if (words[-2][1], key_1) in chains:
            
            key_1 = choice(list(chains[words[-2][1], key_1]))
            words.append(key_1)
        else:
            continue
        # words.append(chains[key_1])

    print(words)

    # return " ".join(words)

    # (choice, are)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
# random_text = make_text(chains)

# print(random_text)
