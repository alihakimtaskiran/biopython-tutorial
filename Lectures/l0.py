from Bio.Seq import Seq

seq=Seq("AGCTGATGCAGTCCAGT")#creating sequence
print(seq)
print(seq.complement())#complement sequence of the sequence
print(seq.reverse_complement())#reverse complement sequence of the sequence
