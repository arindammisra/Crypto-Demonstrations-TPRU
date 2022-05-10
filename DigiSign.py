# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:17:12 2022

@author: Arindam Misra TPRU
Signature Verifier
"""
import hashlib
from ecdsa import SigningKey, SECP256k1
pvtkey = SigningKey.generate(curve=SECP256k1)
pubkey = pvtkey.verifying_key
print("Enter the original message to be signed",'\n')
msg=input()
msghash=hashlib.sha256(msg.encode()).hexdigest()
signature = pvtkey.sign(msghash.encode())
print("Signing with private key.......",pvtkey.to_string().hex(),'\n')
print("The Signature of your message ",msg," is: ", signature.hex(),'\n')

print("Now verifying signature with public key......",pubkey.to_string().hex(),'\n')
print("Input Signature:",'\n')
siginput=input()
siginputb=bytes.fromhex(siginput)
print("Enter the original message ",'\n')
msgi=input()
msghashi=hashlib.sha256(msgi.encode()).hexdigest()
if pubkey.verify(siginputb,msghashi.encode()):
    print("\nSUCCESS\nThe original message and signature decrypted using public key match\n","This message is indeed from the owner of Private Key ",pvtkey.to_string().hex(),'\n')
