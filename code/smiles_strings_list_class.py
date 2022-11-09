#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:22 2022

@author: mac
"""


class SmilesStringsList:

    def __init__(self, smiles_strings_list):
        self.smiles_list = smiles_strings_list

    def add_smiles_string(self, smiles_string):
        self.smiles_list.append(smiles_string)

    def get_smiles_string(self, elem):
        return self.smiles_list[elem]
