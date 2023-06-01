import spacy    # importing nlp md
nlp = spacy.load('en_core_web_md')

# reading movies from the txt file and putting them into a list
with open("Data Science Hyperion Dev\T21\movies.txt") as file:  # open and read the movies.txt file
    movie_list = file.readlines()

watched_movie = "Planet Hulk"
watched_movie_description = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# comparing plant hulk's desription with each of the other movies
model_sentence = nlp(watched_movie_description)

# using list comprehension to create our movie_similarity_dictionary
movie_similarity_dict = {sentence[:7]: nlp(sentence[9:]).similarity(
    model_sentence) for sentence in movie_list}
print(movie_similarity_dict)

# getting and printing the key of the highest value of similarity this is the movie that'll be recommended
closest_similarity_movie = max(
    movie_similarity_dict, key=movie_similarity_dict.get)
print(
    f"Since you watched {watched_movie} we think you might like {closest_similarity_movie}")

# umm not sure if Planet Hulk is anything like movie C but I'm thinking this nlp module is finding the similarities in words only
