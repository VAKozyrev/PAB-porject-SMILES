#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:35:42 2022

@author: mac
"""

import funcs as f
from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import constants as c



def main():
    """
    Firs step: program asks if you want to load SMILES strings from file or
    not. Repeat question until answer != Y or N. If answer is NO program do
    nothing and print list of all commands. If answer is YES program ask for
    file name.
    """
    #list_smiles = SmilesStringsList([])

    answer = input(c.LOAD_SOURSE)
    while answer != c.YES and answer != c.NO:
        print(c.INVALID_ANSWER)
        answer = input(c.LOAD_SOURSE)

    """ 
    smiles_from_file_io(): function which ask user to enter name of file 
    for reading, if file can't be read print 'Failed reading file + 'file name'
    else: read only valid SMILES and return object smiles_strings_list with 
    valid SMILES from the file.
    """

    if answer == c.YES:
        f.open_file()
        smiles_strings_list = smiles_from_file_io()
        if smiles_strings_list == []:
            print(c.LIST_IS_EMPTY)
    if answer == c.NO:
        smiles_strings_list = SmilesStringsList([])

    """
    Second step, program print list of all commands
    """

    print(c.HELP_MESSAGE)

    """
    Third step, main loop with all commands.
    """

    command = input()
    while command.upper() != c.QUIT:

        #if command == COUNT_SUBSTRINGS:

        if command == c.MOLECULAR_FORMULA:
            obtain_molecular_formula

        #if command == DISSIMILARITY:

        if command == c.INPUT_NEW_SMILES:
            f.input_new_io(list_smiles)
        #if command == HELP:
            #print(HELP_MESSAGE)

        command = input()

    """
    Forth step, program ask if you want to save SMILES to file or not. If answer
    is NO program do nothing and close. If answer is YES program ask for a file name. 
    """

    answer = input(c.SAVE_SMILES)
    while answer != c.YES and answer != c.NO:
        print(c.INVALID_ANSWER)
        answer = input(c.SAVE_SMILES)

    """
    smiles_to_file_io(smiles_strings_list): function that asks user for file name, if program 
    can't open the file, print 'Failed open file + 'file name'. Else, program 
    write SMILES from smiles_strings_list to the file, if that SMILES is not already 
    in the file. 
    """

    if answer == c.YES:
        smiles_to_file_io(smiles_strings_list)

    print(c.GOODBYE)