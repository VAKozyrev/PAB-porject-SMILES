#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:22 2022

@author: mac
"""
import re
class SmilesString:

    def __init__(self, smiles_string):
        self.smiles = smiles_string

    def validate(self):
        regex = re.compile('((Cl)|(Br)|[CNIFBrlOPcno])+((\[C@{0,2}H\])*@{0,2}[0-9]{0,1}\({0,1}[\\\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])*\){0,1}[0-9]{0,1})*')
        match = regex.match(self.smiles)
        dic = {'1' : 0, '2': 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0, '(' : 0, ')' : 0}
        for i in self.smiles:
            if i in dic:
                dic[i] += 1
        check = True
        for i in dic:
            if dic[i] % 2 != 0 and i != '(' and i != ')':
                check = False
                break
        if dic['('] != dic[')']:
            check = False
        if bool(match) and check:
            return self.smiles == match.group()
        else:
            return False

    def get_molecular_formula(self):
        elements = {"B": 0,
                    "C": 0,
                    "N": 0,
                    "O": 0,
                    "P": 0,
                    "S": 0,
                    "F": 0,
                    "Cl": 0,
                    "Br": 0,
                    "I": 0}

        molecular_formula = ""

        for i in range(len(self.smiles)):
            if self.smiles[i:i+1] in elements:
                elements[self.smiles[i:i+1]] += 1
            else:
                if self.smiles[i].upper() in elements:
                    elements[self.smiles[i].upper()] += 1

        for key in elements:
            if elements[key] != 0:
                molecular_formula += key
                molecular_formula += elements[key]

        return molecular_formula