# A Python program for Dijkstra's shortest
# path algorithm for adjacency
# list representation of graph

from collections import defaultdict
import sys
from heapq import heappush, heappop

# heap data structure, (value, key), value is used for sorting and key used for identifying


class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	# Adds an edge to an undirected graph
	def addEdge(self, src, dest, weight):

		# Add an edge from src to dest. A new node
		# is added to the adjacency list of src. The
		# node is added at the begining. The first
		# element of the node has the destination
		# and the second elements has the weight
		newNode = [dest, weight]
		self.graph[src].insert(0, newNode)


	# The main function that calulates distances
	# of shortest paths from src to all vertices.
	# It is a O(ELogV) function
	def dijkstra(self, src):

		V = self.V # Get the number of vertices in graph
		dist = [] # dist values used to pick minimum
					# weight edge in cut
		short = [0]*V # if the vertices has the shortest path
		# minHeap represents set E
		minHeap = []

		# Initialize min heap with all vertices.
		# dist value of all vertices
		for v in range(V):
			if v!= src:
				dist.append(sys.maxsize)
				heappush(minHeap, (dist[v] , v) )
			else:
				#v == src , the initialize vertice is 0
				dist.append(0)
				heappush(minHeap, (dist[v], v))



		# Initially size of min heap is equal to V
		#minHeap.size = V;

		# In the following loop, min heap contains all nodes
		# whose shortest distance is not yet finalized.
		while len(minHeap) != 0:

			# Extract the vertex with minimum distance value
			newHeapNode = heappop(minHeap) #(dist value, node id)
			u = newHeapNode[1]
			short[u] = 1 # the node u is make sure to reach the smallest path
			# Traverse through all adjacent vertices of
			# u (the extracted vertex) and update their
			# distance values
			for pCrawl in self.graph[u]:
				v = pCrawl[0]
				# If shortest distance to v is not finalized
				# yet, and distance to v through u is less
				# than its previously calculated distance
				if dist[u] != sys.maxsize and short[v] == 0 and pCrawl[1] + dist[u] < dist[v]:
					# update distance value in min heap also
					minHeap.pop( minHeap.index( (dist[v],v)) )
					dist[v] = pCrawl[1] + dist[u]
					heappush(minHeap, (dist[v],v))
		return dist



