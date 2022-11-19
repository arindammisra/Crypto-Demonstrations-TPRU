# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:11:21 2022

@author: arind

Blockchain first node fetcher
"""
import subprocess
import json
import pandas
inp=input("Enter the Txn hash\n")
"""
istransactionpresent=False
pageno=0
myextractedfile="Block Parser\n"
print("Searching in Bitnode Databse ............")
for i in range(1000):
    comm1=("curl https://bitnodes.io/api/v1/inv/?page="+str(i+1)+" --silent")
    output1 = subprocess.check_output(comm1, shell=True)
    txdbtemp=str(output1)
    flag=txdbtemp.find(inp)
    print("Page No. ",str(i+1))
    if flag>0:
        istransactionpresent=True
        pageno=i
        print("   FOUND   ")
        break
    myextractedfile=myextractedfile+txdbtemp

print("\n\n")
text_file=open("AddressPropagation.txt", "w")
text_file.write(myextractedfile)
text_file.close()
if istransactionpresent==True:
    print("Great!! The transaction with hash",inp," was found on page no.",str(pageno+1),"\n")
"""
comm2=("curl -H \"Accept: application/json; indent=4\""+ " https://bitnodes.io/api/v1/inv/"+inp+"/ --silent")
output2 = subprocess.check_output(comm2, shell=True)
txtrace=json.loads(output2)
txtracestr=str(txtrace)
flag=txtracestr.find('Not found.')
if flag<0:
    statt=txtrace.get('stats')
    #print(statt)
    stattht=statt.get('head')
    # print(stattht)
    print("\n\nThe first 10 nodes which heard this transaction with corresponding times are:\n\n\n")
    for i in range(10) :
        result_ms=pandas.to_datetime(str(stattht[i][1]),unit='ms')
        ipaddr=stattht[i][0].rsplit(':',1)[0]
        ipaddr=ipaddr.replace("[","")
        ipaddr=ipaddr.replace("]","")
        #YOURIPQUALITYSCOREPVTKEY needs to be replaced by the user's IP Quality Score Private Key
        comm3=("curl https://ipqualityscore.com/api/json/ip/YOURIPQUALITYSCOREPVTKEY/"+ipaddr+" --silent")
        output3 = subprocess.check_output(comm3, shell=True)
        txtrace2=json.loads(output3)
        ra=txtrace2.get('recent_abuse')
        fs=txtrace2.get('fraud_score')
        #print(fs)
        vpn=txtrace2.get('vpn')
        #print(vpn)
        tor=txtrace2.get('tor')
       # print(tor)
        #print(txtrace2)
        print("\n")
        print(ipaddr+"     at     "+str(result_ms))
        print("\n")
        print("Fraud Score: ",fs,"\nTor Use: ",tor,"\nVPN Use:",vpn,"\nRecent Abuse:",ra,"\n\n")
else:
    print("\nBad, bad server. No donut for you... Txn not in DB\n")
"""
else:
    print("\n\nSorry The transaction with hash",inp," was not found\n")
"""
"""
316859a364d6dbcb092f4d45a075a636fd262f44982f2190db79c82a881cce45
"""
