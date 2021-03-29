import itertools
import heapq

def top_k(k, stream):
    # Entries are compared by thier lengths
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # push next_string and pop the shortest string in min_heap
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    # builds a list of iterators for each array in sorted_arrays
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # puts first element from each iterator in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []

    #adds first k elements in min_heap, stop if there are fewer than k
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    #continously add element from sequence into min_heap simultaneously poping out the smallest in to result
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
        
    return result