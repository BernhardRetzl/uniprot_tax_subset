from Bio import SeqIO
import glob


fasta_file = glob.glob('./*.fasta') [0]


tax_id_list = list()
with open('./tax_list.txt') as file:
    for line in file:
        line = line.strip()
        tax_id_list.append(line.split('=')[-1])


out_handle = open('./subset.fasta', 'w')

for sequence in SeqIO.parse(fasta_file, "fasta"):
    ox = sequence.description.split('OX=')[-1].split(' ')[0]
    if ox in tax_id_list:
        SeqIO.write(sequence, out_handle, "fasta")
