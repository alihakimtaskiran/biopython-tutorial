from Bio.Alphabet import IUPAC,generic_alphabet
from Bio.Seq import Seq

dna=Seq("ATGGTTAGTCTTTAA",IUPAC.unambiguous_dna)
protein=dna.translate()
#try to concetenate dna and protein sequences
try:
    concetencate=dna+protein
    print("Contenated successfully")
    #this attempt has been failed because dna and protein use different alphabet.
except:
#we need same types to concetenate. 
    dna.alphabet=generic_alphabet
    protein.alphabet=generic_alphabet
    print(dna+protein)