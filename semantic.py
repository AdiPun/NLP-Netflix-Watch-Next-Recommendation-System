import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) # 0.5929930274321619
print(word3.similarity(word2)) # 0.40415016164997786
print(word3.similarity(word1)) # 0.22358825939615987

# interesting as cat is 0.59 similar to monkey maybe because they're in the animals category
# banana is 0.40 similar to monkey maybe because they're associated with eating bananas but not in the same category e.g. food or animal
# but banana is only 0.22 similar to cats because they're not particularly related as much as monkeys and they aren't in the same category

tokens = nlp('cheese cow vegan Somerset milk egg')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# difference between md and sm:
# when using sm get the error: UserWarning: [W007] The model you're 
# using has no word vectors loaded, so the result of the 
# Doc.similarity method will be based on the tagger, parser
# and NER, which may not give useful similarity judgements.

# looks like sm is faster but less accurate with less word vectors
# and md is slower but more accurate with more word vectors

