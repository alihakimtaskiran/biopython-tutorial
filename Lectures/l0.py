from Bio.Seq import Seq

seq=Seq("AGCTGATGCAGTCCAGT")#create sequence
print(seq)
print(seq.complement())#complement sequence of the sequence
print(seq.reverse_complement())#reverse complement sequence of the sequence
print(str(seq))#convert sequence into string
print(seq.upper())#upper case
print(seq.lower())#lower case
