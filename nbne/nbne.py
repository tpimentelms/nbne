#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implementation of Neighbor Based Node Embeddings (NBNE).


Call function with a networkx graph:
>>> train_model(graph, num_permutations, output_filename)


For details read the paper:
    Fast Node Embeddings: Learning Ego-Centric Representations
    Tiago Pimentel, Adriano Veloso and Nivio Ziviani
    ICLR, 2018
'''
import random
import logging
import gensim


class MySentences(object):
    def __init__(self, graph, num_permutations, window_size, min_degree=0):
        self.graph = graph
        self.min_degree = min_degree
        self.num_permutations = num_permutations
        self.window_size = window_size

    def __iter__(self):
        for i in range(self.num_permutations):
            for src_id in self.graph.nodes():
                for sentence in self.get_nodes_senteces(src_id):
                    yield sentence

    def get_nodes_senteces(self, src_id):
        src_node = str(src_id)
        neighbors = list(self.graph.neighbors(src_id))

        if len(neighbors) < self.min_degree:
            return

        # Get all connected edges
        out_nodes = [str(out_id) for out_id in neighbors]
        random.shuffle(out_nodes)

        for j in range(len(out_nodes))[::self.window_size]:
            start_index = min(j, len(out_nodes) - self.window_size)
            end_index = start_index + self.window_size
            nodes_sentence = [src_node] + out_nodes[start_index: end_index]

            yield nodes_sentence


def train_model(graph, num_permutations, output_file=None, embedding_dimension=128, window_size=5, min_count=0, min_degree=0, workers=8):
    sentences = MySentences(graph, num_permutations, window_size, min_degree)
    model = gensim.models.Word2Vec(sentences, min_count=min_count * num_permutations, vector_size=embedding_dimension, window=window_size, sg=1, workers=workers)

    if output_file is not None:
        model.wv.save_word2vec_format(output_file)
    return model


def build_vocab(graph):
    dict_sent = []
    for node in graph.nodes():
        dict_sent += [[str(node)]]
    dict_sentences = gensim.corpora.Dictionary(dict_sent)
    return dict_sentences


# Make training verbose
def verbose_training():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
