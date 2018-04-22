# NBNE

Code to use Neighbor Based Node Embeddings (NBNE) method to create representations to nodes in a graph.


### Installation

You can install NBNE directly from PyPI:

`pip install nbne`

Or from source:

```
git clone https://github.com/tiagopms/nbne.git
cd nbne
pip install .
```
#### Dependencies

NBNE has the following requirements:

* [NetworkX](https://networkx.github.io/)
* [Gensim](https://radimrehurek.com/gensim/)

### Usage

#### Basic Usage

The libraries gensim and networkx should be installed. Then run:

```bash
    $ nbne --input examples/data/watts_strogatz.graph --output examples/data/watts_strogatz.emb
```

#### Using in other Applications

Import nbne module in your application and train model with:

```python
    from nbne import train_model
    train_model(graph, num_permutations)
```

Where graph should be a networkx graph. To save the model in an output file:

```python
    from nbne import train_model
    import networkx as nx
    graph = nx.watts_strogatz_graph(1000, 50, 0.2)
    train_model(graph, num_permutations, output_name)
```

### Input

Input should be a edgelist with format:

```
    node1_id node2_id
    node1_id node3_id
    node2_id node3_id
```

### Output

The output is a document with `n+1` lines. The first has format:

```
    num_nodes embeddings_size
```

And the other:

```
    node_id embedding
```

Where `embedding` is a space separated vector with dimension `d`, i.e. `d1 d2 d3 ... dn`.
