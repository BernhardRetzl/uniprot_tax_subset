from Bio import SeqIO
import glob
import re


protein_group_file = glob.glob('proteinGroups.txt')[0]

tax_ids = set()

with open(protein_group_file) as f:
    for line in f:
        info = line.split('\t')[7]
        tax_info = re.findall(r'OX=\d+', info)
        for tax in tax_info:
            tax_ids.add(tax.split('OX=')[-1])


fasta_files = glob.glob('./*.fasta')
out_handle = open('subset.fasta', 'w')

for fasta_file in fasta_files:
    for sequence in SeqIO.parse(fasta_file, "fasta"):
        ox = sequence.description.split('OX=')[-1].split(' ')[0]
        if ox in tax_ids:
            SeqIO.write(sequence, out_handle, "fasta")

out_handle.close()
