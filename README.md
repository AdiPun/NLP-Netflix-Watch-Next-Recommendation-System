# Natural Language Processing: Netflix Watch Next Recommendation System

## Objective
The objective of this project is to create a program that compares the similarity of a movie description with a list of other movies and provides recommendations based on the similarity of their descriptions. The program utilises spaCy, a natural language processing library, along with the en_core_web_md language model.

## Installation
To use this program, you need to install and import spaCy into your Python library. Run the following command in your terminal:
```
pip3 install spacy
```
Additionally, you need to download the English language model by running the command:
```
python -m spacy download en_core_web_md
```

## How to Use
To use the program, simply run it, and it will output a recommendation based on the similarity of the movie descriptions. For example, it may output "Since you watched Planet Hulk, we think you might like Movie C." 

If you want to try your own comparisons, you can change the `watched_movie_description` variable to the description of your own movie. Additionally, you can modify the descriptions in the `movies.txt` file to customise the movie list.

## Limitations
It's important to note that this program only provides a similarity score based on the text content of the movie descriptions. It doesn't take into account other factors such as genre or age rating when generating recommendations.
