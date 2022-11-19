# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:23:34 2022

@author: arind
"""

import os

def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
            print("Wallet found at the location")
            print (root+'/'+str(filename))
    return result

print(find_files("wallet.dat","C:/"))
