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
        expression = '((Cl)|(Br)|[CNIFBOPcno])+(@{0,2}[0-9]{0,1}\({0,1}[\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])+\){0,1}[0-9]{0,1})*'
        match = re.match(expression, self.smiles)
        return match.group() == self.smiles


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

        molecule = {}
        molecular_formula = ""

        for key in elements:
            molecule[key] = elements[key]

        for i in range(len(self.smiles)):
            if self.smiles[i].upper() in elements:
                molecule[self.smiles[i].upper()] += 1

        for key in molecule:
            if molecule[key] != 0:
                molecular_formula += key
                molecular_formula += molecule[key]

        return molecular_formula