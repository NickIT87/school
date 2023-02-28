import nltk

# Скачиваем необходимые данные
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Задаем предложение
sentence = "The quick brown fox jumps over the lazy dog."

# Токенизация
tokens = nltk.word_tokenize(sentence)

# Частеречная разметка
tagged = nltk.pos_tag(tokens)

# Синтаксический анализ
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(tagged)

# Вывод результата
print(tree)
