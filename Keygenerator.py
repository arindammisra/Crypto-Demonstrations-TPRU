# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:21:00 2022

@author: Arindam Misra TPRU
Bitcoin Key Pair Generator
"""

import bitcoin as btc
import pyautogui
import random as r
import pyqrcode
from PIL import Image
import IPython.display as display
print("-----------Bitcoin Wallet Address Generator---------","\n\n\n")

def rnd_mouse():
    pos = pyautogui.position()
    sd = pos[0]+1j*pos[1]
    r.seed(sd)
    return r.random()

print("Please move your mouse randomly to generate your key\n")
#print("Please enter your secret phrase and copy it somewhere\n")
#phrase=input()
phrase=0
for i in range(500000):
    phrase+=rnd_mouse()
strphrase=str(phrase)
pvtkey=btc.sha256(strphrase)
#print(pvtkey,"  \n")
pubkey=btc.privtopub(pvtkey)
#print(pubkey,"  \n")
pubaddr=btc.pubtoaddr(pubkey)
print("The Public address of your wallet is ",pubaddr,"\n")
print("The Private Key of your wallet is ",pvtkey,"\n")
pubkeyQR=pyqrcode.create(pubaddr)
pvtkeyQR=pyqrcode.create(pvtkey)
pubkeyQR.png("Public Key.png",scale=8)
pvtkeyQR.png("Private Key.png",scale =8)
print("\nPublic Address - ",pubaddr)
display.display(Image.open("Public Key.png"))
print("\nPrivate Key - ",pvtkey)
display.display(Image.open("Private Key.png"))