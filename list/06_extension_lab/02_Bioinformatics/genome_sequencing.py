import copy
import random 
import numpy as np

DEFAULT=object()
sys_random = random.SystemRandom()

def are_rotations(str1,str2):
	if len(str1)!=len(str2):
		return 0
	temp=str1+str1
	if temp.count(str2)>0 or (temp[::-1]).count(str2)>0:
		return 1
	else:
		return 0

def g_seq(g,iter=100000,start_gene=DEFAULT):  #find all possible genome sequences!
	genomes,if_start=[],0	
	start,end=terminals(g)
	if start_gene is DEFAULT:
		if end is not None:
			g[end].append(start)
			if_start=1
			start_gene
	else:
		if end is not None:
			g[end].append(start_gene)
			start=start_gene
			if_start=1
	for j in range(iter):
		final_genome=''
		temp_g=copy.deepcopy(g)  #dictionaries are mutable object during default 'call by name/object' function pass!
		if if_start is 1:
			final_ec=find_ec(temp_g,start)
		else:
			final_ec=find_ec(temp_g)
		if final_ec is not -1:
			for i in range(len(final_ec)):
				if i is 0:
					final_genome+=str(final_ec[i])
				else:
					final_genome+=str(final_ec[i][-1])
			if final_genome not in genomes:
				genomes.append(final_genome)
	return genomes

def find_ec(grap,start_gene=DEFAULT):  #returns eulerian circuit
	if not grap:
		return -1
	if start_gene is DEFAULT:
		r_start=sys_random.choice(list(grap.keys()))  #initial random start
	else:
		r_start=start_gene
	t_ckt,nxt_index=[],-1
	final_ec=np.array([])
	try:
		start=r_start
		t_ckt.append(start)  #temp_circuit
		while(1):
			nxt=sys_random.choice(grap[start])
			grap[start].remove(nxt)
			start=nxt
			if nxt==t_ckt[0]:  #for strings using '==' instead of 'is'
				if nxt is r_start:
					final_ec=t_ckt
				else:
					final_ec=np.concatenate([final_ec[0:nxt_index],np.array(t_ckt),final_ec[nxt_index:]])
					nxt_index=-1
				for i in range(len(final_ec)):
					if grap[final_ec[i]]:
						start=final_ec[i]
						nxt_index=i 
						t_ckt=[start]
				if nxt_index is -1:
					return final_ec
			else:
				t_ckt.append(nxt)
	except:  
		return -1  #no valid eulerian circuit

def pp(genomes,us=0):  #post-processing for genomes & universal strings to remove rotations
	gen=[]
	for i in range(len(genomes)):  #if pop(g) is used, len(g) doesn't vary accordingly
		rot_var=0
		if us is 1:
			genomes[i]=genomes[i][:-1]
		for j in range(i+1,len(genomes)):
			if (us is 1 and are_rotations(genomes[i],genomes[j][:-1])) or (us is 0 and are_rotations(genomes[i],genomes[j])):
				rot_var=1
				break
		if rot_var is 0:
			gen.append(genomes[i])
	return gen

def ustrings_gen(k):  #returns (k-1)mers debruijn graph
	ustring={}
	for j in range(2**k):
		temp_us=reads_gen(format(j,'b').zfill(k),k)
		for tus in temp_us:
			if tus not in list(ustring.keys()):
				ustring[tus]=[]
			if temp_us[tus]:
				ustring[tus].append(temp_us[tus][0])
	return ustring

def reads_gen(genome,k,ckt=0):  #returns (k)mers debruijn graph [with (k-1) length nodes]
	dbg={}
	for i in range(len(genome)-k+1):
		start=genome[i:i+k-1]
		if start not in dbg.keys():
			dbg[start]=[]
		dbg[start].append(genome[i+1:i+k])
	if genome[len(genome)-(k-1):] not in list(dbg.keys()):
		dbg[genome[len(genome)-(k-1):]]=[]
	if ckt is 1:
		dbg[genome[len(genome)-(k-1):]].append(genome[0:k-1])
	l=list(dbg.items())
	sys_random.shuffle(l)
	dbg=dict(l)
	return dbg

def terminals(grap):
	g_count={k:[0,0] for k in list(grap.keys())}  #{node:[#input,#output]}
	start,end=None,None
	for i in list(grap.keys()):
		for j in grap[i]:
			g_count[j][0]+=1
		g_count[i][1]=len(grap[i])
	for i in g_count:
		if g_count[i][0]>g_count[i][1]:
			end=i
		elif g_count[i][0]<g_count[i][1]:
			start=i
	return (start,end)

def print_g(grap,endi=''):  #prints graph nodes & children
	for i in grap:
		print(i,grap[i])
#	print(endi)

def genome_seqencing(genome,k,remove_cycles=1,start_gene=DEFAULT):
	gs=reads_gen(genome,k,0)  #(genome,3,1)-for a eulerian circuit  (not path)
	print(k,'-mer deBruijn graph of genes: ')
	print_g(gs)
	if start_gene is DEFAULT:
		final_genomes=g_seq(gs)
	else:
		final_genomes=g_seq(gs,start_gene=start_gene)
	if remove_cycles is 1:
		final_genomes=pp(final_genomes)
	return final_genomes

def universal_strings(k,remove_cycles=1):
	us=ustrings_gen(k)
	print(k,'-mer deBruijn graph of sub-strings: ')
	print(us)
	final_genomes=g_seq(us)
	if remove_cycles is 1:
		final_genomes=pp(final_genomes,1)  #1 bcz universal_string!
	return final_genomes

if __name__ == '__main__':
	genome="TAATGCCATGGGATGTT"
	genome="TGCCTGGGTGTTTG"
	genome="0001100"
	print('Possible genome(s): ',genome_seqencing(genome,k=3,remove_cycles=1),'\n\n')
	k=3
	print('Possible genome(s): ',universal_strings(k,1),'\n\n')
