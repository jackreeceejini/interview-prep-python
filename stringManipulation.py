"""
Solutions to string manipulation problems

"""

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))




if __name__ == "__main__":
    print(is_palindromic("tenet"))