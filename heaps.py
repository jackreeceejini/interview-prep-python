import itertools
import heapq
import math

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


class Star:
    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z 

    @property
    def distance(self):
        return math.sqrt(self.x**2, self.y**2, self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_stars(k, stars):
    max_heap = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap == k + 1):
            heapq.heappop(max_heap)
    
    return [s[1] for s in heapq.nlargest(k, max_heap)]


def online_median(sequence):
    # min_heap stores the largest half seen so far
    min_heap = []
    # max_heap stores the smaller half seen so far
    # values in max_heap are negative
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # Ensure min_heap and max_heap have equal number of elements if 
        # an even number of elements is read, otherwise min_heap must have
        # one more element than max_heap
        if (max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        result.append(0.5 * (min_heap[0] + (-max_heap[0] if len(min_heap) == len(max_heap) else min_heap[0])))
        

def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    # stores the (-value, index) pair in candidate_max_heap. This heap is 
    # ordered by value field. uses the negative of value to get the effect
    # of max_heap
    candidate_max_heap = []
    # the largest element in A is at index 0
    candidate_max_heap.append((-A[0], 0))
    result = []
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2 
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

