# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)
print(sentences[0])
# Tokenize each sentence into words: token_sentences
token_sentences = [word_tokenize(sent) for sent in sentences]
print(token_sentences[0])
# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 
print(pos_sentences[0])

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)
# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)




### Comparing NLTK with spaCy NER

# Import spacy
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('en')

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    #print(ent)
    print(ent.label_, ent.text)
