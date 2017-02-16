# NBNE

Code to use Neighbor Based Node Embeddings (NBNE) method to create representations to nodes in a graph.

### Usage

#### Basic Usage

The libraries gensim and networkx should be installed. Then run:

```bash
    $ python src/get_embeddings.py --input data/graph/facebook.graph --output data/emb/facebook.emd
```

#### Using in other Applications

Import nbne module in your application and train model with:

```python
    from nbne import train_model
    train_model(graph, num_permutations, output_name)
```

Where graph should be a networkx graph.

### Input

Input should be a edgelist with format:

```
    node1_id,node2_id
    node1_id,node3_id
    node2_id,node3_id
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
