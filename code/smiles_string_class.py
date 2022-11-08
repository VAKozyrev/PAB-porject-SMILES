#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:22 2022

@author: mac
"""


class SmilesString:

    def __init__(self, smiles_string):
        self.smiles = smiles_string

    '''
    validate(): method for class SMILES.
    
    return boolean value

    там где нужно валидировать строку используй этот метод, пусть сначала просто
    всегда возвращает True, потом напишем функцию которая будет валидировать.
    '''

    def validate(self):
        expression = '((Cl)|(Br)|[CNIFBOPcno])+(@{0,2}[0-9]{0,1}\({0,1}[\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])+\){0,1}[0-9]{0,1})*'
        match = re.match(expression, self.smiles)
        return match.group() == self.smiles
