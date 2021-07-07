In Nussinov File:
	The Nussinov Algorithm is imlemented into 2 main blocks of code. it depends on recursion to assess the maximum number of base pairs 	in a sequene of RNA. For i and j in  a sequence Sij they have four possibilites in the structure represented by the Nussinov Four 	equations. The first block of the code is meant to construct a matrix and apply the recursion on the sequence to give every possible 	base paring even a score. the second block is meant to evaluate these scores and insert the scores that represent base paring into 	a list and the output is the number of base pairings and their indecies.


After that the output is converted into dot barcket notation> Vienna RNA package can take the dot bracket notattion of an RNA sequence and plot it into a graph.


We can evalate our results by using the Vienna Package. Vienna Package can calcualte the structure with the minimum free energy and after that blot it into its secondary structure. so we can compare both structures generated from our code and the package for the same sequence of RNA.

The user would have to insert a .fasta file to the RNA_p class either as a DNA or RNA format. In case of the former, it will automatically convert it to RNA and continue. The output file of the 'RNA_PS_rna_plot' function is in the postscript format which can be accessed by a pdf viewer.

