import copy
import math
from functools import reduce 

ktn=input().split(" ")
k,t,n=int(ktn[0]),int(ktn[1]),int(ktn[2])
dna=[]
for i in range(t):
	dna.append(input())

'''	
text_file='rosalind_ba2g.txt'
file=open(text_file)
read_lines=file.read().split('\n')
ktn=read_lines[0].split(' ')
k,t,n=int(ktn[0]),int(ktn[1]),int(ktn[2])
dna=read_lines[1:]
'''
pseudo_count=1
profile={'A':[pseudo_count]*k,'T':[pseudo_count]*k,'G':[pseudo_count]*k,'C':[pseudo_count]*k}
l=len(dna[0])
rseed = 0
RAND_MAX = (1 << 31)-1
bases=['A','T','G','C']
r_start=40
sum_prob=0

def rand():
    global rseed 
    rseed = (rseed * 1103515245 + 12345) & RAND_MAX
    return rseed

def inverse_sampling(prob,length):
	sum_prob=sum(prob)
	dist=[l for l in range(length) for p in range(int(prob[l]*100/sum_prob))]
	sum_per=len(dist)
	dist.extend([dist[rand()%sum_per] for s in range(sum_per,100)])
	return dist[rand()%100]

def mult_product(prob,start_id,end_id,threshold=100,flag=True):
	kk=end_id-start_id
	if kk <= threshold:
		if flag:
			prod=1
			for i in range(start_id,end_id):
				prod*=prob[i]
			return prod
		else:		
			return reduce(lambda x,y: x*prob[y],range(start_id,end_id),1)
	else:
		mid=kk//2+start_id
		return (mult_product(prob,start_id,mid)*mult_product(prob,mid,end_id))

def profile_rand_gen(excluded_motif,dna,profile,t,l,k):
	e_motif=dna[excluded_motif]
	prob=[mult_product([(profile[e_motif[i+j]][j]/(t+3)) for j in range(k)],0,k) for i in range(l-k+1)]
	return inverse_sampling(prob,l-k+1)

def Score(profile,k,t):
	global bases
	score=0
	for i in range(k):
		temp_list=[profile[bases[j]][i] for j in range(len(bases))]
		max_idx=temp_list.index(max(temp_list))
		score+=(t-profile[bases[max_idx]][i]+1)
	return score

def gibbs_sampler(dna,k,t,N):
	global pseudo_count, bases, r_start, profile
	best_motifs,best_score,l=[],t*k,len(dna[0])  #'assume': all string lengths are same!
	best_profile={'A':[pseudo_count]*k,'T':[pseudo_count]*k,'G':[pseudo_count]*k,'C':[pseudo_count]*k} #for d in bases:best_profile[d]=[pseudo_count]*k=*(flexibility)
	for i in range(t):  #1. BestMotif initialization
		rand_indx=rand()%(l-k+1)
		best_motifs.append(rand_indx)  #dna[i][rand_indx:rand_indx+k])
		for v in range(k):
			best_profile[dna[i][best_motifs[i]+v]][v]+=1 
	best_score=Score(best_profile,k,t)
	for r in range(r_start):  #2. Iterating over randomized initializations!
		motifs=[]
		profile={'A':[pseudo_count]*k,'T':[pseudo_count]*k,'G':[pseudo_count]*k,'C':[pseudo_count]*k}
		for i in range(t):
			rand_indx=rand()%(l-k+1)
			motifs.append(rand_indx)  #dna[i][rand_indx:rand_indx+k])
			for v in range(k):
				profile[dna[i][motifs[i]+v]][v]+=1 
		for n in range(N):
			excluded_motif=rand()%t
			popped=motifs.pop(excluded_motif)
			for v in range(k):
				profile[dna[excluded_motif][popped+v]][v]-=1
#			rand_indx=1
			ran_ind=profile_rand_gen(excluded_motif,dna,profile,t,l,k)
			motifs.insert(excluded_motif,ran_ind)  #dna[excluded_motif][ran_ind:ran_ind+k])
			for v in range(k):
				profile[dna[excluded_motif][ran_ind+v]][v]+=1
			score_motifs=Score(profile,k,t)
			if score_motifs<best_score:
				best_motifs=copy.deepcopy(motifs)
				best_score=score_motifs
	return best_motifs

motifs=gibbs_sampler(dna,k,t,n)
output_file=open('output_motifs.txt','w')
for i in range(len(motifs)):
	print(dna[i][motifs[i]:motifs[i]+k])
'''	output_file.write(dna[i][motifs[i]:motifs[i]+k])
	if i!= len(motifs)-1:
		output_file.write('\n')
'''
