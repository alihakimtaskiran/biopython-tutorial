from Bio import SeqIO
#loading fasta files
for sequence_record in SeqIO.parse("ls_orchid.fasta","fasta"):
    print("\n")
    print(sequence_record)
    print(sequence_record.id)
    print(repr(sequence_record.seq))

#loading gbk files
for sequence_record in SeqIO.parse("ls_orchid.gbk","genbank"):
    print("\n")
    print(sequence_record)
    print(sequence_record.id)
    print(sequence_record.seq)