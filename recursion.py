import math

NUM_PEGS = 3

def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    # Initialize pegs
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


def generate_power_set(S):
    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set

def generate_balanced_parentheses(num_pairs):
    def directed_generate_balanced_parentheses(num_left_parens_needed, num_right_parens_needed, valid_prefix, result=[]):
        if num_left_parens_needed > 0: # able to insert '('.
            directed_generate_balanced_parentheses(num_left_parens_needed - 1, num_right_parens_needed, valid_prefix + '(')
        if num_left_parens_needed < num_right_parens_needed:
            # Able to insert ')'.
            directed_generate_balanced_parentheses(num_left_parens_needed, num_right_parens_needed - 1, valid_prefix + ')')
        if not num_right_parens_needed:
            result.append(valid_prefix)
        return result 
    return directed_generate_balanced_parentheses(num_pairs, num_pairs, '')



if __name__ == "__main__":
    print(generate_balanced_parentheses(6))