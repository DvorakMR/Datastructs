from term import *

def first_index_of(array, term, ordering):
    """Returns the index of the *first* element in `array` that equals the search term,
    according to the given ordering, or -1 if there is no matching element.
    Precondition: `array` is sorted according to the given ordering.
    Complexity: O(log N) comparisons where N is the length of `array`.
    """
    (left, right) = (0, len(array)-1)
    result = -1

    while left <= right:
        mid = (left + right)//2

        if ordering(term) == ordering(array[mid]):
            result = mid
            right = mid -1
            
        elif ordering(term) < ordering(array[mid]):
            right = mid -1
            
        else:
            left = mid + 1
    return result



def last_index_of(array, term, ordering):
    """Returns the index of the *last* element in `array` that equals the search term,
    according to the given ordering, or -1 if there are is matching element.
    Precondition: `array` is sorted according to the given ordering.
    Complexity: O(log N) comparisons where N is the length of `array`.
    """

    (left, right) = (0, len(array)-1)

    result = -1

    while left <= right:
        mid = (left + right)//2

        if ordering(term) == ordering(array[mid]):
            result = mid
            left = mid + 1
        
        elif ordering(term) < ordering(array[mid]):
            right = mid -1
        
        else:
            left = mid + 1

    return result



if __name__ == '__main__':
    array = [2, 3, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    term = Term("abc", None)
    array = [Term("abc", 25), Term("abc", 24), Term("abc", 23), Term("ABCD", 21),Term("abd", 20), Term("abd",20)]
    #ordering = Term.lexicographic_order
    #ordering = Term.reverse_weight_order
    ordering = Term.prefix_order(2)
    indexFirst = first_index_of(array, term, ordering)
    indexLast = last_index_of(array, term, ordering)

    if indexFirst != -1:
        print(f'The first occurrence of element {term} is located at index {indexFirst} when ordering is {ordering.__name__}')
    else:
        print('Element not found in the list')

    if indexLast != -1:
        print(f'The last occurrence of element {term} is located at index {indexLast} when ordering is {ordering.__name__}')
    else:
        print('Element not found in the list')
