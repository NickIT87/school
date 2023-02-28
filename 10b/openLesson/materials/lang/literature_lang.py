# Синтаксичний аналіз речення "The quick brown fox jumps over the lazy dog":

# "The" - артикль визначений, однина, чоловічий рід.
# "quick" - прикметник, означає якість лисиці, тобто її швидкість.
# "brown" - прикметник, означає колір лисиці.
# "fox" - іменник, позначає тварину, про яку йдеться.
# "jumps" - дієслово в формі Present Simple, означає дію стрибка.
# "over" - прийменник, вказує на напрямок дії стрибка.
# "the" - артикль визначений, однина, чоловічий рід.
# "lazy" - прикметник, означає якість собаки, тобто її лінощі.
# "dog" - іменник, позначає тварину, над якою стрибає лисиця.

# Отже, речення складається зі словосполучення "The quick brown fox", 
# яке є підметом, і словосполучення "jumps over the lazy dog", 
# яке є присудком. Дієслово "jumps" узгоджується з підметом в числі однина.

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
print(tokens)

from nltk import pos_tag

tagged_tokens = pos_tag(tokens)
print(tagged_tokens)

from nltk import RegexpParser

grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Noun phrase
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Verb phrase
  PP: {<IN><NP>}               # Prepositional phrase
  CLAUSE: {<NP><VP>}           # Clause
"""
parser = RegexpParser(grammar)

parsed_sentence = parser.parse(tagged_tokens)
print(parsed_sentence)
