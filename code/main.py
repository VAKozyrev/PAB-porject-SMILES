#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:35:42 2022

@author: mac
"""

''' 
    What is SmilesString and SmilesStringsList:

    class SmilesString:
        def __init__(self, smiles_string):              smiles_string = str
            self.smiles = smiles_string

    class SmilesStringsList:
        def __init__(self, smiles_strings_list):        smiles_strings_list = [SMILES]
            self.list_smiles = smiles_strings_list
'''

# COMMANDS#
COUNT_SUBSTRINGS = 'C'
MOLECULAR_FORMULA = 'M'
DISSIMILARITY = 'D'
INPUT_NEW_SMILES = 'I'
HELP = 'H'
QUIT = 'Q'
NO = 'N'
YES = 'Y'

# INTERACTIONS#
LOAD_SOURSE = 'Load input from file (Y/N)?'
INPUT_COMMAND = 'Input command to execute:'
INPUT_SOURSE = 'Input source (F/T)'
INPUT_FILE_NAME = 'Input file name: '
SAVE_SMILES = 'Save SMILES list to file (Y/N)?'
GOODBYE = 'Goodbye!'
LIST_IS_EMPTY = 'SMILES list empty'
f = open('helpmessage.txt', 'r', encoding="utf-8")
HELP_MESSAGE = f.read()
f.close()

# ERRORS#
FAILED_READING = 'Failed reading file '
INVALID_ANSWER = 'Answer invalid'
LIST_EMPTY = 'SMILES list empty'
INVALID_COMMAND = 'Command invalid'
SMILES_INVALID = 'SMILES invalid'


def main():
    """
    Firs step: program asks if you want to load SMILES strings from file or
    not. Repeat question until answer != Y or N. If answer is NO program do
    nothing and print list of all commands. If answer is YES program ask for
    file name.
    """

    answer = input(LOAD_SOURSE)
    while answer != YES and answer != NO:
        print(INVALID_ANSWER)
        answer = input(LOAD_SOURSE)


    """ 
    SMILES_from_file(): function which ask user to enter name of file 
    for reading, if file can't be read print 'Failed reading file + 'file name'
    else: read only valid SMILES and return object LIST_SMILES with 
    valid SMILES from the file.
    """

    if answer == YES:
        smiles_strings_list = smiles_from_file_io()
        if smiles_strings_list == []:
            print(LIST_IS_EMPTY)
    if answer == NO:
        smiles_strings_list = SmilesStringsList([])

    """
    Second step, program print list of all commands
    """

    print(HELP_MESSAGE)

    """
    Third step, main loop with all commands.
    """

    command = input()
    while command.upper() != QUIT:

        if command == COUNT_SUBSTRINGS:

        if command == MOLECULAR_FORMULA:

        if command == DISSIMILARITY:

        if command == INPUT_NEW_SMILES:

        if command == HELP:
            print(HELP_MESSAGE)

        command = input()

    """
    Forth step, program ask if you want to save SMILES to file or not. If answer
    is NO program do nothing and close. If answer is YES program ask for a file name. 
    """

    answer = input(SAVE_SMILES)
    while answer != YES and answer != NO:
        print(INVALID_ANSWER)
        answer = input(SAVE_SMILES)

    """
    SMILES_to_file_io(list_SMILES): function that asks user for file name, If program 
    can't open the file, print 'Failed open file + 'file name'. Else, program 
    write SMILES from list_SMILES to the file, if that SMILES is not already 
    in the file. 
    """

    if answer == YES:
        smiles_to_file_io(smiles_strings_list)

    print(GOODBYE)

main()
