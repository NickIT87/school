from nltk.util import ngrams
from difflib import SequenceMatcher

def longest_common_subsequence(str1, str2):
    seq_matcher = SequenceMatcher(None, str1, str2)
    match = seq_matcher.find_longest_match(0, len(str1), 0, len(str2))
    print(match)
    print(type(match))
    return str1[match.a: match.a + match.size]

str1 = "abcde"
str2 = "acdeabc"

lcs = longest_common_subsequence(str1, str2)
print(type(lcs))
print("Longest Common Subsequence:", lcs)
