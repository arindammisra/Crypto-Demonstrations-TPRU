# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:22:25 2021

@author: Arindam Misra, TPRU
Multi Coin Prvate to Public Key Converter
"""
import subprocess
inp=input("Enter the private key\n")
print("The various formats of Private and Public Keys of this wallet are:\n")
comm=('btc_address_dump '+inp)
getkey=subprocess.Popen(comm,shell=True, stdout=subprocess.PIPE).stdout
key=getkey.read()
print(key.decode())

#"olympic wine chicken argue unaware bundle tunnel grid spider slot spell need"
#size envelope work rough gift ghost twice drip subject angle medal tornado
