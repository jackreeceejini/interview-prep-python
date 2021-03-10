"""
Stack manipulations
"""
import math
import collections

Inf = math.inf

def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
    ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []
    
    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(self.ElementWithCachedMax(x, x if self.empty() else max(
            x, self.max())))

def evaluate(RPN_expression):
    """
    Evaluate arithmetic expression written in 
    reverse polish notation (RPN)

    """
    DELIMITER = ','
    OPERATORS = {'+': lambda x, y : x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/' : lambda x, y : int(x/y)}
    intermediate_results = []
    for element in RPN_expression.split(DELIMITER):
        if element in OPERATORS:
            intermediate_results.append(OPERATORS[element](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(element))
    return intermediate_results[-1]

def balanced(inputString):
    """
    checks if inputString is a balance sequence of 
    parentheses, brackets or braces
    inputString  = '((][{{}}])'
    """
    leftParens, lookup = [], { '(' : ')', '[' : ']', '{' : '}'}
    for c in inputString:
        if c in lookup:
            leftParens.append(c)
        elif not leftParens or lookup[leftParens.pop()] != c:
            # Unmatched right paren
            return False
    return not leftParens

def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Empty string is not a valid path.')

    path_names = [] #uses list as stack

    #special case: starts with '/', which is an absolute path

    if path[0] == '/':
        path_names.append('/')
    
    for token in (token for token in path.split('/') if token not in ['.','']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else: # must be a name
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):] # Avoid starting with '//

if __name__ == '__main__':
    print(evaluate("3,4,+,2,*,1,+"))