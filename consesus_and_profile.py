import os
import numpy as np
import pandas as pd
from Bio import SeqIO
os.chdir('/Users/sudha/Downloads/')
pd.set_option('display.max_columns', 1500)
pd.set_option('display.width', 5000)
pd.set_option('max_colwidth', 1)

data=[[str(l.seq)] for l in SeqIO.parse('rosalind_cons (4).txt', 'fasta')]

data = np.array(data).reshape(len(data), len(data[0]))
def convert(a):
    b=[]
    b[:0]=a
    return b
data= [convert(data[i][0]) for i in range(len(data))]

lis={'A':0,'C':1,'G':2,'T':3}

new=np.zeros((4,len(data[0])))
for a in lis.keys():
    for j in range(len(data[0])):
        count=0
        for i in range(len(data)):
            if data[i][j]==a:
                count+=1
        new[lis[a]][j]=int(count)


new=pd.DataFrame(new).astype(int)
new.index=['A','C','G','T']

fin=np.array(new.idxmax())
print(''.join(fin))
new.columns=['']*len(new.columns)
print(new)