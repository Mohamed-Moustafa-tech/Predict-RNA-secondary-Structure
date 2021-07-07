## the code is written to be in a class syntax

class Nussinov(object):
    def __init__(self, data):
        self.data = data
        self.data_length = len(data)                      
        self.base_pairs = []


## Nussinov Algorithm implementation consists of two main blocks of code:
        ## construct th matrix
        
    def Construct_matrix(self):
        data_length = len(self.data)
        self.matrix = [[ 0 if i-1 <= j else -1 for j in range(data_length)]
                   for i in range(data_length)] ## matrix generation
        for d in range(1, self.data_length):
            i = 0
            for j in range(d, self.data_length):
                v = self.matrix[i+1][j-1] + int(self.data[i] + self.data[j] in ('AU','UA','GC','CG'))
                v = max(v, self.matrix[i+1][j])
                v = max(v, self.matrix[i][j-1])
                v = self.matrix[i+1][j-1] + int(self.data[i] + self.data[j] in ('GC','CG','AU','UA'))
                v = max([v] + [self.matrix[i][k] + self.matrix[k+1][j] for k in range(i+1,j)] )
                self.matrix[i][j] = v   ## the 4 Nussinov equations implementation
                i =i+1

## Second part take assess the values nd determine base pairings

    def Find_base_pairs(self,i,j):
        if self.matrix[i][j] == -1 or i>=j:
             return  ## to end the process
        if self.matrix[i][j] == self.matrix[i+1][j]:
            self.Find_base_pairs(i+1, j) ## i and i+1 cann't base pair with j
        elif self.matrix[i][j] == self.matrix[i][j-1]:
            self.Find_base_pairs(i, j-1) ## i cann't base pair with j-1 and j at the same time
        elif self.matrix[i][j] == self.matrix[i+1][j-1] + int(self.data[i] + self.data[j] in ('AU','UA','GC','CG')):
            self.base_pairs.append((i, j)) ## if the 2 bases are complementary insert their indecises in a bracket notation into a list
            self.Find_base_pairs(i+1, j-1)

        else:
            val, k = max([ (self.matrix[i][k] + self.matrix[k+1][j], k) \
                           for k in range(i+1,j) ])
            assert(self.matrix[i][j] == val)
            self.Find_base_pairs(i, k)
            self.Find_base_pairs(k+1, j)
           
## Calculate is a function that do  the two tasks   
    def Calculate(self):
        self.Construct_matrix()
        self.Find_base_pairs(0, self.data_length -1)
        return self.base_pairs


## An example 
##line="AACUAUGGGGGGGGGAUAGUUUGGGGGGGUCCUCCACUUC"
##outfile = open("out.txt","w")
##program = Nussinov(line)
##indecies = program.Calculate()
##outfile.write("%s %s\n" % (len(indecies), indecies))
##outfile.close()


