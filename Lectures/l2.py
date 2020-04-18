from Bio.Alphabet import IUPAC
from Bio import Seq
from Bio.SeqUtils import GC
my_dna=Seq.Seq('ATGGTTAGTTAA',IUPAC.unambiguous_dna)
print(GC(my_dna))#Percentage of Guanine and Cytosine in sequance
my_rna=Seq.Seq("AUGGUUAGUUAA",IUPAC.unambiguous_rna)

my_protein=Seq.Seq("MVS*",IUPAC.protein)
