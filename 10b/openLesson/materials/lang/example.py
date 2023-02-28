import nltk

# Скачиваем необходимые данные
nltk.download('punkt')
nltk.download('stopwords')

# Загружаем текст
text = "Natural Language Processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human languages."

# Токенизация
tokens = nltk.word_tokenize(text)

# Удаление стоп-слов
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Частеречная разметка
tagged = nltk.pos_tag(filtered_tokens)

# Синтаксический анализ
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(tagged)

# Вывод результатов
print("Original Text: ", text)
print("Filtered Text: ", " ".join(filtered_tokens))
print("POS Tags: ", tagged)
print("Syntax Tree: ")
tree.draw()
