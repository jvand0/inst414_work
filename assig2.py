import networkx as nx
from tabulate import tabulate

# Create an empty directed graph
G = nx.DiGraph()

# Read the edge data from the dataset file
with open('twitter_combined.txt', 'r') as file:
    for line in file:
        source, target = map(int, line.strip().split())
        G.add_edge(source, target)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Sort nodes by degree centrality in descending order and get the top 3 nodes
top_nodes = sorted(degree_centrality, key=lambda node: degree_centrality[node], reverse=True)[:3]

# Create a list of lists for tabulation
table_data = []
for node in top_nodes:
    centrality = degree_centrality[node]
    table_data.append([node, centrality])

# Define table headers
headers = ['Node', 'Degree Centrality']

# Print the table using tabulate
table = tabulate(table_data, headers, tablefmt='grid')
print(table)
    







