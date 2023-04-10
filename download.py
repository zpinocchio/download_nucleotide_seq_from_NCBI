# encoding = utf-8
# @Time :2023/4/9 19:49
# Author : Pinocchio

from Bio import Entrez,SeqIO
Entrez.email = "example@163.com"
Entrez.tool  = "exampleScript"
import sys
import re
import os
# os.chdir("/home/sjzhong")
acc_re = re.compile('accession "(.*)"')

p2n_id = open("proteinID2nucleID.txt","w")
seq = open("download.fasta","w")
with open(sys.argv[1],"r") as f:
    for line in f:
        p_id = line.strip()
        try:
            
            handle = Entrez.efetch(db="protein", id=p_id)
            a = handle.read()
            nucle = acc_re.findall(a)[0]
            b  = Entrez.efetch(db="nucleotide",id=nucle,rettype="fasta", retmode="text")
            print(f"{p_id}\t{nucle}",file=p2n_id,flush=True)
            print(b.read(),file=seq,flush=True)
        except:
            print(f"{p_id} download fail",flush=True)
        
p2n_id.close()
seq.close()
