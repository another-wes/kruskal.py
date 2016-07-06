import sys
class Edge:
	def __init__(self,s,d,w):
		self._src=s
		self._dest=d
		self._weight=w
	def getWeight(self):
		return self._weight
	def getSrc(self):
		return self._src
	def getDest(self):
		return self._dest
	def setWeight(self,n):
		self._weight=n
	def reverse(self):
		return Edge(self._dest,self._src,self._weight)	
	def __lt__(self,other):
		return (self._weight<other.getWeight())
	def __le__(self,other):
		return (self._weight<=other.getWeight())
	def __ge__(self,other):
		return (self._weight>=other.getWeight())
	def __gt__(self,other):
		return (self._weight>other.getWeight())
	def __eq__(self,other):
		return ((self._weight==other.getWeight())and((self._src==other.getSrc())and(self._dest==other.getDest()))or((self._src==other.getDest())and(self._dest==other.getSrc())))
def isRed(x):
	if x==None: return False
	else: return x.isRed() 
class RBTNode: #this is just for the list of explored vertices; brings searches and insertions down to O(lg(V)) from O(V)
	def __init__(self,data=None,red=False):
		self._data=data
		self._red = red
		self._l=None
		self._r=None
		self._p=None
	def isRed(self):
		return self._red
	def color(self,color):
		self._red = color
	def getDad(self):
		return(self._p)
	def getLeft(self):
		return(self._l)
	def getRight(self):
		return(self._r)
	def setDad(self,other):
		self._p=other
	def setLeft(self,other):
		self._l=other
		if other != None:other.setDad(self)
	def setRight(self,other):
		self._r=other
		if other != None:other.setDad(self)
	def swap(self,other):
		temp=self._data
		self._data=other._data
		other._data=temp
	def indicate(self,other):
		if (other==self._data): return True
		elif other<self._data: 
			if self._l==None: return False
			return self._l.indicate(other)
		else: 
			if self._r==None: return False
			return self._r.indicate(other)		
	def __int__(self):
		return self._data
	def insert(self,num):
		if num<self._data:
			if self._l==None:
				x=RBTNode(num,True)
				self.setLeft(x)
				fix(x)
			else: self._l.insert(num)
		else:
			if self._r==None:
				x=RBTNode(num,True)
				self.setRight(x)
				fix(x)
			else: self._r.insert(num)

def fix(x):#post-insertion fix for RBT.  x has already been inserted.
	while not (isRed(x.getDad())):
		p=x.getDad()
		if not isRed(p): break
		g=p.getDad()
		if g!=None:
			if int(x)<int(g):
				if isRed(g.getRight()): 
					fixColors(g,x)
					x=g
				else: #uncle black 
					if int(x)<int(p):#left-left
						r = RBTNode(int(g),True)
						r.setLeft(p.getRight())
						r.setRight(g.getRight())
						g.swap(p) #g has p's old value and is now black. p is now red
						g.setLeft(x)
						g.setRight(r)
						g.color(True)
						p.color(False)
					else: #left-right
						p.setRight(x.getRight())
						x.swap(g) #g now has new value, and x now has old gramp value
						x.setRight(g.getRight())
						g.setRight(x)
						g.color(True)
						x.color(False)
						x=p
			else:
				if isRed(g.getLeft()): 
					fixColors(g,x)
					x=g
				else: #uncle black 
					if int(x)>=int(p):#right-right
						r = RBTNode(int(g),True)
						r.setRight(p.getLeft())
						r.setLeft(g.getLeft())
						g.swap(p) #g has p's old value and is now black. p is now red
						g.setRight(x)
						g.setLeft(r)
						g.color(True)
						p.color(False)
					else: #right-left
						p.setLeft(x.getLeft())
						x.swap(g) #g now has new value, and x now has old gramp value
						x.setLeft(g.getLeft())
						g.setLeft(x)
						g.color(True)
						x.color(False)
						x=p
								
def fixColors(g,x):
	g.color(True)
	g.getLeft().color(False)
	g.getRight().color(False)
	x.color(True)

