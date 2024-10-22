import math

wgt_matrix={	'A':{'A':1,'T':-1,'G':-1,'C':-1,'-':-1},
				'T':{'A':-1,'T':1,'G':-1,'C':-1,'-':-1},
				'G':{'A':-1,'T':-1,'G':1,'C':-1,'-':-1},
				'C':{'A':-1,'T':-1,'G':-1,'C':1,'-':-1},
				'-':{'A':-1,'T':-1,'G':-1,'C':-1}
			}	#weight matrix to calculate 'non-skipped' edge weights
res_wgt=0	#weight of 'skipped' edges

class node:
	def __init__(self,idx,score=-math.inf):	#graph node constructor which sets index & score
		self.idx=idx
		self.score=score
		self.children={}
		self.bp1=None
		self.bp2=None
	def set_bp(self,bp_idx,bp1,bp2):	#sets back_tracking pointers
 		self.bp_idx=bp_idx
 		self.bp1=bp1
 		self.bp2=bp2
	def child(self,n_idx,wgt):	#sets child with edge weight
		self.children[n_idx]=wgt

def create_mdag(l1,l2):	#returns manhatten-type dag
	nodes=[]
	for i in range(l1+1):	#row_major node creation
		for j in range(l2+1):	#creating children
			n=node(i*(l2+1)+j)
			if j!=l2:	#insert
				n.child(i*(l2+1)+j+1,wgt_matrix['-'][str2[j]])				
				if i!=l1:	#match/mismatch
					n.child((i+1)*(l2+1)+j+1,wgt_matrix[str1[i]][str2[j]])
			if i!=l1:	#delete
				if j!=0 and j!=l2:
					n.child((i+1)*(l2+1)+j,wgt_matrix[str1[i]]['-'])
				else:
					n.child((i+1)*(l2+1)+j,0)					
			nodes.append(n)
	nodes[0].score=0
	return nodes
'''
			if i==0 and j==0:	#skipped connections (only vertical)
				for k in range(l1):	
					n.child((k+1)*(l2+1),res_wgt)
			if i!=l1 and j==l2:
				n.child((l1+1)*(l2+1)-1,res_wgt)
'''

def topological_sort_utils(idx,visited,stack):
	global nodes
	visited[idx]=True
	for c in list(nodes[idx].children.keys()):
		if visited[c]==False:
			topological_sort_utils(c,visited,stack)
	stack.append(idx)

def topological_sort(nodes,l1,l2):	#returns topologically sorted graph as a list
	n_nodes=len(nodes)
	visited=[False]*n_nodes
	stack=[]
	for i in range((l1+1)*(l2+1)):
		if visited[i]==False:
			topological_sort_utils(i,visited,stack)
	return stack[::-1]

def set_scores(topo_sorted,nodes,str1,str2,l1,l2):	#sets manhatten-scores of all nodes
	for t in topo_sorted:	#checking parents
		i,j=t//(l2+1),t%(l2+1)
		if i:	#delete
			prev_idx=t-(l2+1)
			path=nodes[prev_idx].children[t]+nodes[prev_idx].score
			if path>nodes[t].score:
				nodes[t].score=path
				if j==0 or j==l2:
					nodes[t].set_bp(prev_idx,None,None)
#				elif j==l2:
#					nodes[t].set_bp(prev_idx,None,str2[j-1])				
				else:
					nodes[t].set_bp(prev_idx,str1[i-1],'-')
		if j:	#insert
			prev_idx=t-1
			path=nodes[prev_idx].children[t]+nodes[prev_idx].score
			if path>=nodes[t].score:
				nodes[t].score=path
				nodes[t].set_bp(prev_idx,'-',str2[j-1])
			if i:	#match/mismatch
				prev_idx=t-(l2+1)-1
				path=nodes[prev_idx].children[t]+nodes[prev_idx].score
				if path>=nodes[t].score:
					nodes[t].score=path
					nodes[t].set_bp(prev_idx,str1[i-1],str2[j-1])
'''
		if j==0 and i!=0:	#skipped
			prev_idx=j	#t-(k+1)*l2
			path=nodes[prev_idx].score+res_wgt
			if path>nodes[t].score:
				nodes[t].score=path
				nodes[t].set_bp(prev_idx,None,None)
				print('skipped1',i,j,prev_idx,'None','None',path)
		if j==l2 and i==l1:  #skipped
			for k in range(l1):
				prev_idx=(k+1)*l2
				path=nodes[prev_idx].score+res_wgt
				if path>nodes[t].score:
					nodes[t].score=path
					nodes[t].set_bp(prev_idx,None,None)
					print('skipped2',i,j,prev_idx,'None','None',path)
'''

def back_trace(nodes):
	bp_idx=nodes[-1].bp_idx
	t_node=nodes[bp_idx]
	while(t_node.bp1==None and t_node.bp2==None):
		t_node=nodes[t_node.bp_idx]
	str1_=''
	str2_=''
	count=0
	while(t_node.bp1!=None and t_node.bp2!=None):
		str1_+=t_node.bp1 if t_node.bp1!=None else ''
		str2_+=t_node.bp2 if t_node.bp2!=None else ''
		t_node=nodes[t_node.bp_idx]
	return str1_[::-1], str2_[::-1]

def fit_align(str1,str2):	#returns (max_len,sub_str1,str2) with max fitting alignment;	#len(str1)>=len(str2)
	global nodes
	l1,l2=len(str1),len(str2)
	nodes=create_mdag(l1,l2)
	topo_sorted=topological_sort(nodes,l1,l2)
	set_scores(topo_sorted,nodes,str1,str2,l1,l2)
	max_len=nodes[-1].score
	str1_,str2_=back_trace(nodes)
	print(max_len)
	print(str1_)
	print(str2_)

f=open('input','r')
str1=f.readline().split('\n')[0]
str2=f.readline()
fit_align(str1,str2)