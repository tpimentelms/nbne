import argparse
import networkx as nx

from .nbne import train_model, verbose_training


def parse_args():
    '''
    Parses the node2vec arguments.
    '''
    parser = argparse.ArgumentParser(description="Get node embeddings.")

    parser.add_argument('--input', default='data/graph/facebook.graph', required=True,
                        help='Data graph used. Invalid if input is set.')

    parser.add_argument('--output', default='data/emb/facebook.emb', required=True,
                        help='Path where embeddings should be saved.')

    parser.add_argument('--dimensions', type=int, default=128,
                        help='Size of embedding dimensions. Default is 128.')

    parser.add_argument('--num-permutations', type=int, default=1,
                        help='Number of neighbors permutations per node. Default is 1.')

    parser.add_argument('--window-size', type=int, default=5,
                        help='Context size for optimization. Default is 5.')

    parser.add_argument('--min-degree', type=int, default=0,
                        help='Minimum degree of node to be considered as root for \'sentences\'. Default is 0.')

    parser.add_argument('--min-count', type=int, default=0,
                        help='Minimum number of appearances from node in training \'sentences\'. Default is 0.')

    parser.add_argument('--delimiter', type=str, default=' ',
                        help='Delimiter character in input graph file. Default is \',\'.')

    parser.add_argument('--workers', type=int, default=8,
                        help='Number of parallel workers. Default is 8.')
    
    parser.add_argument('--nodetype', type=str, default='int',
                        help='Type of node ids. Use \'int\' for better performance. Default is \'int\'')

    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='Graph is directed. Default is undirected.')
    parser.set_defaults(directed=False)

    parser.add_argument('--verbose', dest='verbose', action='store_true',
                        help='Stdout gensim info. Default is false. Only used if log-output is false.')
    parser.set_defaults(log=False)

    return parser.parse_args()


# Load graph from edge_list
def get_graph(input_file, directed, delimiter=',', nodetype='int'):
    types = {'int': int, 'str': str}
    graph = nx.read_edgelist(input_file, nodetype=types[nodetype], delimiter=delimiter, create_using=nx.DiGraph())
    if not directed:
        graph = graph.to_undirected()

    return graph


def run_model(graph, args):
    train_model(graph, args.num_permutations, args.output, embedding_dimension=args.dimensions,
                window_size=args.window_size, min_count=args.min_count,
                min_degree=args.min_degree, workers=args.workers)


def main():
    args = parse_args()
    if args.verbose:
        verbose_training()

    graph = get_graph(args.input, args.directed, args.delimiter, args.nodetype)
    run_model(graph, args)


if __name__ == '__main__':
    main()
