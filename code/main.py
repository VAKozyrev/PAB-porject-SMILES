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


    answer = f.read_command(c.LOAD_SOURCE)
    while answer != c.YES and answer != c.NO:
        print(c.INVALID_ANSWER)
        answer = f.read_command(c.LOAD_SOURCE)

    if answer == c.YES:
        file_name = f.read_command(c.PROMPT)
        if f.open_file(file_name):
            smiles_items = f.read_from_file(file_name, 1)
            smiles_list = f.validate_smiles(smiles_items)
            if smiles_list.smiles_list == []:
                print(c.LIST_IS_EMPTY)
            else:
                for smiles in smiles_list.smiles_list:
                    print(smiles)
        else:
            print(c.FAILED_READING + str(file_name))

    if answer == c.NO:
        smiles_list = SmilesStringsList([])


    f.print_help_message()

    command = f.read_command(c.PROMPT)

    while command.upper() != c.QUIT:


        if command == c.COUNT_SUBSTRINGS:
            while answer != c.FILE and answer != c.TERMINAL:
                print(c.INVALID_INPUT)
                answer = f.read_command(c.INPUT_SOURCE)

            if answer == c.FILE:
                file_name = f.read_command(c.PROMPT)
                if f.open_file(file_name):
                    substrings_list = f.read_from_file(file_name, 0)
                    if substrings_list == []:
                        print(c.LIST_IS_EMPTY)
                    else:
                        smiles_list.cout_substrings(substring_list)
                else:
                    print(c.FAILED_READING + str(file_name))

            if answer == c.TERMINAL:
                num_of_strings = f.read_command(c.PROMPT)
                substring_list = f.read_from_terminal(num_of_strings)
                smiles_list.cout_substrings(substring_list)


        elif command == c.MOLECULAR_FORMULA:
            if smiles_list.smiles_list == []:
                print(c.LIST_IS_EMPTY)
            else:
                f.obtain_molecular_formula(smiles_list)


        elif command == c.DISSIMILARITY:
            if smiles_list.smiles_list == [] or len(smiles_list.smiles_list) == 1:
                print(c.LIST_EMPTY_OR_SINGULAR)
            elif len(smiles_list.smiles_list) > 1:
                number_of_substrings = f.read_command(c.NUMBER_OF_SUBSTRINGS)
                while int(num_of_strings) <= 0:
                    number_of_substrings = f.read_command(c.NUMBER_OF_SUBSTRINGS)

                substring_list = f.read_from_terminal(number_of_substrings)
                print(c.COMPARE_STRINGS)
                str1 = input()
                str2 = input()
                while str1 not in smiles_list.smiles_list:
                    print(c.UNKNOWN_SMILES_1)
                    str1 = input()
                while str2 not in smiles_list.smiles_list:
                    print(c.UNKNOWN_SMILES_2)
                    str2 = input()
                dissimilarity = f.count_dissimilarity(str1, str2, substrings_list)


        elif command == c.INPUT:
            f.input_new_smiles(smiles_list)


        elif command == c.HELP:
            f.print_help_message()

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
            print(c.GOODBYE)

        print(c.GOODBYE)

main()