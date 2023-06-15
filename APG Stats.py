# -*- coding: utf-8 -*-
"""

@author: arind

Bitnodes ToR VPN usage stats
"""
import subprocess
import json
import pandas
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
global_torandvpn_count=0
all_iter_count=0
for i in range(1,2):# Can be modified to increaase the number of transactions
    comm2=("curl -H \"Accept: application/json; indent=4\""+ " https://bitnodes.io/api/v1/inv/?page="+str(i)+" --silent")
    output2 = subprocess.check_output(comm2, shell=True)
    txtrace=json.loads(output2)
    results_var=txtrace.get("results")
    
    txtracestr=str(txtrace)
    flag=txtracestr.find('Not found.')
    if flag<0:
        for item in results_var:
            inp=item['inv_hash']
            print(item['inv_hash'])
            comm3=("curl -H \"Accept: application/json; indent=4\""+ " https://bitnodes.io/api/v1/inv/"+inp+"/ --silent")
            output3 = subprocess.check_output(comm3, shell=True)
            txtrace2=json.loads(output3)
            statt=txtrace2.get('stats')
            #print(statt)
            stattht=statt.get('head')
            # print(stattht)
            print("\n\nThe first node which heard this transaction with corresponding time is:\n\n\n")
            for i in range(1) : 
                result_ms=pandas.to_datetime(str(stattht[i][1]),unit='ms')
                ipaddr=stattht[i][0].rsplit(':',1)[0]
                ipaddr=ipaddr.replace("[","")
                ipaddr=ipaddr.replace("]","")
                comm3=("curl https://ipqualityscore.com/api/json/ip/y6yIzhVtHRznt8iew1JsXBCWMEl1YiK6/"+ipaddr+" --silent")
                output3 = subprocess.check_output(comm3, shell=True)
                txtrace2=json.loads(output3)
                ra=txtrace2.get('recent_abuse')
                fs=txtrace2.get('fraud_score')
                #print(fs)
                vpn=txtrace2.get('vpn')
                #print(vpn)
                tor=txtrace2.get('tor')
                res=vpn^tor
                res_int=int(res)
                global_torandvpn_count=global_torandvpn_count+res_int
               # print(tor)
                #print(txtrace2)
                all_iter_count=all_iter_count+1
                #print("\n")
                print(ipaddr+"     at     "+str(result_ms))
               # print("\n")
               # print("Fraud Score: ",fs,"\nTor Use: ",tor,"\nVPN Use:",vpn,"\nRecent Abuse:",ra,"\n\n")
                print("\nTor Use: ",tor,"\nVPN Use:",vpn,"\n\n")
    else:
        print("\nBad, bad server. No donut for you... Could not fetch the transactions\n")
    print("\n")
    print("The number of ToR or VPN originated transactions found were:", global_torandvpn_count)
    print("\n")
    print("The total transactions considred were", all_iter_count)
    
    
    """
    else:
        print("\n\nSorry The transaction with hash",inp," was not found\n")
"""
"""
316859a364d6dbcb092f4d45a075a636fd262f44982f2190db79c82a881cce45
"""

