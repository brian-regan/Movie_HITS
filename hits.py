# python script for running HITS algorithim on the Movielens dataset
# Data from https://grouplens.org/datasets/movielens/

import pandas as pd
import networkx as nx
import operator


def add_link(a,b, net):
	net.add_node(a, group = 'user', color = 'red')
	net.add_node(b, group = 'movie', color = 'blue')
	net.add_edge(a, b)



def main():

	net =nx.DiGraph()

	# Read Data
	data_types = {'userId': 'int32', 'movieId': 'int32', 
				'rating': 'float64', 'timestamp': 'int32'}
	ratings = pd.read_csv('ratings.csv', dtype = data_types)
	n = len(ratings.index)

	# Read Movie titles for print out
	movies =  pd.read_csv('movies.csv', dtype = data_types)
	movies.set_index('movieId', inplace = True)

	mov_dict = movies.to_dict(orient='index')

	# Loop through ratings and add edges
	for row in ratings.itertuples():
		index = row[0]

		user_Id = 'u' + str(row[1])
		movie_Id = 'm' + str(row[2])
		rating = row[3]
		add_link(user_Id, movie_Id, net)
		print("Added Edge {0} of {1}".format(index + 1, n))

	# Print node count
	print("Total Amount of Nodes: {}".format(len(net)))


	# Run HITS algorithim
	hubs, auth = nx.hits(net, max_iter = 1000)
	sorted_auth = sorted(auth.items(), key=operator.itemgetter(1), reverse = True)


	# Print top 100 authority movies
	for i in range(100):
		mov = int(sorted_auth[i][0].replace("m", ""))
		print("{0}. {1}, {2}\n".format(i+1, mov_dict[mov]['title'], sorted_auth[i][1]))


main()


