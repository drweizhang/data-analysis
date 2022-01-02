from ntlk.corpus import stopwords
from collections import counter


text = """The cat is in the box. The cat likes the box.                   The box is over the cat."""

# Tokenize the text to words, and make them lower case. Store all the alphabetical tokens in var token. 
tokens = [w for w in word_tokenize(text.lower()) if w.isalpha()] 

# Remove all the stopwords from tokens 
no_stops = [t for t in tokens if t notin stopwords.words('english')]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stopsi]

# Count the most common used 2 tokens
Counter(lemmatized).most_common(2)
