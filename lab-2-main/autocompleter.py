from range_binary_search import *

class Autocompleter:
    def __init__(self, dictionary):
        """Initializes the dictionary from the given list of terms."""
        self.dictionary = dictionary
        self.sort_dictionary()

    def sort_dictionary(self):
        """Sorts the dictionary in *case-insensitive* lexicographic order.
        Complexity: O(N log N) where N is the number of dictionary terms."""
        self.dictionary.sort(key = lambda x: Term.lexicographic_order(x))

    def number_of_matches(self, prefix):
        """Returns the number of terms that start with the given prefix.
        Precondition: the internal dictionary is in lexicographic order.
        Complexity: O(log N) where N is the number of dictionary terms."""
        first_index = first_index_of(self.dictionary, Term(prefix, None), Term.prefix_order(len(prefix)))
        last_index = last_index_of(self.dictionary, Term(prefix, None), Term.prefix_order(len(prefix)))
        if first_index == -1 or last_index == -1:
            return 0
        else:
            return last_index-first_index + 1


    def all_matches(self, prefix):
        first_index = first_index_of(self.dictionary, Term(prefix, None), Term.prefix_order(len(prefix)))
        last_index = last_index_of(self.dictionary, Term(prefix, None), Term.prefix_order(len(prefix)))
        if first_index == -1 or last_index == -1:
            return 0
        else:
            matches = self.dictionary[first_index:(last_index+1)]
            matches.sort(key = lambda x: Term.reverse_weight_order(x))
            return matches
        """Returns all terms that start with the given prefix, in descending order of weight.
        Precondition: the internal dictionary is in lexicographic order.
        Complexity: O(log N + M log M) where M is the number of matching terms."""


