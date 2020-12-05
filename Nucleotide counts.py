#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

##########################################################################################################################################################################################################


#Open the file containing the DNA sequence
f = open("Data sets/Problem 1 DNA sequence.txt","r")

#Define function to count the number of each base, taking a string as argument
def countBases(string):

#Sets each base count to 0
    A = 0
    C = 0
    G = 0
    T = 0

#Iterate through DNA sequnce modifiying counters eveery time base is encountered   
    for i in range (0,len(string)):
                if (string[i] == 'A'):
                    A = A + 1
                elif (string[i] == 'C'):
                    C = C + 1
                elif (string[i] == 'G'):
                    G = G + 1
                elif (string[i] == "T"):
                    T = T + 1

    return str(A) + " " + str(C) + " " + str(G) +  " " + str(T)

print(countBases(f.read()))

