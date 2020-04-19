"""
                       DNA
                  
5'   ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG   3'
     |||||||||||||||||||||||||||||||||||||||
3'   TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC   5'


|
Transcription
↓
5’   AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG   3’

                   messenger-RNA
"""
from Bio.Seq import Seq,MutableSeq
from Bio.Alphabet import IUPAC

dna=Seq("TACATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGTAA",IUPAC.unambiguous_dna)
print(repr(dna))
dna_m=dna.tomutable()#mutable DNA
dna_m[8]="A"
print(repr(dna_m))

m_rna=dna.complement().transcribe()#transcribtion
print(repr(m_rna))

protein=m_rna.translate()#translation
print(repr(protein))

mitochondrial_protein=m_rna.translate("Bacterial")
print(repr(mitochondrial_protein))

