from Bio.Data import CodonTable

standart_table=CodonTable.unambiguous_dna_by_name["Standard"]
print(standart_table)
mito_table=CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(mito_table)
