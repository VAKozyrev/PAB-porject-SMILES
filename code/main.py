#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:35:42 2022

@author: mac
"""

import funcs as f
import constants as c
from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList



def main():

    answer = f.read_command(c.LOAD_SOURSE)
    while answer != c.YES and answer != c.NO:
        print(c.INVALID_ANSWER)
        answer = f.read_command(c.LOAD_SOURSE)

    if answer == c.YES:
        file_name = f.read_command(c.PROMPT)
        if f.open_file(file_name):
            smiles_strings_list = f.read_from_file(file_name)
            if smiles_strings_list == []:
                print(c.LIST_IS_EMPTY)
            else:
                smiles_list = SmilesStringsList(smiles_strings_list)
                # (Я не понял что дальше) if no string in the file was validated, or prints the valid ones in lexicographic order, one per line.
        else:
            print(c.FAILED_READING + str(file_name))

    if answer == c.NO:
        smiles_list = SmilesStringsList([])
        print(c.HELP_MESSAGE)

        command = f.read_command(c.PROMPT)

        while command.upper() != c.QUIT:

            #if command == COUNT_SUBSTRINGS:

            if command == c.MOLECULAR_FORMULA:
                if smiles_list == []:
                    print(c.LIST_IS_EMPTY)
                else:
                    f.obtain_molecular_formula(smiles_list)

            #if command == DISSIMILARITY:

            elif command == c.INPUT_NEW_SMILES:
                f.input_new_smiles(smiles_list)

            #elif command ==

            #if command == HELP:
                #print(HELP_MESSAGE)

            else:
                print(c.INVALID_COMMAND)

            command = f.read_command(c.PROMPT)

            if command == c.QUIT:
                answer = f.read_command(c.SAVE_SMILES)
                while answer != c.YES and answer != c.NO:
                    print(c.INVALID_ANSWER)
                    answer = f.read_command(c.SAVE_SMILES)

                if answer == c.YES:
                    f.write_to_file(smiles_list)

                if answer == c.NO:
                    print(c.GOODBYE)

main()