# class RedBlackTree: #Opted for incomplete red-black tree over AVL tree, although since deletions are not involved and this is used for lookup-intensive it was a tough decision.
# 	def __init__(self,root_node):
# 		self._root=root_node
# 		#self._list=[root_node]
# 		self._n=1
# 	def __contains__(self,other):
# 		return self._root.indicate(other)
# 	def __len__(self):
# 		return self._n
# 	def insert(self,num):
# 		self._root.insert(num) #did not have to account for the case of an empty tree
# 		self._n+=1
# 		self._root.color(False)
class RedBlackTree: #Opted for incomplete red-black tree over AVL tree, although since deletions are not involved and this is used for lookup-intensive it was a tough decision.
	def __init__(self,root_node=None):
		self._root=root_node
		self._n=int(root_node!=None)
	def __contains__(self,other):
		if (self._root==None) or (other==None): return False
		else: return self._root.indicate(other)
	def __len__(self):
		return self._n
	def insert(self,num):
		if self._root==None:
			self._root=RBTNode(num)
		else:
			self._root.insert(num) #did not have to account for the case of an empty tree
		self._n+=1
		self._root.color(False)
	# def display(self): for testing
	# 	print()
	# 	q=[[self._root,0]]
	# 	curr=0
	# 	while len(q)>0:
	# 		n = q.pop(0)
	# 		if n[1]!=curr:print()
	# 		curr=n[1]
	# 		if isRed(n[0]): print(str(int(n[0]))+"R",end="")
	# 		else: print(str(int(n[0]))+"B",end="")
	# 		if n[0].getDad()!=None: print("("+str(int(n[0].getDad()))+")",end=" ")
	# 		if not n[0].getLeft()==None:
	# 			q.append([n[0].getLeft(),n[1]+1])
	# 		if not n[0].getRight()==None:
	# 			q.append([n[0].getRight(),n[1]+1])
	# 	print()
class Graph:
	def __init__(self,root=None):
		self._v=RedBlackTree() #to reduce work (specifically searching) for addEdge
		self._e=[]
		self._root=root
		self._alt=None
		self._subsets={} 
		self._srcsets={}#these eliminate the need to iterate over self._v when running Kruskal's
	def addEdge(self,s,d,w=1):#have it sort during this process
		if s not in self._v:
			self._v.insert(s)
			self._subsets[s]=SubSet(s)
			self._srcsets[s]=[]
			if self._alt==None:self._alt=s
		if d not in self._v:
			self._v.insert(d)
			self._subsets[d]=SubSet(d)
			self._srcsets[d]=[]
		heapPush(self._e,Edge(s,d,w))
	# sort method removed in favor of storing edges in heap	
	def V(self):
		return len(self._v)
	def dropEdge(self):
		return heapPop(self._e)
	def noEdges(self):
		return (self._e==[])	
	def root(self):
		if self._root in self._v: return self._root
		else: return self._alt
	def subsets(self):
		return self._subsets
	def srcsets(self):
		return self._srcsets	
		
def goDown(heap,i,n):
    x = heap[n]
    while n > i:
        p = (n - 1) >> 1
        parent = heap[p]
        if (x<parent):
            heap[n] = parent
            n = p
            continue
        break
    heap[n] = x
def goUp(heap,n):
    end = len(heap)
    start = n
    x = heap[n]
    # Bubble up the smaller child until hitting a leaf.
    child = 2*n + 1    # leftmost child position
    while child < end:
        # Set childpos to index of smaller child.
        r = child + 1
        if r < end and (heap[child]>=heap[r]):
            child = r
        # Move the smaller child up.
        heap[n] = heap[child]
        n = child
        child = 2*n + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[n] = x
    goDown(heap,start,n)

def heapPush(heap,item):
    heap.append(item)
    goDown(heap,0,len(heap)-1)

def heapPop(heap):    
    last = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = last
        goUp(heap,0)
    else:
        returnitem = last
    return returnitem
