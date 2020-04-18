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
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna=Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",IUPAC.unambiguous_dna)
print(repr(dna))

m_rna=dna.complement().transcribe()#transcribtion
print(repr(m_rna))

protein=m_rna.translate()#translation
print(repr(protein))
