##################################################################################################################
####
####         ELUVIO DS CHALLENGE Core Engineering 
####         Option2: The Longest Strand Of Bytes
####         Owner : Chanoufi Marwen
####         Date : 19/04/2021
####            
##################################################################################################################

import numpy as np
import time
import os.path

t1 = time.time() # time start



## PROBABILTY OF EACH PAIR OF FILES 
########################################################################
lcs_set =set()
res=[]
for i in range(1,10):
        for j in range(10,i, -1):  
            filename1 = open('files/sample.'+ str(i),'rb')
            S = bytes(filename1.read())
            filename2 = open('files/sample.'+ str(j),'rb')
            T = bytes(filename2.read())
            n=len(S)
            m=len(T)


##  Find the identical strand of bytes that exists between two files 
########################################################################
            def lcs(S,T):
                counter = np.zeros(((n+1),(m+1)),dtype=int) ;
                longest = 0
                for i in range(n):
                    for j in range(m):
                        if S[i] == T[j]:
                            c = counter[i][j] + 1
                            counter[i+1][j+1] = c
                            if c > longest:
                                lcs_set = []
                                longest = c
                                lcs_set.append(S[i-c+1:i+1])   
                            elif c == longest:
                                lcs_set.append(S[i-c+1:i+1])

                               
                return lcs_set
##########################################################################




## Get the max Strand from the list of all identicals
##########################################################################
ret = lcs(S,T)
res=[k for k in ret if k not in res]
print('longest strand of bytes that is identical ',max(res),' \n The length of the Strand : ',len(max(res)),'\n' )
######################################################




## Location and Index of the longest strand where apears 
######################################################
for i in range(1,11):
    filename = open('files/Sample.'+ str(i),'rb')
    f = filename.read()
    if max(res) in f :
        print('the file name where the largest strand appears : ',os.path.basename(str(filename)),'\n the offset where the strand appears ',f.index(max(res)),'\n')  
    else:
        pass
######################################################


print('Run time is : ',time.time()-t1) #End Time 