def heapify(x):
    n = len(x)
    for i in reversed(xrange(n//2)):
        goUp(x, i)
class SubSet:
	def __init__(self,vertex):
		self._p=vertex
		self._r=0
	def parent(self):
		return self._p
	def assignParent(self,parent):#O(1)
		self._p=parent		
	def rank(self):
		return self._r	
	def promote(self):
		self._r+=1	

def findSet(subsets,x):#runs in log(V)? possibly log(E), look into this
	if (subsets[x].parent() != x): subsets[x].assignParent(findSet(subsets,subsets[x].parent()))
	return subsets[x].parent()
def union(subsets,x,y):#still log(V), or 2log(V)
	xroot = findSet(subsets,x)#log(V)
	yroot = findSet(subsets,y)#log(V)
	if (subsets[xroot].rank()<subsets[yroot].rank()):subsets[xroot].assignParent(yroot)		#all constant time from here to end of function
	elif (subsets[xroot].rank()>subsets[yroot].rank()):subsets[yroot].assignParent(xroot)
	else:
		subsets[yroot].assignParent(xroot)
		subsets[xroot].promote()
total=0 #probably a cleaner way to do this
'''Remember: E is at most V^2, in which case lg E = 2 lg V'''
def kruskurse(diction,lyst,lvl,reached):#iterates on and traverses already built MST. Worst-case runtime: O(E(log(E)*(log(V)+log(E)))=O(E lg^2 V)
	global total #(V-length dictionary with O(lg(E))-length entries and O(lg(E))-length lists of edges)
	next_level=[]
	print(str(lvl),end=":")
	while len(lyst)>0:#lg E loop, elevated to O(E) loop across all iterations
		e=heapPop(lyst)
		for i in diction[e.getDest()]:#O(lg E) loop
			if i.getDest() not in reached:#RBT implemented for O(lg V) behavior on this check
				heapPush(next_level,i) #O(lg E).  This pushes time complexity a tad higher, but bear in mind that this algorithm sorts the edges in addition to the normal functions of Kruskal's algorithm and BFS 
				reached.insert(i.getDest())
		total+=e.getWeight()
		if lvl==0:print(" "+str(e.getDest()),end=";")
		else: print(" "+str(e.getDest())+"("+str(e.getSrc())+")"+str(e.getWeight()),end=";")
	print()
	if len(next_level)>0:kruskurse(diction,next_level,lvl+1,reached) #recursive calls make sure each pertinent sub-list is fully explored
	return reached
	
def kruskal(graph): #Worst-case runtime of MST construction portion (before Kruskurse): O(E(log(E)+log(V)))=O(E lg V)
	verts=graph.V()
	subsets=graph.subsets()
	by_src=graph.srcsets()
	e=0
	v=graph.V()
	while (e<(v-1)): 					# this loop is potentially bound by both V and E
		if (graph.noEdges()):break		# this indicates this loop maxes out at E iterations
		next_edge=graph.dropEdge() #O(log E)
		x = findSet(subsets,next_edge.getSrc())#O(log(V))
		y = findSet(subsets,next_edge.getDest())#O(log(V))
		if (x!=y):
			by_src[next_edge.getSrc()].append(next_edge)			#does not use heapsort this time as edges will have to be resorted prior to printing
			by_src[next_edge.getDest()].append(next_edge.reverse())	#pushes twice to ensure proper traversal during Kruskurse
			e+=1 #best case for outer loop: this increases every time, for a total of V times
			union(subsets,x,y)#log(V)
	reached = kruskurse(by_src,[Edge(None,graph.root(),0)],0,RedBlackTree(RBTNode(graph.root())))#Assumes there are no edges from root to root: these would be the only trivial edges to be displayed
	print("weight:",total)
	print("unreachable:",v-len(reached))

def main():
	if (sys.argv[1]=="-r"):
		g = Graph(int(sys.argv[2]))
		f=open(sys.argv[3],'r')
	else:
		g = Graph()
		f=open(sys.argv[1],'r')	
	token=""
	src=None
	dest=None
	char=f.read(1)
	while char!="":
		if (char==' ')or(char=='\n'):
			if (src==None):
				if (token!=""):
					src=int(token)
					token=""
			elif (dest==None):
				if (token!=""):
					dest=int(token)
					token=""
		elif (char in "0123456789"):
			token+=char
		elif (char==';'):
			if (token!=""):
				if (src == None):
					print("Error: Insufficient numerical tokens preceding semicolon (Edge identified simply as "+token+")")
					return
				elif (dest==None):
					g.addEdge(src,int(token))
				else:
					g.addEdge(src,dest,int(token))
					
			else:
				if (dest==None):
					print("Error: Insufficient numerical tokens preceding semicolon (Edge identified simply as "+str(src)+")")
					return
				else:
					g.addEdge(src,dest)
			dest = None
			token=""
			src = None
		char=f.read(1)
	f.close()
	kruskal(g)
main()	