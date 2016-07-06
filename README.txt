This project is properly run as follows:

python3 kruskal.py [filename]

or, if the shellscript is present:

kruskal [filename]

The file in question is properly formatted as sets of two or three integers; the first two integers representing the nodes connected by an edge, the optional third integer representing that edge's weight (default weight is 1).

There is an option to set the root node of the minimum spanning tree with -r, which can greatly affect its structure if the starting graph does not span.  This is activated like so:

python3 kruskal.py -r [root #] [filename]
or:
kruskal -r [root #] [filename]

An example with the files given would be:

kruskal -r 10 integers