#Parse file parses a FASTA file and returns the sequence
#the name each in a string 

import re


class RNA_p:

    def __init__ (self, RNA_fasta):
        
        self.RNA_fasta = RNA_fasta
        self.RNA_fasta_data = open(self.RNA_fasta)
        self.parse_RNA_fasta(RNA_fasta)

    def parse_RNA_fasta(self, RNA_fasta):

        read = self.RNA_fasta_data.readlines()
        newread=[]
        count=0
        
        for r in read:                      #checks if the fasta file is has DNA
            if "T" in r and count != 0:     #or RNA as the sequence. If DNA was 
                r=r.replace("T","U")        #found (i.e.'T' is found) then convert
                                            #it to RNA (i.e. T>U).
            newread.append(r.rstrip('\n'))  
            count=count+1                   #change the 'T' in the sequence and 
                                            #and avoids the header

        self.RNA_name = re.findall(r'[^ ]+ ([^,]+).+',newread[0])    
        self.RNA_seq = ''.join(newread[1:])
        
    def __len__(self):
        return len(self.RNA_seq)

    def __str__(self):
        return '%s' % (self.RNA_seq)

#Test commands:
    #RNA_sample1=RNA("Homo_sapiens_5S_rRNA.fasta")
    #print(RNA_sample1)
    #print(RNA_sample1.RNA_seq)
    
