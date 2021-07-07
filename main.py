##This is the main script##
from dotbracket import dotbracket
import RNA
import re
from parse import RNA_p
from nussinov import Nussinov

#####################################   Our function(Nussinov)    ##########################
RNA_nuss=RNA_p('test_seq.fasta')
nuss=Nussinov(RNA_nuss.RNA_seq)
indices=nuss.Calculate()
db=dotbracket(indices, RNA_nuss.RNA_seq)
RNA.PS_rna_plot(RNA_nuss.RNA_seq, db, "RNA_testseq_NUSS.ps")


#####################################   MFE using ViennaRNA RNAfold     ####################

#Running RNAfold producing dotbracket notation
v=RNA.fold('GGGCCUGUAGCUCAGAGGAUUAGAGCACGUGGCUACGAACCACGGUGUCGGGGGUUCGAA') 

#string containing dotbracket notation
db_2=v[0] 

#plotting the secondary structure
RNA.PS_rna_plot(RNA_nuss.RNA_seq, db_2, "RNA_testseq_MFE.ps") 


#####################################   Using ViennaRNA RNAalifold      ########

#list of the resulting sequences from aligning the first sequence
sequence_alignment=['GGGCCUGUAGCUCAGAGGAUUAGAGCACGUGGCUACGAACCACGGUGUCGGGGGUUCGAA','GGGCUAUUAGCUCAGUUGGUUAGAGCGCACCCCUGAUAAGGGUGAGGUCGCUGAUUCGAA','GGCGCCGUGGCGCAGUGGA--AGCGCGCAGGGCUCAUAACCCUGAUGUCCUCGGAUCGAA','GCGUUGGUGGUAUAGUGGUG-AGCAUAGCUGCCUUCCAAGCA-GUUGACCCGGGUUCGAU','ACUCCCUUAGUAUAAUU----AAUAUAACUGACUUCCAAUUA-GUAGAUUCUGAAU-AAA']

#Running RNAalifold producing dotbracket notation
a=RNA.alifold(sequence_alignment)

#string containing dotbracket notation
db_3=a[0]

#plotting the secondary structure
RNA.PS_rna_plot(RNA_nuss.RNA_seq, db_3, "RNA_testseq_ALI.ps") 

'UCCCUCCUCGCCCA','UUCAGCAUAGCCCA','ACCGAGCGGCGCUA','UCCCGGCCAACGCA','CCCAGAAGAGAGUA'


