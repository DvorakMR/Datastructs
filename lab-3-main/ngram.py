import re
from typing import Tuple
from dataclasses import dataclass

@dataclass
class Ngram:
    words: Tuple[str]

    def __hash__(self):
        hash = 5381
        for word in self.words:
             for char in word:
                hash = ((hash << 5) - hash)  + ord(char)
        return hash

        # Now you make a better one!

def make_ngrams(string, n=5):
    """Return all n-grams of a given string (default n=5)."""

    # Split the string into lower-case words
    words = re.split("\\W", string.lower())
    words = [word for word in words if len(word) > 0]

    # Produce the n-grams
    ngrams = [ words[i:i+n] for i in range(len(words)) ]
    # The last few words in the string will give "n-grams" of length
    # less than n - remove them
    ngrams = [ ngram for ngram in ngrams if len(ngram) == n ]

    return [ Ngram(tuple(ngram)) for ngram in ngrams ]
