# Movie_HITS
An application of the HITS (hubs and authorities) algorithm to the Movielens ratings dataset.
Calling *hits.py* builds the bipartite graph, runs the HITS algorithm (max iteration of 1000) and prints the top 100 movies by their authority score.

**Libraries Used:** pandas, networkx

Read about the HITS algorithm [here](https://en.wikipedia.org/wiki/HITS_algorithm).

Data from the MovieLens [Datasets](https://grouplens.org/datasets/movielens/).
Current data set is the 100,000 ratings from 700 users of 9000 movies.

*The actual ratings value is not included in the algorithm but designing a 'weighted' HITS algorithm is the aim*
