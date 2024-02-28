# This is our Markov Chain representation
import random

# Define graph in terms of vertices

class Vertex:
    def __init__(self, value): # Value will be de word
        self.value = value
        self.adjacent = {} # Nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []
    
    def add_edge_to(self, vertex, weight = 0):
        # Adding an edge to the vertex with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # Incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)
    
    def next_word(self):
        # Randomly select the next word, based on weights
        return random.choices(self.neighbors, self.neighbors_weights)[0]

# Now we have a Vertex representation, then we'll put this together in a graph

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # What are the values of all the vertices?
        # Return all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)
    
    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mapping(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()