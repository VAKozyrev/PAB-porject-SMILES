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
        if bool(match):
            return match.group() == self.smiles
        else:
            return False