# finalCapstone
# Netflix watch next reccomendation system

## Objective
Create a program that compares simarlity of a movie description with a list of other movies' to output a 'recomendation'
based on how similar the movie descriptions are.
Using spaCy, a natural language processing library and the more advanced language model: en_core_web_md.

## Installations
You will need to install and import spaCy into your python library, type the command below into your terminal
pip3 install spacy
and download the english language model:
python -m spacy download en_core_web_md

## How to use
Run the programme and it'll output "Since you watched Planet Hulk we think you might like Movie C"
To try your own comparisions, change the watched_movie_description for your own movie, then change up the descriptions in the movies.txt file

## Limitations
This programme will only give a score based on how similar the text content is, it doesn't know any other info such as genre or age rating.
