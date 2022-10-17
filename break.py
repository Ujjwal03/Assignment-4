import math
import os
import random
import re
import sys



def breakingRecords(scores):
    noofhigh=0
    nooflow=0
    high=scores[0]
    low=scores[0]
    
    for i in range(0,len(scores)):
        if(scores[i]>high):
            noofhigh+=1
            high=scores[i]
        if(scores[i]<low):
            nooflow+=1
            low=scores[i]
    print(noofhigh,nooflow)
        
        
    # Write your code here

if __name__ == '__main__':
    

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    breakingRecords(scores)
