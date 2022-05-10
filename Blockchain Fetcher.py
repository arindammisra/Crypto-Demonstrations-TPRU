# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:22:53 2021

@author: Arindam Misra TPRU
Blockchain Raw Block Extractor
"""
import re
import urllib.request as urllib2
n=int(input("Enter the number of blocks you want to search\n"))
start = '"prev_block":"'
end = '","mrkl_root"'
myextractedfile="Block Parser\n"
start_hash=input("Enter the Starting Block Hash\n")
result=start_hash
for i in range(n):
    f = urllib2.urlopen("https://blockchain.info/rawblock/"+result)
    #print("Requesting URL:","https://blockchain.info/rawblock/"+result)
    print("Fetching",i+1,"/",n,"\n")
    myfile=f.read()
    myfiletxt=myfile.decode("utf-8")
    myextractedfile=myextractedfile+myfiletxt
    result = re.search('%s(.*)%s' % (start, end), myfiletxt).group(1)

text_file=open("BlockDump.txt", "w")
text_file.write(myextractedfile)
text_file.close()
#pattern=input("\nEnter the transaction to be searched\n")
#for line in myextractedfile:
#    if re.search(pattern,line):
#        print(line)
#00000000000000000001b9a21f4c12d4b5e1146b390cbe4c361c2e6fe549836d
#00000000000000000015451643f34c083d4ffbb5ce7c6f0b37828d2dd13e0f25
#Search "value":5500