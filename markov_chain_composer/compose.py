import string
import random
import re
import os

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # Remove [text]
        text = re.sub(r'\[(.+)\]',' ',text)

        text = ' '.join(text.split())
        text = text.lower()

        # For this example, we are going to remove all the punctuation
        text = text.translate(str.maketrans('','',string.punctuation))

        words = text.split()
        return words
    
def make_graph(words):
    g = Graph()

    previous_word = None
    # For each word in the graph
    for word in words:
        # We are going to check if that word is in the graph, If not then add it
        word_vertex = g.get_vertex(word)

        # If there was a previous word, then add an edge if it does not already exist
        # in the graph, otherwise increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set the word to previous word and iterate
        previous_word = word_vertex

    # Now remember that we want to generate the probability mappings before composing
    # This is a great place to do it before we return the graph object
    g.generate_probability_mapping()
    return g

def compose(g, words, length = 50):
    composition = []
    word = g.get_vertex(random.choice(words)) # Pick a random word to start

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    # Step 1: Get words from text
    # words = get_words_from_text('markov_chain_composer/texts/hp_sorcerer_stone.txt')

    # For song lyrics
    words = []
    for song_file in os.listdir(f'markov_chain_composer/songs/{artist}'):
        song_words = get_words_from_text(f'markov_chain_composer/songs/{artist}/{song_file}')
        words.extend(song_words)

    # Step 2: Make a graph using those values
    g = make_graph(words)

    # Step 3: Get the next word for x number of words (x defined by user)
    composition = compose(g, words, 100)

    # Step 4: Show the user
    return ' '.join(composition)

if __name__ == '__main__':
    text = main('halsey')
    print(text)